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
    module: azure_rm_virtualmachinescalesetextension
    version_added: '2.9'
    short_description: Manage Azure VirtualMachineScaleSetExtension instance.
    description:
      - 'Create, update and delete instance of Azure VirtualMachineScaleSetExtension.'
    options:
      resource_group:
        description:
          - The name of the resource group.
        required: true
        type: str
      vm_scale_set_name:
        description:
          - >-
            The name of the VM scale set where the extension should be create or
            updated.
          - The name of the VM scale set where the extension should be updated.
          - The name of the VM scale set where the extension should be deleted.
          - The name of the VM scale set containing the extension.
        required: true
        type: str
      vmss_extension_name:
        description:
          - The name of the VM scale set extension.
        required: true
        type: str
      name:
        description:
          - The name of the extension.
        type: str
      force_update_tag:
        description:
          - >-
            If a value is provided and is different from the previous value, the
            extension handler will be forced to update even if the extension
            configuration has not changed.
        type: str
      publisher:
        description:
          - The name of the extension handler publisher.
        type: str
      type_properties_type:
        description:
          - >-
            Specifies the type of the extension; an example is
            "CustomScriptExtension".
        type: str
      type_handler_version:
        description:
          - Specifies the version of the script handler.
        type: str
      auto_upgrade_minor_version:
        description:
          - >-
            Indicates whether the extension should use a newer minor version if one
            is available at deployment time. Once deployed, however, the extension
            will not upgrade minor versions unless redeployed, even with this
            property set to true.
        type: bool
      enable_automatic_upgrade:
        description:
          - >-
            Indicates whether the extension should be automatically upgraded by the
            platform if there is a newer version of the extension available.
        type: bool
      settings:
        description:
          - Json formatted public settings for the extension.
        type: any
      protected_settings:
        description:
          - >-
            The extension can contain either protectedSettings or
            protectedSettingsFromKeyVault or no protected settings at all.
        type: any
      provision_after_extensions:
        description:
          - >-
            Collection of extension names after which this extension needs to be
            provisioned.
        type: list
      expand:
        description:
          - The expand expression to apply on the operation.
        type: str
      state:
        description:
          - Assert the state of the VirtualMachineScaleSetExtension.
          - >-
            Use C(present) to create or update an VirtualMachineScaleSetExtension
            and C(absent) to delete it.
        default: present
        choices:
          - absent
          - present
    extends_documentation_fragment:
      - azure.azcollection.azure
      - azure.azcollection.azure_tags
    author:
      - GuopengLin (@t-glin)
    
'''

EXAMPLES = '''
'''

RETURN = '''
    id:
      description:
        - Resource Id
      returned: always
      type: str
      sample: null
    name:
      description:
        - The name of the extension.
      returned: always
      type: str
      sample: null
    type:
      description:
        - Resource type
      returned: always
      type: str
      sample: null
    force_update_tag:
      description:
        - >-
          If a value is provided and is different from the previous value, the
          extension handler will be forced to update even if the extension
          configuration has not changed.
      returned: always
      type: str
      sample: null
    publisher:
      description:
        - The name of the extension handler publisher.
      returned: always
      type: str
      sample: null
    type_properties_type:
      description:
        - >-
          Specifies the type of the extension; an example is
          "CustomScriptExtension".
      returned: always
      type: str
      sample: null
    type_handler_version:
      description:
        - Specifies the version of the script handler.
      returned: always
      type: str
      sample: null
    auto_upgrade_minor_version:
      description:
        - >-
          Indicates whether the extension should use a newer minor version if one is
          available at deployment time. Once deployed, however, the extension will
          not upgrade minor versions unless redeployed, even with this property set
          to true.
      returned: always
      type: bool
      sample: null
    enable_automatic_upgrade:
      description:
        - >-
          Indicates whether the extension should be automatically upgraded by the
          platform if there is a newer version of the extension available.
      returned: always
      type: bool
      sample: null
    settings:
      description:
        - Json formatted public settings for the extension.
      returned: always
      type: any
      sample: null
    protected_settings:
      description:
        - >-
          The extension can contain either protectedSettings or
          protectedSettingsFromKeyVault or no protected settings at all.
      returned: always
      type: any
      sample: null
    provisioning_state:
      description:
        - 'The provisioning state, which only appears in the response.'
      returned: always
      type: str
      sample: null
    provision_after_extensions:
      description:
        - >-
          Collection of extension names after which this extension needs to be
          provisioned.
      returned: always
      type: list
      sample: null
    
'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMVirtualMachineScaleSetExtension(AzureRMModuleBaseExt):
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
            vmss_extension_name=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                disposition='/name'
            ),
            force_update_tag=dict(
                type='str',
                disposition='/force_update_tag'
            ),
            publisher=dict(
                type='str',
                disposition='/publisher'
            ),
            type_properties_type=dict(
                type='str',
                disposition='/type_properties_type'
            ),
            type_handler_version=dict(
                type='str',
                disposition='/type_handler_version'
            ),
            auto_upgrade_minor_version=dict(
                type='bool',
                disposition='/auto_upgrade_minor_version'
            ),
            enable_automatic_upgrade=dict(
                type='bool',
                disposition='/enable_automatic_upgrade'
            ),
            settings=dict(
                type='any',
                disposition='/settings'
            ),
            protected_settings=dict(
                type='any',
                disposition='/protected_settings'
            ),
            provision_after_extensions=dict(
                type='list',
                disposition='/provision_after_extensions',
                elements='str'
            ),
            expand=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.vm_scale_set_name = None
        self.vmss_extension_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineScaleSetExtension, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                                     supports_check_mode=True,
                                                                     supports_tags=True)

    def exec_module(self, **kwargs):
        for key in list(self.module_arg_spec.keys()):
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
            elif kwargs[key] is not None:
                self.body[key] = kwargs[key]

        self.inflate_parameters(self.module_arg_spec, self.body, 0)

        old_response = None
        response = None

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        old_response = self.get_resource()

        if not old_response:
            if self.state == 'present':
                self.to_do = Actions.Create
        else:
            if self.state == 'absent':
                self.to_do = Actions.Delete
            else:
                modifiers = {}
                self.create_compare_modifiers(self.module_arg_spec, '', modifiers)
                self.results['modifiers'] = modifiers
                self.results['compare'] = []
                if not self.default_compare(modifiers, self.body, old_response, '', self.results):
                    self.to_do = Actions.Update

        if (self.to_do == Actions.Create) or (self.to_do == Actions.Update):
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            response = self.create_update_resource()
        elif self.to_do == Actions.Delete:
            self.results['changed'] = True
            if self.check_mode:
                return self.results
            self.delete_resource()
        else:
            self.results['changed'] = False
            response = old_response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_scale_set_extensions.create_or_update(resource_group=self.resource_group,
                                                                                              vm_scale_set_name=self.vm_scale_set_name,
                                                                                              vmss_extension_name=self.vmss_extension_name,
                                                                                              extension_parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineScaleSetExtension instance.')
            self.fail('Error creating the VirtualMachineScaleSetExtension instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_scale_set_extensions.delete(resource_group=self.resource_group,
                                                                                    vm_scale_set_name=self.vm_scale_set_name,
                                                                                    vmss_extension_name=self.vmss_extension_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineScaleSetExtension instance.')
            self.fail('Error deleting the VirtualMachineScaleSetExtension instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_scale_set_extensions.get(resource_group=self.resource_group,
                                                                                 vm_scale_set_name=self.vm_scale_set_name,
                                                                                 vmss_extension_name=self.vmss_extension_name,
                                                                                 expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineScaleSetExtension()


if __name__ == '__main__':
    main()
