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
module: azure_rm_proximityplacementgroup_info
version_added: '2.9'
short_description: Get ProximityPlacementGroup info.
description:
    - Get info of ProximityPlacementGroup.
options:
    resource_group:
        description:
            - The name of the resource group.
        type: str
    proximity_placement_group_name:
        description:
            - The name of the proximity placement group.
        type: str
    include_colocation_status:
        description:
            - >-
                includeColocationStatus=true enables fetching the colocation status of
                all the resources in the proximity placement group.
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Create a proximity placement group.
      azure_rm_proximityplacementgroup_info: 
        proximity_placement_group_name: myProximityPlacementGroup
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
proximity_placement_groups:
    description: >-
        A list of dict results where the key is the name of the
        ProximityPlacementGroup and the values are the facts for that
        ProximityPlacementGroup.
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
        proximity_placement_group_type:
            description:
                - >-
                    Specifies the type of the proximity placement group.
                    :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`:code:`<br>`
                    **Standard** : Co-locate resources within an Azure region or
                    Availability Zone. :code:`<br>`:code:`<br>` **Ultra** : For future
                    use.
            returned: always
            type: str
            sample: null
        virtual_machines:
            description:
                - >-
                    A list of references to all virtual machines in the proximity
                    placement group.
            returned: always
            type: list
            sample: null
            contains:
                colocation_status:
                    description:
                        - >-
                            Describes colocation status of a resource in the Proximity
                            Placement Group.
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
                    A list of references to all virtual machine scale sets in the
                    proximity placement group.
            returned: always
            type: list
            sample: null
            contains:
                colocation_status:
                    description:
                        - >-
                            Describes colocation status of a resource in the Proximity
                            Placement Group.
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
                    A list of references to all availability sets in the proximity
                    placement group.
            returned: always
            type: list
            sample: null
            contains:
                colocation_status:
                    description:
                        - >-
                            Describes colocation status of a resource in the Proximity
                            Placement Group.
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
        value:
            description:
                - The list of proximity placement groups
            returned: always
            type: list
            sample: null
            contains:
                proximity_placement_group_type:
                    description:
                        - >-
                            Specifies the type of the proximity placement group.
                            :code:`<br>`:code:`<br>` Possible values are:
                            :code:`<br>`:code:`<br>` **Standard** : Co-locate resources within
                            an Azure region or Availability Zone. :code:`<br>`:code:`<br>`
                            **Ultra** : For future use.
                    returned: always
                    type: str
                    sample: null
                virtual_machines:
                    description:
                        - >-
                            A list of references to all virtual machines in the proximity
                            placement group.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        colocation_status:
                            description:
                                - >-
                                    Describes colocation status of a resource in the Proximity
                                    Placement Group.
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
                                            The detailed status message, including for alerts and
                                            error messages.
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
                            A list of references to all virtual machine scale sets in the
                            proximity placement group.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        colocation_status:
                            description:
                                - >-
                                    Describes colocation status of a resource in the Proximity
                                    Placement Group.
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
                                            The detailed status message, including for alerts and
                                            error messages.
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
                            A list of references to all availability sets in the proximity
                            placement group.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        colocation_status:
                            description:
                                - >-
                                    Describes colocation status of a resource in the Proximity
                                    Placement Group.
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
                                            The detailed status message, including for alerts and
                                            error messages.
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
        next_link:
            description:
                - The URI to fetch the next page of proximity placement groups.
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


class AzureRMProximityPlacementGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            proximity_placement_group_name=dict(
                type='str'
            ),
            include_colocation_status=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.proximity_placement_group_name = None
        self.include_colocation_status = None

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
        super(AzureRMProximityPlacementGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.proximity_placement_group_name is not None):
            self.results['proximity_placement_groups'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['proximity_placement_groups'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['proximity_placement_groups'] = self.format_item(self.list_by_subscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.proximity_placement_groups.get(resource_group=self.resource_group,
                                                                       proximity_placement_group_name=self.proximity_placement_group_name,
                                                                       include_colocation_status=self.include_colocation_status)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.proximity_placement_groups.list_by_resource_group(resource_group=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_subscription(self):
        response = None

        try:
            response = self.mgmt_client.proximity_placement_groups.list_by_subscription()
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
    AzureRMProximityPlacementGroupInfo()


if __name__ == '__main__':
    main()
