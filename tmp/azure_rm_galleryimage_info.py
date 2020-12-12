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
module: azure_rm_galleryimage_info
version_added: '2.9'
short_description: Get GalleryImage info.
description:
    - Get info of GalleryImage.
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    gallery_name:
        description:
            - >-
                The name of the Shared Image Gallery from which the Image Definitions
                are to be retrieved.
            - >-
                The name of the Shared Image Gallery from which Image Definitions are to
                be listed.
        required: true
        type: str
    gallery_image_name:
        description:
            - The name of the gallery Image Definition to be retrieved.
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a gallery image.
      azure_rm_galleryimage_info: 
        gallery_image_name: myGalleryImageName
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: List gallery images in a gallery.
      azure_rm_galleryimage_info: 
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
gallery_images:
    description: >-
        A list of dict results where the key is the name of the GalleryImage and the
        values are the facts for that GalleryImage.
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
                    The description of this gallery Image Definition resource. This
                    property is updatable.
            returned: always
            type: str
            sample: null
        eula:
            description:
                - The Eula agreement for the gallery Image Definition.
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
        os_type:
            description:
                - >-
                    This property allows you to specify the type of the OS that is
                    included in the disk when creating a VM from a managed image.
                    :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`:code:`<br>`
                    **Windows** :code:`<br>`:code:`<br>` **Linux**
            returned: always
            type: sealed-choice
            sample: null
        os_state:
            description:
                - >-
                    This property allows the user to specify whether the virtual machines
                    created under this image are 'Generalized' or 'Specialized'.
            returned: always
            type: sealed-choice
            sample: null
        hyper_v_generation:
            description:
                - >-
                    The hypervisor generation of the Virtual Machine. Applicable to OS
                    disks only.
            returned: always
            type: str
            sample: null
        end_of_life_date:
            description:
                - >-
                    The end of life date of the gallery Image Definition. This property
                    can be used for decommissioning purposes. This property is updatable.
            returned: always
            type: str
            sample: null
        identifier:
            description:
                - This is the gallery Image Definition identifier.
            returned: always
            type: dict
            sample: null
            contains:
                publisher:
                    description:
                        - The name of the gallery Image Definition publisher.
                    returned: always
                    type: str
                    sample: null
                offer:
                    description:
                        - The name of the gallery Image Definition offer.
                    returned: always
                    type: str
                    sample: null
                sku:
                    description:
                        - The name of the gallery Image Definition SKU.
                    returned: always
                    type: str
                    sample: null
        recommended:
            description:
                - >-
                    The properties describe the recommended machine configuration for this
                    Image Definition. These properties are updatable.
            returned: always
            type: dict
            sample: null
            contains:
                v_cp_us:
                    description:
                        - Describes the resource range.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        min:
                            description:
                                - The minimum number of the resource.
                            returned: always
                            type: int
                            sample: null
                        max:
                            description:
                                - The maximum number of the resource.
                            returned: always
                            type: int
                            sample: null
                memory:
                    description:
                        - Describes the resource range.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        min:
                            description:
                                - The minimum number of the resource.
                            returned: always
                            type: int
                            sample: null
                        max:
                            description:
                                - The maximum number of the resource.
                            returned: always
                            type: int
                            sample: null
        disallowed:
            description:
                - Describes the disallowed disk types.
            returned: always
            type: dict
            sample: null
            contains:
                disk_types:
                    description:
                        - A list of disk types.
                    returned: always
                    type: list
                    sample: null
        purchase_plan:
            description:
                - >-
                    Describes the gallery Image Definition purchase plan. This is used by
                    marketplace images.
            returned: always
            type: dict
            sample: null
            contains:
                name:
                    description:
                        - The plan ID.
                    returned: always
                    type: str
                    sample: null
                publisher:
                    description:
                        - The publisher ID.
                    returned: always
                    type: str
                    sample: null
                product:
                    description:
                        - The product ID.
                    returned: always
                    type: str
                    sample: null
        provisioning_state:
            description:
                - 'The provisioning state, which only appears in the response.'
            returned: always
            type: str
            sample: null
        value:
            description:
                - A list of Shared Image Gallery images.
            returned: always
            type: list
            sample: null
            contains:
                description:
                    description:
                        - >-
                            The description of this gallery Image Definition resource. This
                            property is updatable.
                    returned: always
                    type: str
                    sample: null
                eula:
                    description:
                        - The Eula agreement for the gallery Image Definition.
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
                os_type:
                    description:
                        - >-
                            This property allows you to specify the type of the OS that is
                            included in the disk when creating a VM from a managed image.
                            :code:`<br>`:code:`<br>` Possible values are:
                            :code:`<br>`:code:`<br>` **Windows** :code:`<br>`:code:`<br>`
                            **Linux**
                    returned: always
                    type: sealed-choice
                    sample: null
                os_state:
                    description:
                        - >-
                            This property allows the user to specify whether the virtual
                            machines created under this image are 'Generalized' or
                            'Specialized'.
                    returned: always
                    type: sealed-choice
                    sample: null
                hyper_v_generation:
                    description:
                        - >-
                            The hypervisor generation of the Virtual Machine. Applicable to OS
                            disks only.
                    returned: always
                    type: str
                    sample: null
                end_of_life_date:
                    description:
                        - >-
                            The end of life date of the gallery Image Definition. This
                            property can be used for decommissioning purposes. This property
                            is updatable.
                    returned: always
                    type: str
                    sample: null
                identifier:
                    description:
                        - This is the gallery Image Definition identifier.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        publisher:
                            description:
                                - The name of the gallery Image Definition publisher.
                            returned: always
                            type: str
                            sample: null
                        offer:
                            description:
                                - The name of the gallery Image Definition offer.
                            returned: always
                            type: str
                            sample: null
                        sku:
                            description:
                                - The name of the gallery Image Definition SKU.
                            returned: always
                            type: str
                            sample: null
                recommended:
                    description:
                        - >-
                            The properties describe the recommended machine configuration for
                            this Image Definition. These properties are updatable.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        v_cp_us:
                            description:
                                - Describes the resource range.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                min:
                                    description:
                                        - The minimum number of the resource.
                                    returned: always
                                    type: int
                                    sample: null
                                max:
                                    description:
                                        - The maximum number of the resource.
                                    returned: always
                                    type: int
                                    sample: null
                        memory:
                            description:
                                - Describes the resource range.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                min:
                                    description:
                                        - The minimum number of the resource.
                                    returned: always
                                    type: int
                                    sample: null
                                max:
                                    description:
                                        - The maximum number of the resource.
                                    returned: always
                                    type: int
                                    sample: null
                disallowed:
                    description:
                        - Describes the disallowed disk types.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        disk_types:
                            description:
                                - A list of disk types.
                            returned: always
                            type: list
                            sample: null
                purchase_plan:
                    description:
                        - >-
                            Describes the gallery Image Definition purchase plan. This is used
                            by marketplace images.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        name:
                            description:
                                - The plan ID.
                            returned: always
                            type: str
                            sample: null
                        publisher:
                            description:
                                - The publisher ID.
                            returned: always
                            type: str
                            sample: null
                        product:
                            description:
                                - The product ID.
                            returned: always
                            type: str
                            sample: null
        next_link:
            description:
                - >-
                    The uri to fetch the next page of Image Definitions in the Shared
                    Image Gallery. Call ListNext() with this to fetch the next page of
                    gallery Image Definitions.
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


class AzureRMGalleryImageInfo(AzureRMModuleBase):
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
            gallery_image_name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.gallery_name = None
        self.gallery_image_name = None

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
        super(AzureRMGalleryImageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01')

        if (self.resource_group is not None and
            self.gallery_name is not None and
            self.gallery_image_name is not None):
            self.results['gallery_images'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.gallery_name is not None):
            self.results['gallery_images'] = self.format_item(self.list_by_gallery())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gallery_images.get(resource_group=self.resource_group,
                                                           gallery_name=self.gallery_name,
                                                           gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_gallery(self):
        response = None

        try:
            response = self.mgmt_client.gallery_images.list_by_gallery(resource_group=self.resource_group,
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
    AzureRMGalleryImageInfo()


if __name__ == '__main__':
    main()
