/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

// import { ExamplePostProcessor, ExampleType } from "../Common/ExamplePostProcessor";
import {Indent, ToSnakeCase} from "../../utils/helper";
import {Module} from "../Common/Module";
import {ModuleOption, ModuleOptionKind} from "../Common/ModuleOption";
import {ModuleMethod} from "../Common/ModuleMethod";
import * as yaml from "node-yaml";

export function AppendModuleHeader(output: string[])
{
    output.push("#!/usr/bin/python");
    output.push("#");
    output.push("# Copyright (c) 2020 GuopengLin, (@t-glin)");
    output.push("#");
    output.push("# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)");
    output.push("");
    output.push("from __future__ import absolute_import, division, print_function");
    output.push("__metaclass__ = type");
    output.push("");
    output.push("");
    output.push("ANSIBLE_METADATA = {'metadata_version': '1.1',");
    output.push("                    'status': ['preview'],");
    output.push("                    'supported_by': 'community'}");
    output.push("");
    output.push("");
}

export function AppendModuleDocumentation(output: string[], module: Module, isInfoModule: boolean, isCollection: boolean)
{
    output.push("DOCUMENTATION = '''");
    output.push("---");

    var doc: any = {};
    let moduleName = module.ModuleName;

    if (isCollection)
    {
        if (!isInfoModule)
        {
            moduleName = module.ModuleName.split("_").pop();
        }
        else
        {
            moduleName = module.ModuleName.split("_info")[0].split("_").pop() + "_info";
        }
    }
    doc['module'] = moduleName;
    doc['version_added'] = '2.9';

    if (isInfoModule)
    {
        doc['short_description'] = "Get " + module.ObjectName + " info.";
        doc['description'] = [ "Get info of " + module.ObjectName + "."];
    }
    else
    {
        doc['short_description'] = "Manage Azure " + module.ObjectName + " instance.";
        doc['description'] = [ "Create, update and delete instance of Azure " + module.ObjectName + "."];
    }

    doc['options'] = ModuleHelp(module, isInfoModule);

    if (!isInfoModule)
    {
        doc['options']['state'] = {}
        doc['options']['state']['description'] = ["Assert the state of the " + module.ObjectName + ".", "Use C(present) to create or update an " + module.ObjectName + " and C(absent) to delete it."]
        doc['options']['state']['default'] = 'present';
        doc['options']['state']['choices'] = ['absent', 'present'];
    }
    doc['extends_documentation_fragment'] = ['azure.azcollection.azure', 'azure.azcollection.azure_tags'];
    if (module.SupportsTags() && !isInfoModule)
    {
        doc['extends_documentation_fragment'].push('azure_tags');
    }
    doc['author'] = ['GuopengLin (@t-glin)'];
    let s = yaml.dump(doc).split("\n");
    for (let i = 0; i < s.length;i++){
        let j = 0;
        let temp = "";
        for (j = 0; j < s[i].length;j++){
            if (s[i][j] != ' ')
                break;
            temp = temp + " ";
        }
        output.push(temp+s[i]);
    }
    // yaml.dump(doc).split("\n").forEach(element => {
    //     output.push("    "+element);
    // });
    output.push("'''");
    output.push("");
}

// export function AppendModuleExamples(output: string[], module: Module, isCollection: boolean)
// {
//     output.push("EXAMPLES = '''");
//
//     let pp = new ExamplePostProcessor(module.Module);
//     let examples = module.ModuleExamples;
//     let processedExamples: any[] = []
//
//     for (let exampleIdx in examples)
//     {
//         let example = examples[exampleIdx];
//         processedExamples.push(pp.ProcessExample(example, isCollection ? ExampleType.AnsibleCollection : ExampleType.Ansible, false));
//     }
//
//     yaml.dump(processedExamples).split(/\r?\n/).forEach(element => {
//         output.push(element);
//     });
//
//     output.push("'''");
//     output.push("");
// }

export function AppendModuleExamples(output: string[], module: Module, isInfoModule: boolean){
    output.push("EXAMPLES = '''");
    for (let example of module.ModuleExamples){
        output.push("    - name: "+example.Name);
        output.push("      " + module.ModuleName + ": ");
        if (!(JSON.stringify(example.Value) === '{}')){
            yaml.dump(example.Value).split('\n').forEach(element => {
                if (element.length > 0){
                    output.push("        "+element);
                }

            });
        }


        output.push("");
    }
    output.push("'''");
    output.push("");
}

