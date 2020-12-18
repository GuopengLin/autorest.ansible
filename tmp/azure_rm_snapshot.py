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
module: azure_rm_snapshot
version_added: '2.9'
short_description: Manage Azure Snapshot instance.
description:
    - 'Create, update and delete instance of Azure Snapshot.'
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    name:
        description:
            - >-
                The name of the snapshot that is being created. The name can't be
                changed after the snapshot is created. Supported characters for the name
                are a-z, A-Z, 0-9 and _. The max name length is 80 characters.
        required: true
        type: str
    sku:
        description:
            - >-
                The snapshots sku name. Can be Standard_LRS, Premium_LRS, or
                Standard_ZRS.
        type: dict
        suboptions:
            name:
                description:
                    - The sku name.
                type: str
                choices:
                    - Standard_LRS
                    - Premium_LRS
                    - Standard_ZRS
    os_type:
        description:
            - The Operating System type.
            - the Operating System type.
        type: sealed-choice
    hyper_v_generation:
        description:
            - >-
                The hypervisor generation of the Virtual Machine. Applicable to OS disks
                only.
        type: str
        choices:
            - V1
            - V2
    creation_data:
        description:
            - >-
                Disk source information. CreationData information cannot be changed
                after the disk has been created.
        type: dict
        suboptions:
            create_option:
                description:
                    - This enumerates the possible sources of a disk's creation.
                required: true
                type: str
                choices:
                    - Empty
                    - Attach
                    - FromImage
                    - Import
                    - Copy
                    - Restore
                    - Upload
            storage_account_id:
                description:
                    - >-
                        Required if createOption is Import. The Azure Resource Manager
                        identifier of the storage account containing the blob to import as a
                        disk.
                type: str
            image_reference:
                description:
                    - Disk source information.
                type: dict
                suboptions:
                    id:
                        description:
                            - >-
                                A relative uri containing either a Platform Image Repository or
                                user image reference.
                        required: true
                        type: str
                    lun:
                        description:
                            - >-
                                If the disk is created from an image's data disk, this is an
                                index that indicates which of the data disks in the image to
                                use. For OS disks, this field is null.
                        type: int
            gallery_image_reference:
                description:
                    - >-
                        Required if creating from a Gallery Image. The id of the
                        ImageDiskReference will be the ARM id of the shared galley image
                        version from which to create a disk.
                type: dict
                suboptions:
                    id:
                        description:
                            - >-
                                A relative uri containing either a Platform Image Repository or
                                user image reference.
                        required: true
                        type: str
                    lun:
                        description:
                            - >-
                                If the disk is created from an image's data disk, this is an
                                index that indicates which of the data disks in the image to
                                use. For OS disks, this field is null.
                        type: int
            source_uri:
                description:
                    - >-
                        If createOption is Import, this is the URI of a blob to be imported
                        into a managed disk.
                type: str
            source_resource_id:
                description:
                    - >-
                        If createOption is Copy, this is the ARM id of the source snapshot
                        or disk.
                type: str
            upload_size_bytes:
                description:
                    - >-
                        If createOption is Upload, this is the size of the contents of the
                        upload including the VHD footer. This value should be between
                        20972032 (20 MiB + 512 bytes for the VHD footer) and 35183298347520
                        bytes (32 TiB + 512 bytes for the VHD footer).
                type: int
            logical_sector_size:
                description:
                    - >-
                        Logical sector size in bytes for Ultra disks. Supported values are
                        512 ad 4096. 4096 is the default.
                type: int
    disk_size_gb:
        description:
            - >-
                If creationData.createOption is Empty, this field is mandatory and it
                indicates the size of the disk to create. If this field is present for
                updates or creation with other options, it indicates a resize. Resizes
                are only allowed if the disk is not attached to a running VM, and can
                only increase the disk's size.
        type: int
    encryption_settings_collection:
        description:
            - >-
                Encryption settings collection used be Azure Disk Encryption, can
                contain multiple encryption settings per disk or snapshot.
        type: dict
        suboptions:
            enabled:
                description:
                    - >-
                        Set this flag to true and provide DiskEncryptionKey and optional
                        KeyEncryptionKey to enable encryption. Set this flag to false and
                        remove DiskEncryptionKey and KeyEncryptionKey to disable encryption.
                        If EncryptionSettings is null in the request object, the existing
                        settings remain unchanged.
                required: true
                type: bool
            encryption_settings:
                description:
                    - 'A collection of encryption settings, one for each disk volume.'
                type: list
                suboptions:
                    disk_encryption_key:
                        description:
                            - Key Vault Secret Url and vault id of the disk encryption key
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
                            secret_url:
                                description:
                                    - Url pointing to a key or secret in KeyVault
                                required: true
                                type: str
                    key_encryption_key:
                        description:
                            - >-
                                Key Vault Key Url and vault id of the key encryption key.
                                KeyEncryptionKey is optional and when provided is used to unwrap
                                the disk encryption key.
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
            encryption_settings_version:
                description:
                    - >-
                        Describes what type of encryption is used for the disks. Once this
                        field is set, it cannot be overwritten. '1.0' corresponds to Azure
                        Disk Encryption with AAD app.'1.1' corresponds to Azure Disk
                        Encryption.
                type: str
    incremental:
        description:
            - >-
                Whether a snapshot is incremental. Incremental snapshots on the same
                disk occupy less space than full snapshots and can be diffed.
        type: bool
    encryption:
        description:
            - >-
                Encryption property can be used to encrypt data at rest with customer
                managed keys or platform managed keys.
        type: dict
        suboptions:
            disk_encryption_set_id:
                description:
                    - >-
                        ResourceId of the disk encryption set to use for enabling encryption
                        at rest.
                type: str
            type:
                description:
                    - The type of key used to encrypt the data of the disk.
                type: str
                choices:
                    - EncryptionAtRestWithPlatformKey
                    - EncryptionAtRestWithCustomerKey
                    - EncryptionAtRestWithPlatformAndCustomerKeys
    network_access_policy:
        description:
            - Policy for accessing the disk via network.
        type: str
        choices:
            - AllowAll
            - AllowPrivate
            - DenyAll
    disk_access_id:
        description:
            - ARM id of the DiskAccess resource for using private endpoints on disks.
        type: str
    state:
        description:
            - Assert the state of the Snapshot.
            - >-
                Use C(present) to create or update an Snapshot and C(absent) to delete
                it.
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
    - name: Create a snapshot by importing an unmanaged blob from a different subscription.
      azure_rm_snapshot: 
        resource_group_name: myResourceGroup
        snapshot_name: mySnapshot1
        location: West US
        properties:
          creation_data:
            create_option: Import
            source_uri: 'https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd'
            storage_account_id: >-
              subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Storage/storageAccounts/myStorageAccount

    - name: Create a snapshot by importing an unmanaged blob from the same subscription.
      azure_rm_snapshot: 
        resource_group_name: myResourceGroup
        snapshot_name: mySnapshot1
        location: West US
        properties:
          creation_data:
            create_option: Import
            source_uri: 'https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd'

    - name: Create a snapshot from an existing snapshot in the same or a different subscription.
      azure_rm_snapshot: 
        resource_group_name: myResourceGroup
        snapshot_name: mySnapshot2
        location: West US
        properties:
          creation_data:
            create_option: Copy
            source_resource_id: >-
              subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot1

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
managed_by:
    description:
        - Unused. Always Null.
    type: str
    sample: null
