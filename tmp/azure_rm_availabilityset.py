
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


class AzureRMAvailabilitySet(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            availability_set_name=dict(
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
            platform_update_domain_count=dict(
                type='int',
                disposition='/platform_update_domain_count'
            ),
            platform_fault_domain_count=dict(
                type='int',
                disposition='/platform_fault_domain_count'
            ),
            virtual_machines=dict(
                type='list',
                disposition='/virtual_machines',
                elements='dict',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            proximity_placement_group=dict(
                type='dict',
                disposition='/proximity_placement_group',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            statuses=dict(
                type='list',
                updatable=False,
                disposition='/statuses',
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
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.availability_set_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMAvailabilitySet, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.availability_sets.create_or_update(resource_group=self.resource_group,
                                                                           availability_set_name=self.availability_set_name,
                                                                           parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the AvailabilitySet instance.')
            self.fail('Error creating the AvailabilitySet instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.availability_sets.delete(resource_group=self.resource_group,
                                                                 availability_set_name=self.availability_set_name)
        except CloudError as e:
            self.log('Error attempting to delete the AvailabilitySet instance.')
            self.fail('Error deleting the AvailabilitySet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.availability_sets.get(resource_group=self.resource_group,
                                                              availability_set_name=self.availability_set_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMAvailabilitySet()


if __name__ == '__main__':
    main()