// export function AppendParameter(output: string[], indent: string, name: string, content: any){
//     if (typeof content == 'object'){
//         if (content instanceof Array){
//
//         }else {
//             for (let subName in content)
//                 AppendParameter(output,indent+"    ", subName, content[subName]);
//         }
//     }
//     else {
//         output.push(indent+name+": "+content);
//     }
//
// }

export function AppendModuleReturnDoc(output: string[], module: Module, isInfoModule: boolean)
{
    output.push("RETURN = '''");

    let doc: any = isInfoModule ? ModuleInfoReturnResponseFields(module) : ModuleReturnResponseFields(module);

    let s = yaml.dump(doc).split(/\r?\n/);
    for (let i = 0; i < s.length;i++){
        let j = 0;
        let temp = "";
        for (j = 0; j < s[i].length;j++){
            if (s[i][j] != ' ')
                break;
            temp = temp + " ";
        }
        output.push(temp+s[i]);
    }
    // yaml.dump(doc).split(/\r?\n/).forEach(element => {
    //     output.push("    "+element);
    // });
    output.push("'''");

}

export function AppendModuleArgSpec(output: string[], module: Module, mainModule: boolean, useSdk: boolean)
{
    output.push("        self.module_arg_spec = dict(");

    let argspec = GetModuleArgSpec(module, module.ModuleOptions, mainModule, mainModule, useSdk);
    for (var i = 0; i < argspec.length; i++) {
        output.push("            " + argspec[i]);
    }
    output.push("        )");
}

export function AppendInfoModuleLogic(output: string[], module: Module)
{
    let ifStatement: string = "if";
    let sortedMethods = module.ModuleMethods.sort((m1,m2) => {
        if (m1.RequiredOptions.length > m2.RequiredOptions.length)
            return -1;
        if (m1.RequiredOptions.length == m2.RequiredOptions.length && m1.Options.length > m2.Options.length)
            return -1;
        return 1;
    });
    for (let method of sortedMethods)
    {
        let ps: ModuleOption[] = method.RequiredOptions;

        if (ps.length == 0)
        {
            output.push("        else:");
        }
        else
        {
            let ifPadding = ifStatement + " (";
            for (let idx: number = 0; idx < ps.length; idx++)
            {
                let optionName: string = ps[idx].NameAnsible;
                output.push("        " + ifPadding + "self." + optionName + " is not None" + ((idx != ps.length - 1) ? " and" : "):"))
                ifPadding = ' '.repeat(ifPadding.length);
            }
        }



        output.push("            self.results['" + module.ModuleOperationName +"'] = self.format_item(self." + method.Name.toLowerCase() + "())");

        // output.push("            self.results['" + module.ModuleOperationName +"'] = self.format_item(self." + method.Name.toLowerCase() + "())");

        ifStatement = "elif"
    }
    output.push("        return self.results");
}

export function AppendMain(output: string[], module: Module)
{
    output.push("def main():");
    output.push("    " + module.ModuleClassName + "()");
    output.push("");
    output.push("");
    output.push("if __name__ == '__main__':");
    output.push("    main()");
    output.push("");
}
//-----------------------------------------------------------------------------
// get module documentation
//-----------------------------------------------------------------------------
function ModuleHelp(module: Module, isInfoModule: boolean): any
{
    return GetHelpFromOptions(module, module.ModuleOptions, "    ");
}

