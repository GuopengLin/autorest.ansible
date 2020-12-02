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
    module: azure_rm_image
    version_added: '2.9'
    short_description: Manage Azure Image instance.
    description:
      - 'Create, update and delete instance of Azure Image.'
    options:
      resource_group:
        description:
          - The name of the resource group.
        required: true
        type: str
      image_name:
        description:
          - The name of the image.
        required: true
        type: str
      source_virtual_machine:
        description:
          - The source virtual machine from which Image is created.
        type: dict
        suboptions:
          id:
            description:
              - Resource Id
            type: str
      storage_profile:
        description:
          - Specifies the storage settings for the virtual machine disks.
        type: dict
        suboptions:
          os_disk:
            description:
              - >-
                Specifies information about the operating system disk used by the
                virtual machine. :code:`<br>`:code:`<br>` For more information about
                disks, see `About disks and VHDs for Azure virtual machines
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
            type: dict
            suboptions:
              os_type:
                description:
                  - >-
                    This property allows you to specify the type of the OS that is
                    included in the disk if creating a VM from a custom image.
                    :code:`<br>`:code:`<br>` Possible values are:
                    :code:`<br>`:code:`<br>` **Windows** :code:`<br>`:code:`<br>`
                    **Linux**
                required: true
                type: sealed-choice
              os_state:
                description:
                  - The OS State.
                required: true
                type: sealed-choice
          data_disks:
            description:
              - >-
                Specifies the parameters that are used to add a data disk to a
                virtual machine. :code:`<br>`:code:`<br>` For more information about
                disks, see `About disks and VHDs for Azure virtual machines
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
            type: list
            suboptions:
              lun:
                description:
                  - >-
                    Specifies the logical unit number of the data disk. This value
                    is used to identify data disks within the VM and therefore must
                    be unique for each data disk attached to a VM.
                required: true
                type: int
          zone_resilient:
            description:
              - >-
                Specifies whether an image is zone resilient or not. Default is
                false. Zone resilient images can be created only in regions that
                provide Zone Redundant Storage (ZRS).
            type: bool
      hyper_v_generation:
        description:
          - >-
            Gets the HyperVGenerationType of the VirtualMachine created from the
            image
        type: str
        choices:
          - V1
          - V2
      expand:
        description:
          - The expand expression to apply on the operation.
        type: str
      state:
        description:
          - Assert the state of the Image.
          - Use C(present) to create or update an Image and C(absent) to delete it.
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
    - name: Create a virtual machine image from a blob with DiskEncryptionSet resource.
      azure_rm_image: 
        image_name: myImage
        resource_group_name: myResourceGroup
        location: West US
        properties:
          storage_profile:
            os_disk:
              blob_uri: 'https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd'
              disk_encryption_set:
                id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSets/{existing-diskEncryptionSet-name}
              os_state: Generalized
              os_type: Linux
        

    - name: Create a virtual machine image from a blob.
      azure_rm_image: 
        image_name: myImage
        resource_group_name: myResourceGroup
        location: West US
        properties:
          storage_profile:
            os_disk:
              blob_uri: 'https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd'
              os_state: Generalized
              os_type: Linux
            zone_resilient: true
        

    - name: Create a virtual machine image from a managed disk with DiskEncryptionSet resource.
      azure_rm_image: 
        image_name: myImage
        resource_group_name: myResourceGroup
        location: West US
        properties:
          storage_profile:
            os_disk:
              disk_encryption_set:
                id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSets/{existing-diskEncryptionSet-name}
              managed_disk:
                id: >-
                  subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myManagedDisk
              os_state: Generalized
              os_type: Linux
        

    - name: Create a virtual machine image from a managed disk.
      azure_rm_image: 
        image_name: myImage
        resource_group_name: myResourceGroup
        location: West US
        properties:
          storage_profile:
            os_disk:
              managed_disk:
                id: >-
                  subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myManagedDisk
              os_state: Generalized
              os_type: Linux
            zone_resilient: true
        

    - name: Create a virtual machine image from a snapshot with DiskEncryptionSet resource.
      azure_rm_image: 
        image_name: myImage
        resource_group_name: myResourceGroup
        location: West US
        properties:
          storage_profile:
            os_disk:
              disk_encryption_set:
                id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSets/{existing-diskEncryptionSet-name}
              os_state: Generalized
              os_type: Linux
              snapshot:
                id: >-
                  subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot
        

    - name: Create a virtual machine image from a snapshot.
      azure_rm_image: 
        image_name: myImage
        resource_group_name: myResourceGroup
        location: West US
        properties:
          storage_profile:
            os_disk:
              os_state: Generalized
              os_type: Linux
              snapshot:
                id: >-
                  subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot
            zone_resilient: false
        

    - name: Create a virtual machine image from an existing virtual machine.
      azure_rm_image: 
        image_name: myImage
        resource_group_name: myResourceGroup
        location: West US
        properties:
          source_virtual_machine:
            id: >-
              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM
        

    - name: Create a virtual machine image that includes a data disk from a blob.
      azure_rm_image: 
        image_name: myImage
        resource_group_name: myResourceGroup
        location: West US
        properties:
          storage_profile:
            data_disks:
              - blob_uri: >-
                  https://mystorageaccount.blob.core.windows.net/dataimages/dataimage.vhd
                lun: 1
            os_disk:
              blob_uri: 'https://mystorageaccount.blob.core.windows.net/osimages/osimage.vhd'
              os_state: Generalized
              os_type: Linux
            zone_resilient: false
        

    - name: Create a virtual machine image that includes a data disk from a managed disk.
      azure_rm_image: 
        image_name: myImage
        resource_group_name: myResourceGroup
        location: West US
        properties:
          storage_profile:
            data_disks:
              - lun: 1
                managed_disk:
                  id: >-
                    subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myManagedDisk2
            os_disk:
              managed_disk:
                id: >-
                  subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/myManagedDisk
              os_state: Generalized
              os_type: Linux
            zone_resilient: false
        

    - name: Create a virtual machine image that includes a data disk from a snapshot.
      azure_rm_image: 
        image_name: myImage
        resource_group_name: myResourceGroup
        location: West US
        properties:
          storage_profile:
            data_disks:
              - lun: 1
                snapshot:
                  id: >-
                    subscriptions/{subscriptionId}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot2
            os_disk:
              os_state: Generalized
              os_type: Linux
              snapshot:
                id: >-
                  subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/snapshots/mySnapshot
            zone_resilient: true
        

    - name: Updates tags of an Image.
      azure_rm_image: 
        image_name: myImage
        resource_group_name: myResourceGroup
        properties:
          hyper_vgeneration: V1
          source_virtual_machine:
            id: >-
              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVM
        tags:
          department: HR
        

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
              virtual machine. :code:`<br>`:code:`<br>` For more information about
              disks, see `About disks and VHDs for Azure virtual machines
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
              Specifies the parameters that are used to add a data disk to a virtual
              machine. :code:`<br>`:code:`<br>` For more information about disks,
              see `About disks and VHDs for Azure virtual machines
              <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
          returned: always
          type: list
          sample: null
          contains:
            lun:
              description:
                - >-
                  Specifies the logical unit number of the data disk. This value is
                  used to identify data disks within the VM and therefore must be
                  unique for each data disk attached to a VM.
              returned: always
              type: int
              sample: null
        zone_resilient:
          description:
            - >-
              Specifies whether an image is zone resilient or not. Default is false.
              Zone resilient images can be created only in regions that provide Zone
              Redundant Storage (ZRS).
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
        - Gets the HyperVGenerationType of the VirtualMachine created from the image
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