sku:
    description:
        - 'The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS.'
    type: dict
    sample: null
    contains:
        name:
            description:
                - The sku name.
            type: str
            sample: null
time_created:
    description:
        - The time when the snapshot was created.
    type: str
    sample: null
os_type:
    description:
        - The Operating System type.
    type: sealed-choice
    sample: null
hyper_v_generation:
    description:
        - >-
            The hypervisor generation of the Virtual Machine. Applicable to OS disks
            only.
    type: str
    sample: null
creation_data:
    description:
        - >-
            Disk source information. CreationData information cannot be changed after
            the disk has been created.
    type: dict
    sample: null
    contains:
        create_option:
            description:
                - This enumerates the possible sources of a disk's creation.
            returned: always
            type: str
            sample: null
        storage_account_id:
            description:
                - >-
                    Required if createOption is Import. The Azure Resource Manager
                    identifier of the storage account containing the blob to import as a
                    disk.
            type: str
            sample: null
        image_reference:
            description:
                - Disk source information.
            type: dict
            sample: null
            contains:
                id:
                    description:
                        - >-
                            A relative uri containing either a Platform Image Repository or
                            user image reference.
                    returned: always
                    type: str
                    sample: null
                lun:
                    description:
                        - >-
                            If the disk is created from an image's data disk, this is an index
                            that indicates which of the data disks in the image to use. For OS
                            disks, this field is null.
                    type: int
                    sample: null
        gallery_image_reference:
            description:
                - >-
                    Required if creating from a Gallery Image. The id of the
                    ImageDiskReference will be the ARM id of the shared galley image
                    version from which to create a disk.
            type: dict
            sample: null
            contains:
                id:
                    description:
                        - >-
                            A relative uri containing either a Platform Image Repository or
                            user image reference.
                    returned: always
                    type: str
                    sample: null
                lun:
                    description:
                        - >-
                            If the disk is created from an image's data disk, this is an index
                            that indicates which of the data disks in the image to use. For OS
                            disks, this field is null.
                    type: int
                    sample: null
        source_uri:
            description:
                - >-
                    If createOption is Import, this is the URI of a blob to be imported
                    into a managed disk.
            type: str
            sample: null
        source_resource_id:
            description:
                - >-
                    If createOption is Copy, this is the ARM id of the source snapshot or
                    disk.
            type: str
            sample: null
        upload_size_bytes:
            description:
                - >-
                    If createOption is Upload, this is the size of the contents of the
                    upload including the VHD footer. This value should be between 20972032
                    (20 MiB + 512 bytes for the VHD footer) and 35183298347520 bytes (32
                    TiB + 512 bytes for the VHD footer).
            type: int
            sample: null
        logical_sector_size:
            description:
                - >-
                    Logical sector size in bytes for Ultra disks. Supported values are 512
                    ad 4096. 4096 is the default.
            type: int
            sample: null
