/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

import {
    ModuleTopLevelOptionsVariables,
    AppendModuleHeader,
    AppendModuleDocumentation,
    AppendModuleExamples,
    AppendMain,
    AppendModuleArgSpec,
    AppendModuleReturnDoc,
    ModuleGenerateApiCall,
    AppendInfoModuleLogic
} from "./AnsibleModuleCommon"
import {Module} from "../Common/Module";

export function GenerateModuleSdkInfo(module: Module, skipDoc: boolean) : string[] {

    var output: string[] = [];
    if (!skipDoc){
        AppendModuleHeader(output);
        AppendModuleDocumentation(output, module, true, false);
        AppendModuleExamples(output, module, false);
        AppendModuleReturnDoc(output, module, true);
    }

    output.push("");
    output.push("from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase");
    output.push("try:");
    output.push("    from msrestazure.azure_exceptions import CloudError");
    output.push("    from " + module.PythonNamespace + " import " + module.PythonMgmtClient + "");
    output.push("    from msrestazure.azure_operation import AzureOperationPoller");
    output.push("    from msrest.polling import LROPoller");
    output.push("except ImportError:");
    output.push("    # This is handled in azure_rm_common");
    output.push("    pass");    
    output.push("");
    output.push("");
    output.push("class " + module.ModuleClassName + "(AzureRMModuleBase):");
    output.push("    def __init__(self):");

    AppendModuleArgSpec(output, module, false, true);
    output.push("");

    let vars = ModuleTopLevelOptionsVariables(module.ModuleOptions, true);
    for (var i = 0; i < vars.length; i++) {
        output.push("        " + vars[i]);
    }

    output.push("");
    output.push("        self.results = dict(changed=False)");
    output.push("        self.mgmt_client = None");
    output.push("        self.state = None");
    output.push("        self.url = None");
    output.push("        self.status_code = [200]");
    output.push("");
    output.push("        self.query_parameters = {}");
    output.push("        self.query_parameters['api-version'] = '" + module.ModuleApiVersion + "'");
    output.push("        self.header_parameters = {}");
    output.push("        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'");
    output.push("");
    output.push("        self.mgmt_client = None");

    output.push("        super(" + module.ModuleClassName + ", self).__init__(self.module_arg_spec, supports_tags=" + (module.SupportsTags ? "True" : "False") + ")");
    output.push("");
    output.push("    def exec_module(self, **kwargs):");
    output.push("");
    output.push("        for key in self.module_arg_spec:");
    output.push("            setattr(self, key, kwargs[key])");
    output.push("");        
    output.push("        self.mgmt_client = self.get_mgmt_svc_client(" + module.PythonMgmtClient + ",");
    output.push("                                                    base_url=self._cloud_environment.endpoints.resource_manager,");
    output.push("                                                    api_version='"+module.ModuleApiVersion+"')");
    output.push("");

    AppendInfoModuleLogic(output, module);

    output.push("");

    for (let m of module.ModuleMethods)
    {
        output.push("    def " + m.Name.toLowerCase() + "(self):");
        output.push("        response = None");
        output.push("");
        output.push("        try:");
        ModuleGenerateApiCall(output, "            ", module, m.Name);
        output.push("        except CloudError as e:");
        output.push("            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')");
        output.push("");
        output.push("        return response");
        output.push("");
    }
    output.push("    def format_item(self, item):");
    output.push("        if hasattr(item, 'as_dict'):");
    output.push("            return [item.as_dict()]");
    output.push("        else:");
    output.push("            result = []");
    output.push("            items = list(item)");
    output.push("            for tmp in items:");
    output.push("                result.append(tmp.as_dict())");
    output.push("            return result");
    output.push("");
    output.push("");

    AppendMain(output, module);

    return output;
}
