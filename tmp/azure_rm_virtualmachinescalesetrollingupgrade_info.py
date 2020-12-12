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
module: azure_rm_virtualmachinescalesetrollingupgrade_info
version_added: '2.9'
short_description: Get VirtualMachineScaleSetRollingUpgrade info.
description:
    - Get info of VirtualMachineScaleSetRollingUpgrade.
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    vm_scale_set_name:
        description:
            - The name of the VM scale set.
        required: true
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
'''

RETURN = '''
virtual_machine_scale_set_rolling_upgrades:
    description: >-
        A list of dict results where the key is the name of the
        VirtualMachineScaleSetRollingUpgrade and the values are the facts for that
        VirtualMachineScaleSetRollingUpgrade.
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
        policy:
            description:
                - The rolling upgrade policies applied for this upgrade.
            returned: always
            type: dict
            sample: null
            contains:
                max_batch_instance_percent:
                    description:
                        - >-
                            The maximum percent of total virtual machine instances that will
                            be upgraded simultaneously by the rolling upgrade in one batch. As
                            this is a maximum, unhealthy instances in previous or future
                            batches can cause the percentage of instances in a batch to
                            decrease to ensure higher reliability. The default value for this
                            parameter is 20%.
                    returned: always
                    type: int
                    sample: null
                max_unhealthy_instance_percent:
                    description:
                        - >-
                            The maximum percentage of the total virtual machine instances in
                            the scale set that can be simultaneously unhealthy, either as a
                            result of being upgraded, or by being found in an unhealthy state
                            by the virtual machine health checks before the rolling upgrade
                            aborts. This constraint will be checked prior to starting any
                            batch. The default value for this parameter is 20%.
                    returned: always
                    type: int
                    sample: null
                max_unhealthy_upgraded_instance_percent:
                    description:
                        - >-
                            The maximum percentage of upgraded virtual machine instances that
                            can be found to be in an unhealthy state. This check will happen
                            after each batch is upgraded. If this percentage is ever exceeded,
                            the rolling update aborts. The default value for this parameter is
                            20%.
                    returned: always
                    type: int
                    sample: null
                pause_time_between_batches:
                    description:
                        - >-
                            The wait time between completing the update for all virtual
                            machines in one batch and starting the next batch. The time
                            duration should be specified in ISO 8601 format. The default value
                            is 0 seconds (PT0S).
                    returned: always
                    type: str
                    sample: null
        running_status:
            description:
                - Information about the current running state of the overall upgrade.
            returned: always
            type: dict
            sample: null
        progress:
            description:
                - >-
                    Information about the number of virtual machine instances in each
                    upgrade state.
            returned: always
            type: dict
            sample: null
        error:
            description:
                - 'Error details for this upgrade, if there are any.'
            returned: always
            type: dict
            sample: null
            contains:
                details:
                    description:
                        - The Api error details
                    returned: always
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The error code.
                            returned: always
                            type: str
                            sample: null
                        target:
                            description:
                                - The target of the particular error.
                            returned: always
                            type: str
                            sample: null
                        message:
                            description:
                                - The error message.
                            returned: always
                            type: str
                            sample: null
                innererror:
                    description:
                        - The Api inner error
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        exceptiontype:
                            description:
                                - The exception type.
                            returned: always
                            type: str
                            sample: null
                        errordetail:
                            description:
                                - The internal error message or exception dump.
                            returned: always
                            type: str
                            sample: null
                code:
                    description:
                        - The error code.
                    returned: always
                    type: str
                    sample: null
                target:
                    description:
                        - The target of the particular error.
                    returned: always
                    type: str
                    sample: null
                message:
                    description:
                        - The error message.
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


class AzureRMVirtualMachineScaleSetRollingUpgradeInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            vm_scale_set_name=dict(
                type='str',
                required=True
            )
        )

        self.resource_group = None
        self.vm_scale_set_name = None

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
        super(AzureRMVirtualMachineScaleSetRollingUpgradeInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.vm_scale_set_name is not None):
            self.results['virtual_machine_scale_set_rolling_upgrades'] = self.format_item(self.get_latest())
        return self.results

    def get_latest(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_rolling_upgrades.get_latest(resource_group=self.resource_group,
                                                                                              vm_scale_set_name=self.vm_scale_set_name)
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
    AzureRMVirtualMachineScaleSetRollingUpgradeInfo()


if __name__ == '__main__':
    main()
