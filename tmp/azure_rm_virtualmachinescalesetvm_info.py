
from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMVirtualMachineScaleSetVMInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            vm_scale_set_name=dict(
                type='str'
            ),
            instance_id=dict(
                type='str'
            ),
            expand=dict(
                type='constant'
            ),
            virtual_machine_scale_set_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            select=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.vm_scale_set_name = None
        self.instance_id = None
        self.expand = None
        self.virtual_machine_scale_set_name = None
        self.filter = None
        self.select = None

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
        super(AzureRMVirtualMachineScaleSetVMInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.vm_scale_set_name is not None and
            self.instance_id is not None):
            self.results['virtual_machine_scale_set_vms'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.vm_scale_set_name is not None and
              self.instance_id is not None):
            self.results['virtual_machine_scale_set_vms'] = self.format_item(self.get_instance_view())
        elif (self.resource_group is not None and
              self.virtual_machine_scale_set_name is not None):
            self.results['virtual_machine_scale_set_vms'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vms.get(resource_group=self.resource_group,
                                                                          vm_scale_set_name=self.vm_scale_set_name,
                                                                          instance_id=self.instance_id,
                                                                          expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get_instance_view(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vms.get_instance_view(resource_group=self.resource_group,
                                                                                        vm_scale_set_name=self.vm_scale_set_name,
                                                                                        instance_id=self.instance_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vms.list(resource_group=self.resource_group,
                                                                           virtual_machine_scale_set_name=self.virtual_machine_scale_set_name,
                                                                           filter=self.filter,
                                                                           select=self.select,
                                                                           expand=self.expand)
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
    AzureRMVirtualMachineScaleSetVMInfo()


if __name__ == '__main__':
    main()
