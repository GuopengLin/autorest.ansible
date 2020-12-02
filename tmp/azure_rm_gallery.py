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
module: azure_rm_gallery
version_added: '2.9'
short_description: Manage Azure Gallery instance.
description:
    - 'Create, update and delete instance of Azure Gallery.'
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    gallery_name:
        description:
            - >-
                The name of the Shared Image Gallery. The allowed characters are
                alphabets and numbers with dots and periods allowed in the middle. The
                maximum length is 80 characters.
            - The name of the Shared Image Gallery to be deleted.
        required: true
        type: str
    description:
        description:
            - >-
                The description of this Shared Image Gallery resource. This property is
                updatable.
        type: str
    state:
        description:
            - Assert the state of the Gallery.
            - >-
                Use C(present) to create or update an Gallery and C(absent) to delete
                it.
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
    - name: Create or update a simple gallery.
      azure_rm_gallery: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        location: West US
        properties:
          description: This is the gallery description.
        

    - name: Update a simple gallery.
      azure_rm_gallery: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        properties:
          description: This is the gallery description.
        

    - name: Delete a gallery.
      azure_rm_gallery: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
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
description:
    description:
        - >-
            The description of this Shared Image Gallery resource. This property is
            updatable.
    returned: always
    type: str
    sample: null
identifier:
    description:
        - Describes the gallery unique name.
    returned: always
    type: dict
    sample: null
provisioning_state:
    description:
        - 'The provisioning state, which only appears in the response.'
    returned: always
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


class AzureRMGallery(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            gallery_name=dict(
                type='str',
                required=True
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.gallery_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGallery, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2019-12-01')

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

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.galleries.create_or_update(resource_group=self.resource_group,
                                                                   gallery_name=self.gallery_name,
                                                                   gallery=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Gallery instance.')
            self.fail('Error creating the Gallery instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.galleries.delete(resource_group=self.resource_group,
                                                         gallery_name=self.gallery_name)
        except CloudError as e:
            self.log('Error attempting to delete the Gallery instance.')
            self.fail('Error deleting the Gallery instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.galleries.get(resource_group=self.resource_group,
                                                      gallery_name=self.gallery_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGallery()


if __name__ == '__main__':
    main()
