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
module: azure_rm_galleryapplication_info
version_added: '2.9'
short_description: Get GalleryApplication info.
description:
    - Get info of GalleryApplication.
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    gallery_name:
        description:
            - >-
                The name of the Shared Application Gallery from which the Application
                Definitions are to be retrieved.
            - >-
                The name of the Shared Application Gallery from which Application
                Definitions are to be listed.
        required: true
        type: str
    gallery_application_name:
        description:
            - The name of the gallery Application Definition to be retrieved.
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a gallery Application.
      azure_rm_galleryapplication_info: 
        gallery_application_name: myGalleryApplicationName
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: List gallery Applications in a gallery.
      azure_rm_galleryapplication_info: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
gallery_applications:
    description: >-
        A list of dict results where the key is the name of the GalleryApplication
        and the values are the facts for that GalleryApplication.
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
        description:
            description:
                - >-
                    The description of this gallery Application Definition resource. This
                    property is updatable.
            returned: always
            type: str
            sample: null
        eula:
            description:
                - The Eula agreement for the gallery Application Definition.
            returned: always
            type: str
            sample: null
        privacy_statement_uri:
            description:
                - The privacy statement uri.
            returned: always
            type: str
            sample: null
        release_note_uri:
            description:
                - The release note uri.
            returned: always
            type: str
            sample: null
        end_of_life_date:
            description:
                - >-
                    The end of life date of the gallery Application Definition. This
                    property can be used for decommissioning purposes. This property is
                    updatable.
            returned: always
            type: str
            sample: null
        supported_os_type:
            description:
                - >-
                    This property allows you to specify the supported type of the OS that
                    application is built for. :code:`<br>`:code:`<br>` Possible values
                    are: :code:`<br>`:code:`<br>` **Windows** :code:`<br>`:code:`<br>`
                    **Linux**
            returned: always
            type: sealed-choice
            sample: null
        value:
            description:
                - A list of Gallery Applications.
            returned: always
            type: list
            sample: null
            contains:
                description:
                    description:
                        - >-
                            The description of this gallery Application Definition resource.
                            This property is updatable.
                    returned: always
                    type: str
                    sample: null
                eula:
                    description:
                        - The Eula agreement for the gallery Application Definition.
                    returned: always
                    type: str
                    sample: null
                privacy_statement_uri:
                    description:
                        - The privacy statement uri.
                    returned: always
                    type: str
                    sample: null
                release_note_uri:
                    description:
                        - The release note uri.
                    returned: always
                    type: str
                    sample: null
                end_of_life_date:
                    description:
                        - >-
                            The end of life date of the gallery Application Definition. This
                            property can be used for decommissioning purposes. This property
                            is updatable.
                    returned: always
                    type: str
                    sample: null
                supported_os_type:
                    description:
                        - >-
                            This property allows you to specify the supported type of the OS
                            that application is built for. :code:`<br>`:code:`<br>` Possible
                            values are: :code:`<br>`:code:`<br>` **Windows**
                            :code:`<br>`:code:`<br>` **Linux**
                    returned: always
                    type: sealed-choice
                    sample: null
        next_link:
            description:
                - >-
                    The uri to fetch the next page of Application Definitions in the
                    Application Gallery. Call ListNext() with this to fetch the next page
                    of gallery Application Definitions.
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


class AzureRMGalleryApplicationInfo(AzureRMModuleBase):
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
            gallery_application_name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.gallery_name = None
        self.gallery_application_name = None

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
        super(AzureRMGalleryApplicationInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01')

        if (self.resource_group is not None and
            self.gallery_name is not None and
            self.gallery_application_name is not None):
            self.results['gallery_applications'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.gallery_name is not None):
            self.results['gallery_applications'] = self.format_item(self.list_by_gallery())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gallery_applications.get(resource_group=self.resource_group,
                                                                 gallery_name=self.gallery_name,
                                                                 gallery_application_name=self.gallery_application_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_gallery(self):
        response = None

        try:
            response = self.mgmt_client.gallery_applications.list_by_gallery(resource_group=self.resource_group,
                                                                             gallery_name=self.gallery_name)
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
    AzureRMGalleryApplicationInfo()


if __name__ == '__main__':
    main()
