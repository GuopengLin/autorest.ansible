
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


class AzureRMDedicatedHost(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            host_group_name=dict(
                type='str',
                required=True
            ),
            host_name=dict(
                type='str',
                required=True
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    ),
                    capacity=dict(
                        type='int',
                        disposition='capacity'
                    )
                )
            ),
            platform_fault_domain=dict(
                type='int',
                disposition='/platform_fault_domain'
            ),
            auto_replace_on_failure=dict(
                type='bool',
                disposition='/auto_replace_on_failure'
            ),
            license_type=dict(
                type='sealed-choice',
                disposition='/license_type'
            ),
            instance_view=dict(
                type='dict',
                updatable=False,
                disposition='/instance_view',
                options=dict(
                    available_capacity=dict(
                        type='dict',
                        disposition='available_capacity',
                        options=dict(
                            allocatable_v_ms=dict(
                                type='list',
                                disposition='allocatable_v_ms',
                                elements='dict',
                                options=dict(
                                    vm_size=dict(
                                        type='str',
                                        disposition='vm_size'
                                    ),
                                    count=dict(
                                        type='number',
                                        disposition='count'
                                    )
                                )
                            )
                        )
                    ),
                    statuses=dict(
                        type='list',
                        disposition='statuses',
                        elements='dict',
                        options=dict(
                            code=dict(
                                type='str',
                                disposition='code'
                            ),
                            level=dict(
                                type='sealed-choice',
                                disposition='level'
                            ),
                            display_status=dict(
                                type='str',
                                disposition='display_status'
                            ),
                            message=dict(
                                type='str',
                                disposition='message'
                            ),
                            time=dict(
                                type='str',
                                disposition='time'
                            )
                        )
                    )
                )
            ),
            expand=dict(
                type='constant'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.host_group_name = None
        self.host_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDedicatedHost, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2020-06-01')

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
            response = self.mgmt_client.dedicated_hosts.create_or_update(resource_group=self.resource_group,
                                                                         host_group_name=self.host_group_name,
                                                                         host_name=self.host_name,
                                                                         parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DedicatedHost instance.')
            self.fail('Error creating the DedicatedHost instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.dedicated_hosts.delete(resource_group=self.resource_group,
                                                               host_group_name=self.host_group_name,
                                                               host_name=self.host_name)
        except CloudError as e:
            self.log('Error attempting to delete the DedicatedHost instance.')
            self.fail('Error deleting the DedicatedHost instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.dedicated_hosts.get(resource_group=self.resource_group,
                                                            host_group_name=self.host_group_name,
                                                            host_name=self.host_name,
                                                            expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDedicatedHost()


if __name__ == '__main__':
    main()
