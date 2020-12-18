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
module: azure_rm_virtualmachineimage
version_added: '2.9'
short_description: Manage Azure VirtualMachineImage instance.
description:
    - 'Create, update and delete instance of Azure VirtualMachineImage.'
options:
    location:
        description:
            - The name of a supported Azure region.
        required: true
        type: str
    publisher_name:
        description:
            - A valid image publisher.
        required: true
        type: str
    offer:
        description:
            - A valid image publisher offer.
        required: true
        type: str
    skus:
        description:
            - A valid image SKU.
        required: true
        type: str
    version:
        description:
            - A valid image SKU version.
        required: true
        type: str
    state:
        description:
            - Assert the state of the VirtualMachineImage.
            - >-
                Use C(present) to create or update an VirtualMachineImage and C(absent)
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
'''

RETURN = '''
name:
    description:
        - The name of the resource.
    returned: always
    type: str
    sample: null
location:
    description:
        - The supported Azure location of the resource.
    returned: always
    type: str
    sample: null
tags:
    description:
        - >-
            Specifies the tags that are assigned to the virtual machine. For more
            information about using tags, see `Using tags to organize your Azure
            resources
            <https://docs.microsoft.com/azure/azure-resource-manager/resource-group-using-tags.md>`_.
    type: dict
    sample: null
plan:
    description:
        - >-
            Used for establishing the purchase context of any 3rd Party artifact
            through MarketPlace.
    type: dict
    sample: null
    contains:
        publisher:
            description:
                - The publisher ID.
            returned: always
            type: str
            sample: null
        name:
            description:
                - The plan ID.
            returned: always
            type: str
            sample: null
        product:
            description:
                - >-
                    Specifies the product of the image from the marketplace. This is the
                    same value as Offer under the imageReference element.
            returned: always
            type: str
            sample: null
os_disk_image:
    description:
        - Contains the os disk image information.
    type: dict
    sample: null
    contains:
        operating_system:
            description:
                - The operating system of the osDiskImage.
            returned: always
            type: sealed-choice
            sample: null
data_disk_images:
    description:
        - ''
    type: list
    sample: null
automatic_os_upgrade_properties:
    description:
        - Describes automatic OS upgrade properties on the image.
    type: dict
    sample: null
    contains:
        automatic_os_upgrade_supported:
            description:
                - Specifies whether automatic OS upgrade is supported on the image.
            returned: always
            type: bool
            sample: null
hyper_v_generation:
    description:
        - Specifies the HyperVGeneration Type
    type: str
    sample: null
disallowed:
    description:
        - >-
            Specifies disallowed configuration for the VirtualMachine created from the
            image
    type: dict
    sample: null
    contains:
        vm_disk_type:
            description:
                - VM disk types which are disallowed.
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


class AzureRMVirtualMachineImage(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            publisher_name=dict(
                type='str',
                required=True
            ),
            offer=dict(
                type='str',
                required=True
            ),
            skus=dict(
                type='str',
                required=True
            ),
            version=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.location = None
        self.publisher_name = None
        self.offer = None
        self.skus = None
        self.version = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineImage, self).__init__(derived_arg_spec=self.module_arg_spec,
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

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_images.get(location=self.location,
                                                                   publisher_name=self.publisher_name,
                                                                   offer=self.offer,
                                                                   skus=self.skus,
                                                                   version=self.version)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineImage()


if __name__ == '__main__':
    main()
