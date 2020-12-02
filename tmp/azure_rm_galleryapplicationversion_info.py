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
    module: azure_rm_galleryapplicationversion_info
    version_added: '2.9'
    short_description: Get GalleryApplicationVersion info.
    description:
      - Get info of GalleryApplicationVersion.
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
            Definition resides.
        required: true
        type: str
      gallery_application_name:
        description:
          - >-
            The name of the gallery Application Definition in which the Application
            Version resides.
          - >-
            The name of the Shared Application Gallery Application Definition from
            which the Application Versions are to be listed.
        required: true
        type: str
      gallery_application_version_name:
        description:
          - The name of the gallery Application Version to be retrieved.
        type: str
      expand:
        description:
          - The expand expression to apply on the operation.
        type: str
        choices:
          - ReplicationStatus
    extends_documentation_fragment:
      - azure.azcollection.azure
      - azure.azcollection.azure_tags
    author:
      - GuopengLin (@t-glin)
    
'''

EXAMPLES = '''
    - name: Get a gallery Application Version with replication status.
      azure_rm_galleryapplicationversion_info: 
        gallery_application_name: myGalleryApplicationName
        gallery_application_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Get a gallery Application Version.
      azure_rm_galleryapplicationversion_info: 
        gallery_application_name: myGalleryApplicationName
        gallery_application_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: List gallery Application Versions in a gallery Application Definition.
      azure_rm_galleryapplicationversion_info: 
        gallery_application_name: myGalleryApplicationName
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
    gallery_application_versions:
      description: >-
        A list of dict results where the key is the name of the
        GalleryApplicationVersion and the values are the facts for that
        GalleryApplicationVersion.
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
        publishing_profile:
          description:
            - The publishing profile of a gallery Image Version.
          returned: always
          type: dict
          sample: null
          contains:
            source:
              description:
                - >-
                  The source image from which the Image Version is going to be
                  created.
              returned: always
              type: dict
              sample: null
              contains:
                file_name:
                  description:
                    - Required. The fileName of the artifact.
                  returned: always
                  type: str
                  sample: null
                media_link:
                  description:
                    - >-
                      Required. The mediaLink of the artifact, must be a readable
                      storage blob.
                  returned: always
                  type: str
                  sample: null
            content_type:
              description:
                - >-
                  Optional. May be used to help process this file. The type of file
                  contained in the source, e.g. zip, json, etc.
              returned: always
              type: str
              sample: null
            enable_health_check:
              description:
                - Optional. Whether or not this application reports health.
              returned: always
              type: bool
              sample: null
        provisioning_state:
          description:
            - 'The provisioning state, which only appears in the response.'
          returned: always
          type: str
          sample: null
        replication_status:
          description:
            - This is the replication status of the gallery Image Version.
          returned: always
          type: dict
          sample: null
        value:
          description:
            - A list of gallery Application Versions.
          returned: always
          type: list
          sample: null
          contains:
            publishing_profile:
              description:
                - The publishing profile of a gallery Image Version.
              returned: always
              type: dict
              sample: null
              contains:
                source:
                  description:
                    - >-
                      The source image from which the Image Version is going to be
                      created.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    file_name:
                      description:
                        - Required. The fileName of the artifact.
                      returned: always
                      type: str
                      sample: null
                    media_link:
                      description:
                        - >-
                          Required. The mediaLink of the artifact, must be a
                          readable storage blob.
                      returned: always
                      type: str
                      sample: null
                content_type:
                  description:
                    - >-
                      Optional. May be used to help process this file. The type of
                      file contained in the source, e.g. zip, json, etc.
                  returned: always
                  type: str
                  sample: null
                enable_health_check:
                  description:
                    - Optional. Whether or not this application reports health.
                  returned: always
                  type: bool
                  sample: null
        next_link:
          description:
            - >-
              The uri to fetch the next page of gallery Application Versions. Call
              ListNext() with this to fetch the next page of gallery Application
              Versions.
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


class AzureRMGalleryApplicationVersionInfo(AzureRMModuleBase):
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
            gallery_application_version_name=dict(
                type='str'
            ),
            expand=dict(
                type='str',
                choices=['ReplicationStatus']
            )
        )

        self.resource_group = None
        self.gallery_name = None
        self.gallery_application_name = None
        self.gallery_application_version_name = None
        self.expand = None

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
        super(AzureRMGalleryApplicationVersionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01')

        if (self.resource_group is not None and
            self.gallery_name is not None and
            self.gallery_application_name is not None and
            self.gallery_application_version_name is not None):
            self.results['gallery_application_versions'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.gallery_name is not None and
              self.gallery_application_name is not None):
            self.results['gallery_application_versions'] = self.format_item(self.list_by_gallery_application())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gallery_application_versions.get(resource_group=self.resource_group,
                                                                         gallery_name=self.gallery_name,
                                                                         gallery_application_name=self.gallery_application_name,
                                                                         gallery_application_version_name=self.gallery_application_version_name,
                                                                         expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_gallery_application(self):
        response = None

        try:
            response = self.mgmt_client.gallery_application_versions.list_by_gallery_application(resource_group=self.resource_group,
                                                                                                 gallery_name=self.gallery_name,
                                                                                                 gallery_application_name=self.gallery_application_name)
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
    AzureRMGalleryApplicationVersionInfo()


if __name__ == '__main__':
    main()
