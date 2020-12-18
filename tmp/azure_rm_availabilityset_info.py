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
module: azure_rm_availabilityset_info
version_added: '2.9'
short_description: Get AvailabilitySet info.
description:
    - Get info of AvailabilitySet.
options:
    resource_group:
        description:
            - The name of the resource group.
        type: str
    availability_set_name:
        description:
            - The name of the availability set.
        type: str
    expand:
        description:
            - >-
                The expand expression to apply to the operation. Allowed values are
                'instanceView'.
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: List availability sets in a subscription.
      azure_rm_availabilityset_info: 

'''

RETURN = '''
availability_sets:
    description: >-
        A list of dict results where the key is the name of the AvailabilitySet and
        the values are the facts for that AvailabilitySet.
    returned: always
    type: complex
    contains:
        id:
            description:
                - Resource Id
            type: str
            sample: null
        name:
            description:
                - Resource name
            type: str
            sample: null
        type:
            description:
                - Resource type
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
            type: dict
            sample: null
        sku:
            description:
                - >-
                    Sku of the availability set, only name is required to be set. See
                    AvailabilitySetSkuTypes for possible set of values. Use 'Aligned' for
                    virtual machines with managed disks and 'Classic' for virtual machines
                    with unmanaged disks. Default value is 'Classic'.
            type: dict
            sample: null
            contains:
                name:
                    description:
                        - The sku name.
                    type: str
                    sample: null
                tier:
                    description:
                        - >-
                            Specifies the tier of virtual machines in a scale set.:code:`<br
                            />`:code:`<br />` Possible Values::code:`<br />`:code:`<br />`
                            **Standard**\ :code:`<br />`:code:`<br />` **Basic**
                    type: str
                    sample: null
                capacity:
                    description:
                        - Specifies the number of virtual machines in the scale set.
                    type: int
                    sample: null
        platform_update_domain_count:
            description:
                - Update Domain count.
            type: int
            sample: null
        platform_fault_domain_count:
            description:
                - Fault Domain count.
            type: int
            sample: null
        virtual_machines:
            description:
                - A list of references to all virtual machines in the availability set.
            type: list
            sample: null
            contains:
                id:
                    description:
                        - Resource Id
                    type: str
                    sample: null
        proximity_placement_group:
            description:
                - >-
                    Specifies information about the proximity placement group that the
                    availability set should be assigned to.
                    :code:`<br>`:code:`<br>`Minimum api-version: 2018-04-01.
            type: dict
            sample: null
            contains:
                id:
                    description:
                        - Resource Id
                    type: str
                    sample: null
        statuses:
            description:
                - The resource status information.
            type: list
            sample: null
            contains:
                code:
                    description:
                        - The status code.
                    type: str
                    sample: null
                level:
                    description:
                        - The level code.
                    type: sealed-choice
                    sample: null
                display_status:
                    description:
                        - The short localizable label for the status.
                    type: str
                    sample: null
                message:
                    description:
                        - >-
                            The detailed status message, including for alerts and error
                            messages.
                    type: str
                    sample: null
                time:
                    description:
                        - The time of the status.
                    type: str
                    sample: null
        value:
            description:
                - |-
                    The list of availability sets
                    The list of virtual machine sizes.
            returned: always
            type: list
            sample: null
            contains:
                sku:
                    description:
                        - >-
                            Sku of the availability set, only name is required to be set. See
                            AvailabilitySetSkuTypes for possible set of values. Use 'Aligned'
                            for virtual machines with managed disks and 'Classic' for virtual
                            machines with unmanaged disks. Default value is 'Classic'.
                    type: dict
                    sample: null
                    contains:
                        name:
                            description:
                                - The sku name.
                            type: str
                            sample: null
                        tier:
                            description:
                                - >-
                                    Specifies the tier of virtual machines in a scale
                                    set.:code:`<br />`:code:`<br />` Possible Values::code:`<br
                                    />`:code:`<br />` **Standard**\ :code:`<br />`:code:`<br />`
                                    **Basic**
                            type: str
                            sample: null
                        capacity:
                            description:
                                - Specifies the number of virtual machines in the scale set.
                            type: int
                            sample: null
                platform_update_domain_count:
                    description:
                        - Update Domain count.
                    type: int
                    sample: null
                platform_fault_domain_count:
                    description:
                        - Fault Domain count.
                    type: int
                    sample: null
                virtual_machines:
                    description:
                        - >-
                            A list of references to all virtual machines in the availability
                            set.
                    type: list
                    sample: null
                    contains:
                        id:
                            description:
                                - Resource Id
                            type: str
                            sample: null
                proximity_placement_group:
                    description:
                        - >-
                            Specifies information about the proximity placement group that the
                            availability set should be assigned to.
                            :code:`<br>`:code:`<br>`Minimum api-version: 2018-04-01.
                    type: dict
                    sample: null
                    contains:
                        id:
                            description:
                                - Resource Id
                            type: str
                            sample: null
                statuses:
                    description:
                        - The resource status information.
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            type: str
                            sample: null
        next_link:
            description:
                - >-
                    The URI to fetch the next page of AvailabilitySets. Call ListNext()
                    with this URI to fetch the next page of AvailabilitySets.
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


class AzureRMAvailabilitySetInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            availability_set_name=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.availability_set_name = None
        self.expand = None

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
        super(AzureRMAvailabilitySetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.availability_set_name is not None):
            self.results['availability_sets'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.availability_set_name is not None):
            self.results['availability_sets'] = self.format_item(self.list_available_sizes())
        elif (self.resource_group is not None):
            self.results['availability_sets'] = self.format_item(self.list())
        else:
            self.results['availability_sets'] = self.format_item(self.list_by_subscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.availability_sets.get(resource_group=self.resource_group,
                                                              availability_set_name=self.availability_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_available_sizes(self):
        response = None

        try:
            response = self.mgmt_client.availability_sets.list_available_sizes(resource_group=self.resource_group,
                                                                               availability_set_name=self.availability_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.availability_sets.list(resource_group=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_subscription(self):
        response = None

        try:
            response = self.mgmt_client.availability_sets.list_by_subscription(expand=self.expand)
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
    AzureRMAvailabilitySetInfo()


if __name__ == '__main__':
    main()
