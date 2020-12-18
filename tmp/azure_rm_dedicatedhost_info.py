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
module: azure_rm_dedicatedhost_info
version_added: '2.9'
short_description: Get DedicatedHost info.
description:
    - Get info of DedicatedHost.
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
            - The name of the dedicated host.
        type: str
    expand:
        description:
            - The expand expression to apply on the operation.
        type: constant
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a dedicated host.
      azure_rm_dedicatedhost_info: 
        host_group_name: myDedicatedHostGroup
        host_name: myHost
        resource_group_name: myResourceGroup

'''

RETURN = '''
dedicated_hosts:
    description: >-
        A list of dict results where the key is the name of the DedicatedHost and
        the values are the facts for that DedicatedHost.
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
                    SKU of the dedicated host for Hardware Generation and VM family. Only
                    name is required to be set. List Microsoft.Compute SKUs for a list of
                    possible values.
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
                    Specifies whether the dedicated host should be replaced automatically
                    in case of a failure. The value is defaulted to 'true' when not
                    provided.
            type: bool
            sample: null
        host_id:
            description:
                - >-
                    A unique id generated and assigned to the dedicated host by the
                    platform. :code:`<br>`:code:`<br>` Does not change throughout the
                    lifetime of the host.
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
                    deployed on the dedicated host. :code:`<br>`:code:`<br>` Possible
                    values are: :code:`<br>`:code:`<br>` **None** :code:`<br>`:code:`<br>`
                    **Windows_Server_Hybrid** :code:`<br>`:code:`<br>`
                    **Windows_Server_Perpetual** :code:`<br>`:code:`<br>` Default:
                    **None**
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
                                    The unutilized capacity of the dedicated host represented in
                                    terms of each VM size that is allowed to be deployed to the
                                    dedicated host.
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
        value:
            description:
                - The list of dedicated hosts
            returned: always
            type: list
            sample: null
            contains:
                sku:
                    description:
                        - >-
                            SKU of the dedicated host for Hardware Generation and VM family.
                            Only name is required to be set. List Microsoft.Compute SKUs for a
                            list of possible values.
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
                platform_fault_domain:
                    description:
                        - Fault domain of the dedicated host within a dedicated host group.
                    type: int
                    sample: null
                auto_replace_on_failure:
                    description:
                        - >-
                            Specifies whether the dedicated host should be replaced
                            automatically in case of a failure. The value is defaulted to
                            'true' when not provided.
                    type: bool
                    sample: null
                license_type:
                    description:
                        - >-
                            Specifies the software license type that will be applied to the
                            VMs deployed on the dedicated host. :code:`<br>`:code:`<br>`
                            Possible values are: :code:`<br>`:code:`<br>` **None**
                            :code:`<br>`:code:`<br>` **Windows_Server_Hybrid**
                            :code:`<br>`:code:`<br>` **Windows_Server_Perpetual**
                            :code:`<br>`:code:`<br>` Default: **None**
                    type: sealed-choice
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
                                            The unutilized capacity of the dedicated host represented
                                            in terms of each VM size that is allowed to be deployed to
                                            the dedicated host.
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
                                                    Maximum number of VMs of size vmSize that can fit in
                                                    the dedicated host's remaining capacity.
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
                                            The detailed status message, including for alerts and
                                            error messages.
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
                    The URI to fetch the next page of dedicated hosts. Call ListNext()
                    with this URI to fetch the next page of dedicated hosts.
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


class AzureRMDedicatedHostInfo(AzureRMModuleBase):
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
                type='str'
            ),
            expand=dict(
                type='constant'
            )
        )

        self.resource_group = None
        self.host_group_name = None
        self.host_name = None
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
        super(AzureRMDedicatedHostInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.host_group_name is not None and
            self.host_name is not None):
            self.results['dedicated_hosts'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.host_group_name is not None):
            self.results['dedicated_hosts'] = self.format_item(self.list_by_host_group())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_hosts.get(resource_group=self.resource_group,
                                                            host_group_name=self.host_group_name,
                                                            host_name=self.host_name,
                                                            expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_host_group(self):
        response = None

        try:
            response = self.mgmt_client.dedicated_hosts.list_by_host_group(resource_group=self.resource_group,
                                                                           host_group_name=self.host_group_name)
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
    AzureRMDedicatedHostInfo()


if __name__ == '__main__':
    main()