disk_size_gb:
    description:
        - >-
            If creationData.createOption is Empty, this field is mandatory and it
            indicates the size of the disk to create. If this field is present for
            updates or creation with other options, it indicates a resize. Resizes are
            only allowed if the disk is not attached to a running VM, and can only
            increase the disk's size.
    type: int
    sample: null
disk_size_bytes:
    description:
        - The size of the disk in bytes. This field is read only.
    type: int
    sample: null
disk_state:
    description:
        - The state of the snapshot.
    type: str
    sample: null
unique_id:
    description:
        - Unique Guid identifying the resource.
    type: str
    sample: null
encryption_settings_collection:
    description:
        - >-
            Encryption settings collection used be Azure Disk Encryption, can contain
            multiple encryption settings per disk or snapshot.
    type: dict
    sample: null
    contains:
        enabled:
            description:
                - >-
                    Set this flag to true and provide DiskEncryptionKey and optional
                    KeyEncryptionKey to enable encryption. Set this flag to false and
                    remove DiskEncryptionKey and KeyEncryptionKey to disable encryption.
                    If EncryptionSettings is null in the request object, the existing
                    settings remain unchanged.
            returned: always
            type: bool
            sample: null
        encryption_settings:
            description:
                - 'A collection of encryption settings, one for each disk volume.'
            type: list
            sample: null
            contains:
                disk_encryption_key:
                    description:
                        - Key Vault Secret Url and vault id of the disk encryption key
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
                        secret_url:
                            description:
                                - Url pointing to a key or secret in KeyVault
                            returned: always
                            type: str
                            sample: null
                key_encryption_key:
                    description:
                        - >-
                            Key Vault Key Url and vault id of the key encryption key.
                            KeyEncryptionKey is optional and when provided is used to unwrap
                            the disk encryption key.
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
        encryption_settings_version:
            description:
                - >-
                    Describes what type of encryption is used for the disks. Once this
                    field is set, it cannot be overwritten. '1.0' corresponds to Azure
                    Disk Encryption with AAD app.'1.1' corresponds to Azure Disk
                    Encryption.
            type: str
            sample: null
provisioning_state:
    description:
        - The disk provisioning state.
    type: str
    sample: null
incremental:
    description:
        - >-
            Whether a snapshot is incremental. Incremental snapshots on the same disk
            occupy less space than full snapshots and can be diffed.
    type: bool
    sample: null
encryption:
    description:
        - >-
            Encryption property can be used to encrypt data at rest with customer
            managed keys or platform managed keys.
    type: dict
    sample: null
    contains:
        disk_encryption_set_id:
            description:
                - >-
                    ResourceId of the disk encryption set to use for enabling encryption
                    at rest.
            type: str
            sample: null
        type:
            description:
                - The type of key used to encrypt the data of the disk.
            type: str
            sample: null
