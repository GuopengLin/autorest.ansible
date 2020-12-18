import {AnsibleCodeModel} from "./plugins/Common/AnsibleCodeModel";
import {ArtifactType, GenerateAll} from "./plugins/Ansible/AnsibleGenerator";
import {EOL} from "os";


export type LogCallback = (message: string) => void;
export type FileCallback = (path: string, rows: string[]) => void;



export async function main() {

    let ss : string[] = [];
    function Info(s: string)
    {
        ss.push(s);
    }

    function WriteFile(path: string, rows: string[])
    {
        let fs = require("fs");
        fs.writeFile("./tmp/"+path, rows.join('\r\n'), function (err) {
            if (err) {
                return console.error(err);
            }
        })
    }
    let fs = require("fs");
    const inputFileUri = "./tmp/model4.yaml";


    const input : string = fs.readFileSync(inputFileUri);

    const jsyaml = require('js-yaml');
    let model = jsyaml.safeLoad(input);

    let codeModel = new AnsibleCodeModel(model, "Galleries", false, console.log);
    let files = {};
    files = GenerateAll(codeModel, ArtifactType.ArtifactTypeAnsibleSdk, false);
    for (let f in files) {
        console.log(f);
        WriteFile(f, files[f]);
    }
}

main();
