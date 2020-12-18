
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


class AzureRMGalleryImageVersion(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            gallery_name=dict(
                type='str',
                required=True
            ),
            gallery_image_name=dict(
                type='str',
                required=True
            ),
            gallery_image_version_name=dict(
                type='str',
                required=True
            ),
            publishing_profile=dict(
                type='dict',
                disposition='/publishing_profile',
                options=dict(
                    target_regions=dict(
                        type='list',
                        disposition='target_regions',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name',
                                required=True
                            ),
                            regional_replica_count=dict(
                                type='int',
                                disposition='regional_replica_count'
                            ),
                            storage_account_type=dict(
                                type='str',
                                disposition='storage_account_type',
                                choices=['Standard_LRS',
                                         'Standard_ZRS',
                                         'Premium_LRS']
                            ),
                            encryption=dict(
                                type='dict',
                                disposition='encryption',
                                options=dict(
                                    os_disk_image=dict(
                                        type='dict',
                                        disposition='os_disk_image',
                                        options=dict(
                                            disk_encryption_set_id=dict(
                                                type='str',
                                                disposition='disk_encryption_set_id'
                                            )
                                        )
                                    ),
                                    data_disk_images=dict(
                                        type='list',
                                        disposition='data_disk_images',
                                        elements='dict',
                                        options=dict(
                                            lun=dict(
                                                type='int',
                                                disposition='lun',
                                                required=True
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    replica_count=dict(
                        type='int',
                        disposition='replica_count'
                    ),
                    exclude_from_latest=dict(
                        type='bool',
                        disposition='exclude_from_latest'
                    ),
                    end_of_life_date=dict(
                        type='str',
                        disposition='end_of_life_date'
                    ),
                    storage_account_type=dict(
                        type='str',
                        disposition='storage_account_type',
                        choices=['Standard_LRS',
                                 'Standard_ZRS',
                                 'Premium_LRS']
                    )
                )
            ),
            storage_profile=dict(
                type='dict',
                disposition='/storage_profile',
                options=dict(
                    source=dict(
                        type='dict',
                        disposition='source',
                        options=dict(
                            id=dict(
                                type='str',
                                disposition='id'
                            )
                        )
                    ),
                    os_disk_image=dict(
                        type='dict',
                        disposition='os_disk_image',
                        options=dict(
                            host_caching=dict(
                                type='sealed-choice',
                                disposition='host_caching'
                            ),
                            source=dict(
                                type='dict',
                                disposition='source',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            )
                        )
                    ),
                    data_disk_images=dict(
                        type='list',
                        disposition='data_disk_images',
                        elements='dict',
                        options=dict(
                            lun=dict(
                                type='int',
                                disposition='lun',
                                required=True
                            )
                        )
                    )
                )
            ),
            expand=dict(
                type='str',
                choices=['ReplicationStatus']
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.gallery_name = None
        self.gallery_image_name = None
        self.gallery_image_version_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleryImageVersion, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2019-12-01')

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
            response = self.mgmt_client.gallery_image_versions.create_or_update(resource_group=self.resource_group,
                                                                                gallery_name=self.gallery_name,
                                                                                gallery_image_name=self.gallery_image_name,
                                                                                gallery_image_version_name=self.gallery_image_version_name,
                                                                                gallery_image_version=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GalleryImageVersion instance.')
            self.fail('Error creating the GalleryImageVersion instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.gallery_image_versions.delete(resource_group=self.resource_group,
                                                                      gallery_name=self.gallery_name,
                                                                      gallery_image_name=self.gallery_image_name,
                                                                      gallery_image_version_name=self.gallery_image_version_name)
        except CloudError as e:
            self.log('Error attempting to delete the GalleryImageVersion instance.')
            self.fail('Error deleting the GalleryImageVersion instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.gallery_image_versions.get(resource_group=self.resource_group,
                                                                   gallery_name=self.gallery_name,
                                                                   gallery_image_name=self.gallery_image_name,
                                                                   gallery_image_version_name=self.gallery_image_version_name,
                                                                   expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleryImageVersion()


if __name__ == '__main__':
    main()
