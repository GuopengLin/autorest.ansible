/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/


import { AnsibleCodeModel} from "../Common/AnsibleCodeModel";


import {Channel, Host, startSession} from "@azure-tools/autorest-extension-base";
import {CodeModel, codeModelSchema} from "@azure-tools/codemodel";
import {ArtifactType, GenerateAll} from "./AnsibleGenerator";
import {serialize} from "@azure-tools/codegen";


export async function processRequest(host: Host) {
    const debug = await host.GetValue('debug') || false;
    function WriteFile(path: string, rows: string[])
    {
        if (rows instanceof Array){
            host.WriteFile(path, rows.join("\n"));
        }
    }
    function Info(message: string) {
        host.Message({
            Channel: Channel.Information,
            Text: message
        });
    }
    try {

        const session = await startSession<CodeModel>(host, {}, codeModelSchema);

        host.WriteFile("model4.yaml",serialize(session.model));
        let chooseModule = await host.GetValue("module");
        let onlyList = await host.GetValue("list");
        let codeModel = new AnsibleCodeModel(session.model, chooseModule, onlyList, Info);
        let skipDoc = await host.GetValue("skipDoc");
        let files = {};
        files = GenerateAll(codeModel, ArtifactType.ArtifactTypeAnsibleSdk, skipDoc);
        for (let f in files) {
            Info(f);
            WriteFile(f, files[f]);
        }
    } catch (E) {
        if (debug) {
            console.error(`${__filename} - FAILURE  ${JSON.stringify(E)} ${E.stack}`);
        }
        throw E;
    }

}

