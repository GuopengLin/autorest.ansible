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
    module: azure_rm_image_info
    version_added: '2.9'
    short_description: Get Image info.
    description:
      - Get info of Image.
    options:
      resource_group:
        description:
          - The name of the resource group.
        type: str
      image_name:
        description:
          - The name of the image.
        type: str
      expand:
        description:
          - The expand expression to apply on the operation.
        type: str
    extends_documentation_fragment:
      - azure.azcollection.azure
      - azure.azcollection.azure_tags
    author:
      - GuopengLin (@t-glin)
    
'''

EXAMPLES = '''
    - name: Get information about a virtual machine image.
      azure_rm_image_info: 
        image_name: myImage
        resource_group_name: myResourceGroup
        

    - name: List all virtual machine images in a resource group.
      azure_rm_image_info: 
        resource_group_name: myResourceGroup
        

    - name: List all virtual machine images in a subscription.
      azure_rm_image_info: 

'''

RETURN = '''
    images:
      description: >-
        A list of dict results where the key is the name of the Image and the values
        are the facts for that Image.
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
        source_virtual_machine:
          description:
            - The source virtual machine from which Image is created.
          returned: always
          type: dict
          sample: null
          contains:
            id:
              description:
                - Resource Id
              returned: always
              type: str
              sample: null
        storage_profile:
          description:
            - Specifies the storage settings for the virtual machine disks.
          returned: always
          type: dict
          sample: null
          contains:
            os_disk:
              description:
                - >-
                  Specifies information about the operating system disk used by the
                  virtual machine. :code:`<br>`:code:`<br>` For more information
                  about disks, see `About disks and VHDs for Azure virtual machines
                  <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
              returned: always
              type: dict
              sample: null
              contains:
                os_type:
                  description:
                    - >-
                      This property allows you to specify the type of the OS that is
                      included in the disk if creating a VM from a custom image.
                      :code:`<br>`:code:`<br>` Possible values are:
                      :code:`<br>`:code:`<br>` **Windows** :code:`<br>`:code:`<br>`
                      **Linux**
                  returned: always
                  type: sealed-choice
                  sample: null
                os_state:
                  description:
                    - The OS State.
                  returned: always
                  type: sealed-choice
                  sample: null
            data_disks:
              description:
                - >-
                  Specifies the parameters that are used to add a data disk to a
                  virtual machine. :code:`<br>`:code:`<br>` For more information
                  about disks, see `About disks and VHDs for Azure virtual machines
                  <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
              returned: always
              type: list
              sample: null
              contains:
                lun:
                  description:
                    - >-
                      Specifies the logical unit number of the data disk. This value
                      is used to identify data disks within the VM and therefore
                      must be unique for each data disk attached to a VM.
                  returned: always
                  type: int
                  sample: null
            zone_resilient:
              description:
                - >-
                  Specifies whether an image is zone resilient or not. Default is
                  false. Zone resilient images can be created only in regions that
                  provide Zone Redundant Storage (ZRS).
              returned: always
              type: bool
              sample: null
        provisioning_state:
          description:
            - The provisioning state.
          returned: always
          type: str
          sample: null
        hyper_v_generation:
          description:
            - >-
              Gets the HyperVGenerationType of the VirtualMachine created from the
              image
          returned: always
          type: str
          sample: null
        value:
          description:
            - The list of Images.
          returned: always
          type: list
          sample: null
          contains:
            source_virtual_machine:
              description:
                - The source virtual machine from which Image is created.
              returned: always
              type: dict
              sample: null
              contains:
                id:
                  description:
                    - Resource Id
                  returned: always
                  type: str
                  sample: null
            storage_profile:
              description:
                - Specifies the storage settings for the virtual machine disks.
              returned: always
              type: dict
              sample: null
              contains:
                os_disk:
                  description:
                    - >-
                      Specifies information about the operating system disk used by
                      the virtual machine. :code:`<br>`:code:`<br>` For more
                      information about disks, see `About disks and VHDs for Azure
                      virtual machines
                      <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                  returned: always
                  type: dict
                  sample: null
                  contains:
                    os_type:
                      description:
                        - >-
                          This property allows you to specify the type of the OS
                          that is included in the disk if creating a VM from a
                          custom image. :code:`<br>`:code:`<br>` Possible values
                          are: :code:`<br>`:code:`<br>` **Windows**
                          :code:`<br>`:code:`<br>` **Linux**
                      returned: always
                      type: sealed-choice
                      sample: null
                    os_state:
                      description:
                        - The OS State.
                      returned: always
                      type: sealed-choice
                      sample: null
                data_disks:
                  description:
                    - >-
                      Specifies the parameters that are used to add a data disk to a
                      virtual machine. :code:`<br>`:code:`<br>` For more information
                      about disks, see `About disks and VHDs for Azure virtual
                      machines
                      <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    lun:
                      description:
                        - >-
                          Specifies the logical unit number of the data disk. This
                          value is used to identify data disks within the VM and
                          therefore must be unique for each data disk attached to a
                          VM.
                      returned: always
                      type: int
                      sample: null
                zone_resilient:
                  description:
                    - >-
                      Specifies whether an image is zone resilient or not. Default
                      is false. Zone resilient images can be created only in regions
                      that provide Zone Redundant Storage (ZRS).
                  returned: always
                  type: bool
                  sample: null
            hyper_v_generation:
              description:
                - >-
                  Gets the HyperVGenerationType of the VirtualMachine created from
                  the image
              returned: always
              type: str
              sample: null
        next_link:
          description:
            - >-
              The uri to fetch the next page of Images. Call ListNext() with this to
              fetch the next page of Images.
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


class AzureRMImageInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            image_name=dict(
                type='str'
            ),
            expand=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.image_name = None
        self.expand = None

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
        super(AzureRMImageInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.image_name is not None):
            self.results['images'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['images'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['images'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.images.get(resource_group=self.resource_group,
                                                   image_name=self.image_name,
                                                   expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.images.list_by_resource_group(resource_group=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.images.list()
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
    AzureRMImageInfo()


if __name__ == '__main__':
    main()
