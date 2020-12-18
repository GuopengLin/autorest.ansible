
from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualMachineInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str'
            ),
            resource_group=dict(
                type='str'
            ),
            vm_name=dict(
                type='str'
            ),
            expand=dict(
                type='constant'
            ),
            status_only=dict(
                type='str'
            )
        )

        self.location = None
        self.resource_group = None
        self.vm_name = None
        self.expand = None
        self.status_only = None

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
        super(AzureRMVirtualMachineInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.vm_name is not None):
            self.results['virtual_machines'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.vm_name is not None):
            self.results['virtual_machines'] = self.format_item(self.instance_view())
        elif (self.resource_group is not None and
              self.vm_name is not None):
            self.results['virtual_machines'] = self.format_item(self.list_available_sizes())
        elif (self.location is not None):
            self.results['virtual_machines'] = self.format_item(self.list_by_location())
        elif (self.resource_group is not None):
            self.results['virtual_machines'] = self.format_item(self.list())
        else:
            self.results['virtual_machines'] = self.format_item(self.list_all())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.get(resource_group=self.resource_group,
                                                             vm_name=self.vm_name,
                                                             expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def instance_view(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.instance_view(resource_group=self.resource_group,
                                                                       vm_name=self.vm_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_available_sizes(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.list_available_sizes(resource_group=self.resource_group,
                                                                              vm_name=self.vm_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_location(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.list_by_location(location=self.location)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.list(resource_group=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_all(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machines.list_all(status_only=self.status_only)
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
    AzureRMVirtualMachineInfo()


if __name__ == '__main__':
    main()
