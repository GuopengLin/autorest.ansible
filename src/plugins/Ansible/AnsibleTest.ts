import {Test} from "../Common/Test";
import * as yaml from "node-yaml";
import {ModuleOption, ModuleOptionKind} from "../Common/ModuleOption";
import {SwaggerModelType} from "../../utils/helper";
import {ModuleMethod} from "../Common/ModuleMethod";

export function GenerateTest(test: Test){
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
    // test.GenerateCreate(output, test);
    // test.GenerateUpdate(output, test);
    // test.GenerateUpdateWithoutChange(output, test);
    // test.GenerateDelete(output, test);
    return output;
}


export function UpdateParameters(test: Test){
    for (let method of test.ModuleMethods){
        for (let parameter of method.Options){
            if (test.ParameterValues.has(parameter.Name)  && parameter.Kind == ModuleOptionKind.MODULE_OPTION_BODY)
                test.ParameterValues.set(parameter.Name, test.ParameterValues.get(parameter.Name)+"2");
        }
    }
}
export function GetParameter(test: Test, parameter: ModuleOption){
    if (test.ParameterValues.has(parameter.Name))
        return test.ParameterValues.get(parameter.Name);
    let value = GetValue(test, parameter);
    if (value != null)
        test.ParameterValues.set(parameter.Name, value);
}
export function GetValue(test: Test, parameter: ModuleOption){
    // need to add more situations
    if (parameter.SwaggerType == SwaggerModelType.SWAGGER_MODEL_STRING){
        return "my_"+parameter.Name;
    }
    if (parameter.SwaggerType == SwaggerModelType.SWAGGER_MODEL_BOOLEAN){
        return true;
    }
    return null;
}
export function GetExample(test: Test, methodName: Set<string>, exampleName: string){
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


// function GenerateCreate(output: string[], test: Test){
//
// }
//
// function GenerateUpdate(output: string[], test: Test){
//
// }
//
// function GenerateUpdateWithoutChange(output: string[], test: Test){
//
// }
//
// function GenerateDelete(output: string[], test: Test){
//
// }
//
// function GenerateExample(output: string[], test: Test, name: string){
//     let example = test.Examples['create'];
//     output.push("    - name: create "+example.Name);
//     output.push("      " + test.ModuleName + ": ");
//     if (!(JSON.stringify(example.Value) === '{}')){
//         yaml.dump(example.Value).split('\n').forEach(element => {
//             output.push("        "+element);
//         });
//     }
//     output.push("");
// }

