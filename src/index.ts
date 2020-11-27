import { AutoRestExtension, Channel, Host } from "@azure-tools/autorest-extension-base";

import * as yaml from "node-yaml";


import { processRequest as ansible } from "./plugins/Ansible/Generator"
// export type LogCallback = (message: string) => void;
// export type FileCallback = (path: string, rows: string[]) => void;
//


// export async function main() {
//     const extension = new AutoRestExtension();
//     extension.Add('hider', hider);
//     extension.Add("ansible", async autoRestApi => {
//         let log = await autoRestApi.GetValue("log");
//
//         function Info(s: string)
//         {
//             if (log)
//             {
//                 autoRestApi.Message({
//                     Channel: Channel.Information,
//                     Text: s
//                 });
//             }
//
//         }
//         function Debug(s: string)
//         {
//                 autoRestApi.Message({
//                     Channel: Channel.Debug,
//                     Text: s
//                 });
//         }
//         function WriteFile(path: string, rows: string[])
//         {
//             autoRestApi.WriteFile(path, rows.join('\r\n'));
//             Info("321");
//         }
//         const inputFileUris = await autoRestApi.ListInputs();
//         Info("input file:" + inputFileUris);
//         const inputFiles: string[] = await Promise.all(inputFileUris.filter(uri =>uri.endsWith("no-tags.yaml")).map(uri => autoRestApi.ReadFile(uri)));
//         WriteFile("model4.yaml", inputFiles);
//         Info("123");
//         // for (let iff of inputFiles){
//         //     const jsyaml = require('js-yaml');
//         //     let climodel = jsyaml.safeLoad(iff);
//         //     let modelGroup = new CodeModelGroup(climodel, Debug);
//         //     modelGroup.Init();
//         //     GenerateAnsible(ArtifactType.ArtifactTypeAnsibleRest, modelGroup, WriteFile, Info);
//         //     // for (let m of climodel.operationGroups){
//         //     //     Info("============== moduleName: "+m["$key"]+" =================");
//         //     //
//         //     //     let idx1 = 1;
//         //     //     for (let method of m.operations){
//         //     //         Info("============== method: "+idx1+"  =================");
//         //     //         Info("      method: "+method.requests[0].protocol.http.method);
//         //     //         Info("      name: "+method.language.default.name);
//         //     //         Info("      path:" + method.requests[0].protocol.http.path);
//         //     //         Info("      version:" + method.apiVersions[0].version)
//         //     //         idx1++;
//         //     //         let idx2 = 1;
//         //     //         for (var p of method.parameters){
//         //     //             Info("============parameter: "+idx2 + "==============")
//         //     //             Info("" + yaml.dump(p));
//         //     //             idx2++;
//         //     //         }
//         //     //     }
//         //     // }
//         // }
//
//     });
//     extension.Run();
// }

export function main(){
    const extension = new AutoRestExtension();
    extension.Add("ansible", ansible);
    extension.Run();
}
main();