class AzureRMImage(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            image_name=dict(
                type='str',
                required=True
            ),
            source_virtual_machine=dict(
                type='dict',
                disposition='/source_virtual_machine',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            storage_profile=dict(
                type='dict',
                disposition='/storage_profile',
                options=dict(
                    os_disk=dict(
                        type='dict',
                        disposition='os_disk',
                        options=dict(
                            os_type=dict(
                                type='sealed-choice',
                                disposition='os_type',
                                required=True
                            ),
                            os_state=dict(
                                type='sealed-choice',
                                disposition='os_state',
                                required=True
                            )
                        )
                    ),
                    data_disks=dict(
                        type='list',
                        disposition='data_disks',
                        elements='dict',
                        options=dict(
                            lun=dict(
                                type='int',
                                disposition='lun',
                                required=True
                            )
                        )
                    ),
                    zone_resilient=dict(
                        type='bool',
                        disposition='zone_resilient'
                    )
                )
            ),
            hyper_v_generation=dict(
                type='str',
                disposition='/hyper_v_generation',
                choices=['V1',
                         'V2']
            ),
            expand=dict(
                type='str'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.image_name = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMImage, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2020-06-01')

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
            response = self.mgmt_client.images.create_or_update(resource_group=self.resource_group,
                                                                image_name=self.image_name,
                                                                parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the Image instance.')
            self.fail('Error creating the Image instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.images.delete(resource_group=self.resource_group,
                                                      image_name=self.image_name)
        except CloudError as e:
            self.log('Error attempting to delete the Image instance.')
            self.fail('Error deleting the Image instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.images.get(resource_group=self.resource_group,
                                                   image_name=self.image_name,
                                                   expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMImage()


if __name__ == '__main__':
    main()
