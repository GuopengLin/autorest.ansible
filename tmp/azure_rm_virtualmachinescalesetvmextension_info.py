#!/usr/bin/python
#
# Copyright (c) 2020 GuopengLin, (@t-glin)
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: azure_rm_virtualmachinescalesetvmextension_info
version_added: '2.9'
short_description: Get VirtualMachineScaleSetVMExtension info.
description:
    - Get info of VirtualMachineScaleSetVMExtension.
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    vm_scale_set_name:
        description:
            - The name of the VM scale set.
        required: true
        type: str
    instance_id:
        description:
            - The instance ID of the virtual machine.
        required: true
        type: str
    vm_extension_name:
        description:
            - The name of the virtual machine extension.
        type: str
    expand:
        description:
            - The expand expression to apply on the operation.
        required: true
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get VirtualMachineScaleSet VM extension.
      azure_rm_virtualmachinescalesetvmextension_info: 
        instance_id: '0'
        resource_group_name: myResourceGroup
        vm_extension_name: myVMExtension
        vm_scale_set_name: myvmScaleSet

    - name: List extensions in Vmss instance.
      azure_rm_virtualmachinescalesetvmextension_info: 
        instance_id: '0'
        resource_group_name: myResourceGroup
        vm_scale_set_name: myvmScaleSet

'''

RETURN = '''
virtual_machine_scale_set_vmextensions:
    description: >-
        A list of dict results where the key is the name of the
        VirtualMachineScaleSetVMExtension and the values are the facts for that
        VirtualMachineScaleSetVMExtension.
    returned: always
    type: complex
    contains:
        id:
            description:
                - Resource Id
            type: str
            sample: null
        name:
            description:
                - Resource name
            type: str
            sample: null
        type:
            description:
                - Resource type
            type: str
            sample: null
        location:
            description:
                - Resource location
            returned: always
            type: str
            sample: null
        tags:
            description:
                - Resource tags
            type: dict
            sample: null
        force_update_tag:
            description:
                - >-
                    How the extension handler should be forced to update even if the
                    extension configuration has not changed.
            type: str
            sample: null
        publisher:
            description:
                - The name of the extension handler publisher.
            type: str
            sample: null
        type_properties_type:
            description:
                - >-
                    Specifies the type of the extension; an example is
                    "CustomScriptExtension".
            type: str
            sample: null
        type_handler_version:
            description:
                - Specifies the version of the script handler.
            type: str
            sample: null
        auto_upgrade_minor_version:
            description:
                - >-
                    Indicates whether the extension should use a newer minor version if
                    one is available at deployment time. Once deployed, however, the
                    extension will not upgrade minor versions unless redeployed, even with
                    this property set to true.
            type: bool
            sample: null
        enable_automatic_upgrade:
            description:
                - >-
                    Indicates whether the extension should be automatically upgraded by
                    the platform if there is a newer version of the extension available.
            type: bool
            sample: null
        settings:
            description:
                - Json formatted public settings for the extension.
            type: any
            sample: null
        protected_settings:
            description:
                - >-
                    The extension can contain either protectedSettings or
                    protectedSettingsFromKeyVault or no protected settings at all.
            type: any
            sample: null
        provisioning_state:
            description:
                - 'The provisioning state, which only appears in the response.'
            type: str
            sample: null
        instance_view:
            description:
                - The virtual machine extension instance view.
            type: dict
            sample: null
            contains:
                name:
                    description:
                        - The virtual machine extension name.
                    type: str
                    sample: null
                type:
                    description:
                        - >-
                            Specifies the type of the extension; an example is
                            "CustomScriptExtension".
                    type: str
                    sample: null
                type_handler_version:
                    description:
                        - Specifies the version of the script handler.
                    type: str
                    sample: null
                substatuses:
                    description:
                        - The resource status information.
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            type: str
                            sample: null
                statuses:
                    description:
                        - The resource status information.
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            type: str
                            sample: null
        value:
            description:
                - The list of extensions
            type: list
            sample: null
            contains:
                force_update_tag:
                    description:
                        - >-
                            How the extension handler should be forced to update even if the
                            extension configuration has not changed.
                    type: str
                    sample: null
                publisher:
                    description:
                        - The name of the extension handler publisher.
                    type: str
                    sample: null
                type_properties_type:
                    description:
                        - >-
                            Specifies the type of the extension; an example is
                            "CustomScriptExtension".
                    type: str
                    sample: null
                type_handler_version:
                    description:
                        - Specifies the version of the script handler.
                    type: str
                    sample: null
                auto_upgrade_minor_version:
                    description:
                        - >-
                            Indicates whether the extension should use a newer minor version
                            if one is available at deployment time. Once deployed, however,
                            the extension will not upgrade minor versions unless redeployed,
                            even with this property set to true.
                    type: bool
                    sample: null
                enable_automatic_upgrade:
                    description:
                        - >-
                            Indicates whether the extension should be automatically upgraded
                            by the platform if there is a newer version of the extension
                            available.
                    type: bool
                    sample: null
                settings:
                    description:
                        - Json formatted public settings for the extension.
                    type: any
                    sample: null
                protected_settings:
                    description:
                        - >-
                            The extension can contain either protectedSettings or
                            protectedSettingsFromKeyVault or no protected settings at all.
                    type: any
                    sample: null
                instance_view:
                    description:
                        - The virtual machine extension instance view.
                    type: dict
                    sample: null
                    contains:
                        name:
                            description:
                                - The virtual machine extension name.
                            type: str
                            sample: null
                        type:
                            description:
                                - >-
                                    Specifies the type of the extension; an example is
                                    "CustomScriptExtension".
                            type: str
                            sample: null
                        type_handler_version:
                            description:
                                - Specifies the version of the script handler.
                            type: str
                            sample: null
                        substatuses:
                            description:
                                - The resource status information.
                            type: list
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null
                        statuses:
                            description:
                                - The resource status information.
                            type: list
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualMachineScaleSetVMExtensionInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            vm_scale_set_name=dict(
                type='str',
                required=True
            ),
            instance_id=dict(
                type='str',
                required=True
            ),
            vm_extension_name=dict(
                type='str'
            ),
            expand=dict(
                type='str',
                required=True
            )
        )

        self.resource_group = None
        self.vm_scale_set_name = None
        self.instance_id = None
        self.vm_extension_name = None
        self.expand = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMVirtualMachineScaleSetVMExtensionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.vm_scale_set_name is not None and
            self.instance_id is not None and
            self.vm_extension_name is not None):
            self.results['virtual_machine_scale_set_vmextensions'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.vm_scale_set_name is not None and
              self.instance_id is not None):
            self.results['virtual_machine_scale_set_vmextensions'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vmextensions.get(resource_group=self.resource_group,
                                                                                   vm_scale_set_name=self.vm_scale_set_name,
                                                                                   instance_id=self.instance_id,
                                                                                   vm_extension_name=self.vm_extension_name,
                                                                                   expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vmextensions.list(resource_group=self.resource_group,
                                                                                    vm_scale_set_name=self.vm_scale_set_name,
                                                                                    instance_id=self.instance_id,
                                                                                    expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def format_item(self, item):
        if hasattr(item, 'as_dict'):
            return [item.as_dict()]
        else:
            result = []
            items = list(item)
            for tmp in items:
                result.append(tmp.as_dict())
            return result


def main():
    AzureRMVirtualMachineScaleSetVMExtensionInfo()


if __name__ == '__main__':
    main()
