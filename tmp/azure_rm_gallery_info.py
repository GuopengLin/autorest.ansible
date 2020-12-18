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
module: azure_rm_gallery_info
version_added: '2.9'
short_description: Get Gallery info.
description:
    - Get info of Gallery.
options:
    resource_group:
        description:
            - The name of the resource group.
        type: str
    name:
        description:
            - The name of the Shared Image Gallery.
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a gallery.
      azure_rm_gallery_info: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup

    - name: List galleries in a resource group.
      azure_rm_gallery_info: 
        resource_group_name: myResourceGroup

    - name: List galleries in a subscription.
      azure_rm_gallery_info: 

'''

RETURN = '''
galleries:
    description: >-
        A list of dict results where the key is the name of the Gallery and the
        values are the facts for that Gallery.
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
        description:
            description:
                - >-
                    The description of this Shared Image Gallery resource. This property
                    is updatable.
            type: str
            sample: null
        identifier:
            description:
                - Describes the gallery unique name.
            type: dict
            sample: null
        provisioning_state:
            description:
                - 'The provisioning state, which only appears in the response.'
            type: str
            sample: null
        value:
            description:
                - A list of galleries.
            returned: always
            type: list
            sample: null
            contains:
                description:
                    description:
                        - >-
                            The description of this Shared Image Gallery resource. This
                            property is updatable.
                    type: str
                    sample: null
        next_link:
            description:
                - >-
                    The uri to fetch the next page of galleries. Call ListNext() with this
                    to fetch the next page of galleries.
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


class AzureRMGalleryInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2019-12-01'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMGalleryInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01')

        if (self.resource_group is not None and
            self.name is not None):
            self.results['galleries'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['galleries'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['galleries'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.galleries.get(resource_group=self.resource_group,
                                                      name=self.name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.galleries.list_by_resource_group(resource_group=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.galleries.list()
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
    AzureRMGalleryInfo()


if __name__ == '__main__':
    main()
