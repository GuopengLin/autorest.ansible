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
module: azure_rm_virtualmachineruncommand
version_added: '2.9'
short_description: Manage Azure VirtualMachineRunCommand instance.
description:
    - 'Create, update and delete instance of Azure VirtualMachineRunCommand.'
options:
    location:
        description:
            - The location upon which run commands is queried.
        required: true
        type: str
    command_id:
        description:
            - The command id.
        required: true
        type: str
    state:
        description:
            - Assert the state of the VirtualMachineRunCommand.
            - >-
                Use C(present) to create or update an VirtualMachineRunCommand and
                C(absent) to delete it.
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
schema:
    description:
        - The VM run command schema.
    returned: always
    type: str
    sample: null
id:
    description:
        - The VM run command id.
    returned: always
    type: str
    sample: null
os_type:
    description:
        - The Operating System type.
    returned: always
    type: sealed-choice
    sample: null
label:
    description:
        - The VM run command label.
    returned: always
    type: str
    sample: null
description:
    description:
        - The VM run command description.
    returned: always
    type: str
    sample: null
script:
    description:
        - The script to be executed.
    returned: always
    type: list
    sample: null
parameters:
    description:
        - The parameters used by the script.
    type: list
    sample: null
    contains:
        name:
            description:
                - The run command parameter name.
            returned: always
            type: str
            sample: null
        type:
            description:
                - The run command parameter type.
            returned: always
            type: str
            sample: null
        default_value:
            description:
                - The run command parameter default value.
            type: str
            sample: null
        required:
            description:
                - The run command parameter required.
            type: bool
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


class AzureRMVirtualMachineRunCommand(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            command_id=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.location = None
        self.command_id = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineRunCommand, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            self.result['state'] = response

        return self.results

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_run_commands.get(location=self.location,
                                                                         command_id=self.command_id)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineRunCommand()


if __name__ == '__main__':
    main()
