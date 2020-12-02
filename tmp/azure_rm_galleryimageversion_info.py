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
    module: azure_rm_galleryimageversion_info
    version_added: '2.9'
    short_description: Get GalleryImageVersion info.
    description:
      - Get info of GalleryImageVersion.
    options:
      resource_group:
        description:
          - The name of the resource group.
        required: true
        type: str
      gallery_name:
        description:
          - >-
            The name of the Shared Image Gallery in which the Image Definition
            resides.
        required: true
        type: str
      gallery_image_name:
        description:
          - >-
            The name of the gallery Image Definition in which the Image Version
            resides.
          - >-
            The name of the Shared Image Gallery Image Definition from which the
            Image Versions are to be listed.
        required: true
        type: str
      gallery_image_version_name:
        description:
          - The name of the gallery Image Version to be retrieved.
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
    - name: Get a gallery Image Version with replication status.
      azure_rm_galleryimageversion_info: 
        gallery_image_name: myGalleryImageName
        gallery_image_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Get a gallery Image Version with snapshots as a source.
      azure_rm_galleryimageversion_info: 
        gallery_image_name: myGalleryImageName
        gallery_image_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: Get a gallery Image Version.
      azure_rm_galleryimageversion_info: 
        gallery_image_name: myGalleryImageName
        gallery_image_version_name: 1.0.0
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

    - name: List gallery Image Versions in a gallery Image Definition.
      azure_rm_galleryimageversion_info: 
        gallery_image_name: myGalleryImageName
        gallery_name: myGalleryName
        resource_group_name: myResourceGroup
        

