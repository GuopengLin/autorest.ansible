/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
import * as yaml from "node-yaml";

// import { Example } from "../Common/Example";


import { AnsibleCodeModel} from "../Common/AnsibleCodeModel";

import { GenerateModuleRest } from "./AnsibleModuleRest";
import { GenerateModuleRestInfo } from "./AnsibleModuleRestInfo";
import { GenerateModuleSdk } from "./AnsibleModuleSdk";
import { GenerateModuleSdkInfo } from "./AnsibleModuleSdkInfo";

import {Channel, Host, startSession} from "@azure-tools/autorest-extension-base";
import {CodeModel, codeModelSchema} from "@azure-tools/codemodel";
import {EOL} from "os";
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
        // const inputFileUris = await host.ListInputs();
        // Info("12345");
        // Info("input file"+inputFileUris);
        // const inputFiles: string[] = await Promise.all(inputFileUris.filter(uri =>uri.endsWith("no-tags.yaml")).map(uri => host.ReadFile(uri)));
        // for (let iff of inputFiles){
        //     const jsyaml = require('js-yaml');
        //     let climodel = jsyaml.safeLoad(iff);
        //     host.WriteFile("model4.yaml",yaml.dump(climodel));
        //     Info("1234");
        //     let codeModel = new  AnsibleCodeModel(climodel);
        //     // let files = {};
        //     // files = GenerateAll(codeModel, ArtifactType.ArtifactTypeAnsibleSdk);
        //     // for (let f in files) {
        //     //     Info(f);
        //     //     WriteFile(f, files[f]);
        //     // }
        // }
        const session = await startSession<CodeModel>(host, {}, codeModelSchema);

        host.WriteFile("model4.yaml",serialize(session.model));
        let chooseModule = await host.GetValue("module");
        let onlyList = await host.GetValue("list");
        let codeModel = new AnsibleCodeModel(session.model, chooseModule, onlyList, Info);

        let files = {};
        files = GenerateAll(codeModel, ArtifactType.ArtifactTypeAnsibleSdk);
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

