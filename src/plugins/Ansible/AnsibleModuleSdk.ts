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
    ModuleGenerateApiCall
} from "./AnsibleModuleCommon"
import { Indent } from "../../utils/helper";
import {Module} from "../Common/Module";

export function GenerateModuleSdk(module: Module, skipDoc: boolean) : string[] {
    
    var output: string[] = [];
    if (!skipDoc){
        AppendModuleHeader(output);
        AppendModuleDocumentation(output, module, false, false);
        AppendModuleExamples(output, module, false);
        AppendModuleReturnDoc(output, module, false);
    }
    output.push("");
    output.push("from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt");
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
    output.push("class Actions:");
    output.push("    NoAction, Create, Update, Delete = range(4)");
    output.push("");
    output.push("");
    output.push("class " + module.ModuleClassName + "(AzureRMModuleBaseExt):");
    output.push("    def __init__(self):");
    AppendModuleArgSpec(output, module, true, true);
    output.push("");

    let vars = ModuleTopLevelOptionsVariables(module.ModuleOptions, true);
    for (var i = 0; i < vars.length; i++) {
        output.push("        " + vars[i]);
    }
    output.push("        self.body = {}");
    output.push("");
    output.push("        self.results = dict(changed=False)");
    output.push("        self.mgmt_client = None");
    output.push("        self.state = None");
    output.push("        self.to_do = Actions.NoAction");
    output.push("");
    output.push("        super(" + module.ModuleClassName + ", self).__init__(derived_arg_spec=self.module_arg_spec,");
    output.push("                               " + Indent(module.ModuleClassName) + "supports_check_mode=True,");
    output.push("                               " + Indent(module.ModuleClassName) + "supports_tags=" + (module.SupportsTags ? "True" : "False") + ")");
    output.push("");
    output.push("    def exec_module(self, **kwargs):");
    output.push("        for key in list(self.module_arg_spec.keys()):");
    output.push("            if hasattr(self, key):");
    output.push("                setattr(self, key, kwargs[key])");
    output.push("            elif kwargs[key] is not None:");
    output.push("                self.body[key] = kwargs[key]");
    output.push("");
    output.push("        self.inflate_parameters(self.module_arg_spec, self.body, 0)");    
    output.push("");
    output.push("        old_response = None");
    output.push("        response = None");
    output.push("");
    output.push("        self.mgmt_client = self.get_mgmt_svc_client(" + module.PythonMgmtClient + ",");
    output.push("                                                    base_url=self._cloud_environment.endpoints.resource_manager,");
    output.push("                                                    api_version='"+module.ModuleApiVersion+"')");
    if (module.HasResourceGroup())
    {
        output.push("");
        output.push("        resource_group = self.get_resource_group(self.resource_group)");
    }
    output.push("");

    let locationDisposition: string = module.LocationDisposition;
    if (null != locationDisposition)
    {
        if (locationDisposition == "/")
        {
            output.push("        if 'location' not in self.body:");
            output.push("            self.body['location'] = resource_group.location");
        }
        else
        {
            output.push("        if self.location is None:");
            output.push("            self.location = resource_group.location");
        }
        output.push("");
    }

    output.push("        old_response = self.get_resource()");
    output.push("");
    output.push("        if not old_response:");
    output.push("            if self.state == 'present':");
    output.push("                self.to_do = Actions.Create");
    output.push("        else:");
    output.push("            if self.state == 'absent':");
    output.push("                self.to_do = Actions.Delete");
    output.push("            else:");
    output.push("                modifiers = {}");
    output.push("                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)");
    output.push("                self.results['modifiers'] = modifiers");
    output.push("                self.results['compare'] = []");
    output.push("                if not self.default_compare(modifiers, self.body, old_response, '', self.results):");
    output.push("                    self.to_do = Actions.Update");

    if (module.NeedsDeleteBeforeUpdate)
    {
        if (module.NeedsForceUpdate)
        {
            output.push("        if self.to_do == Actions.Update:");
            output.push("            if self.force_update:");
            output.push("                if not self.check_mode:");
            output.push("                    self.delete_resource()");
            output.push("            else:");
            output.push("                self.to_do = Actions.NoAction");
        }
        else
        {
            output.push("        if self.to_do == Actions.Update:");
            output.push("            self.delete_resource()");
        }
    }

    output.push("");
    output.push("        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):");
    output.push("            self.results['changed'] = True");
    output.push("            if self.check_mode:");
    output.push("                return self.results");
    output.push("            response = self.create_update_resource()");
    output = output.concat(module.DeleteResponseNoLogFields);
    output.push("        elif self.to_do == Actions.Delete:");
    output.push("            self.results['changed'] = True");
    output.push("            if self.check_mode:");
    output.push("                return self.results");
    output.push("            self.delete_resource()");
    output.push("        else:");
    output.push("            self.results['changed'] = False");
    output.push("            response = old_response");
    output.push("            self.result['state'] = response");
    output.push("");
    output.push("        return self.results");
    output.push("");
    if (module.GetMethod('create_or_update') != null || module.GetMethod('create') != null){
        output.push("    def create_update_resource(self):");
        output.push("        try:");
        if (module.HasCreateOrUpdate())
        {
            ModuleGenerateApiCall(output, "            ", module, "create_or_update");
        }
        else
        {
            output.push("            if self.to_do == Actions.Create:");
            ModuleGenerateApiCall(output, "                ", module, "create");
            output.push("            else:");
            ModuleGenerateApiCall(output, "                ", module, "update");
        }
        output.push("            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):");
        output.push("                response = self.get_poller_result(response)");
        output.push("        except CloudError as exc:");
        output.push("            self.log('Error attempting to create the " + module.ObjectName + " instance.')");
        output.push("            self.fail('Error creating the " + module.ObjectName + " instance: {0}'.format(str(exc)))");
        output.push("        return response.as_dict()");
        output.push("");
    }
    if (module.GetMethod('delete') != null){
        output.push("    def delete_resource(self):");
        output.push("        try:");

        ModuleGenerateApiCall(output, "            ", module, "delete");

        output.push("        except CloudError as e:");
        output.push("            self.log('Error attempting to delete the " + module.ObjectName + " instance.')");
        output.push("            self.fail('Error deleting the " + module.ObjectName + " instance: {0}'.format(str(e)))");
        output.push("");
        output.push("        return True");
        output.push("");
    }
    output.push("    def get_resource(self):");
    output.push("        try:");
    ModuleGenerateApiCall(output, "            ", module, "get");
    output.push("        except CloudError as e:");
    output.push("            return False");
    output.push("        return response.as_dict()");
    output.push("");
    output.push("");
    AppendMain(output, module);
    return output;
}
