
from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualMachineExtensionImageInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            publisher_name=dict(
                type='str',
                required=True
            ),
            type=dict(
                type='str'
            ),
            version=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            top=dict(
                type='int'
            ),
            orderby=dict(
                type='str'
            )
        )

        self.location = None
        self.publisher_name = None
        self.type = None
        self.version = None
        self.filter = None
        self.top = None
        self.orderby = None

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
        super(AzureRMVirtualMachineExtensionImageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.location is not None and
            self.publisher_name is not None and
            self.type is not None and
            self.version is not None):
            self.results['virtual_machine_extension_images'] = self.format_item(self.get())
        elif (self.location is not None and
              self.publisher_name is not None and
              self.type is not None):
            self.results['virtual_machine_extension_images'] = self.format_item(self.list_versions())
        elif (self.location is not None and
              self.publisher_name is not None):
            self.results['virtual_machine_extension_images'] = self.format_item(self.list_types())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_extension_images.get(location=self.location,
                                                                             publisher_name=self.publisher_name,
                                                                             type=self.type,
                                                                             version=self.version)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_versions(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_extension_images.list_versions(location=self.location,
                                                                                       publisher_name=self.publisher_name,
                                                                                       type=self.type,
                                                                                       filter=self.filter,
                                                                                       top=self.top,
                                                                                       orderby=self.orderby)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_types(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_extension_images.list_types(location=self.location,
                                                                                    publisher_name=self.publisher_name)
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
    AzureRMVirtualMachineExtensionImageInfo()


if __name__ == '__main__':
    main()
