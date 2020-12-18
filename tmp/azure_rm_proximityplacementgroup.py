
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


class AzureRMProximityPlacementGroup(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            proximity_placement_group_name=dict(
                type='str',
                required=True
            ),
            proximity_placement_group_type=dict(
                type='str',
                disposition='/proximity_placement_group_type',
                choices=['Standard',
                         'Ultra']
            ),
            virtual_machines=dict(
                type='list',
                updatable=False,
                disposition='/virtual_machines',
                elements='dict',
                options=dict(
                    colocation_status=dict(
                        type='dict',
                        disposition='colocation_status',
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
            virtual_machine_scale_sets=dict(
                type='list',
                updatable=False,
                disposition='/virtual_machine_scale_sets',
                elements='dict',
                options=dict(
                    colocation_status=dict(
                        type='dict',
                        disposition='colocation_status',
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
            availability_sets=dict(
                type='list',
                updatable=False,
                disposition='/availability_sets',
                elements='dict',
                options=dict(
                    colocation_status=dict(
                        type='dict',
                        disposition='colocation_status',
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
            colocation_status=dict(
                type='dict',
                disposition='/colocation_status',
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
            include_colocation_status=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.proximity_placement_group_name = None
        self.include_colocation_status = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMProximityPlacementGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.proximity_placement_groups.create_or_update(resource_group=self.resource_group,
                                                                                    proximity_placement_group_name=self.proximity_placement_group_name,
                                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ProximityPlacementGroup instance.')
            self.fail('Error creating the ProximityPlacementGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.proximity_placement_groups.delete(resource_group=self.resource_group,
                                                                          proximity_placement_group_name=self.proximity_placement_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the ProximityPlacementGroup instance.')
            self.fail('Error deleting the ProximityPlacementGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.proximity_placement_groups.get(resource_group=self.resource_group,
                                                                       proximity_placement_group_name=self.proximity_placement_group_name,
                                                                       include_colocation_status=self.include_colocation_status)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMProximityPlacementGroup()


if __name__ == '__main__':
    main()
