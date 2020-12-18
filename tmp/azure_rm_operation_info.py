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
module: azure_rm_operation_info
version_added: '2.9'
short_description: Get Operation info.
description:
    - Get info of Operation.
options: {}
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get Registration Operations
      azure_rm_operation_info: 

'''

RETURN = '''
operations:
    description: >-
        A list of dict results where the key is the name of the Operation and the
        values are the facts for that Operation.
    returned: always
    type: complex
    contains:
        value:
            description:
                - List of Microsoft.ManagedServices operations.
            type: list
            sample: null
            contains:
                display:
                    description:
                        - The object that represents the operation.
                    type: dict
                    sample: null
                    contains:
                        provider:
                            description:
                                - 'Service provider: Microsoft.ManagedServices'
                            type: str
                            sample: null
                        resource:
                            description:
                                - >-
                                    Resource on which the operation is performed: Registration
                                    definition, registration assignment etc.
                            type: str
                            sample: null
                        operation:
                            description:
                                - 'Operation type: Read, write, delete, etc.'
                            type: str
                            sample: null
                        description:
                            description:
                                - Description of the operation.
                            type: str
                            sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.managed import ManagedServicesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMOperationInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
        )


        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-02-01-preview'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMOperationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ManagedServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-01-preview')

        else:
            self.results['operations'] = self.format_item(self.list())
        return self.results

    def list(self):
        response = None

        try:
            response = self.mgmt_client.operations.list()
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
    AzureRMOperationInfo()


if __name__ == '__main__':
    main()