'''

RETURN = '''
    gallery_image_versions:
      description: >-
        A list of dict results where the key is the name of the GalleryImageVersion
        and the values are the facts for that GalleryImageVersion.
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
            - Describes the basic gallery artifact publishing profile.
          returned: always
          type: dict
          sample: null
          contains:
            target_regions:
              description:
                - >-
                  The target regions where the Image Version is going to be
                  replicated to. This property is updatable.
              returned: always
              type: list
              sample: null
              contains:
                name:
                  description:
                    - The name of the region.
                  returned: always
                  type: str
                  sample: null
                regional_replica_count:
                  description:
                    - >-
                      The number of replicas of the Image Version to be created per
                      region. This property is updatable.
                  returned: always
                  type: int
                  sample: null
                storage_account_type:
                  description:
                    - >-
                      Specifies the storage account type to be used to store the
                      image. This property is not updatable.
                  returned: always
                  type: str
                  sample: null
                encryption:
                  description:
                    - >-
                      Optional. Allows users to provide customer managed keys for
                      encrypting the OS and data disks in the gallery artifact.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    os_disk_image:
                      description:
                        - This is the disk image encryption base class.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        disk_encryption_set_id:
                          description:
                            - >-
                              A relative URI containing the resource ID of the disk
                              encryption set.
                          returned: always
                          type: str
                          sample: null
                    data_disk_images:
                      description:
                        - A list of encryption specifications for data disk images.
                      returned: always
                      type: list
                      sample: null
                      contains:
                        lun:
                          description:
                            - >-
                              This property specifies the logical unit number of the
                              data disk. This value is used to identify data disks
                              within the Virtual Machine and therefore must be
                              unique for each data disk attached to the Virtual
                              Machine.
                          returned: always
                          type: int
                          sample: null
            replica_count:
              description:
                - >-
                  The number of replicas of the Image Version to be created per
                  region. This property would take effect for a region when
                  regionalReplicaCount is not specified. This property is updatable.
              returned: always
              type: int
              sample: null
            exclude_from_latest:
              description:
                - >-
                  If set to true, Virtual Machines deployed from the latest version
                  of the Image Definition won't use this Image Version.
              returned: always
              type: bool
              sample: null
            end_of_life_date:
              description:
                - >-
                  The end of life date of the gallery Image Version. This property
                  can be used for decommissioning purposes. This property is
                  updatable.
              returned: always
              type: str
              sample: null
            storage_account_type:
              description:
                - >-
                  Specifies the storage account type to be used to store the image.
                  This property is not updatable.
              returned: always
              type: str
              sample: null
        provisioning_state:
          description:
            - 'The provisioning state, which only appears in the response.'
          returned: always
          type: str
          sample: null
        storage_profile:
          description:
            - This is the storage profile of a Gallery Image Version.
          returned: always
          type: dict
          sample: null
          contains:
            source:
              description:
                - The gallery artifact version source.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - >-
                      The id of the gallery artifact version source. Can specify a
                      disk uri, snapshot uri, or user image.
                  returned: always
                  type: str
                  sample: null
            os_disk_image:
              description:
                - This is the disk image base class.
              returned: always
              type: dict
              sample: null
              contains:
                host_caching:
                  description:
                    - >-
                      The host caching of the disk. Valid values are 'None',
                      'ReadOnly', and 'ReadWrite'
                  returned: always
                  type: sealed-choice
                  sample: null
                source:
                  description:
                    - The gallery artifact version source.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    id:
                      description:
                        - >-
                          The id of the gallery artifact version source. Can specify
                          a disk uri, snapshot uri, or user image.
                      returned: always
                      type: str
                      sample: null
            data_disk_images:
              description:
                - A list of data disk images.
              returned: always
              type: list
              sample: null
              contains:
                lun:
                  description:
                    - >-
                      This property specifies the logical unit number of the data
                      disk. This value is used to identify data disks within the
                      Virtual Machine and therefore must be unique for each data
                      disk attached to the Virtual Machine.
                  returned: always
                  type: int
                  sample: null
        replication_status:
          description:
            - This is the replication status of the gallery Image Version.
          returned: always
          type: dict
          sample: null
        value:
          description:
            - A list of gallery Image Versions.
          returned: always
          type: list
          sample: null
          contains:
            publishing_profile:
              description:
                - Describes the basic gallery artifact publishing profile.
              returned: always
              type: dict
              sample: null
              contains:
                target_regions:
                  description:
                    - >-
                      The target regions where the Image Version is going to be
                      replicated to. This property is updatable.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    name:
                      description:
                        - The name of the region.
                      returned: always
                      type: str
                      sample: null
                    regional_replica_count:
                      description:
                        - >-
                          The number of replicas of the Image Version to be created
                          per region. This property is updatable.
                      returned: always
                      type: int
                      sample: null
                    storage_account_type:
                      description:
                        - >-
                          Specifies the storage account type to be used to store the
                          image. This property is not updatable.
                      returned: always
                      type: str
                      sample: null
                    encryption:
                      description:
                        - >-
                          Optional. Allows users to provide customer managed keys
                          for encrypting the OS and data disks in the gallery
                          artifact.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        os_disk_image:
                          description:
                            - This is the disk image encryption base class.
                          returned: always
                          type: dict
                          sample: null
                          contains:
                            disk_encryption_set_id:
                              description:
                                - >-
                                  A relative URI containing the resource ID of the
                                  disk encryption set.
                              returned: always
                              type: str
                              sample: null
                        data_disk_images:
                          description:
                            - >-
                              A list of encryption specifications for data disk
                              images.
                          returned: always
                          type: list
                          sample: null
                          contains:
                            lun:
                              description:
                                - >-
                                  This property specifies the logical unit number of
                                  the data disk. This value is used to identify data
                                  disks within the Virtual Machine and therefore
                                  must be unique for each data disk attached to the
                                  Virtual Machine.
                              returned: always
                              type: int
                              sample: null
                replica_count:
                  description:
                    - >-
                      The number of replicas of the Image Version to be created per
                      region. This property would take effect for a region when
                      regionalReplicaCount is not specified. This property is
                      updatable.
                  returned: always
                  type: int
                  sample: null
                exclude_from_latest:
                  description:
                    - >-
                      If set to true, Virtual Machines deployed from the latest
                      version of the Image Definition won't use this Image Version.
                  returned: always
                  type: bool
                  sample: null
                end_of_life_date:
                  description:
                    - >-
                      The end of life date of the gallery Image Version. This
                      property can be used for decommissioning purposes. This
                      property is updatable.
                  returned: always
                  type: str
                  sample: null
                storage_account_type:
                  description:
                    - >-
                      Specifies the storage account type to be used to store the
                      image. This property is not updatable.
                  returned: always
                  type: str
                  sample: null
            storage_profile:
              description:
                - This is the storage profile of a Gallery Image Version.
              returned: always
              type: dict
              sample: null
              contains:
                source:
                  description:
                    - The gallery artifact version source.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    id:
                      description:
                        - >-
                          The id of the gallery artifact version source. Can specify
                          a disk uri, snapshot uri, or user image.
                      returned: always
                      type: str
                      sample: null
                os_disk_image:
                  description:
                    - This is the disk image base class.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    host_caching:
                      description:
                        - >-
                          The host caching of the disk. Valid values are 'None',
                          'ReadOnly', and 'ReadWrite'
                      returned: always
                      type: sealed-choice
                      sample: null
                    source:
                      description:
                        - The gallery artifact version source.
                      returned: always
                      type: dict
                      sample: null
                      contains:
                        id:
                          description:
                            - >-
                              The id of the gallery artifact version source. Can
                              specify a disk uri, snapshot uri, or user image.
                          returned: always
                          type: str
                          sample: null
                data_disk_images:
                  description:
                    - A list of data disk images.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    lun:
                      description:
                        - >-
                          This property specifies the logical unit number of the
                          data disk. This value is used to identify data disks
                          within the Virtual Machine and therefore must be unique
                          for each data disk attached to the Virtual Machine.
                      returned: always
                      type: int
                      sample: null
        next_link:
          description:
            - >-
              The uri to fetch the next page of gallery Image Versions. Call
              ListNext() with this to fetch the next page of gallery Image Versions.
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


class AzureRMGalleryImageVersionInfo(AzureRMModuleBase):
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
            gallery_image_version_name=dict(
                type='str'
            ),
            expand=dict(
                type='str',
                choices=['ReplicationStatus']
            )
        )

        self.resource_group = None
        self.gallery_name = None
        self.gallery_image_name = None
        self.gallery_image_version_name = None
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
        super(AzureRMGalleryImageVersionInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2019-12-01')

        if (self.resource_group is not None and
            self.gallery_name is not None and
            self.gallery_image_name is not None and
            self.gallery_image_version_name is not None):
            self.results['gallery_image_versions'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.gallery_name is not None and
              self.gallery_image_name is not None):
            self.results['gallery_image_versions'] = self.format_item(self.list_by_gallery_image())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.gallery_image_versions.get(resource_group=self.resource_group,
                                                                   gallery_name=self.gallery_name,
                                                                   gallery_image_name=self.gallery_image_name,
                                                                   gallery_image_version_name=self.gallery_image_version_name,
                                                                   expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_gallery_image(self):
        response = None

        try:
            response = self.mgmt_client.gallery_image_versions.list_by_gallery_image(resource_group=self.resource_group,
                                                                                     gallery_name=self.gallery_name,
                                                                                     gallery_image_name=self.gallery_image_name)
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
    AzureRMGalleryImageVersionInfo()


if __name__ == '__main__':
    main()
