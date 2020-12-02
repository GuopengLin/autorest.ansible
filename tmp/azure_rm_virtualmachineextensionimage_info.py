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
    module: azure_rm_virtualmachineextensionimage_info
    version_added: '2.9'
    short_description: Get VirtualMachineExtensionImage info.
    description:
      - Get info of VirtualMachineExtensionImage.
    options:
      location:
        description:
          - The name of a supported Azure region.
        required: true
        type: str
      publisher_name:
        description:
          - undefined
        required: true
        type: str
      type:
        description:
          - undefined
        type: str
      version:
        description:
          - undefined
        type: str
      filter:
        description:
          - The filter to apply on the operation.
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
    virtual_machine_extension_images:
      description: >-
        A list of dict results where the key is the name of the
        VirtualMachineExtensionImage and the values are the facts for that
        VirtualMachineExtensionImage.
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
        operating_system:
          description:
            - The operating system this extension supports.
          returned: always
          type: str
          sample: null
        compute_role:
          description:
            - The type of role (IaaS or PaaS) this extension supports.
          returned: always
          type: str
          sample: null
        handler_schema:
          description:
            - >-
              The schema defined by publisher, where extension consumers should
              provide settings in a matching schema.
          returned: always
          type: str
          sample: null
        vm_scale_set_enabled:
          description:
            - >-
              Whether the extension can be used on xRP VMScaleSets. By default
              existing extensions are usable on scalesets, but there might be cases
              where a publisher wants to explicitly indicate the extension is only
              enabled for CRP VMs but not VMSS.
          returned: always
          type: bool
          sample: null
        supports_multiple_extensions:
          description:
            - Whether the handler can support multiple extensions.
          returned: always
          type: bool
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


class AzureRMVirtualMachineExtensionImageInfo(AzureRMModuleBase):
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
            type=dict(
                type='str'
            ),
            version=dict(
                type='str'
            ),
            filter=dict(
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
        self.type = None
        self.version = None
        self.filter = None
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
        super(AzureRMVirtualMachineExtensionImageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.location is not None and
            self.publisher_name is not None and
            self.type is not None and
            self.version is not None):
            self.results['virtual_machine_extension_images'] = self.format_item(self.get())
        elif (self.location is not None and
              self.publisher_name is not None and
              self.type is not None):
            self.results['virtual_machine_extension_images'] = self.format_item(self.list_versions())
        elif (self.location is not None and
              self.publisher_name is not None):
            self.results['virtual_machine_extension_images'] = self.format_item(self.list_types())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_extension_images.get(location=self.location,
                                                                             publisher_name=self.publisher_name,
                                                                             type=self.type,
                                                                             version=self.version)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_versions(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_extension_images.list_versions(location=self.location,
                                                                                       publisher_name=self.publisher_name,
                                                                                       type=self.type,
                                                                                       filter=self.filter,
                                                                                       top=self.top,
                                                                                       orderby=self.orderby)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_types(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_extension_images.list_types(location=self.location,
                                                                                    publisher_name=self.publisher_name)
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
    AzureRMVirtualMachineExtensionImageInfo()


if __name__ == '__main__':
    main()
