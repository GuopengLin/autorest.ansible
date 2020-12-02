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
    module: azure_rm_virtualmachineimage_info
    version_added: '2.9'
    short_description: Get VirtualMachineImage info.
    description:
      - Get info of VirtualMachineImage.
    options:
      location:
        description:
          - The name of a supported Azure region.
        required: true
        type: str
      publisher_name:
        description:
          - A valid image publisher.
        type: str
      offer:
        description:
          - A valid image publisher offer.
        type: str
      skus:
        description:
          - A valid image SKU.
        type: str
      version:
        description:
          - A valid image SKU version.
        type: str
      expand:
        description:
          - The expand expression to apply on the operation.
        type: str
      top:
        description:
          - undefined
        type: int
      orderby:
        description:
          - undefined
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
    virtual_machine_images:
      description: >-
        A list of dict results where the key is the name of the VirtualMachineImage
        and the values are the facts for that VirtualMachineImage.
      returned: always
      type: complex
      contains:
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
          returned: always
          type: dict
          sample: null
        plan:
          description:
            - >-
              Used for establishing the purchase context of any 3rd Party artifact
              through MarketPlace.
          returned: always
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
                  Specifies the product of the image from the marketplace. This is
                  the same value as Offer under the imageReference element.
              returned: always
              type: str
              sample: null
        os_disk_image:
          description:
            - Contains the os disk image information.
          returned: always
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
          returned: always
          type: list
          sample: null
        automatic_os_upgrade_properties:
          description:
            - Describes automatic OS upgrade properties on the image.
          returned: always
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
          returned: always
          type: str
          sample: null
        disallowed:
          description:
            - >-
              Specifies disallowed configuration for the VirtualMachine created from
              the image
          returned: always
          type: dict
          sample: null
          contains:
            vm_disk_type:
              description:
                - VM disk types which are disallowed.
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


class AzureRMVirtualMachineImageInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            location=dict(
                type='str',
                required=True
            ),
            publisher_name=dict(
                type='str'
            ),
            offer=dict(
                type='str'
            ),
            skus=dict(
                type='str'
            ),
            version=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            ),
            top=dict(
                type='int'
            ),
            orderby=dict(
                type='str'
            )
        )

        self.location = None
        self.publisher_name = None
        self.offer = None
        self.skus = None
        self.version = None
        self.expand = None
        self.top = None
        self.orderby = None

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
        super(AzureRMVirtualMachineImageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.location is not None and
            self.publisher_name is not None and
            self.offer is not None and
            self.skus is not None and
            self.version is not None):
            self.results['virtual_machine_images'] = self.format_item(self.get())
        elif (self.location is not None and
              self.publisher_name is not None and
              self.offer is not None and
              self.skus is not None):
            self.results['virtual_machine_images'] = self.format_item(self.list())
        elif (self.location is not None and
              self.publisher_name is not None and
              self.offer is not None):
            self.results['virtual_machine_images'] = self.format_item(self.list_skus())
        elif (self.location is not None and
              self.publisher_name is not None):
            self.results['virtual_machine_images'] = self.format_item(self.list_offers())
        elif (self.location is not None):
            self.results['virtual_machine_images'] = self.format_item(self.list_publishers())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_images.get(location=self.location,
                                                                   publisher_name=self.publisher_name,
                                                                   offer=self.offer,
                                                                   skus=self.skus,
                                                                   version=self.version)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_images.list(location=self.location,
                                                                    publisher_name=self.publisher_name,
                                                                    offer=self.offer,
                                                                    skus=self.skus,
                                                                    expand=self.expand,
                                                                    top=self.top,
                                                                    orderby=self.orderby)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_skus(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_images.list_skus(location=self.location,
                                                                         publisher_name=self.publisher_name,
                                                                         offer=self.offer)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_offers(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_images.list_offers(location=self.location,
                                                                           publisher_name=self.publisher_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_publishers(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_images.list_publishers(location=self.location)
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
    AzureRMVirtualMachineImageInfo()


if __name__ == '__main__':
    main()
