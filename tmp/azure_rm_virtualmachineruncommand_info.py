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
    module: azure_rm_virtualmachineruncommand_info
    version_added: '2.9'
    short_description: Get VirtualMachineRunCommand info.
    description:
      - Get info of VirtualMachineRunCommand.
    options:
      location:
        description:
          - The location upon which run commands is queried.
        required: true
        type: str
      command_id:
        description:
          - The command id.
        type: str
    extends_documentation_fragment:
      - azure.azcollection.azure
      - azure.azcollection.azure_tags
    author:
      - GuopengLin (@t-glin)
    
'''

EXAMPLES = '''
    - name: VirtualMachineRunCommandList
      azure_rm_virtualmachineruncommand_info: 
        location: SoutheastAsia
        

    - name: VirtualMachineRunCommandGet
      azure_rm_virtualmachineruncommand_info: 
        command_id: RunPowerShellScript
        location: SoutheastAsia
        

'''

RETURN = '''
    virtual_machine_run_commands:
      description: >-
        A list of dict results where the key is the name of the
        VirtualMachineRunCommand and the values are the facts for that
        VirtualMachineRunCommand.
      returned: always
      type: complex
      contains:
        value:
          description:
            - The list of virtual machine run commands.
          returned: always
          type: list
          sample: null
          contains:
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
        next_link:
          description:
            - >-
              The uri to fetch the next page of run commands. Call ListNext() with
              this to fetch the next page of run commands.
          returned: always
          type: str
          sample: null
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
          returned: always
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
              returned: always
              type: str
              sample: null
            required:
              description:
                - The run command parameter required.
              returned: always
              type: bool
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


class AzureRMVirtualMachineRunCommandInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            command_id=dict(
                type='str'
            )
        )

        self.location = None
        self.command_id = None

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
        super(AzureRMVirtualMachineRunCommandInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.location is not None and
            self.command_id is not None):
            self.results['virtual_machine_run_commands'] = self.format_item(self.get())
        elif (self.location is not None):
            self.results['virtual_machine_run_commands'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_run_commands.get(location=self.location,
                                                                         command_id=self.command_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_run_commands.list(location=self.location)
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
    AzureRMVirtualMachineRunCommandInfo()


if __name__ == '__main__':
    main()