//-----------------------------------------------------------------------------
// get module documentation from subset of options
//-----------------------------------------------------------------------------
function GetHelpFromOptions(module: Module, options: ModuleOption[], padding: string): any
{
    var help: any = {};

    for (var option of options)
    {
        let option_doc = {};

        if (option.Hidden)
            continue;

        // check if option should be included in documentation
        if (!option.IncludeInDocumentation)
            continue;

        if (option.NameSwagger == "tags")
            continue;

        let doc: string = option.Documentation ? option.Documentation : "undefined";

        help[option.NameAnsible] = option_doc;

        option_doc['description'] = doc.split("\n");

        // write only if true
        if (option.Required)
        {
            option_doc['required'] = true;
        }

        // right now just add type if option is a list or bool
        //if (option.IsList || option.Type == "bool")
        //{
            option_doc['type'] = (option.IsList ? "list" : option.Type);
        //}

        if (option.DefaultValue != null)
        {
            option_doc['default'] = option.DefaultValue;
        }

        /* XXXX
        if (option.EnumValues != null && option.EnumValues.Length > 0)
        {
            //string line = padding + "    choices: [";
            string line = padding + "    choices:";
            help.push(line);
            for (int i = 0; i < option.EnumValues.Length; i++)
            {
                line = padding + "        - '" + option.EnumValues[i].Key + "'";
                help.push(line);
                //line += "'" + option.EnumValues[i].Key + "'" + ((i < option.EnumValues.Length - 1) ? ", " : "]");
            }
            //help.push(line);
        }
        */
        if (option.EnumValues != null && option.EnumValues.length > 0){
            option_doc['choices'] = option.EnumValues;
        }
        if (haveSuboptions(option))
        {
            option_doc['suboptions'] = GetHelpFromOptions(module, option.SubOptions, padding + "        ");
        }
    }

    return help;
}

//---------------------------------------------------------------------------------------------------------------------------------------
// Return module options as module_arg_spec
//---------------------------------------------------------------------------------------------------------------------------------------
export function GetModuleArgSpec(module: Module, options: ModuleOption[], appendMainModuleOptions: boolean, mainModule: boolean, useSdk: boolean): string[]
{
    var argSpec: string[] = GetArgSpecFromOptions(module, options, "", mainModule, useSdk);

    if (appendMainModuleOptions)
    {
        argSpec.push(argSpec.pop() + ",");
        //if (this.NeedsForceUpdate)
        //{
        //    argSpec.push("force_update=dict(");
        //    argSpec.push("    type='bool'");
        //    argSpec.push("),");
        //}

        argSpec.push("state=dict(");
        argSpec.push("    type='str',");
        argSpec.push("    default='present',");
        argSpec.push("    choices=['present', 'absent']");
        argSpec.push(")");
    }

    return argSpec;
}

