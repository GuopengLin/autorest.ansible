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
module: azure_rm_snapshot_info
version_added: '2.9'
short_description: Get Snapshot info.
description:
    - Get info of Snapshot.
options:
    resource_group:
        description:
            - The name of the resource group.
        type: str
    name:
        description:
            - >-
                The name of the snapshot that is being created. The name can't be
                changed after the snapshot is created. Supported characters for the name
                are a-z, A-Z, 0-9 and _. The max name length is 80 characters.
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get information about a snapshot.
      azure_rm_snapshot_info: 
        resource_group_name: myResourceGroup
        snapshot_name: mySnapshot
        

    - name: List all snapshots in a resource group.
      azure_rm_snapshot_info: 
        resource_group_name: myResourceGroup
        

    - name: List all snapshots in a subscription.
      azure_rm_snapshot_info: 

'''

RETURN = '''
snapshots:
    description: >-
        A list of dict results where the key is the name of the Snapshot and the
        values are the facts for that Snapshot.
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
        managed_by:
            description:
                - Unused. Always Null.
            returned: always
            type: str
            sample: null
        sku:
            description:
                - >-
                    The snapshots sku name. Can be Standard_LRS, Premium_LRS, or
                    Standard_ZRS.
            returned: always
            type: dict
            sample: null
            contains:
                name:
                    description:
                        - The sku name.
                    returned: always
                    type: str
                    sample: null
        time_created:
            description:
                - The time when the snapshot was created.
            returned: always
            type: str
            sample: null
        os_type:
            description:
                - The Operating System type.
            returned: always
            type: sealed-choice
            sample: null
        hyper_v_generation:
            description:
                - >-
                    The hypervisor generation of the Virtual Machine. Applicable to OS
                    disks only.
            returned: always
            type: str
            sample: null
        creation_data:
            description:
                - >-
                    Disk source information. CreationData information cannot be changed
                    after the disk has been created.
            returned: always
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
                            identifier of the storage account containing the blob to import as
                            a disk.
                    returned: always
                    type: str
                    sample: null
                image_reference:
                    description:
                        - Disk source information.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        id:
                            description:
                                - >-
                                    A relative uri containing either a Platform Image Repository
                                    or user image reference.
                            returned: always
                            type: str
                            sample: null
                        lun:
                            description:
                                - >-
                                    If the disk is created from an image's data disk, this is an
                                    index that indicates which of the data disks in the image to
                                    use. For OS disks, this field is null.
                            returned: always
                            type: int
                            sample: null
                gallery_image_reference:
                    description:
                        - >-
                            Required if creating from a Gallery Image. The id of the
                            ImageDiskReference will be the ARM id of the shared galley image
                            version from which to create a disk.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        id:
                            description:
                                - >-
                                    A relative uri containing either a Platform Image Repository
                                    or user image reference.
                            returned: always
                            type: str
                            sample: null
                        lun:
                            description:
                                - >-
                                    If the disk is created from an image's data disk, this is an
                                    index that indicates which of the data disks in the image to
                                    use. For OS disks, this field is null.
                            returned: always
                            type: int
                            sample: null
                source_uri:
                    description:
                        - >-
                            If createOption is Import, this is the URI of a blob to be
                            imported into a managed disk.
                    returned: always
                    type: str
                    sample: null
                source_resource_id:
                    description:
                        - >-
                            If createOption is Copy, this is the ARM id of the source snapshot
                            or disk.
                    returned: always
                    type: str
                    sample: null
                upload_size_bytes:
                    description:
                        - >-
                            If createOption is Upload, this is the size of the contents of the
                            upload including the VHD footer. This value should be between
                            20972032 (20 MiB + 512 bytes for the VHD footer) and
                            35183298347520 bytes (32 TiB + 512 bytes for the VHD footer).
                    returned: always
                    type: int
                    sample: null
                logical_sector_size:
                    description:
                        - >-
                            Logical sector size in bytes for Ultra disks. Supported values are
                            512 ad 4096. 4096 is the default.
                    returned: always
                    type: int
                    sample: null
        disk_size_gb:
            description:
                - >-
                    If creationData.createOption is Empty, this field is mandatory and it
                    indicates the size of the disk to create. If this field is present for
                    updates or creation with other options, it indicates a resize. Resizes
                    are only allowed if the disk is not attached to a running VM, and can
                    only increase the disk's size.
            returned: always
            type: int
            sample: null
        disk_size_bytes:
            description:
                - The size of the disk in bytes. This field is read only.
            returned: always
            type: int
            sample: null
        disk_state:
            description:
                - The state of the snapshot.
            returned: always
            type: str
            sample: null
        unique_id:
            description:
                - Unique Guid identifying the resource.
            returned: always
            type: str
            sample: null
        encryption_settings_collection:
            description:
                - >-
                    Encryption settings collection used be Azure Disk Encryption, can
                    contain multiple encryption settings per disk or snapshot.
            returned: always
            type: dict
            sample: null
            contains:
                enabled:
                    description:
                        - >-
                            Set this flag to true and provide DiskEncryptionKey and optional
                            KeyEncryptionKey to enable encryption. Set this flag to false and
                            remove DiskEncryptionKey and KeyEncryptionKey to disable
                            encryption. If EncryptionSettings is null in the request object,
                            the existing settings remain unchanged.
                    returned: always
                    type: bool
                    sample: null
                encryption_settings:
                    description:
                        - 'A collection of encryption settings, one for each disk volume.'
                    returned: always
                    type: list
                    sample: null
                    contains:
                        disk_encryption_key:
                            description:
                                - Key Vault Secret Url and vault id of the disk encryption key
                            returned: always
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
                                            returned: always
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
                                    KeyEncryptionKey is optional and when provided is used to
                                    unwrap the disk encryption key.
                            returned: always
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
                                            returned: always
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
                    returned: always
                    type: str
                    sample: null
        provisioning_state:
            description:
                - The disk provisioning state.
            returned: always
            type: str
            sample: null
        incremental:
            description:
                - >-
                    Whether a snapshot is incremental. Incremental snapshots on the same
                    disk occupy less space than full snapshots and can be diffed.
            returned: always
            type: bool
            sample: null
        encryption:
            description:
                - >-
                    Encryption property can be used to encrypt data at rest with customer
                    managed keys or platform managed keys.
            returned: always
            type: dict
            sample: null
            contains:
                disk_encryption_set_id:
                    description:
                        - >-
                            ResourceId of the disk encryption set to use for enabling
                            encryption at rest.
                    returned: always
                    type: str
                    sample: null
                type:
                    description:
                        - The type of key used to encrypt the data of the disk.
                    returned: always
                    type: str
                    sample: null
        network_access_policy:
            description:
                - Policy for accessing the disk via network.
            returned: always
            type: str
            sample: null
        disk_access_id:
            description:
                - >-
                    ARM id of the DiskAccess resource for using private endpoints on
                    disks.
            returned: always
            type: str
            sample: null
        value:
            description:
                - A list of snapshots.
            returned: always
            type: list
            sample: null
            contains:
                sku:
                    description:
                        - >-
                            The snapshots sku name. Can be Standard_LRS, Premium_LRS, or
                            Standard_ZRS.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        name:
                            description:
                                - The sku name.
                            returned: always
                            type: str
                            sample: null
                os_type:
                    description:
                        - The Operating System type.
                    returned: always
                    type: sealed-choice
                    sample: null
                hyper_v_generation:
                    description:
                        - >-
                            The hypervisor generation of the Virtual Machine. Applicable to OS
                            disks only.
                    returned: always
                    type: str
                    sample: null
                creation_data:
                    description:
                        - >-
                            Disk source information. CreationData information cannot be
                            changed after the disk has been created.
                    returned: always
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
                                    identifier of the storage account containing the blob to
                                    import as a disk.
                            returned: always
                            type: str
                            sample: null
                        image_reference:
                            description:
                                - Disk source information.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                id:
                                    description:
                                        - >-
                                            A relative uri containing either a Platform Image
                                            Repository or user image reference.
                                    returned: always
                                    type: str
                                    sample: null
                                lun:
                                    description:
                                        - >-
                                            If the disk is created from an image's data disk, this is
                                            an index that indicates which of the data disks in the
                                            image to use. For OS disks, this field is null.
                                    returned: always
                                    type: int
                                    sample: null
                        gallery_image_reference:
                            description:
                                - >-
                                    Required if creating from a Gallery Image. The id of the
                                    ImageDiskReference will be the ARM id of the shared galley
                                    image version from which to create a disk.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                id:
                                    description:
                                        - >-
                                            A relative uri containing either a Platform Image
                                            Repository or user image reference.
                                    returned: always
                                    type: str
                                    sample: null
                                lun:
                                    description:
                                        - >-
                                            If the disk is created from an image's data disk, this is
                                            an index that indicates which of the data disks in the
                                            image to use. For OS disks, this field is null.
                                    returned: always
                                    type: int
                                    sample: null
                        source_uri:
                            description:
                                - >-
                                    If createOption is Import, this is the URI of a blob to be
                                    imported into a managed disk.
                            returned: always
                            type: str
                            sample: null
                        source_resource_id:
                            description:
                                - >-
                                    If createOption is Copy, this is the ARM id of the source
                                    snapshot or disk.
                            returned: always
                            type: str
                            sample: null
                        upload_size_bytes:
                            description:
                                - >-
                                    If createOption is Upload, this is the size of the contents of
                                    the upload including the VHD footer. This value should be
                                    between 20972032 (20 MiB + 512 bytes for the VHD footer) and
                                    35183298347520 bytes (32 TiB + 512 bytes for the VHD footer).
                            returned: always
                            type: int
                            sample: null
                        logical_sector_size:
                            description:
                                - >-
                                    Logical sector size in bytes for Ultra disks. Supported values
                                    are 512 ad 4096. 4096 is the default.
                            returned: always
                            type: int
                            sample: null
                disk_size_gb:
                    description:
                        - >-
                            If creationData.createOption is Empty, this field is mandatory and
                            it indicates the size of the disk to create. If this field is
                            present for updates or creation with other options, it indicates a
                            resize. Resizes are only allowed if the disk is not attached to a
                            running VM, and can only increase the disk's size.
                    returned: always
                    type: int
                    sample: null
                encryption_settings_collection:
                    description:
                        - >-
                            Encryption settings collection used be Azure Disk Encryption, can
                            contain multiple encryption settings per disk or snapshot.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        enabled:
                            description:
                                - >-
                                    Set this flag to true and provide DiskEncryptionKey and
                                    optional KeyEncryptionKey to enable encryption. Set this flag
                                    to false and remove DiskEncryptionKey and KeyEncryptionKey to
                                    disable encryption. If EncryptionSettings is null in the
                                    request object, the existing settings remain unchanged.
                            returned: always
                            type: bool
                            sample: null
                        encryption_settings:
                            description:
                                - 'A collection of encryption settings, one for each disk volume.'
                            returned: always
                            type: list
                            sample: null
                            contains:
                                disk_encryption_key:
                                    description:
                                        - >-
                                            Key Vault Secret Url and vault id of the disk encryption
                                            key
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        source_vault:
                                            description:
                                                - >-
                                                    Resource id of the KeyVault containing the key or
                                                    secret
                                            returned: always
                                            type: dict
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    returned: always
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
                                            KeyEncryptionKey is optional and when provided is used to
                                            unwrap the disk encryption key.
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        source_vault:
                                            description:
                                                - >-
                                                    Resource id of the KeyVault containing the key or
                                                    secret
                                            returned: always
                                            type: dict
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    returned: always
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
                                    Describes what type of encryption is used for the disks. Once
                                    this field is set, it cannot be overwritten. '1.0' corresponds
                                    to Azure Disk Encryption with AAD app.'1.1' corresponds to
                                    Azure Disk Encryption.
                            returned: always
                            type: str
                            sample: null
                incremental:
                    description:
                        - >-
                            Whether a snapshot is incremental. Incremental snapshots on the
                            same disk occupy less space than full snapshots and can be diffed.
                    returned: always
                    type: bool
                    sample: null
                encryption:
                    description:
                        - >-
                            Encryption property can be used to encrypt data at rest with
                            customer managed keys or platform managed keys.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        disk_encryption_set_id:
                            description:
                                - >-
                                    ResourceId of the disk encryption set to use for enabling
                                    encryption at rest.
                            returned: always
                            type: str
                            sample: null
                        type:
                            description:
                                - The type of key used to encrypt the data of the disk.
                            returned: always
                            type: str
                            sample: null
                network_access_policy:
                    description:
                        - Policy for accessing the disk via network.
                    returned: always
                    type: str
                    sample: null
                disk_access_id:
                    description:
                        - >-
                            ARM id of the DiskAccess resource for using private endpoints on
                            disks.
                    returned: always
                    type: str
                    sample: null
        next_link:
            description:
                - >-
                    The uri to fetch the next page of snapshots. Call ListNext() with this
                    to fetch the next page of snapshots.
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


class AzureRMSnapshotInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None

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
        super(AzureRMSnapshotInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-30')

        if (self.resource_group is not None and
            self.name is not None):
            self.results['snapshots'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['snapshots'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['snapshots'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.snapshots.get(resource_group=self.resource_group,
                                                      name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.snapshots.list_by_resource_group(resource_group=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.snapshots.list()
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
    AzureRMSnapshotInfo()


if __name__ == '__main__':
    main()
