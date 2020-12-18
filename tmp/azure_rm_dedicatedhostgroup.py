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
module: azure_rm_dedicatedhostgroup
version_added: '2.9'
short_description: Manage Azure DedicatedHostGroup instance.
description:
    - 'Create, update and delete instance of Azure DedicatedHostGroup.'
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    host_group_name:
        description:
            - The name of the dedicated host group.
        required: true
        type: str
    zones:
        description:
            - >-
                Availability Zone to use for this host group. Only single zone is
                supported. The zone can be assigned only during creation. If not
                provided, the group supports all zones in the region. If provided,
                enforces each host in the group to be in the same zone.
        type: list
    platform_fault_domain_count:
        description:
            - Number of fault domains that the host group can span.
        type: int
    support_automatic_placement:
        description:
            - >-
                Specifies whether virtual machines or virtual machine scale sets can be
                placed automatically on the dedicated host group. Automatic placement
                means resources are allocated on dedicated hosts, that are chosen by
                Azure, under the dedicated host group. The value is defaulted to 'true'
                when not provided. :code:`<br>`:code:`<br>`Minimum api-version:
                2020-06-01.
        type: bool
    expand:
        description:
            - >-
                The expand expression to apply on the operation. The response shows the
                list of instance view of the dedicated hosts under the dedicated host
                group.
        type: constant
    state:
        description:
            - Assert the state of the DedicatedHostGroup.
            - >-
                Use C(present) to create or update an DedicatedHostGroup and C(absent)
                to delete it.
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
    - name: Create or update a dedicated host group.
      azure_rm_dedicatedhostgroup: 
        host_group_name: myDedicatedHostGroup
        resource_group_name: myResourceGroup
        location: westus
        properties:
          platform_fault_domain_count: 3
          support_automatic_placement: true
        tags:
          department: finance
        zones:
          - '1'

'''

RETURN = '''
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
            supported. The zone can be assigned only during creation. If not provided,
            the group supports all zones in the region. If provided, enforces each
            host in the group to be in the same zone.
    type: list
    sample: null
platform_fault_domain_count:
    description:
        - Number of fault domains that the host group can span.
    type: int
    sample: null
hosts:
    description:
        - A list of references to all dedicated hosts in the dedicated host group.
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
            Specifies whether virtual machines or virtual machine scale sets can be
            placed automatically on the dedicated host group. Automatic placement
            means resources are allocated on dedicated hosts, that are chosen by
            Azure, under the dedicated host group. The value is defaulted to 'true'
            when not provided. :code:`<br>`:code:`<br>`Minimum api-version:
            2020-06-01.
    type: bool
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


class AzureRMDedicatedHostGroup(AzureRMModuleBaseExt):
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
            zones=dict(
                type='list',
                disposition='/zones',
                elements='str'
            ),
            platform_fault_domain_count=dict(
                type='int',
                disposition='/platform_fault_domain_count'
            ),
            support_automatic_placement=dict(
                type='bool',
                disposition='/support_automatic_placement'
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
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMDedicatedHostGroup, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.dedicated_host_groups.create_or_update(resource_group=self.resource_group,
                                                                               host_group_name=self.host_group_name,
                                                                               parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the DedicatedHostGroup instance.')
            self.fail('Error creating the DedicatedHostGroup instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.dedicated_host_groups.delete(resource_group=self.resource_group,
                                                                     host_group_name=self.host_group_name)
        except CloudError as e:
            self.log('Error attempting to delete the DedicatedHostGroup instance.')
            self.fail('Error deleting the DedicatedHostGroup instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.dedicated_host_groups.get(resource_group=self.resource_group,
                                                                  host_group_name=self.host_group_name,
                                                                  expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMDedicatedHostGroup()


if __name__ == '__main__':
    main()
