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
module: azure_rm_diskaccesse
version_added: '2.9'
short_description: Manage Azure DiskAccesse instance.
description:
    - 'Create, update and delete instance of Azure DiskAccesse.'
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    disk_access_name:
        description:
            - >-
                The name of the disk access resource that is being created. The name
                can't be changed after the disk encryption set is created. Supported
                characters for the name are a-z, A-Z, 0-9 and _. The maximum name length
                is 80 characters.
        required: true
        type: str
    private_endpoint_connections:
        description:
            - >-
                A readonly collection of private endpoint connections created on the
                disk. Currently only one endpoint connection is supported.
        type: list
        suboptions:
            private_link_service_connection_state:
                description:
                    - >-
                        A collection of information about the state of the connection
                        between DiskAccess and Virtual Network.
                type: dict
                suboptions:
                    status:
                        description:
                            - >-
                                Indicates whether the connection has been
                                Approved/Rejected/Removed by the owner of the service.
                        type: str
                        choices:
                            - Pending
                            - Approved
                            - Rejected
                    description:
                        description:
                            - The reason for approval/rejection of the connection.
                        type: str
                    actions_required:
                        description:
                            - >-
                                A message indicating if changes on the service provider require
                                any updates on the consumer.
                        type: str
    state:
        description:
            - Assert the state of the DiskAccesse.
            - >-
                Use C(present) to create or update an DiskAccesse and C(absent) to
                delete it.
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
    - name: Create a disk access resource.
      azure_rm_diskaccesse: 
        disk_access_name: myDiskAccess
        resource_group_name: myResourceGroup

    - name: Update a disk access resource.
      azure_rm_diskaccesse: 
        disk_access_name: myDiskAccess
        resource_group_name: myResourceGroup

    - name: Delete a disk access resource.
      azure_rm_diskaccesse: 
        disk_access_name: myDiskAccess
        resource_group_name: myResourceGroup

'''

RETURN = '''
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
private_endpoint_connections:
    description:
        - >-
            A readonly collection of private endpoint connections created on the disk.
            Currently only one endpoint connection is supported.
    type: list
    sample: null
    contains:
        private_link_service_connection_state:
            description:
                - >-
                    A collection of information about the state of the connection between
                    DiskAccess and Virtual Network.
            type: dict
            sample: null
            contains:
                status:
                    description:
                        - >-
                            Indicates whether the connection has been
                            Approved/Rejected/Removed by the owner of the service.
                    type: str
                    sample: null
                description:
                    description:
                        - The reason for approval/rejection of the connection.
                    type: str
                    sample: null
                actions_required:
                    description:
                        - >-
                            A message indicating if changes on the service provider require
                            any updates on the consumer.
                    type: str
                    sample: null
provisioning_state:
    description:
        - The disk access resource provisioning state.
    type: str
    sample: null
time_created:
    description:
        - The time when the disk access was created.
    type: str
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


class AzureRMDiskAccesse(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            disk_access_name=dict(
                type='str',
                required=True
            ),
            private_endpoint_connections=dict(
                type='list',
                updatable=False,
                disposition='/private_endpoint_connections',
                elements='dict',
                options=dict(
                    private_link_service_connection_state=dict(
                        type='dict',
                        disposition='private_link_service_connection_state',
                        options=dict(
                            status=dict(
                                type='str',
                                disposition='status',
                                choices=['Pending',
                                         'Approved',
                                         'Rejected']
                            ),
                            description=dict(
                                type='str',
                                disposition='description'
                            ),
                            actions_required=dict(
                                type='str',
                                disposition='actions_required'
                            )
                        )
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.disk_access_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDiskAccesse, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2020-06-30')

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

    def create_update_resource(self):
        try:
            response = self.mgmt_client.disk_accesses.create_or_update(resource_group=self.resource_group,
                                                                       disk_access_name=self.disk_access_name,
                                                                       disk_access=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DiskAccesse instance.')
            self.fail('Error creating the DiskAccesse instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.disk_accesses.delete(resource_group=self.resource_group,
                                                             disk_access_name=self.disk_access_name)
        except CloudError as e:
            self.log('Error attempting to delete the DiskAccesse instance.')
            self.fail('Error deleting the DiskAccesse instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.disk_accesses.get(resource_group=self.resource_group,
                                                          disk_access_name=self.disk_access_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDiskAccesse()


if __name__ == '__main__':
    main()