network_access_policy:
    description:
        - Policy for accessing the disk via network.
    type: str
    sample: null
disk_access_id:
    description:
        - ARM id of the DiskAccess resource for using private endpoints on disks.
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


class AzureRMSnapshot(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            name=dict(
                type='str',
                required=True
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        choices=['Standard_LRS',
                                 'Premium_LRS',
                                 'Standard_ZRS']
                    )
                )
            ),
            os_type=dict(
                type='sealed-choice',
                disposition='/os_type'
            ),
            hyper_v_generation=dict(
                type='str',
                disposition='/hyper_v_generation',
                choices=['V1',
                         'V2']
            ),
            creation_data=dict(
                type='dict',
                disposition='/creation_data',
                options=dict(
                    create_option=dict(
                        type='str',
                        disposition='create_option',
                        choices=['Empty',
                                 'Attach',
                                 'FromImage',
                                 'Import',
                                 'Copy',
                                 'Restore',
                                 'Upload'],
                        required=True
                    ),
                    storage_account_id=dict(
                        type='str',
                        disposition='storage_account_id'
                    ),
                    image_reference=dict(
                        type='dict',
                        disposition='image_reference',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id',
                                required=True
                            ),
                            lun=dict(
                                type='int',
                                disposition='lun'
                            )
                        )
                    ),
                    gallery_image_reference=dict(
                        type='dict',
                        disposition='gallery_image_reference',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id',
                                required=True
                            ),
                            lun=dict(
                                type='int',
                                disposition='lun'
                            )
                        )
                    ),
                    source_uri=dict(
                        type='str',
                        disposition='source_uri'
                    ),
                    source_resource_id=dict(
                        type='str',
                        disposition='source_resource_id'
                    ),
                    upload_size_bytes=dict(
                        type='int',
                        disposition='upload_size_bytes'
                    ),
                    logical_sector_size=dict(
                        type='int',
                        disposition='logical_sector_size'
                    )
                )
            ),
            disk_size_gb=dict(
                type='int',
                disposition='/disk_size_gb'
            ),
            encryption_settings_collection=dict(
                type='dict',
                disposition='/encryption_settings_collection',
                options=dict(
                    enabled=dict(
                        type='bool',
                        disposition='enabled',
                        required=True
                    ),
                    encryption_settings=dict(
                        type='list',
                        disposition='encryption_settings',
                        elements='dict',
                        options=dict(
                            disk_encryption_key=dict(
                                type='dict',
                                disposition='disk_encryption_key',
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
                                    secret_url=dict(
                                        type='str',
                                        disposition='secret_url',
                                        required=True
                                    )
                                )
                            ),
                            key_encryption_key=dict(
                                type='dict',
                                disposition='key_encryption_key',
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
                            )
                        )
                    ),
                    encryption_settings_version=dict(
                        type='str',
                        disposition='encryption_settings_version'
                    )
                )
            ),
            incremental=dict(
                type='bool',
                disposition='/incremental'
            ),
            encryption=dict(
                type='dict',
                disposition='/encryption',
                options=dict(
                    disk_encryption_set_id=dict(
                        type='str',
                        disposition='disk_encryption_set_id'
                    ),
                    type=dict(
                        type='str',
                        disposition='type',
                        choices=['EncryptionAtRestWithPlatformKey',
                                 'EncryptionAtRestWithCustomerKey',
                                 'EncryptionAtRestWithPlatformAndCustomerKeys']
                    )
                )
            ),
            network_access_policy=dict(
                type='str',
                disposition='/network_access_policy',
                choices=['AllowAll',
                         'AllowPrivate',
                         'DenyAll']
            ),
            disk_access_id=dict(
                type='str',
                disposition='/disk_access_id'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSnapshot, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.snapshots.create_or_update(resource_group=self.resource_group,
                                                                   name=self.name,
                                                                   snapshot=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Snapshot instance.')
            self.fail('Error creating the Snapshot instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.snapshots.delete(resource_group=self.resource_group,
                                                         name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Snapshot instance.')
            self.fail('Error deleting the Snapshot instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.snapshots.get(resource_group=self.resource_group,
                                                      name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSnapshot()


if __name__ == '__main__':
    main()
