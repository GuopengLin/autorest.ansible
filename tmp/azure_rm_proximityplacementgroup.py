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
    module: azure_rm_proximityplacementgroup
    version_added: '2.9'
    short_description: Manage Azure ProximityPlacementGroup instance.
    description:
      - 'Create, update and delete instance of Azure ProximityPlacementGroup.'
    options:
      resource_group:
        description:
          - The name of the resource group.
        required: true
        type: str
      proximity_placement_group_name:
        description:
          - The name of the proximity placement group.
        required: true
        type: str
      proximity_placement_group_type:
        description:
          - >-
            Specifies the type of the proximity placement group.
            :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`:code:`<br>`
            **Standard** : Co-locate resources within an Azure region or
            Availability Zone. :code:`<br>`:code:`<br>` **Ultra** : For future use.
        type: str
        choices:
          - Standard
          - Ultra
      virtual_machines:
        description:
          - >-
            A list of references to all virtual machines in the proximity placement
            group.
        type: list
        suboptions:
          colocation_status:
            description:
              - >-
                Describes colocation status of a resource in the Proximity Placement
                Group.
            type: dict
            suboptions:
              code:
                description:
                  - The status code.
                type: str
              level:
                description:
                  - The level code.
                type: sealed-choice
              display_status:
                description:
                  - The short localizable label for the status.
                type: str
              message:
                description:
                  - >-
                    The detailed status message, including for alerts and error
                    messages.
                type: str
              time:
                description:
                  - The time of the status.
                type: str
      virtual_machine_scale_sets:
        description:
          - >-
            A list of references to all virtual machine scale sets in the proximity
            placement group.
        type: list
        suboptions:
          colocation_status:
            description:
              - >-
                Describes colocation status of a resource in the Proximity Placement
                Group.
            type: dict
            suboptions:
              code:
                description:
                  - The status code.
                type: str
              level:
                description:
                  - The level code.
                type: sealed-choice
              display_status:
                description:
                  - The short localizable label for the status.
                type: str
              message:
                description:
                  - >-
                    The detailed status message, including for alerts and error
                    messages.
                type: str
              time:
                description:
                  - The time of the status.
                type: str
      availability_sets:
        description:
          - >-
            A list of references to all availability sets in the proximity placement
            group.
        type: list
        suboptions:
          colocation_status:
            description:
              - >-
                Describes colocation status of a resource in the Proximity Placement
                Group.
            type: dict
            suboptions:
              code:
                description:
                  - The status code.
                type: str
              level:
                description:
                  - The level code.
                type: sealed-choice
              display_status:
                description:
                  - The short localizable label for the status.
                type: str
              message:
                description:
                  - >-
                    The detailed status message, including for alerts and error
                    messages.
                type: str
              time:
                description:
                  - The time of the status.
                type: str
      colocation_status:
        description:
          - Describes colocation status of the Proximity Placement Group.
        type: dict
        suboptions:
          code:
            description:
              - The status code.
            type: str
          level:
            description:
              - The level code.
            type: sealed-choice
          display_status:
            description:
              - The short localizable label for the status.
            type: str
          message:
            description:
              - >-
                The detailed status message, including for alerts and error
                messages.
            type: str
          time:
            description:
              - The time of the status.
            type: str
      include_colocation_status:
        description:
          - >-
            includeColocationStatus=true enables fetching the colocation status of
            all the resources in the proximity placement group.
        type: str
      state:
        description:
          - Assert the state of the ProximityPlacementGroup.
          - >-
            Use C(present) to create or update an ProximityPlacementGroup and
            C(absent) to delete it.
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
    - name: Create or Update a proximity placement group.
      azure_rm_proximityplacementgroup: 
        proximity_placement_group_name: myProximityPlacementGroup
        resource_group_name: myResourceGroup
        location: westus
        properties:
          proximity_placement_group_type: Standard
        

    - name: Create a proximity placement group.
      azure_rm_proximityplacementgroup: 
        proximity_placement_group_name: myProximityPlacementGroup
        resource_group_name: myResourceGroup
        tags:
          additional_prop1: string
        

'''

RETURN = '''
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
    proximity_placement_group_type:
      description:
        - >-
          Specifies the type of the proximity placement group.
          :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`:code:`<br>`
          **Standard** : Co-locate resources within an Azure region or Availability
          Zone. :code:`<br>`:code:`<br>` **Ultra** : For future use.
      returned: always
      type: str
      sample: null
    virtual_machines:
      description:
        - >-
          A list of references to all virtual machines in the proximity placement
          group.
      returned: always
      type: list
      sample: null
      contains:
        colocation_status:
          description:
            - >-
              Describes colocation status of a resource in the Proximity Placement
              Group.
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - The status code.
              returned: always
              type: str
              sample: null
            level:
              description:
                - The level code.
              returned: always
              type: sealed-choice
              sample: null
            display_status:
              description:
                - The short localizable label for the status.
              returned: always
              type: str
              sample: null
            message:
              description:
                - >-
                  The detailed status message, including for alerts and error
                  messages.
              returned: always
              type: str
              sample: null
            time:
              description:
                - The time of the status.
              returned: always
              type: str
              sample: null
    virtual_machine_scale_sets:
      description:
        - >-
          A list of references to all virtual machine scale sets in the proximity
          placement group.
      returned: always
      type: list
      sample: null
      contains:
        colocation_status:
          description:
            - >-
              Describes colocation status of a resource in the Proximity Placement
              Group.
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - The status code.
              returned: always
              type: str
              sample: null
            level:
              description:
                - The level code.
              returned: always
              type: sealed-choice
              sample: null
            display_status:
              description:
                - The short localizable label for the status.
              returned: always
              type: str
              sample: null
            message:
              description:
                - >-
                  The detailed status message, including for alerts and error
                  messages.
              returned: always
              type: str
              sample: null
            time:
              description:
                - The time of the status.
              returned: always
              type: str
              sample: null
    availability_sets:
      description:
        - >-
          A list of references to all availability sets in the proximity placement
          group.
      returned: always
      type: list
      sample: null
      contains:
        colocation_status:
          description:
            - >-
              Describes colocation status of a resource in the Proximity Placement
              Group.
          returned: always
          type: dict
          sample: null
          contains:
            code:
              description:
                - The status code.
              returned: always
              type: str
              sample: null
            level:
              description:
                - The level code.
              returned: always
              type: sealed-choice
              sample: null
            display_status:
              description:
                - The short localizable label for the status.
              returned: always
              type: str
              sample: null
            message:
              description:
                - >-
                  The detailed status message, including for alerts and error
                  messages.
              returned: always
              type: str
              sample: null
            time:
              description:
                - The time of the status.
              returned: always
              type: str
              sample: null
    colocation_status:
      description:
        - Describes colocation status of the Proximity Placement Group.
      returned: always
      type: dict
      sample: null
      contains:
        code:
          description:
            - The status code.
          returned: always
          type: str
          sample: null
        level:
          description:
            - The level code.
          returned: always
          type: sealed-choice
          sample: null
        display_status:
          description:
            - The short localizable label for the status.
          returned: always
          type: str
          sample: null
        message:
          description:
            - 'The detailed status message, including for alerts and error messages.'
          returned: always
          type: str
          sample: null
        time:
          description:
            - The time of the status.
          returned: always
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