function GetArgSpecFromOptions(module: Module, options: ModuleOption[], prefix: string, mainModule: boolean, useSdk: boolean): string[]
{
    var argSpec: string[] = [];

    for (var i = 0; i < options.length; i++)
    {
        var option: ModuleOption = options[i];
        // if (option.Hidden)
        //     continue;

        if (!option.IncludeInArgSpec)
            continue;

        // tags shouldn't be added directly
        if (option.NameAnsible == "tags")
            continue;

        // for info Modules, only options included in path should be included
        // if (!mainModule && option.DispositionSdk != "*")
        //     continue;

        let required: boolean =  option.Required;
        let choices: boolean = (option.EnumValues != null) && option.EnumValues.length > 0;

        // add coma before previous option
        if (argSpec.length > 0) argSpec.push(argSpec.pop() + ",");

        argSpec.push(prefix + option.NameAnsible + "=dict(");

        let type = (option.IsList ? "list" : option.Type);

        // XXX - clean it up
        // XXX - do the same in documentation
        if (option.ExampleValue && (typeof option.ExampleValue == "string") && option.ExampleValue.startsWith('/subscriptions/'))
        {
            type = "raw";
        }

        argSpec.push(prefix + "    type='" + type + "'");

        if (option.NoLog)
        {
            argSpec.push(argSpec.pop() + ",");
            argSpec.push(prefix + "    no_log=True");
        }

        if (mainModule && option.Kind == ModuleOptionKind.MODULE_OPTION_BODY)
        {
            // if (option.Comparison != "")
            // {
            //     argSpec.push(argSpec.pop() + ",");
            //     argSpec.push(prefix + "    comparison='" + option.Comparison + "'");
            // }

            if (!option.Updatable)
            {
                argSpec.push(argSpec.pop() + ",");
                argSpec.push(prefix + "    updatable=" + (option.Updatable ? "True" : "False"));
            }

            let disposition = useSdk ? option.DispositionSdk : option.DispositionRest;

            // adjust disposition here if necessary
            if (useSdk)
            {
                if (option.NameAnsible != option.NamePythonSdk)
                {
                    disposition = disposition.replace("*", option.NamePythonSdk)
                }
            }
            else
            {
                if (option.NameAnsible != option.NameSwagger)
                {
                    disposition = disposition.replace("*", option.NameSwagger)
                }
            }

            if (disposition != "*")
            {
                if (disposition == "/*") disposition = "/";
                argSpec.push(argSpec.pop() + ",");
                argSpec.push(prefix + "    disposition='" + disposition + "'");
            }
        }

        if (choices)
        {
            argSpec.push(argSpec.pop() + ",");
            let choicesList: string = "    choices=[";

            for (var ci = 0; ci < option.EnumValues.length; ci++)
            {
                choicesList += "'" + option.EnumValues[ci]+ "'";

                if (ci < option.EnumValues.length - 1)
                {
                    choicesList += ",";
                }
                else
                {
                    choicesList += "]";
                }
                argSpec.push(prefix + choicesList);
                choicesList = "             ";
            }
            // I don't know why Zim chooses dictionary to store the choices, so I change it to string
            // for (var ci = 0; ci < option.EnumValues.length; ci++)
            // {
            //     choicesList += "'" + option.EnumValues[ci].Key + "'";
            //
            //     if (ci < option.EnumValues.length - 1)
            //     {
            //         choicesList += ",";
            //     }
            //     else
            //     {
            //         choicesList += "]";
            //     }
            //     argSpec.push(prefix + choicesList);
            //     choicesList = "             ";
            // }
        }

        if (required)
        {
            argSpec.push(argSpec.pop() + ",");
            if (option.DefaultValue != null)
            {
                argSpec.push(prefix + "    default=" + option.DefaultValue);
            }
            else
            {
                argSpec.push(prefix + "    required=True");
            }
        }
        if (option.ExampleValue && (typeof option.ExampleValue == "string") && option.ExampleValue.startsWith('/subscriptions/'))
        {
            argSpec.push(argSpec.pop() + ",");

            // last should be "{{ name }}"
            let pattern = option.ExampleValue;
            let start = pattern.lastIndexOf("{{") + 2;
            let end = pattern.lastIndexOf("}}");
            let old_name = pattern.substring(start, end);
            if (old_name.trim().endsWith("_name"))
            {
                pattern = pattern.replace(old_name, " name ");
            }

            // split pattern into parts
            let parts: string[] = pattern.split('/');
            let line = prefix + "    pattern=('/";
            for (let i = 1; i < parts.length; i++)
            {
                if (line.length + parts[i].length > 80)
                {
                    line += "'";
                    argSpec.push(line);
                    line = prefix + "             '";
                }
                line += "/" + parts[i];
            }
            argSpec.push(line + "')");

        }
        if (option.Type == 'list'){
            argSpec.push(argSpec.pop() + ",");
            argSpec.push(prefix + "    elements='" + option.ElementType+"'");
        }
        if (haveSuboptions(option))
        {

            argSpec.push(argSpec.pop() + ",");
            argSpec.push(prefix + "    options=dict(");

            argSpec = argSpec.concat(GetArgSpecFromOptions(module, option.SubOptions, prefix + "        ", mainModule, useSdk));

            argSpec.push(prefix + "    )");
        }

        argSpec.push(prefix + ")");
    }

    return argSpec;
}

function haveSuboptions(option: ModuleOption): boolean
{
    if (option.SubOptions == null)
        return false;

    if (option.SubOptions == [])
        return false;

    let cnt = 0;

    for (var so of option.SubOptions)
    {
        if (so.Hidden)
            continue;

        cnt++;
    }

    return (cnt > 0);
}

export function ModuleTopLevelOptionsVariables(options: ModuleOption[], useSdk: boolean): string[]
{
    var variables: string[] = [];

    for (let option of options)
    {
        if (option.Kind == ModuleOptionKind.MODULE_OPTION_BODY)
            continue;
        variables.push("self." + option.NameAnsible + " = None");
        // if (option.DispositionSdk == "*")
        // {
        //     variables.push("self." + option.NameAnsible + " = None");
        // }
        // else if (option.Kind == ModuleOptionKind.MODULE_OPTION_PLACEHOLDER)
        // {
        //     variables.push("self." + option.NameAnsible + " = dict()");
        // }
        // else
        // {
        //     // XXX - right now just supporting 2 levels
        //     //string[] path = option.Disposition.Split(":");
        //     //string variable = "self." + path[0] + "['" + option.NameAlt + "'] = dict()";
        //     //variables.push(variable);
        // }
    }

    return variables;
}

