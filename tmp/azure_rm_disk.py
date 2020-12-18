
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


class AzureRMDisk(AzureRMModuleBaseExt):
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
            managed_by_extended=dict(
                type='list',
                updatable=False,
                disposition='/managed_by_extended',
                elements='str'
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
                                 'StandardSSD_LRS',
                                 'UltraSSD_LRS']
                    )
                )
            ),
            zones=dict(
                type='list',
                disposition='/zones',
                elements='str'
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
            disk_iops_read_write=dict(
                type='int',
                disposition='/disk_iops_read_write'
            ),
            disk_m_bps_read_write=dict(
                type='int',
                disposition='/disk_m_bps_read_write'
            ),
            disk_iops_read_only=dict(
                type='int',
                disposition='/disk_iops_read_only'
            ),
            disk_m_bps_read_only=dict(
                type='int',
                disposition='/disk_m_bps_read_only'
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
            max_shares=dict(
                type='int',
                disposition='/max_shares'
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
            tier=dict(
                type='str',
                disposition='/tier'
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

        super(AzureRMDisk, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.disks.create_or_update(resource_group=self.resource_group,
                                                               name=self.name,
                                                               disk=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Disk instance.')
            self.fail('Error creating the Disk instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.disks.delete(resource_group=self.resource_group,
                                                     name=self.name)
        except CloudError as e:
            self.log('Error attempting to delete the Disk instance.')
            self.fail('Error deleting the Disk instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.disks.get(resource_group=self.resource_group,
                                                  name=self.name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDisk()


if __name__ == '__main__':
    main()
