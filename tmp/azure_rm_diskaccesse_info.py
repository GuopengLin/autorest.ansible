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
    module: azure_rm_diskaccesse_info
    version_added: '2.9'
    short_description: Get DiskAccesse info.
    description:
      - Get info of DiskAccesse.
    options:
      resource_group:
        description:
          - The name of the resource group.
        type: str
      disk_access_name:
        description:
          - >-
            The name of the disk access resource that is being created. The name
            can't be changed after the disk encryption set is created. Supported
            characters for the name are a-z, A-Z, 0-9 and _. The maximum name length
            is 80 characters.
        type: str
    extends_documentation_fragment:
      - azure.azcollection.azure
      - azure.azcollection.azure_tags
    author:
      - GuopengLin (@t-glin)
    
'''

EXAMPLES = '''
    - name: Get information about a disk access resource with private endpoints.
      azure_rm_diskaccesse_info: 
        disk_access_name: myDiskAccess
        resource_group_name: myResourceGroup
        

    - name: Get information about a disk access resource.
      azure_rm_diskaccesse_info: 
        disk_access_name: myDiskAccess
        resource_group_name: myResourceGroup
        

    - name: List all disk access resources in a resource group.
      azure_rm_diskaccesse_info: 
        resource_group_name: myResourceGroup
        

    - name: List all disk access resources in a subscription.
      azure_rm_diskaccesse_info: 

    - name: List all possible private link resources under disk access resource.
      azure_rm_diskaccesse_info: 
        disk_access_name: myDiskAccess
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
    disk_accesses:
      description: >-
        A list of dict results where the key is the name of the DiskAccesse and the
        values are the facts for that DiskAccesse.
      returned: always
      type: complex
      contains:
        id:
          description:
            - Resource Id
          returned: always
          type: str
          sample: null
        name:
          description:
            - Resource name
          returned: always
          type: str
          sample: null
        type:
          description:
            - Resource type
          returned: always
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
          returned: always
          type: dict
          sample: null
        private_endpoint_connections:
          description:
            - >-
              A readonly collection of private endpoint connections created on the
              disk. Currently only one endpoint connection is supported.
          returned: always
          type: list
          sample: null
          contains:
            private_link_service_connection_state:
              description:
                - >-
                  A collection of information about the state of the connection
                  between DiskAccess and Virtual Network.
              returned: always
              type: dict
              sample: null
              contains:
                status:
                  description:
                    - >-
                      Indicates whether the connection has been
                      Approved/Rejected/Removed by the owner of the service.
                  returned: always
                  type: str
                  sample: null
                description:
                  description:
                    - The reason for approval/rejection of the connection.
                  returned: always
                  type: str
                  sample: null
                actions_required:
                  description:
                    - >-
                      A message indicating if changes on the service provider
                      require any updates on the consumer.
                  returned: always
                  type: str
                  sample: null
        provisioning_state:
          description:
            - The disk access resource provisioning state.
          returned: always
          type: str
          sample: null
        time_created:
          description:
            - The time when the disk access was created.
          returned: always
          type: str
          sample: null
        value:
          description:
            - |-
              A list of disk access resources.
              Array of private link resources
          returned: always
          type: list
          sample: null
          contains:
            private_endpoint_connections:
              description:
                - >-
                  A readonly collection of private endpoint connections created on
                  the disk. Currently only one endpoint connection is supported.
              returned: always
              type: list
              sample: null
              contains:
                private_link_service_connection_state:
                  description:
                    - >-
                      A collection of information about the state of the connection
                      between DiskAccess and Virtual Network.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    status:
                      description:
                        - >-
                          Indicates whether the connection has been
                          Approved/Rejected/Removed by the owner of the service.
                      returned: always
                      type: str
                      sample: null
                    description:
                      description:
                        - The reason for approval/rejection of the connection.
                      returned: always
                      type: str
                      sample: null
                    actions_required:
                      description:
                        - >-
                          A message indicating if changes on the service provider
                          require any updates on the consumer.
                      returned: always
                      type: str
                      sample: null
        next_link:
          description:
            - >-
              The uri to fetch the next page of disk access resources. Call
              ListNext() with this to fetch the next page of disk access resources.
          returned: always
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


class AzureRMDiskAccesseInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            disk_access_name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.disk_access_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2020-06-30'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMDiskAccesseInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-30')

        if (self.resource_group is not None and
            self.disk_access_name is not None):
            self.results['disk_accesses'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.disk_access_name is not None):
            self.results['disk_accesses'] = self.format_item(self.get_private_link_resources())
        elif (self.resource_group is not None):
            self.results['disk_accesses'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['disk_accesses'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.disk_accesses.get(resource_group=self.resource_group,
                                                          disk_access_name=self.disk_access_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get_private_link_resources(self):
        response = None

        try:
            response = self.mgmt_client.disk_accesses.get_private_link_resources(resource_group=self.resource_group,
                                                                                 disk_access_name=self.disk_access_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.disk_accesses.list_by_resource_group(resource_group=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.disk_accesses.list()
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
    AzureRMDiskAccesseInfo()


if __name__ == '__main__':
    main()