export function ModuleGenerateApiCall(output: string[], indent: string, module: Module, methodName: string): string[]
{
    // XXX - ModuleOperationName
    let line: string = indent + "response = self.mgmt_client." + module.ModuleOperationName + "." + ToSnakeCase(methodName) + "(";
    indent = Indent(line);
    let method: ModuleMethod = module.GetMethod(methodName);

    if (method != null)
    {
        for (let option of method.Options)
        {

            if (option.Kind == ModuleOptionKind.MODULE_OPTION_BODY)
                continue;

            if (line.endsWith("("))
            {
                line += option.NameAnsible + "=self." + option.NameAnsible;
            }
            else
            {
                line += ",";
                output.push(line);
                line = indent + option.NameAnsible + "=self." + option.NameAnsible;
            }
        }
        if (method.HasBody){
            line += ",";
            output.push(line);
            line = indent + method.ParameterName + "=self.body";
        }
    }
    line += ")";
    output.push(line);

    return output;
}



export function GetFixUrlStatements(baseUrl: string): string[]
{
    let ss: string[] = [];
    let url = baseUrl;
    let reg = /{([^{}]*)}/g
    let result;
    while ((result = reg.exec(url)) != null){
            ss.push("self.url = self.url.replace('{" + result[1] + "}', self." + ToSnakeCase(result[1]) + ")");
    }

    return ss;
}


function ModuleReturnResponseFields(module: Module): any
{
    return GetHelpFromResponseFields(module, module.ModuleResponseFields, "");
}

function ModuleInfoReturnResponseFields(module: Module):  any
{
    let help: any = {}     
    help[module.ModuleOperationName] = {};
    help[module.ModuleOperationName]['description'] = "A list of dict results where the key is the name of the " + module.ObjectName + " and the values are the facts for that " + module.ObjectName + ".";
    help[module.ModuleOperationName]['returned'] = 'always';
    help[module.ModuleOperationName]['type'] = 'complex';
    help[module.ModuleOperationName]['contains'] = {};
    help[module.ModuleOperationName]['contains'] = GetHelpFromResponseFields(module, module.ModuleResponseFields, "                ");
    // help[module.ModuleOperationName]['contains'][module.ObjectNamePythonized + "_name"] = {};
    // help[module.ModuleOperationName]['contains'][module.ObjectNamePythonized + "_name"]['description'] = "The key is the name of the server that the values relate to.";
    // help[module.ModuleOperationName]['contains'][module.ObjectNamePythonized + "_name"]['type'] = 'complex';
    // help[module.ModuleOperationName]['contains'][module.ObjectNamePythonized + "_name"]['contains'] = GetHelpFromResponseFields(module, module.ModuleResponseFields, "                ");
    return help;
}

function GetHelpFromResponseFields(module: Module, fields: ModuleOption[], padding: string): any
{
    //let help: string[] = [];
    let help: any = {}
    if (fields != null)
    {
        for (let field of fields)
        {
            // setting nameAlt to empty or "x" will remove the field
            if (field.NameAnsible == "" || field.NameAnsible.toLowerCase() == "x" || field.NameAnsible.toLowerCase() == "nl")
                continue;
            let field_doc = {};
            help[field.NameAnsible] = field_doc;

            //let doc: string = this.NormalizeString(field.Description);
            //help.push(padding + field.NameAlt + ":");
            //help.push(padding + "    description:");
            //help.concat(this.WrapString(padding + "        - ", doc));

            field_doc['description'] = [ field.Documentation ];
            field_doc['returned'] = "always"; //field.Returned;
            field_doc['type'] = field.Type;

            //help.push(padding + "    returned: " + field.Returned);
            //help.push(padding + "    type: " + field.Type);

            //help.concat(this.WrapString(padding + "    sample: ", field.SampleValue));
            field_doc['sample'] = field.ExampleValue;

            if (haveSuboptions(field))
            {
                field_doc['contains'] = GetHelpFromResponseFields(module, field.SubOptions, padding + "        ");
                //help.push(padding + "    contains:");
                //help.concat(this.GetHelpFromResponseFields(field.SubOptions, padding + "        "));
            }
        }
    }

    return help;
}
