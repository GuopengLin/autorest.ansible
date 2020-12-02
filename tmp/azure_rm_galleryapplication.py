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
    module: azure_rm_galleryapplication
    version_added: '2.9'
    short_description: Manage Azure GalleryApplication instance.
    description:
      - 'Create, update and delete instance of Azure GalleryApplication.'
    options:
      resource_group:
        description:
          - The name of the resource group.
        required: true
        type: str
      gallery_name:
        description:
          - >-
            The name of the Shared Application Gallery in which the Application
            Definition is to be created.
          - >-
            The name of the Shared Application Gallery in which the Application
            Definition is to be updated.
          - >-
            The name of the Shared Application Gallery from which the Application
            Definitions are to be retrieved.
          - >-
            The name of the Shared Application Gallery in which the Application
            Definition is to be deleted.
        required: true
        type: str
      gallery_application_name:
        description:
          - >-
            The name of the gallery Application Definition to be created or updated.
            The allowed characters are alphabets and numbers with dots, dashes, and
            periods allowed in the middle. The maximum length is 80 characters.
          - >-
            The name of the gallery Application Definition to be updated. The
            allowed characters are alphabets and numbers with dots, dashes, and
            periods allowed in the middle. The maximum length is 80 characters.
          - The name of the gallery Application Definition to be retrieved.
          - The name of the gallery Application Definition to be deleted.
        required: true
        type: str
      description:
        description:
          - >-
            The description of this gallery Application Definition resource. This
            property is updatable.
        type: str
      eula:
        description:
          - The Eula agreement for the gallery Application Definition.
        type: str
      privacy_statement_uri:
        description:
          - The privacy statement uri.
        type: str
      release_note_uri:
        description:
          - The release note uri.
        type: str
      end_of_life_date:
        description:
          - >-
            The end of life date of the gallery Application Definition. This
            property can be used for decommissioning purposes. This property is
            updatable.
        type: str
      supported_os_type:
        description:
          - >-
            This property allows you to specify the supported type of the OS that
            application is built for. :code:`<br>`:code:`<br>` Possible values are:
            :code:`<br>`:code:`<br>` **Windows** :code:`<br>`:code:`<br>` **Linux**
        type: sealed-choice
      state:
        description:
          - Assert the state of the GalleryApplication.
          - >-
            Use C(present) to create or update an GalleryApplication and C(absent)
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
    - name: Create or update a simple gallery Application.
      azure_rm_galleryapplication: 
        gallery_application_name: myGalleryApplicationName
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Update a simple gallery Application.
      azure_rm_galleryapplication: 
        gallery_application_name: myGalleryApplicationName
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Delete a gallery Application.
      azure_rm_galleryapplication: 
        gallery_application_name: myGalleryApplicationName
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
          The end of life date of the gallery Application Definition. This property
          can be used for decommissioning purposes. This property is updatable.
      returned: always
      type: str
      sample: null
    supported_os_type:
      description:
        - >-
          This property allows you to specify the supported type of the OS that
          application is built for. :code:`<br>`:code:`<br>` Possible values are:
          :code:`<br>`:code:`<br>` **Windows** :code:`<br>`:code:`<br>` **Linux**
      returned: always
      type: sealed-choice
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


class AzureRMGalleryApplication(AzureRMModuleBaseExt):
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
            end_of_life_date=dict(
                type='str',
                disposition='/end_of_life_date'
            ),
            supported_os_type=dict(
                type='sealed-choice',
                disposition='/supported_os_type'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.gallery_name = None
        self.gallery_application_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMGalleryApplication, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.gallery_applications.create_or_update(resource_group=self.resource_group,
                                                                              gallery_name=self.gallery_name,
                                                                              gallery_application_name=self.gallery_application_name,
                                                                              gallery_application=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the GalleryApplication instance.')
            self.fail('Error creating the GalleryApplication instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.gallery_applications.delete(resource_group=self.resource_group,
                                                                    gallery_name=self.gallery_name,
                                                                    gallery_application_name=self.gallery_application_name)
        except CloudError as e:
            self.log('Error attempting to delete the GalleryApplication instance.')
            self.fail('Error deleting the GalleryApplication instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.gallery_applications.get(resource_group=self.resource_group,
                                                                 gallery_name=self.gallery_name,
                                                                 gallery_application_name=self.gallery_application_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMGalleryApplication()


if __name__ == '__main__':
    main()
