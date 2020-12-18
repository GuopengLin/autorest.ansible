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
module: azure_rm_dedicatedhostgroup_info
version_added: '2.9'
short_description: Get DedicatedHostGroup info.
description:
    - Get info of DedicatedHostGroup.
options:
    resource_group:
        description:
            - The name of the resource group.
        type: str
    host_group_name:
        description:
            - The name of the dedicated host group.
        type: str
    expand:
        description:
            - >-
                The expand expression to apply on the operation. The response shows the
                list of instance view of the dedicated hosts under the dedicated host
                group.
        type: constant
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Create a dedicated host group.
      azure_rm_dedicatedhostgroup_info: 
        expand: instanceView
        host_group_name: myDedicatedHostGroup
        resource_group_name: myResourceGroup

'''

RETURN = '''
dedicated_host_groups:
    description: >-
        A list of dict results where the key is the name of the DedicatedHostGroup
        and the values are the facts for that DedicatedHostGroup.
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
        zones:
            description:
                - >-
                    Availability Zone to use for this host group. Only single zone is
                    supported. The zone can be assigned only during creation. If not
                    provided, the group supports all zones in the region. If provided,
                    enforces each host in the group to be in the same zone.
            type: list
            sample: null
        platform_fault_domain_count:
            description:
                - Number of fault domains that the host group can span.
            type: int
            sample: null
        hosts:
            description:
                - >-
                    A list of references to all dedicated hosts in the dedicated host
                    group.
            type: list
            sample: null
        instance_view:
            description:
                - >-
                    The dedicated host group instance view, which has the list of instance
                    view of the dedicated hosts under the dedicated host group.
            type: dict
            sample: null
        support_automatic_placement:
            description:
                - >-
                    Specifies whether virtual machines or virtual machine scale sets can
                    be placed automatically on the dedicated host group. Automatic
                    placement means resources are allocated on dedicated hosts, that are
                    chosen by Azure, under the dedicated host group. The value is
                    defaulted to 'true' when not provided. :code:`<br>`:code:`<br>`Minimum
                    api-version: 2020-06-01.
            type: bool
            sample: null
        value:
            description:
                - The list of dedicated host groups
            returned: always
            type: list
            sample: null
            contains:
                zones:
                    description:
                        - >-
                            Availability Zone to use for this host group. Only single zone is
                            supported. The zone can be assigned only during creation. If not
                            provided, the group supports all zones in the region. If provided,
                            enforces each host in the group to be in the same zone.
                    type: list
                    sample: null
                platform_fault_domain_count:
                    description:
                        - Number of fault domains that the host group can span.
                    type: int
                    sample: null
                support_automatic_placement:
                    description:
                        - >-
                            Specifies whether virtual machines or virtual machine scale sets
                            can be placed automatically on the dedicated host group. Automatic
                            placement means resources are allocated on dedicated hosts, that
                            are chosen by Azure, under the dedicated host group. The value is
                            defaulted to 'true' when not provided.
                            :code:`<br>`:code:`<br>`Minimum api-version: 2020-06-01.
                    type: bool
                    sample: null
        next_link:
            description:
                - >-
                    The URI to fetch the next page of Dedicated Host Groups. Call
                    ListNext() with this URI to fetch the next page of Dedicated Host
                    Groups.
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


class AzureRMDedicatedHostGroupInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            host_group_name=dict(
                type='str'
            ),
            expand=dict(
                type='constant'
            )
        )

        self.resource_group = None
        self.host_group_name = None
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
        super(AzureRMDedicatedHostGroupInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.host_group_name is not None):
            self.results['dedicated_host_groups'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['dedicated_host_groups'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['dedicated_host_groups'] = self.format_item(self.list_by_subscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_host_groups.get(resource_group=self.resource_group,
                                                                  host_group_name=self.host_group_name,
                                                                  expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_host_groups.list_by_resource_group(resource_group=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_subscription(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_host_groups.list_by_subscription()
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
    AzureRMDedicatedHostGroupInfo()


if __name__ == '__main__':
    main()
