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
    module: azure_rm_galleryimage
    version_added: '2.9'
    short_description: Manage Azure GalleryImage instance.
    description:
      - 'Create, update and delete instance of Azure GalleryImage.'
    options:
      resource_group:
        description:
          - The name of the resource group.
        required: true
        type: str
      gallery_name:
        description:
          - >-
            The name of the Shared Image Gallery in which the Image Definition is to
            be created.
          - >-
            The name of the Shared Image Gallery in which the Image Definition is to
            be updated.
          - >-
            The name of the Shared Image Gallery from which the Image Definitions
            are to be retrieved.
          - >-
            The name of the Shared Image Gallery in which the Image Definition is to
            be deleted.
        required: true
        type: str
      gallery_image_name:
        description:
          - >-
            The name of the gallery Image Definition to be created or updated. The
            allowed characters are alphabets and numbers with dots, dashes, and
            periods allowed in the middle. The maximum length is 80 characters.
          - >-
            The name of the gallery Image Definition to be updated. The allowed
            characters are alphabets and numbers with dots, dashes, and periods
            allowed in the middle. The maximum length is 80 characters.
          - The name of the gallery Image Definition to be retrieved.
          - The name of the gallery Image Definition to be deleted.
        required: true
        type: str
      description:
        description:
          - >-
            The description of this gallery Image Definition resource. This property
            is updatable.
        type: str
      eula:
        description:
          - The Eula agreement for the gallery Image Definition.
        type: str
      privacy_statement_uri:
        description:
          - The privacy statement uri.
        type: str
      release_note_uri:
        description:
          - The release note uri.
        type: str
      os_type:
        description:
          - >-
            This property allows you to specify the type of the OS that is included
            in the disk when creating a VM from a managed image.
            :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`:code:`<br>`
            **Windows** :code:`<br>`:code:`<br>` **Linux**
        type: sealed-choice
      os_state:
        description:
          - >-
            This property allows the user to specify whether the virtual machines
            created under this image are 'Generalized' or 'Specialized'.
        type: sealed-choice
      hyper_v_generation:
        description:
          - >-
            The hypervisor generation of the Virtual Machine. Applicable to OS disks
            only.
        type: str
        choices:
          - V1
          - V2
      end_of_life_date:
        description:
          - >-
            The end of life date of the gallery Image Definition. This property can
            be used for decommissioning purposes. This property is updatable.
        type: str
      identifier:
        description:
          - This is the gallery Image Definition identifier.
        type: dict
        suboptions:
          publisher:
            description:
              - The name of the gallery Image Definition publisher.
            required: true
            type: str
          offer:
            description:
              - The name of the gallery Image Definition offer.
            required: true
            type: str
          sku:
            description:
              - The name of the gallery Image Definition SKU.
            required: true
            type: str
      recommended:
        description:
          - >-
            The properties describe the recommended machine configuration for this
            Image Definition. These properties are updatable.
        type: dict
        suboptions:
          v_cp_us:
            description:
              - Describes the resource range.
            type: dict
            suboptions:
              min:
                description:
                  - The minimum number of the resource.
                type: int
              max:
                description:
                  - The maximum number of the resource.
                type: int
          memory:
            description:
              - Describes the resource range.
            type: dict
            suboptions:
              min:
                description:
                  - The minimum number of the resource.
                type: int
              max:
                description:
                  - The maximum number of the resource.
                type: int
      disallowed:
        description:
          - Describes the disallowed disk types.
        type: dict
        suboptions:
          disk_types:
            description:
              - A list of disk types.
            type: list
      purchase_plan:
        description:
          - >-
            Describes the gallery Image Definition purchase plan. This is used by
            marketplace images.
        type: dict
        suboptions:
          name:
            description:
              - The plan ID.
            type: str
          publisher:
            description:
              - The publisher ID.
            type: str
          product:
            description:
              - The product ID.
            type: str
      state:
        description:
          - Assert the state of the GalleryImage.
          - >-
            Use C(present) to create or update an GalleryImage and C(absent) to
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
    - name: Create or update a simple gallery image.
      azure_rm_galleryimage: 
        gallery_image_name: myGalleryImageName
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Update a simple gallery image.
      azure_rm_galleryimage: 
        gallery_image_name: myGalleryImageName
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Delete a gallery image.
      azure_rm_galleryimage: 
        gallery_image_name: myGalleryImageName
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
          The description of this gallery Image Definition resource. This property
          is updatable.
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
          This property allows you to specify the type of the OS that is included in
          the disk when creating a VM from a managed image. :code:`<br>`:code:`<br>`
          Possible values are: :code:`<br>`:code:`<br>` **Windows**
          :code:`<br>`:code:`<br>` **Linux**
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
          The hypervisor generation of the Virtual Machine. Applicable to OS disks
          only.
      returned: always
      type: str
      sample: null
    end_of_life_date:
      description:
        - >-
          The end of life date of the gallery Image Definition. This property can be
          used for decommissioning purposes. This property is updatable.
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


class AzureRMGalleryImage(AzureRMModuleBaseExt):
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
                type='str',
                required=True
            ),
            description=dict(
                type='str',
                disposition='/description'
            ),
            eula=dict(
                type='str',
                disposition='/eula'
            ),
            privacy_statement_uri=dict(
                type='str',
                disposition='/privacy_statement_uri'
            ),
            release_note_uri=dict(
                type='str',
                disposition='/release_note_uri'
            ),
            os_type=dict(
                type='sealed-choice',
                disposition='/os_type'
            ),
            os_state=dict(
                type='sealed-choice',
                disposition='/os_state'
            ),
            hyper_v_generation=dict(
                type='str',
                disposition='/hyper_v_generation',
                choices=['V1',
                         'V2']
            ),
            end_of_life_date=dict(
                type='str',
                disposition='/end_of_life_date'
            ),
            identifier=dict(
                type='dict',
                disposition='/identifier',
                options=dict(
                    publisher=dict(
                        type='str',
                        disposition='publisher',
                        required=True
                    ),
                    offer=dict(
                        type='str',
                        disposition='offer',
                        required=True
                    ),
                    sku=dict(
                        type='str',
                        disposition='sku',
                        required=True
                    )
                )
            ),
            recommended=dict(
                type='dict',
                disposition='/recommended',
                options=dict(
                    v_cp_us=dict(
                        type='dict',
                        disposition='v_cp_us',
                        options=dict(
                            min=dict(
                                type='int',
                                disposition='min'
                            ),
                            max=dict(
                                type='int',
                                disposition='max'
                            )
                        )
                    ),
                    memory=dict(
                        type='dict',
                        disposition='memory',
                        options=dict(
                            min=dict(
                                type='int',
                                disposition='min'
                            ),
                            max=dict(
                                type='int',
                                disposition='max'
                            )
                        )
                    )
                )
            ),
            disallowed=dict(
                type='dict',
                disposition='/disallowed',
                options=dict(
                    disk_types=dict(
                        type='list',
                        disposition='disk_types',
                        elements='str'
                    )
                )
            ),
            purchase_plan=dict(
                type='dict',
                disposition='/purchase_plan',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    publisher=dict(
                        type='str',
                        disposition='publisher'
                    ),
                    product=dict(
                        type='str',
                        disposition='product'
                    )
                )
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.gallery_name = None
        self.gallery_image_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleryImage, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.gallery_images.create_or_update(resource_group=self.resource_group,
                                                                        gallery_name=self.gallery_name,
                                                                        gallery_image_name=self.gallery_image_name,
                                                                        gallery_image=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GalleryImage instance.')
            self.fail('Error creating the GalleryImage instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.gallery_images.delete(resource_group=self.resource_group,
                                                              gallery_name=self.gallery_name,
                                                              gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            self.log('Error attempting to delete the GalleryImage instance.')
            self.fail('Error deleting the GalleryImage instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.gallery_images.get(resource_group=self.resource_group,
                                                           gallery_name=self.gallery_name,
                                                           gallery_image_name=self.gallery_image_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleryImage()


if __name__ == '__main__':
    main()
