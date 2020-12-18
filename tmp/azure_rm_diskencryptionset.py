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
module: azure_rm_diskencryptionset
version_added: '2.9'
short_description: Manage Azure DiskEncryptionSet instance.
description:
    - 'Create, update and delete instance of Azure DiskEncryptionSet.'
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    disk_encryption_set_name:
        description:
            - >-
                The name of the disk encryption set that is being created. The name
                can't be changed after the disk encryption set is created. Supported
                characters for the name are a-z, A-Z, 0-9 and _. The maximum name length
                is 80 characters.
        required: true
        type: str
    identity:
        description:
            - >-
                The managed identity for the disk encryption set. It should be given
                permission on the key vault before it can be used to encrypt disks.
        type: dict
        suboptions:
            type:
                description:
                    - >-
                        The type of Managed Identity used by the DiskEncryptionSet. Only
                        SystemAssigned is supported.
                type: str
                choices:
                    - SystemAssigned
    encryption_type:
        description:
            - The type of key used to encrypt the data of the disk.
        type: str
        choices:
            - EncryptionAtRestWithCustomerKey
            - EncryptionAtRestWithPlatformAndCustomerKeys
    active_key:
        description:
            - The key vault key which is currently used by this disk encryption set.
            - >-
                Key Vault Key Url and vault id of KeK, KeK is optional and when provided
                is used to unwrap the encryptionKey
        type: dict
        suboptions:
            source_vault:
                description:
                    - Resource id of the KeyVault containing the key or secret
                required: true
                type: dict
                suboptions:
                    id:
                        description:
                            - Resource Id
                        type: str
            key_url:
                description:
                    - Url pointing to a key or secret in KeyVault
                required: true
                type: str
    previous_keys:
        description:
            - >-
                A readonly collection of key vault keys previously used by this disk
                encryption set while a key rotation is in progress. It will be empty if
                there is no ongoing key rotation.
        type: list
        suboptions:
            source_vault:
                description:
                    - Resource id of the KeyVault containing the key or secret
                required: true
                type: dict
                suboptions:
                    id:
                        description:
                            - Resource Id
                        type: str
            key_url:
                description:
                    - Url pointing to a key or secret in KeyVault
                required: true
                type: str
    state:
        description:
            - Assert the state of the DiskEncryptionSet.
            - >-
                Use C(present) to create or update an DiskEncryptionSet and C(absent) to
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
    - name: Create a disk encryption set.
      azure_rm_diskencryptionset: 
        disk_encryption_set_name: myDiskEncryptionSet
        resource_group_name: myResourceGroup

    - name: Update a disk encryption set.
      azure_rm_diskencryptionset: 
        disk_encryption_set_name: myDiskEncryptionSet
        resource_group_name: myResourceGroup

    - name: Delete a disk encryption set.
      azure_rm_diskencryptionset: 
        disk_encryption_set_name: myDiskEncryptionSet
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
identity:
    description:
        - >-
            The managed identity for the disk encryption set. It should be given
            permission on the key vault before it can be used to encrypt disks.
    type: dict
    sample: null
    contains:
        type:
            description:
                - >-
                    The type of Managed Identity used by the DiskEncryptionSet. Only
                    SystemAssigned is supported.
            type: str
            sample: null
encryption_type:
    description:
        - The type of key used to encrypt the data of the disk.
    type: str
    sample: null
active_key:
    description:
        - The key vault key which is currently used by this disk encryption set.
    type: dict
    sample: null
    contains:
        source_vault:
            description:
                - Resource id of the KeyVault containing the key or secret
            returned: always
            type: dict
            sample: null
            contains:
                id:
                    description:
                        - Resource Id
                    type: str
                    sample: null
        key_url:
            description:
                - Url pointing to a key or secret in KeyVault
            returned: always
            type: str
            sample: null
previous_keys:
    description:
        - >-
            A readonly collection of key vault keys previously used by this disk
            encryption set while a key rotation is in progress. It will be empty if
            there is no ongoing key rotation.
    type: list
    sample: null
    contains:
        source_vault:
            description:
                - Resource id of the KeyVault containing the key or secret
            returned: always
            type: dict
            sample: null
            contains:
                id:
                    description:
                        - Resource Id
                    type: str
                    sample: null
        key_url:
            description:
                - Url pointing to a key or secret in KeyVault
            returned: always
            type: str
            sample: null
provisioning_state:
    description:
        - The disk encryption set provisioning state.
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


class AzureRMDiskEncryptionSet(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            disk_encryption_set_name=dict(
                type='str',
                required=True
            ),
            identity=dict(
                type='dict',
                disposition='/identity',
                options=dict(
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['SystemAssigned']
                    )
                )
            ),
            encryption_type=dict(
                type='str',
                disposition='/encryption_type',
                choices=['EncryptionAtRestWithCustomerKey',
                         'EncryptionAtRestWithPlatformAndCustomerKeys']
            ),
            active_key=dict(
                type='dict',
                disposition='/active_key',
                options=dict(
                    source_vault=dict(
                        type='dict',
                        disposition='source_vault',
                        required=True,
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    key_url=dict(
                        type='str',
                        disposition='key_url',
                        required=True
                    )
                )
            ),
            previous_keys=dict(
                type='list',
                updatable=False,
                disposition='/previous_keys',
                elements='dict',
                options=dict(
                    source_vault=dict(
                        type='dict',
                        disposition='source_vault',
                        required=True,
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    key_url=dict(
                        type='str',
                        disposition='key_url',
                        required=True
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
        self.disk_encryption_set_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDiskEncryptionSet, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.disk_encryption_sets.create_or_update(resource_group=self.resource_group,
                                                                              disk_encryption_set_name=self.disk_encryption_set_name,
                                                                              disk_encryption_set=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DiskEncryptionSet instance.')
            self.fail('Error creating the DiskEncryptionSet instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.disk_encryption_sets.delete(resource_group=self.resource_group,
                                                                    disk_encryption_set_name=self.disk_encryption_set_name)
        except CloudError as e:
            self.log('Error attempting to delete the DiskEncryptionSet instance.')
            self.fail('Error deleting the DiskEncryptionSet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.disk_encryption_sets.get(resource_group=self.resource_group,
                                                                 disk_encryption_set_name=self.disk_encryption_set_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDiskEncryptionSet()


if __name__ == '__main__':
    main()
