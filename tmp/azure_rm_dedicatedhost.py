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
module: azure_rm_dedicatedhost
version_added: '2.9'
short_description: Manage Azure DedicatedHost instance.
description:
    - 'Create, update and delete instance of Azure DedicatedHost.'
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
    host_name:
        description:
            - The name of the dedicated host .
            - The name of the dedicated host.
        required: true
        type: str
    sku:
        description:
            - >-
                SKU of the dedicated host for Hardware Generation and VM family. Only
                name is required to be set. List Microsoft.Compute SKUs for a list of
                possible values.
        type: dict
        suboptions:
            name:
                description:
                    - The sku name.
                type: str
            tier:
                description:
                    - >-
                        Specifies the tier of virtual machines in a scale set.:code:`<br
                        />`:code:`<br />` Possible Values::code:`<br />`:code:`<br />`
                        **Standard**\ :code:`<br />`:code:`<br />` **Basic**
                type: str
            capacity:
                description:
                    - Specifies the number of virtual machines in the scale set.
                type: int
    platform_fault_domain:
        description:
            - Fault domain of the dedicated host within a dedicated host group.
        type: int
    auto_replace_on_failure:
        description:
            - >-
                Specifies whether the dedicated host should be replaced automatically in
                case of a failure. The value is defaulted to 'true' when not provided.
        type: bool
    license_type:
        description:
            - >-
                Specifies the software license type that will be applied to the VMs
                deployed on the dedicated host. :code:`<br>`:code:`<br>` Possible values
                are: :code:`<br>`:code:`<br>` **None** :code:`<br>`:code:`<br>`
                **Windows_Server_Hybrid** :code:`<br>`:code:`<br>`
                **Windows_Server_Perpetual** :code:`<br>`:code:`<br>` Default: **None**
        type: sealed-choice
    instance_view:
        description:
            - The dedicated host instance view.
        type: dict
        suboptions:
            available_capacity:
                description:
                    - Unutilized capacity of the dedicated host.
                type: dict
                suboptions:
                    allocatable_v_ms:
                        description:
                            - >-
                                The unutilized capacity of the dedicated host represented in
                                terms of each VM size that is allowed to be deployed to the
                                dedicated host.
                        type: list
                        suboptions:
                            vm_size:
                                description:
                                    - >-
                                        VM size in terms of which the unutilized capacity is
                                        represented.
                                type: str
                            count:
                                description:
                                    - >-
                                        Maximum number of VMs of size vmSize that can fit in the
                                        dedicated host's remaining capacity.
                                type: number
            statuses:
                description:
                    - The resource status information.
                type: list
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
    expand:
        description:
            - The expand expression to apply on the operation.
        type: constant
    state:
        description:
            - Assert the state of the DedicatedHost.
            - >-
                Use C(present) to create or update an DedicatedHost and C(absent) to
                delete it.
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
    - name: Create or update a dedicated host .
      azure_rm_dedicatedhost: 
        host_group_name: myDedicatedHostGroup
        host_name: myDedicatedHost
        resource_group_name: myResourceGroup
        location: westus
        properties:
          platform_fault_domain: 1
        sku:
          name: DSv3-Type1
        tags:
          department: HR

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
sku:
    description:
        - >-
            SKU of the dedicated host for Hardware Generation and VM family. Only name
            is required to be set. List Microsoft.Compute SKUs for a list of possible
            values.
    returned: always
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
platform_fault_domain:
    description:
        - Fault domain of the dedicated host within a dedicated host group.
    type: int
    sample: null
auto_replace_on_failure:
    description:
        - >-
            Specifies whether the dedicated host should be replaced automatically in
            case of a failure. The value is defaulted to 'true' when not provided.
    type: bool
    sample: null
host_id:
    description:
        - >-
            A unique id generated and assigned to the dedicated host by the platform.
            :code:`<br>`:code:`<br>` Does not change throughout the lifetime of the
            host.
    type: str
    sample: null
virtual_machines:
    description:
        - A list of references to all virtual machines in the Dedicated Host.
    type: list
    sample: null
license_type:
    description:
        - >-
            Specifies the software license type that will be applied to the VMs
            deployed on the dedicated host. :code:`<br>`:code:`<br>` Possible values
            are: :code:`<br>`:code:`<br>` **None** :code:`<br>`:code:`<br>`
            **Windows_Server_Hybrid** :code:`<br>`:code:`<br>`
            **Windows_Server_Perpetual** :code:`<br>`:code:`<br>` Default: **None**
    type: sealed-choice
    sample: null
provisioning_time:
    description:
        - The date when the host was first provisioned.
    type: str
    sample: null
provisioning_state:
    description:
        - 'The provisioning state, which only appears in the response.'
    type: str
    sample: null
instance_view:
    description:
        - The dedicated host instance view.
    type: dict
    sample: null
    contains:
        available_capacity:
            description:
                - Unutilized capacity of the dedicated host.
            type: dict
            sample: null
            contains:
                allocatable_v_ms:
                    description:
                        - >-
                            The unutilized capacity of the dedicated host represented in terms
                            of each VM size that is allowed to be deployed to the dedicated
                            host.
                    type: list
                    sample: null
                    contains:
                        vm_size:
                            description:
                                - >-
                                    VM size in terms of which the unutilized capacity is
                                    represented.
                            type: str
                            sample: null
                        count:
                            description:
                                - >-
                                    Maximum number of VMs of size vmSize that can fit in the
                                    dedicated host's remaining capacity.
                            type: number
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
