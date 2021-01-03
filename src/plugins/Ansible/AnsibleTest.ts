/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/


import {ModuleTest} from "../Common/ModuleTest";
import * as yaml from "node-yaml";
import {ModuleOption, ModuleOptionKind} from "../Common/ModuleOption";
import {SwaggerModelType} from "../../utils/helper";
import {ModuleMethod} from "../Common/ModuleMethod";

export function GenerateTest(test: ModuleTest){
    var output: string[] = [];

    for (let method of test.ModuleMethods){
        for (let parameter of method.Options){
            GetParameter(test, parameter);
        }
    }
    GetExample(test, new Set(["create", "create_or_update"]), "Create a " + test.ObjectName);
    GetExample(test, new Set(["get"]), "get the " + test.ObjectName );
    GetExample(test, new Set(["update", "create_or_update"]), "Update the " + test.ObjectName + " (no change)");
    UpdateParameters(test);
    GetExample(test, new Set(["update", "create_or_update"]), "Update the " + test.ObjectName + "");
    GetExample(test, new Set(["delete"]), "Delete the " + test.ObjectName);
    
    for (let example of test.Examples){
        output.push(" - name: "+example['name']);
        if (!(JSON.stringify(example['content']) === '{}')){
            yaml.dump(example['content']).split('\n').forEach(element => {
                output.push("   "+element);
            });
        }
        output.push("");
    }
    return output;
}


export function UpdateParameters(test: ModuleTest){
    for (let method of test.ModuleMethods){
        for (let parameter of method.Options){
            if (test.ParameterValues.has(parameter.Name)  && parameter.Kind == ModuleOptionKind.MODULE_OPTION_BODY)
                test.ParameterValues.set(parameter.Name, test.ParameterValues.get(parameter.Name)+"2");
        }
    }
}
export function GetParameter(test: ModuleTest, parameter: ModuleOption){
    if (test.ParameterValues.has(parameter.Name))
        return test.ParameterValues.get(parameter.Name);
    let value = GetValue(test, parameter);
    if (value != null)
        test.ParameterValues.set(parameter.Name, value);
}
export function GetValue(test: ModuleTest, parameter: ModuleOption){
    // need to add more situations
    if (parameter.SwaggerType == SwaggerModelType.SWAGGER_MODEL_STRING){
        return "my_"+parameter.Name;
    }
    if (parameter.SwaggerType == SwaggerModelType.SWAGGER_MODEL_BOOLEAN){
        return true;
    }
    return null;
}
export function GetExample(test: ModuleTest, methodName: Set<string>, exampleName: string){
    let nowMethod: ModuleMethod = null;
    for (let method of test.ModuleMethods){
        if (methodName.has(method.Name)){
            nowMethod = method;
            break;
        }
    }
    if (nowMethod == null)
        return;
    let example = {};
    example['name'] = exampleName;
    let parameters = {};
    for (let parameter of nowMethod.Options){
        if (test.ParameterValues.has(parameter.Name)){
            parameters[parameter.Name] = test.ParameterValues.get(parameter.Name);
        }
    }
    if (methodName.has('delete'))
        parameters['state'] = 'absent';
    let content = {};
    if (methodName.has("get")){
        content[test.ModuleName +"_info"] = parameters;
    }else {
        content[test.ModuleName] = parameters;
    }

    example['content'] = content;

    test.Examples.push(example);
}




