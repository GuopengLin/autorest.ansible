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
module: azure_rm_virtualmachine
version_added: '2.9'
short_description: Manage Azure VirtualMachine instance.
description:
    - 'Create, update and delete instance of Azure VirtualMachine.'
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    vm_name:
        description:
            - The name of the virtual machine.
        required: true
        type: str
    plan:
        description:
            - >-
                Specifies information about the marketplace image used to create the
                virtual machine. This element is only used for marketplace images.
                Before you can use a marketplace image from an API, you must enable the
                image for programmatic use.  In the Azure portal, find the marketplace
                image that you want to use and then click **Want to deploy
                programmatically, Get Started ->**. Enter any required information and
                then click **Save**.
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
                    - >-
                        Specifies the product of the image from the marketplace. This is the
                        same value as Offer under the imageReference element.
                type: str
            promotion_code:
                description:
                    - The promotion code.
                type: str
    resources:
        description:
            - The virtual machine child extension resources.
        type: list
        suboptions:
            force_update_tag:
                description:
                    - >-
                        How the extension handler should be forced to update even if the
                        extension configuration has not changed.
                type: str
            publisher:
                description:
                    - The name of the extension handler publisher.
                type: str
            type_properties_type:
                description:
                    - >-
                        Specifies the type of the extension; an example is
                        "CustomScriptExtension".
                type: str
            type_handler_version:
                description:
                    - Specifies the version of the script handler.
                type: str
            auto_upgrade_minor_version:
                description:
                    - >-
                        Indicates whether the extension should use a newer minor version if
                        one is available at deployment time. Once deployed, however, the
                        extension will not upgrade minor versions unless redeployed, even
                        with this property set to true.
                type: bool
            enable_automatic_upgrade:
                description:
                    - >-
                        Indicates whether the extension should be automatically upgraded by
                        the platform if there is a newer version of the extension available.
                type: bool
            settings:
                description:
                    - Json formatted public settings for the extension.
                type: any
            protected_settings:
                description:
                    - >-
                        The extension can contain either protectedSettings or
                        protectedSettingsFromKeyVault or no protected settings at all.
                type: any
            instance_view:
                description:
                    - The virtual machine extension instance view.
                type: dict
                suboptions:
                    name:
                        description:
                            - The virtual machine extension name.
                        type: str
                    type:
                        description:
                            - >-
                                Specifies the type of the extension; an example is
                                "CustomScriptExtension".
                        type: str
                    type_handler_version:
                        description:
                            - Specifies the version of the script handler.
                        type: str
                    substatuses:
                        description:
                            - The resource status information.
                        type: list
                        suboptions:
                            code:
                                description:
                                    - The status code.
                                type: str
                            level:
                                description:
                                    - The level code.
                                type: sealed-choice
                            display_status:
                                description:
                                    - The short localizable label for the status.
                                type: str
                            message:
                                description:
                                    - >-
                                        The detailed status message, including for alerts and error
                                        messages.
                                type: str
                            time:
                                description:
                                    - The time of the status.
                                type: str
                    statuses:
                        description:
                            - The resource status information.
                        type: list
                        suboptions:
                            code:
                                description:
                                    - The status code.
                                type: str
                            level:
                                description:
                                    - The level code.
                                type: sealed-choice
                            display_status:
                                description:
                                    - The short localizable label for the status.
                                type: str
                            message:
                                description:
                                    - >-
                                        The detailed status message, including for alerts and error
                                        messages.
                                type: str
                            time:
                                description:
                                    - The time of the status.
                                type: str
    identity:
        description:
            - 'The identity of the virtual machine, if configured.'
        type: dict
        suboptions:
            type:
                description:
                    - >-
                        The type of identity used for the virtual machine. The type
                        'SystemAssigned, UserAssigned' includes both an implicitly created
                        identity and a set of user assigned identities. The type 'None' will
                        remove any identities from the virtual machine.
                type: sealed-choice
            user_assigned_identities:
                description:
                    - >-
                        The list of user identities associated with the Virtual Machine. The
                        user identity dictionary key references will be ARM resource ids in
                        the form:
                        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
                type: dict
    zones:
        description:
            - The virtual machine zones.
        type: list
    hardware_profile:
        description:
            - Specifies the hardware settings for the virtual machine.
        type: dict
        suboptions:
            vm_size:
                description:
                    - >-
                        Specifies the size of the virtual machine. For more information
                        about virtual machine sizes, see `Sizes for virtual machines
                        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-sizes?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                        :code:`<br>`:code:`<br>` The available VM sizes depend on region and
                        availability set. For a list of available sizes use these APIs: 
                        :code:`<br>`:code:`<br>` `List all available virtual machine sizes
                        in an availability set
                        <https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes>`_
                        :code:`<br>`:code:`<br>` `List all available virtual machine sizes
                        in a region
                        <https://docs.microsoft.com/rest/api/compute/virtualmachinesizes/list>`_
                        :code:`<br>`:code:`<br>` `List all available virtual machine sizes
                        for resizing
                        <https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes>`_
                type: str
                choices:
                    - Basic_A0
                    - Basic_A1
                    - Basic_A2
                    - Basic_A3
                    - Basic_A4
                    - Standard_A0
                    - Standard_A1
                    - Standard_A2
                    - Standard_A3
                    - Standard_A4
                    - Standard_A5
                    - Standard_A6
                    - Standard_A7
                    - Standard_A8
                    - Standard_A9
                    - Standard_A10
                    - Standard_A11
                    - Standard_A1_v2
                    - Standard_A2_v2
                    - Standard_A4_v2
                    - Standard_A8_v2
                    - Standard_A2m_v2
                    - Standard_A4m_v2
                    - Standard_A8m_v2
                    - Standard_B1s
                    - Standard_B1ms
                    - Standard_B2s
                    - Standard_B2ms
                    - Standard_B4ms
                    - Standard_B8ms
                    - Standard_D1
                    - Standard_D2
                    - Standard_D3
                    - Standard_D4
                    - Standard_D11
                    - Standard_D12
                    - Standard_D13
                    - Standard_D14
                    - Standard_D1_v2
                    - Standard_D2_v2
                    - Standard_D3_v2
                    - Standard_D4_v2
                    - Standard_D5_v2
                    - Standard_D2_v3
                    - Standard_D4_v3
                    - Standard_D8_v3
                    - Standard_D16_v3
                    - Standard_D32_v3
                    - Standard_D64_v3
                    - Standard_D2s_v3
                    - Standard_D4s_v3
                    - Standard_D8s_v3
                    - Standard_D16s_v3
                    - Standard_D32s_v3
                    - Standard_D64s_v3
                    - Standard_D11_v2
                    - Standard_D12_v2
                    - Standard_D13_v2
                    - Standard_D14_v2
                    - Standard_D15_v2
                    - Standard_DS1
                    - Standard_DS2
                    - Standard_DS3
                    - Standard_DS4
                    - Standard_DS11
                    - Standard_DS12
                    - Standard_DS13
                    - Standard_DS14
                    - Standard_DS1_v2
                    - Standard_DS2_v2
                    - Standard_DS3_v2
                    - Standard_DS4_v2
                    - Standard_DS5_v2
                    - Standard_DS11_v2
                    - Standard_DS12_v2
                    - Standard_DS13_v2
                    - Standard_DS14_v2
                    - Standard_DS15_v2
                    - Standard_DS13-4_v2
                    - Standard_DS13-2_v2
                    - Standard_DS14-8_v2
                    - Standard_DS14-4_v2
                    - Standard_E2_v3
                    - Standard_E4_v3
                    - Standard_E8_v3
                    - Standard_E16_v3
                    - Standard_E32_v3
                    - Standard_E64_v3
                    - Standard_E2s_v3
                    - Standard_E4s_v3
                    - Standard_E8s_v3
                    - Standard_E16s_v3
                    - Standard_E32s_v3
                    - Standard_E64s_v3
                    - Standard_E32-16_v3
                    - Standard_E32-8s_v3
                    - Standard_E64-32s_v3
                    - Standard_E64-16s_v3
                    - Standard_F1
                    - Standard_F2
                    - Standard_F4
                    - Standard_F8
                    - Standard_F16
                    - Standard_F1s
                    - Standard_F2s
                    - Standard_F4s
                    - Standard_F8s
                    - Standard_F16s
                    - Standard_F2s_v2
                    - Standard_F4s_v2
                    - Standard_F8s_v2
                    - Standard_F16s_v2
                    - Standard_F32s_v2
                    - Standard_F64s_v2
                    - Standard_F72s_v2
                    - Standard_G1
                    - Standard_G2
                    - Standard_G3
                    - Standard_G4
                    - Standard_G5
                    - Standard_GS1
                    - Standard_GS2
                    - Standard_GS3
                    - Standard_GS4
                    - Standard_GS5
                    - Standard_GS4-8
                    - Standard_GS4-4
                    - Standard_GS5-16
                    - Standard_GS5-8
                    - Standard_H8
                    - Standard_H16
                    - Standard_H8m
                    - Standard_H16m
                    - Standard_H16r
                    - Standard_H16mr
                    - Standard_L4s
                    - Standard_L8s
                    - Standard_L16s
                    - Standard_L32s
                    - Standard_M64s
                    - Standard_M64ms
                    - Standard_M128s
                    - Standard_M128ms
                    - Standard_M64-32ms
                    - Standard_M64-16ms
                    - Standard_M128-64ms
                    - Standard_M128-32ms
                    - Standard_NC6
                    - Standard_NC12
                    - Standard_NC24
                    - Standard_NC24r
                    - Standard_NC6s_v2
                    - Standard_NC12s_v2
                    - Standard_NC24s_v2
                    - Standard_NC24rs_v2
                    - Standard_NC6s_v3
                    - Standard_NC12s_v3
                    - Standard_NC24s_v3
                    - Standard_NC24rs_v3
                    - Standard_ND6s
                    - Standard_ND12s
                    - Standard_ND24s
                    - Standard_ND24rs
                    - Standard_NV6
                    - Standard_NV12
                    - Standard_NV24
    storage_profile:
        description:
            - Specifies the storage settings for the virtual machine disks.
        type: dict
        suboptions:
            image_reference:
                description:
                    - >-
                        Specifies information about the image to use. You can specify
                        information about platform images, marketplace images, or virtual
                        machine images. This element is required when you want to use a
                        platform image, marketplace image, or virtual machine image, but is
                        not used in other creation operations.
                type: dict
                suboptions:
                    publisher:
                        description:
                            - The image publisher.
                        type: str
                    offer:
                        description:
                            - >-
                                Specifies the offer of the platform image or marketplace image
                                used to create the virtual machine.
                        type: str
                    sku:
                        description:
                            - The image SKU.
                        type: str
                    version:
                        description:
                            - >-
                                Specifies the version of the platform image or marketplace image
                                used to create the virtual machine. The allowed formats are
                                Major.Minor.Build or 'latest'. Major, Minor, and Build are
                                decimal numbers. Specify 'latest' to use the latest version of
                                an image available at deploy time. Even if you use 'latest', the
                                VM image will not automatically update after deploy time even if
                                a new version becomes available.
                        type: str
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
                                included in the disk if creating a VM from user-image or a
                                specialized VHD. :code:`<br>`:code:`<br>` Possible values are:
                                :code:`<br>`:code:`<br>` **Windows** :code:`<br>`:code:`<br>`
                                **Linux**
                        type: sealed-choice
                    encryption_settings:
                        description:
                            - >-
                                Specifies the encryption settings for the OS Disk.
                                :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
                        type: dict
                        suboptions:
                            disk_encryption_key:
                                description:
                                    - >-
                                        Specifies the location of the disk encryption key, which is
                                        a Key Vault Secret.
                                type: dict
                                suboptions:
                                    secret_url:
                                        description:
                                            - The URL referencing a secret in a Key Vault.
                                        required: true
                                        type: str
                                    source_vault:
                                        description:
                                            - The relative URL of the Key Vault containing the secret.
                                        required: true
                                        type: dict
                                        suboptions:
                                            id:
                                                description:
                                                    - Resource Id
                                                type: str
                            key_encryption_key:
                                description:
                                    - >-
                                        Specifies the location of the key encryption key in Key
                                        Vault.
                                type: dict
                                suboptions:
                                    key_url:
                                        description:
                                            - The URL referencing a key encryption key in Key Vault.
                                        required: true
                                        type: str
                                    source_vault:
                                        description:
                                            - The relative URL of the Key Vault containing the key.
                                        required: true
                                        type: dict
                                        suboptions:
                                            id:
                                                description:
                                                    - Resource Id
                                                type: str
                            enabled:
                                description:
                                    - >-
                                        Specifies whether disk encryption should be enabled on the
                                        virtual machine.
                                type: bool
                    name:
                        description:
                            - The disk name.
                        type: str
                    vhd:
                        description:
                            - The virtual hard disk.
                        type: dict
                        suboptions:
                            uri:
                                description:
                                    - Specifies the virtual hard disk's uri.
                                type: str
                    image:
                        description:
                            - >-
                                The source user image virtual hard disk. The virtual hard disk
                                will be copied before being attached to the virtual machine. If
                                SourceImage is provided, the destination virtual hard drive must
                                not exist.
                        type: dict
                        suboptions:
                            uri:
                                description:
                                    - Specifies the virtual hard disk's uri.
                                type: str
                    caching:
                        description:
                            - >-
                                Specifies the caching requirements. :code:`<br>`:code:`<br>`
                                Possible values are: :code:`<br>`:code:`<br>` **None**
                                :code:`<br>`:code:`<br>` **ReadOnly** :code:`<br>`:code:`<br>`
                                **ReadWrite** :code:`<br>`:code:`<br>` Default: **None** for
                                Standard storage. **ReadOnly** for Premium storage.
                        type: sealed-choice
                    write_accelerator_enabled:
                        description:
                            - >-
                                Specifies whether writeAccelerator should be enabled or disabled
                                on the disk.
                        type: bool
                    diff_disk_settings:
                        description:
                            - >-
                                Specifies the ephemeral Disk Settings for the operating system
                                disk used by the virtual machine.
                        type: dict
                        suboptions:
                            option:
                                description:
                                    - >-
                                        Specifies the ephemeral disk settings for operating system
                                        disk.
                                type: str
                                choices:
                                    - Local
                            placement:
                                description:
                                    - >-
                                        Specifies the ephemeral disk placement for operating system
                                        disk.:code:`<br>`:code:`<br>` Possible values are:
                                        :code:`<br>`:code:`<br>` **CacheDisk**
                                        :code:`<br>`:code:`<br>` **ResourceDisk**
                                        :code:`<br>`:code:`<br>` Default: **CacheDisk** if one is
                                        configured for the VM size otherwise **ResourceDisk** is
                                        used.:code:`<br>`:code:`<br>` Refer to VM size documentation
                                        for Windows VM at
                                        https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
                                        and Linux VM at
                                        https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes
                                        to check which VM sizes exposes a cache disk.
                                type: str
                                choices:
                                    - CacheDisk
                                    - ResourceDisk
                    create_option:
                        description:
                            - >-
                                Specifies how the virtual machine should be
                                created.:code:`<br>`:code:`<br>` Possible values
                                are::code:`<br>`:code:`<br>` **Attach** \u2013 This value is
                                used when you are using a specialized disk to create the virtual
                                machine.:code:`<br>`:code:`<br>` **FromImage** \u2013 This value
                                is used when you are using an image to create the virtual
                                machine. If you are using a platform image, you also use the
                                imageReference element described above. If you are using a
                                marketplace image, you  also use the plan element previously
                                described.
                        required: true
                        type: str
                        choices:
                            - FromImage
                            - Empty
                            - Attach
                    disk_size_gb:
                        description:
                            - >-
                                Specifies the size of an empty data disk in gigabytes. This
                                element can be used to overwrite the size of the disk in a
                                virtual machine image. :code:`<br>`:code:`<br>` This value
                                cannot be larger than 1023 GB
                        type: int
                    managed_disk:
                        description:
                            - The managed disk parameters.
                        type: dict
                        suboptions:
                            storage_account_type:
                                description:
                                    - >-
                                        Specifies the storage account type for the managed disk.
                                        NOTE: UltraSSD_LRS can only be used with data disks, it
                                        cannot be used with OS Disk.
                                type: str
                                choices:
                                    - Standard_LRS
                                    - Premium_LRS
                                    - StandardSSD_LRS
                                    - UltraSSD_LRS
                            disk_encryption_set:
                                description:
                                    - >-
                                        Specifies the customer managed disk encryption set resource
                                        id for the managed disk.
                                type: dict
                                suboptions:
                                    id:
                                        description:
                                            - Resource Id
                                        type: str
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
                    name:
                        description:
                            - The disk name.
                        type: str
                    vhd:
                        description:
                            - The virtual hard disk.
                        type: dict
                        suboptions:
                            uri:
                                description:
                                    - Specifies the virtual hard disk's uri.
                                type: str
                    image:
                        description:
                            - >-
                                The source user image virtual hard disk. The virtual hard disk
                                will be copied before being attached to the virtual machine. If
                                SourceImage is provided, the destination virtual hard drive must
                                not exist.
                        type: dict
                        suboptions:
                            uri:
                                description:
                                    - Specifies the virtual hard disk's uri.
                                type: str
                    caching:
                        description:
                            - >-
                                Specifies the caching requirements. :code:`<br>`:code:`<br>`
                                Possible values are: :code:`<br>`:code:`<br>` **None**
                                :code:`<br>`:code:`<br>` **ReadOnly** :code:`<br>`:code:`<br>`
                                **ReadWrite** :code:`<br>`:code:`<br>` Default: **None for
                                Standard storage. ReadOnly for Premium storage**
                        type: sealed-choice
                    write_accelerator_enabled:
                        description:
                            - >-
                                Specifies whether writeAccelerator should be enabled or disabled
                                on the disk.
                        type: bool
                    create_option:
                        description:
                            - >-
                                Specifies how the virtual machine should be
                                created.:code:`<br>`:code:`<br>` Possible values
                                are::code:`<br>`:code:`<br>` **Attach** \u2013 This value is
                                used when you are using a specialized disk to create the virtual
                                machine.:code:`<br>`:code:`<br>` **FromImage** \u2013 This value
                                is used when you are using an image to create the virtual
                                machine. If you are using a platform image, you also use the
                                imageReference element described above. If you are using a
                                marketplace image, you  also use the plan element previously
                                described.
                        required: true
                        type: str
                        choices:
                            - FromImage
                            - Empty
                            - Attach
                    disk_size_gb:
                        description:
                            - >-
                                Specifies the size of an empty data disk in gigabytes. This
                                element can be used to overwrite the size of the disk in a
                                virtual machine image. :code:`<br>`:code:`<br>` This value
                                cannot be larger than 1023 GB
                        type: int
                    managed_disk:
                        description:
                            - The managed disk parameters.
                        type: dict
                        suboptions:
                            storage_account_type:
                                description:
                                    - >-
                                        Specifies the storage account type for the managed disk.
                                        NOTE: UltraSSD_LRS can only be used with data disks, it
                                        cannot be used with OS Disk.
                                type: str
                                choices:
                                    - Standard_LRS
                                    - Premium_LRS
                                    - StandardSSD_LRS
                                    - UltraSSD_LRS
                            disk_encryption_set:
                                description:
                                    - >-
                                        Specifies the customer managed disk encryption set resource
                                        id for the managed disk.
                                type: dict
                                suboptions:
                                    id:
                                        description:
                                            - Resource Id
                                        type: str
                    to_be_detached:
                        description:
                            - >-
                                Specifies whether the data disk is in process of detachment from
                                the VirtualMachine/VirtualMachineScaleset
                        type: bool
    additional_capabilities:
        description:
            - >-
                Specifies additional capabilities enabled or disabled on the virtual
                machine.
        type: dict
        suboptions:
            ultra_ssd_enabled:
                description:
                    - >-
                        The flag that enables or disables a capability to have one or more
                        managed data disks with UltraSSD_LRS storage account type on the VM
                        or VMSS. Managed disks with storage account type UltraSSD_LRS can be
                        added to a virtual machine or virtual machine scale set only if this
                        property is enabled.
                type: bool
    os_profile:
        description:
            - >-
                Specifies the operating system settings used while creating the virtual
                machine. Some of the settings cannot be changed once VM is provisioned.
        type: dict
        suboptions:
            computer_name:
                description:
                    - >-
                        Specifies the host OS name of the virtual machine.
                        :code:`<br>`:code:`<br>` This name cannot be updated after the VM is
                        created. :code:`<br>`:code:`<br>` **Max-length (Windows):** 15
                        characters :code:`<br>`:code:`<br>` **Max-length (Linux):** 64
                        characters. :code:`<br>`:code:`<br>` For naming conventions and
                        restrictions see `Azure infrastructure services implementation
                        guidelines
                        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-infrastructure-subscription-accounts-guidelines?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#1-naming-conventions>`_.
                type: str
            admin_username:
                description:
                    - >-
                        Specifies the name of the administrator account.
                        :code:`<br>`:code:`<br>` This property cannot be updated after the
                        VM is created. :code:`<br>`:code:`<br>` **Windows-only
                        restriction:** Cannot end in "." :code:`<br>`:code:`<br>`
                        **Disallowed values:** "administrator", "admin", "user", "user1",
                        "test", "user2", "test1", "user3", "admin1", "1", "123", "a",
                        "actuser", "adm", "admin2", "aspnet", "backup", "console", "david",
                        "guest", "john", "owner", "root", "server", "sql", "support",
                        "support_388945a0", "sys", "test2", "test3", "user4", "user5".
                        :code:`<br>`:code:`<br>` **Minimum-length (Linux):** 1  character
                        :code:`<br>`:code:`<br>` **Max-length (Linux):** 64 characters
                        :code:`<br>`:code:`<br>` **Max-length (Windows):** 20 characters 
                        :code:`<br>`:code:`<br>`:code:`<li>` For root access to the Linux
                        VM, see `Using root privileges on Linux virtual machines in Azure
                        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_\
                        :code:`<br>`:code:`<li>` For a list of built-in system users on
                        Linux that should not be used in this field, see `Selecting User
                        Names for Linux on Azure
                        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-usernames?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                type: str
            admin_password:
                description:
                    - >-
                        Specifies the password of the administrator account.
                        :code:`<br>`:code:`<br>` **Minimum-length (Windows):** 8 characters
                        :code:`<br>`:code:`<br>` **Minimum-length (Linux):** 6 characters
                        :code:`<br>`:code:`<br>` **Max-length (Windows):** 123 characters
                        :code:`<br>`:code:`<br>` **Max-length (Linux):** 72 characters
                        :code:`<br>`:code:`<br>` **Complexity requirements:** 3 out of 4
                        conditions below need to be fulfilled :code:`<br>` Has lower
                        characters :code:`<br>`Has upper characters :code:`<br>` Has a digit
                        :code:`<br>` Has a special character (Regex match [\W_])
                        :code:`<br>`:code:`<br>` **Disallowed values:** "abc@123",
                        "P@$$w0rd", "P@ssw0rd", "P@ssword123", "Pa$$word", "pass@word1",
                        "Password!", "Password1", "Password22", "iloveyou!"
                        :code:`<br>`:code:`<br>` For resetting the password, see `How to
                        reset the Remote Desktop service or its login password in a Windows
                        VM
                        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                        :code:`<br>`:code:`<br>` For resetting root password, see `Manage
                        users, SSH, and check or repair disks on Azure Linux VMs using the
                        VMAccess Extension
                        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password>`_
                type: str
            custom_data:
                description:
                    - >-
                        Specifies a base-64 encoded string of custom data. The base-64
                        encoded string is decoded to a binary array that is saved as a file
                        on the Virtual Machine. The maximum length of the binary array is
                        65535 bytes. :code:`<br>`:code:`<br>` **Note: Do not pass any
                        secrets or passwords in customData property**
                        :code:`<br>`:code:`<br>` This property cannot be updated after the
                        VM is created. :code:`<br>`:code:`<br>` customData is passed to the
                        VM to be saved as a file, for more information see `Custom Data on
                        Azure VMs
                        <https://azure.microsoft.com/en-us/blog/custom-data-and-cloud-init-on-windows-azure/>`_
                        :code:`<br>`:code:`<br>` For using cloud-init for your Linux VM, see
                        `Using cloud-init to customize a Linux VM during creation
                        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                type: str
            windows_configuration:
                description:
                    - Specifies Windows operating system settings on the virtual machine.
                type: dict
                suboptions:
                    provision_vm_agent:
                        description:
                            - >-
                                Indicates whether virtual machine agent should be provisioned on
                                the virtual machine. :code:`<br>`:code:`<br>` When this property
                                is not specified in the request body, default behavior is to set
                                it to true.  This will ensure that VM Agent is installed on the
                                VM so that extensions can be added to the VM later.
                        type: bool
                    enable_automatic_updates:
                        description:
                            - >-
                                Indicates whether Automatic Updates is enabled for the Windows
                                virtual machine. Default value is true. :code:`<br>`:code:`<br>`
                                For virtual machine scale sets, this property can be updated and
                                updates will take effect on OS reprovisioning.
                        type: bool
                    time_zone:
                        description:
                            - >-
                                Specifies the time zone of the virtual machine. e.g. "Pacific
                                Standard Time". :code:`<br>`:code:`<br>` Possible values can be
                                `TimeZoneInfo.Id
                                <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.id?#System_TimeZoneInfo_Id>`_
                                value from time zones returned by
                                `TimeZoneInfo.GetSystemTimeZones
                                <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.getsystemtimezones>`_.
                        type: str
                    additional_unattend_content:
                        description:
                            - >-
                                Specifies additional base-64 encoded XML formatted information
                                that can be included in the Unattend.xml file, which is used by
                                Windows Setup.
                        type: list
                        suboptions:
                            pass_name:
                                description:
                                    - >-
                                        The pass name. Currently, the only allowable value is
                                        OobeSystem.
                                type: constant
                            component_name:
                                description:
                                    - >-
                                        The component name. Currently, the only allowable value is
                                        Microsoft-Windows-Shell-Setup.
                                type: constant
                            setting_name:
                                description:
                                    - >-
                                        Specifies the name of the setting to which the content
                                        applies. Possible values are: FirstLogonCommands and
                                        AutoLogon.
                                type: sealed-choice
                            content:
                                description:
                                    - >-
                                        Specifies the XML formatted content that is added to the
                                        unattend.xml file for the specified path and component. The
                                        XML must be less than 4KB and must include the root element
                                        for the setting or feature that is being inserted.
                                type: str
                    patch_settings:
                        description:
                            - Specifies settings related to in-guest patching (KBs).
                        type: dict
                        suboptions:
                            patch_mode:
                                description:
                                    - >-
                                        Specifies the mode of in-guest patching to IaaS virtual
                                        machine.:code:`<br />`:code:`<br />` Possible values
                                        are::code:`<br />`:code:`<br />` **Manual** - You  control
                                        the application of patches to a virtual machine. You do this
                                        by applying patches manually inside the VM. In this mode,
                                        automatic updates are disabled; the property
                                        WindowsConfiguration.enableAutomaticUpdates must be
                                        false:code:`<br />`:code:`<br />` **AutomaticByOS** - The
                                        virtual machine will automatically be updated by the OS. The
                                        property WindowsConfiguration.enableAutomaticUpdates must be
                                        true. :code:`<br />`:code:`<br />` ** AutomaticByPlatform**
                                        - the virtual machine will automatically updated by the
                                        platform. The properties provisionVMAgent and
                                        WindowsConfiguration.enableAutomaticUpdates must be true
                                type: str
                                choices:
                                    - Manual
                                    - AutomaticByOS
                                    - AutomaticByPlatform
                    win_rm:
                        description:
                            - >-
                                Specifies the Windows Remote Management listeners. This enables
                                remote Windows PowerShell.
                        type: dict
                        suboptions:
                            listeners:
                                description:
                                    - The list of Windows Remote Management listeners
                                type: list
                                suboptions:
                                    protocol:
                                        description:
                                            - >-
                                                Specifies the protocol of WinRM listener.
                                                :code:`<br>`:code:`<br>` Possible values are:
                                                :code:`<br>`\ **http** :code:`<br>`:code:`<br>`
                                                **https**
                                        type: sealed-choice
                                    certificate_url:
                                        description:
                                            - >-
                                                This is the URL of a certificate that has been uploaded
                                                to Key Vault as a secret. For adding a secret to the Key
                                                Vault, see `Add a key or secret to the key vault
                                                <https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add>`_.
                                                In this case, your certificate needs to be It is the
                                                Base64 encoding of the following JSON Object which is
                                                encoded in UTF-8: :code:`<br>`:code:`<br>`
                                                {:code:`<br>` 
                                                "data":":code:`<Base64-encoded-certificate>`",:code:`<br>` 
                                                "dataType":"pfx",:code:`<br>` 
                                                "password":":code:`<pfx-file-password>`":code:`<br>`}
                                        type: str
            linux_configuration:
                description:
                    - >-
                        Specifies the Linux operating system settings on the virtual
                        machine. :code:`<br>`:code:`<br>`For a list of supported Linux
                        distributions, see `Linux on Azure-Endorsed Distributions
                        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-endorsed-distros?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                        :code:`<br>`:code:`<br>` For running non-endorsed distributions, see
                        `Information for Non-Endorsed Distributions
                        <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-create-upload-generic?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
                type: dict
                suboptions:
                    disable_password_authentication:
                        description:
                            - Specifies whether password authentication should be disabled.
                        type: bool
                    ssh:
                        description:
                            - Specifies the ssh key configuration for a Linux OS.
                        type: dict
                        suboptions:
                            public_keys:
                                description:
                                    - >-
                                        The list of SSH public keys used to authenticate with linux
                                        based VMs.
                                type: list
                                suboptions:
                                    path:
                                        description:
                                            - >-
                                                Specifies the full path on the created VM where ssh
                                                public key is stored. If the file already exists, the
                                                specified key is appended to the file. Example:
                                                /home/user/.ssh/authorized_keys
                                        type: str
                                    key_data:
                                        description:
                                            - >-
                                                SSH public key certificate used to authenticate with the
                                                VM through ssh. The key needs to be at least 2048-bit
                                                and in ssh-rsa format. :code:`<br>`:code:`<br>` For
                                                creating ssh keys, see `Create SSH keys on Linux and Mac
                                                for Linux VMs in Azure
                                                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-mac-create-ssh-keys?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
                                        type: str
                    provision_vm_agent:
                        description:
                            - >-
                                Indicates whether virtual machine agent should be provisioned on
                                the virtual machine. :code:`<br>`:code:`<br>` When this property
                                is not specified in the request body, default behavior is to set
                                it to true.  This will ensure that VM Agent is installed on the
                                VM so that extensions can be added to the VM later.
                        type: bool
            secrets:
                description:
                    - >-
                        Specifies set of certificates that should be installed onto the
                        virtual machine.
                type: list
                suboptions:
                    source_vault:
                        description:
                            - >-
                                The relative URL of the Key Vault containing all of the
                                certificates in VaultCertificates.
                        type: dict
                        suboptions:
                            id:
                                description:
                                    - Resource Id
                                type: str
                    vault_certificates:
                        description:
                            - >-
                                The list of key vault references in SourceVault which contain
                                certificates.
                        type: list
                        suboptions:
                            certificate_url:
                                description:
                                    - >-
                                        This is the URL of a certificate that has been uploaded to
                                        Key Vault as a secret. For adding a secret to the Key Vault,
                                        see `Add a key or secret to the key vault
                                        <https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add>`_.
                                        In this case, your certificate needs to be It is the Base64
                                        encoding of the following JSON Object which is encoded in
                                        UTF-8: :code:`<br>`:code:`<br>` {:code:`<br>` 
                                        "data":":code:`<Base64-encoded-certificate>`",:code:`<br>` 
                                        "dataType":"pfx",:code:`<br>` 
                                        "password":":code:`<pfx-file-password>`":code:`<br>`}
                                type: str
                            certificate_store:
                                description:
                                    - >-
                                        For Windows VMs, specifies the certificate store on the
                                        Virtual Machine to which the certificate should be added.
                                        The specified certificate store is implicitly in the
                                        LocalMachine account. :code:`<br>`:code:`<br>`For Linux VMs,
                                        the certificate file is placed under the /var/lib/waagent
                                        directory, with the file name
                                        &lt;UppercaseThumbprint&gt;.crt for the X509 certificate
                                        file and &lt;UppercaseThumbprint&gt;.prv for private key.
                                        Both of these files are .pem formatted.
                                type: str
            allow_extension_operations:
                description:
                    - >-
                        Specifies whether extension operations should be allowed on the
                        virtual machine. :code:`<br>`:code:`<br>`This may only be set to
                        False when no extensions are present on the virtual machine.
                type: bool
            require_guest_provision_signal:
                description:
                    - >-
                        Specifies whether the guest provision signal is required to infer
                        provision success of the virtual machine.  **Note: This property is
                        for private testing only, and all customers must not set the
                        property to false.**
                type: bool
    network_profile:
        description:
            - Specifies the network interfaces of the virtual machine.
        type: dict
        suboptions:
            network_interfaces:
                description:
                    - >-
                        Specifies the list of resource Ids for the network interfaces
                        associated with the virtual machine.
                type: list
                suboptions:
                    primary:
                        description:
                            - >-
                                Specifies the primary network interface in case the virtual
                                machine has more than 1 network interface.
                        type: bool
    security_profile:
        description:
            - Specifies the Security related profile settings for the virtual machine.
        type: dict
        suboptions:
            encryption_at_host:
                description:
                    - >-
                        This property can be used by user in the request to enable or
                        disable the Host Encryption for the virtual machine or virtual
                        machine scale set. This will enable the encryption for all the disks
                        including Resource/Temp disk at host itself.
                        :code:`<br>`:code:`<br>` Default: The Encryption at host will be
                        disabled unless this property is set to true for the resource.
                type: bool
    diagnostics_profile:
        description:
            - >-
                Specifies the boot diagnostic settings state.
                :code:`<br>`:code:`<br>`Minimum api-version: 2015-06-15.
        type: dict
        suboptions:
            boot_diagnostics:
                description:
                    - >-
                        Boot Diagnostics is a debugging feature which allows you to view
                        Console Output and Screenshot to diagnose VM status.
                        :code:`<br>`:code:`<br>` You can easily view the output of your
                        console log. :code:`<br>`:code:`<br>` Azure also enables you to see
                        a screenshot of the VM from the hypervisor.
                type: dict
                suboptions:
                    enabled:
                        description:
                            - >-
                                Whether boot diagnostics should be enabled on the Virtual
                                Machine.
                        type: bool
                    storage_uri:
                        description:
                            - >-
                                Uri of the storage account to use for placing the console output
                                and screenshot. :code:`<br>`:code:`<br>`If storageUri is not
                                specified while enabling boot diagnostics, managed storage will
                                be used.
                        type: str
    availability_set:
        description:
            - >-
                Specifies information about the availability set that the virtual
                machine should be assigned to. Virtual machines specified in the same
                availability set are allocated to different nodes to maximize
                availability. For more information about availability sets, see `Manage
                the availability of virtual machines
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-manage-availability?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                :code:`<br>`:code:`<br>` For more information on Azure planned
                maintenance, see `Planned maintenance for virtual machines in Azure
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-planned-maintenance?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                :code:`<br>`:code:`<br>` Currently, a VM can only be added to
                availability set at creation time. The availability set to which the VM
                is being added should be under the same resource group as the
                availability set resource. An existing VM cannot be added to an
                availability set. :code:`<br>`:code:`<br>`This property cannot exist
                along with a non-null properties.virtualMachineScaleSet reference.
        type: dict
        suboptions:
            id:
                description:
                    - Resource Id
                type: str
    virtual_machine_scale_set:
        description:
            - >-
                Specifies information about the virtual machine scale set that the
                virtual machine should be assigned to. Virtual machines specified in the
                same virtual machine scale set are allocated to different nodes to
                maximize availability. Currently, a VM can only be added to virtual
                machine scale set at creation time. An existing VM cannot be added to a
                virtual machine scale set. :code:`<br>`:code:`<br>`This property cannot
                exist along with a non-null properties.availabilitySet reference.
                :code:`<br>`:code:`<br>`Minimum api‐version: 2019‐03‐01
        type: dict
        suboptions:
            id:
                description:
                    - Resource Id
                type: str
    proximity_placement_group:
        description:
            - >-
                Specifies information about the proximity placement group that the
                virtual machine should be assigned to. :code:`<br>`:code:`<br>`Minimum
                api-version: 2018-04-01.
        type: dict
        suboptions:
            id:
                description:
                    - Resource Id
                type: str
    priority:
        description:
            - >-
                Specifies the priority for the virtual machine.
                :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01
        type: str
        choices:
            - Regular
            - Low
            - Spot
    eviction_policy:
        description:
            - >-
                Specifies the eviction policy for the Azure Spot virtual machine and
                Azure Spot scale set. :code:`<br>`:code:`<br>`For Azure Spot virtual
                machines, both 'Deallocate' and 'Delete' are supported and the minimum
                api-version is 2019-03-01. :code:`<br>`:code:`<br>`For Azure Spot scale
                sets, both 'Deallocate' and 'Delete' are supported and the minimum
                api-version is 2017-10-30-preview.
        type: str
        choices:
            - Deallocate
            - Delete
    billing_profile:
        description:
            - >-
                Specifies the billing related details of a Azure Spot virtual machine.
                :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
        type: dict
        suboptions:
            max_price:
                description:
                    - >-
                        Specifies the maximum price you are willing to pay for a Azure Spot
                        VM/VMSS. This price is in US Dollars. :code:`<br>`:code:`<br>` This
                        price will be compared with the current Azure Spot price for the VM
                        size. Also, the prices are compared at the time of create/update of
                        Azure Spot VM/VMSS and the operation will only succeed if  the
                        maxPrice is greater than the current Azure Spot price.
                        :code:`<br>`:code:`<br>` The maxPrice will also be used for evicting
                        a Azure Spot VM/VMSS if the current Azure Spot price goes beyond the
                        maxPrice after creation of VM/VMSS. :code:`<br>`:code:`<br>`
                        Possible values are: :code:`<br>`:code:`<br>` - Any decimal value
                        greater than zero. Example: 0.01538 :code:`<br>`:code:`<br>` -1 –
                        indicates default price to be up-to on-demand.
                        :code:`<br>`:code:`<br>` You can set the maxPrice to -1 to indicate
                        that the Azure Spot VM/VMSS should not be evicted for price reasons.
                        Also, the default max price is -1 if it is not provided by you.
                        :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
                type: number
    host:
        description:
            - >-
                Specifies information about the dedicated host that the virtual machine
                resides in. :code:`<br>`:code:`<br>`Minimum api-version: 2018-10-01.
        type: dict
        suboptions:
            id:
                description:
                    - Resource Id
                type: str
    host_group:
        description:
            - >-
                Specifies information about the dedicated host group that the virtual
                machine resides in. :code:`<br>`:code:`<br>`Minimum api-version:
                2020-06-01. :code:`<br>`:code:`<br>`NOTE: User cannot specify both host
                and hostGroup properties.
        type: dict
        suboptions:
            id:
                description:
                    - Resource Id
                type: str
    instance_view:
        description:
            - The virtual machine instance view.
        type: dict
        suboptions:
            platform_update_domain:
                description:
                    - Specifies the update domain of the virtual machine.
                type: int
            platform_fault_domain:
                description:
                    - Specifies the fault domain of the virtual machine.
                type: int
            computer_name:
                description:
                    - The computer name assigned to the virtual machine.
                type: str
            os_name:
                description:
                    - The Operating System running on the virtual machine.
                type: str
            os_version:
                description:
                    - The version of Operating System running on the virtual machine.
                type: str
            hyper_v_generation:
                description:
                    - Specifies the HyperVGeneration Type associated with a resource
                type: str
                choices:
                    - V1
                    - V2
            rdp_thumb_print:
                description:
                    - The Remote desktop certificate thumbprint.
                type: str
            vm_agent:
                description:
                    - The VM Agent running on the virtual machine.
                type: dict
                suboptions:
                    vm_agent_version:
                        description:
                            - The VM Agent full version.
                        type: str
                    extension_handlers:
                        description:
                            - The virtual machine extension handler instance view.
                        type: list
                        suboptions:
                            type:
                                description:
                                    - >-
                                        Specifies the type of the extension; an example is
                                        "CustomScriptExtension".
                                type: str
                            type_handler_version:
                                description:
                                    - Specifies the version of the script handler.
                                type: str
                            status:
                                description:
                                    - The extension handler status.
                                type: dict
                                suboptions:
                                    code:
                                        description:
                                            - The status code.
                                        type: str
                                    level:
                                        description:
                                            - The level code.
                                        type: sealed-choice
                                    display_status:
                                        description:
                                            - The short localizable label for the status.
                                        type: str
                                    message:
                                        description:
                                            - >-
                                                The detailed status message, including for alerts and
                                                error messages.
                                        type: str
                                    time:
                                        description:
                                            - The time of the status.
                                        type: str
                    statuses:
                        description:
                            - The resource status information.
                        type: list
                        suboptions:
                            code:
                                description:
                                    - The status code.
                                type: str
                            level:
                                description:
                                    - The level code.
                                type: sealed-choice
                            display_status:
                                description:
                                    - The short localizable label for the status.
                                type: str
                            message:
                                description:
                                    - >-
                                        The detailed status message, including for alerts and error
                                        messages.
                                type: str
                            time:
                                description:
                                    - The time of the status.
                                type: str
            maintenance_redeploy_status:
                description:
                    - The Maintenance Operation status on the virtual machine.
                type: dict
                suboptions:
                    is_customer_initiated_maintenance_allowed:
                        description:
                            - 'True, if customer is allowed to perform Maintenance.'
                        type: bool
                    pre_maintenance_window_start_time:
                        description:
                            - Start Time for the Pre Maintenance Window.
                        type: str
                    pre_maintenance_window_end_time:
                        description:
                            - End Time for the Pre Maintenance Window.
                        type: str
                    maintenance_window_start_time:
                        description:
                            - Start Time for the Maintenance Window.
                        type: str
                    maintenance_window_end_time:
                        description:
                            - End Time for the Maintenance Window.
                        type: str
                    last_operation_result_code:
                        description:
                            - The Last Maintenance Operation Result Code.
                        type: sealed-choice
                    last_operation_message:
                        description:
                            - Message returned for the last Maintenance Operation.
                        type: str
            disks:
                description:
                    - The virtual machine disk information.
                type: list
                suboptions:
                    name:
                        description:
                            - The disk name.
                        type: str
                    encryption_settings:
                        description:
                            - >-
                                Specifies the encryption settings for the OS Disk.
                                :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
                        type: list
                        suboptions:
                            disk_encryption_key:
                                description:
                                    - >-
                                        Specifies the location of the disk encryption key, which is
                                        a Key Vault Secret.
                                type: dict
                                suboptions:
                                    secret_url:
                                        description:
                                            - The URL referencing a secret in a Key Vault.
                                        required: true
                                        type: str
                                    source_vault:
                                        description:
                                            - The relative URL of the Key Vault containing the secret.
                                        required: true
                                        type: dict
                                        suboptions:
                                            id:
                                                description:
                                                    - Resource Id
                                                type: str
                            key_encryption_key:
                                description:
                                    - >-
                                        Specifies the location of the key encryption key in Key
                                        Vault.
                                type: dict
                                suboptions:
                                    key_url:
                                        description:
                                            - The URL referencing a key encryption key in Key Vault.
                                        required: true
                                        type: str
                                    source_vault:
                                        description:
                                            - The relative URL of the Key Vault containing the key.
                                        required: true
                                        type: dict
                                        suboptions:
                                            id:
                                                description:
                                                    - Resource Id
                                                type: str
                            enabled:
                                description:
                                    - >-
                                        Specifies whether disk encryption should be enabled on the
                                        virtual machine.
                                type: bool
                    statuses:
                        description:
                            - The resource status information.
                        type: list
                        suboptions:
                            code:
                                description:
                                    - The status code.
                                type: str
                            level:
                                description:
                                    - The level code.
                                type: sealed-choice
                            display_status:
                                description:
                                    - The short localizable label for the status.
                                type: str
                            message:
                                description:
                                    - >-
                                        The detailed status message, including for alerts and error
                                        messages.
                                type: str
                            time:
                                description:
                                    - The time of the status.
                                type: str
            extensions:
                description:
                    - The extensions information.
                type: list
                suboptions:
                    name:
                        description:
                            - The virtual machine extension name.
                        type: str
                    type:
                        description:
                            - >-
                                Specifies the type of the extension; an example is
                                "CustomScriptExtension".
                        type: str
                    type_handler_version:
                        description:
                            - Specifies the version of the script handler.
                        type: str
                    substatuses:
                        description:
                            - The resource status information.
                        type: list
                        suboptions:
                            code:
                                description:
                                    - The status code.
                                type: str
                            level:
                                description:
                                    - The level code.
                                type: sealed-choice
                            display_status:
                                description:
                                    - The short localizable label for the status.
                                type: str
                            message:
                                description:
                                    - >-
                                        The detailed status message, including for alerts and error
                                        messages.
                                type: str
                            time:
                                description:
                                    - The time of the status.
                                type: str
                    statuses:
                        description:
                            - The resource status information.
                        type: list
                        suboptions:
                            code:
                                description:
                                    - The status code.
                                type: str
                            level:
                                description:
                                    - The level code.
                                type: sealed-choice
                            display_status:
                                description:
                                    - The short localizable label for the status.
                                type: str
                            message:
                                description:
                                    - >-
                                        The detailed status message, including for alerts and error
                                        messages.
                                type: str
                            time:
                                description:
                                    - The time of the status.
                                type: str
            vm_health:
                description:
                    - The health status for the VM.
                type: dict
                suboptions:
                    status:
                        description:
                            - The health status information for the VM.
                        type: dict
                        suboptions:
                            code:
                                description:
                                    - The status code.
                                type: str
                            level:
                                description:
                                    - The level code.
                                type: sealed-choice
                            display_status:
                                description:
                                    - The short localizable label for the status.
                                type: str
                            message:
                                description:
                                    - >-
                                        The detailed status message, including for alerts and error
                                        messages.
                                type: str
                            time:
                                description:
                                    - The time of the status.
                                type: str
            boot_diagnostics:
                description:
                    - >-
                        Boot Diagnostics is a debugging feature which allows you to view
                        Console Output and Screenshot to diagnose VM status.
                        :code:`<br>`:code:`<br>` You can easily view the output of your
                        console log. :code:`<br>`:code:`<br>` Azure also enables you to see
                        a screenshot of the VM from the hypervisor.
                type: dict
                suboptions:
                    status:
                        description:
                            - >-
                                The boot diagnostics status information for the VM.
                                :code:`<br>`:code:`<br>` NOTE: It will be set only if there are
                                errors encountered in enabling boot diagnostics.
                        type: dict
                        suboptions:
                            code:
                                description:
                                    - The status code.
                                type: str
                            level:
                                description:
                                    - The level code.
                                type: sealed-choice
                            display_status:
                                description:
                                    - The short localizable label for the status.
                                type: str
                            message:
                                description:
                                    - >-
                                        The detailed status message, including for alerts and error
                                        messages.
                                type: str
                            time:
                                description:
                                    - The time of the status.
                                type: str
            statuses:
                description:
                    - The resource status information.
                type: list
                suboptions:
                    code:
                        description:
                            - The status code.
                        type: str
                    level:
                        description:
                            - The level code.
                        type: sealed-choice
                    display_status:
                        description:
                            - The short localizable label for the status.
                        type: str
                    message:
                        description:
                            - >-
                                The detailed status message, including for alerts and error
                                messages.
                        type: str
                    time:
                        description:
                            - The time of the status.
                        type: str
            patch_status:
                description:
                    - The status of virtual machine patch operations.
                type: dict
                suboptions:
                    available_patch_summary:
                        description:
                            - >-
                                The available patch summary of the latest assessment operation
                                for the virtual machine.
                        type: dict
                        suboptions:
                            error:
                                description:
                                    - >-
                                        The errors that were encountered during execution of the
                                        operation. The details array contains the list of them.
                                type: dict
                                suboptions:
                                    details:
                                        description:
                                            - The Api error details
                                        type: list
                                        suboptions:
                                            code:
                                                description:
                                                    - The error code.
                                                type: str
                                            target:
                                                description:
                                                    - The target of the particular error.
                                                type: str
                                            message:
                                                description:
                                                    - The error message.
                                                type: str
                                    innererror:
                                        description:
                                            - The Api inner error
                                        type: dict
                                        suboptions:
                                            exceptiontype:
                                                description:
                                                    - The exception type.
                                                type: str
                                            errordetail:
                                                description:
                                                    - The internal error message or exception dump.
                                                type: str
                                    code:
                                        description:
                                            - The error code.
                                        type: str
                                    target:
                                        description:
                                            - The target of the particular error.
                                        type: str
                                    message:
                                        description:
                                            - The error message.
                                        type: str
                    last_patch_installation_summary:
                        description:
                            - >-
                                The installation summary of the latest installation operation
                                for the virtual machine.
                        type: dict
                        suboptions:
                            error:
                                description:
                                    - >-
                                        The errors that were encountered during execution of the
                                        operation. The details array contains the list of them.
                                type: dict
                                suboptions:
                                    details:
                                        description:
                                            - The Api error details
                                        type: list
                                        suboptions:
                                            code:
                                                description:
                                                    - The error code.
                                                type: str
                                            target:
                                                description:
                                                    - The target of the particular error.
                                                type: str
                                            message:
                                                description:
                                                    - The error message.
                                                type: str
                                    innererror:
                                        description:
                                            - The Api inner error
                                        type: dict
                                        suboptions:
                                            exceptiontype:
                                                description:
                                                    - The exception type.
                                                type: str
                                            errordetail:
                                                description:
                                                    - The internal error message or exception dump.
                                                type: str
                                    code:
                                        description:
                                            - The error code.
                                        type: str
                                    target:
                                        description:
                                            - The target of the particular error.
                                        type: str
                                    message:
                                        description:
                                            - The error message.
                                        type: str
    license_type:
        description:
            - >-
                Specifies that the image or disk that is being used was licensed
                on-premises. This element is only used for images that contain the
                Windows Server operating system. :code:`<br>`:code:`<br>` Possible
                values are: :code:`<br>`:code:`<br>` Windows_Client
                :code:`<br>`:code:`<br>` Windows_Server :code:`<br>`:code:`<br>` If this
                element is included in a request for an update, the value must match the
                initial value. This value cannot be updated. :code:`<br>`:code:`<br>`
                For more information, see `Azure Hybrid Use Benefit for Windows Server
                <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
        type: str
    extensions_time_budget:
        description:
            - >-
                Specifies the time alloted for all extensions to start. The time
                duration should be between 15 minutes and 120 minutes (inclusive) and
                should be specified in ISO 8601 format. The default value is 90 minutes
                (PT1H30M). :code:`<br>`:code:`<br>` Minimum api-version: 2020-06-01
        type: str
    force_deletion:
        description:
            - Optional parameter to force delete virtual machines.
        type: bool
    expand:
        description:
            - The expand expression to apply on the operation.
        type: constant
    state:
        description:
            - Assert the state of the VirtualMachine.
            - >-
                Use C(present) to create or update an VirtualMachine and C(absent) to
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
    - name: Create a custom-image vm from an unmanaged generalized os image.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: '{vm-name}'
        location: westus
        properties:
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              image:
                uri: >-
                  http://{existing-storage-account-name}.blob.core.windows.net/{existing-container-name}/{existing-generalized-os-image-blob-name}.vhd
              name: myVMosdisk
              os_type: Windows
              vhd:
                uri: >-
                  http://{existing-storage-account-name}.blob.core.windows.net/{existing-container-name}/myDisk.vhd
        

    - name: Create a platform-image vm with unmanaged os and data disks.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: '{vm-name}'
        location: westus
        properties:
          hardware_profile:
            vm_size: Standard_D2_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            data_disks:
              - create_option: Empty
                disk_size_gb: 1023
                lun: 0
                vhd:
                  uri: >-
                    http://{existing-storage-account-name}.blob.core.windows.net/{existing-container-name}/myDisk0.vhd
              - create_option: Empty
                disk_size_gb: 1023
                lun: 1
                vhd:
                  uri: >-
                    http://{existing-storage-account-name}.blob.core.windows.net/{existing-container-name}/myDisk1.vhd
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              name: myVMosdisk
              vhd:
                uri: >-
                  http://{existing-storage-account-name}.blob.core.windows.net/{existing-container-name}/myDisk.vhd
        

    - name: Create a vm from a custom image.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            image_reference:
              id: >-
                /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/images/{existing-custom-image-name}
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm in an availability set.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          availability_set:
            id: >-
              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/availabilitySets/{existing-availability-set-name}
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with DiskEncryptionSet resource id in the os disk and data disk.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            data_disks:
              - caching: ReadWrite
                create_option: Empty
                disk_size_gb: 1023
                lun: 0
                managed_disk:
                  disk_encryption_set:
                    id: >-
                      /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSets/{existing-diskEncryptionSet-name}
                  storage_account_type: Standard_LRS
              - caching: ReadWrite
                create_option: Attach
                disk_size_gb: 1023
                lun: 1
                managed_disk:
                  disk_encryption_set:
                    id: >-
                      /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSets/{existing-diskEncryptionSet-name}
                  id: >-
                    /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/{existing-managed-disk-name}
                  storage_account_type: Standard_LRS
            image_reference:
              id: >-
                /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/images/{existing-custom-image-name}
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                disk_encryption_set:
                  id: >-
                    /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/diskEncryptionSets/{existing-diskEncryptionSet-name}
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with Host Encryption using encryptionAtHost property.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        plan:
          name: windows2016
          product: windows-data-science-vm
          publisher: microsoft-ads
        properties:
          hardware_profile:
            vm_size: Standard_DS1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          security_profile:
            encryption_at_host: true
          storage_profile:
            image_reference:
              offer: windows-data-science-vm
              publisher: microsoft-ads
              sku: windows2016
              version: latest
            os_disk:
              caching: ReadOnly
              create_option: FromImage
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with a marketplace image plan.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        plan:
          name: windows2016
          product: windows-data-science-vm
          publisher: microsoft-ads
        properties:
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            image_reference:
              offer: windows-data-science-vm
              publisher: microsoft-ads
              sku: windows2016
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with a patch setting patchMode of AutomaticByOS.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/nsgExistingNic
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
            windows_configuration:
              enable_automatic_updates: true
              patch_settings:
                patch_mode: AutomaticByOS
              provision_vmagent: true
          storage_profile:
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Premium_LRS
              name: myVMosdisk
        

    - name: Create a vm with a patch setting patchMode of AutomaticByPlatform.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
            windows_configuration:
              enable_automatic_updates: true
              patch_settings:
                patch_mode: AutomaticByPlatform
              provision_vmagent: true
          storage_profile:
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Premium_LRS
              name: myVMosdisk
        

    - name: Create a vm with a patch setting patchMode of Manual.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
            windows_configuration:
              enable_automatic_updates: true
              patch_settings:
                patch_mode: Manual
              provision_vmagent: true
          storage_profile:
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Premium_LRS
              name: myVMosdisk
        

    - name: Create a vm with an extensions time budget.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          diagnostics_profile:
            boot_diagnostics:
              enabled: true
              storage_uri: 'http://{existing-storage-account-name}.blob.core.windows.net'
          extensions_time_budget: PT30M
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with boot diagnostics.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          diagnostics_profile:
            boot_diagnostics:
              enabled: true
              storage_uri: 'http://{existing-storage-account-name}.blob.core.windows.net'
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with empty data disks.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          hardware_profile:
            vm_size: Standard_D2_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            data_disks:
              - create_option: Empty
                disk_size_gb: 1023
                lun: 0
              - create_option: Empty
                disk_size_gb: 1023
                lun: 1
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with ephemeral os disk provisioning in Cache disk using placement property.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        plan:
          name: windows2016
          product: windows-data-science-vm
          publisher: microsoft-ads
        properties:
          hardware_profile:
            vm_size: Standard_DS1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            image_reference:
              offer: windows-data-science-vm
              publisher: microsoft-ads
              sku: windows2016
              version: latest
            os_disk:
              caching: ReadOnly
              create_option: FromImage
              diff_disk_settings:
                option: Local
                placement: CacheDisk
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with ephemeral os disk provisioning in Resource disk using placement property.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        plan:
          name: windows2016
          product: windows-data-science-vm
          publisher: microsoft-ads
        properties:
          hardware_profile:
            vm_size: Standard_DS1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            image_reference:
              offer: windows-data-science-vm
              publisher: microsoft-ads
              sku: windows2016
              version: latest
            os_disk:
              caching: ReadOnly
              create_option: FromImage
              diff_disk_settings:
                option: Local
                placement: ResourceDisk
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with ephemeral os disk.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        plan:
          name: windows2016
          product: windows-data-science-vm
          publisher: microsoft-ads
        properties:
          hardware_profile:
            vm_size: Standard_DS1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            image_reference:
              offer: windows-data-science-vm
              publisher: microsoft-ads
              sku: windows2016
              version: latest
            os_disk:
              caching: ReadOnly
              create_option: FromImage
              diff_disk_settings:
                option: Local
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with managed boot diagnostics.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          diagnostics_profile:
            boot_diagnostics:
              enabled: true
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with password authentication.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Create a vm with premium storage.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Premium_LRS
              name: myVMosdisk
        

    - name: Create a vm with ssh authentication.
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        location: westus
        properties:
          hardware_profile:
            vm_size: Standard_D1_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_username: '{your-username}'
            computer_name: myVM
            linux_configuration:
              disable_password_authentication: true
              ssh:
                public_keys:
                  - key_data: >-
                      ssh-rsa
                      AAAAB3NzaC1yc2EAAAADAQABAAABAQCeClRAk2ipUs/l5voIsDC5q9RI+YSRd1Bvd/O+axgY4WiBzG+4FwJWZm/mLLe5DoOdHQwmU2FrKXZSW4w2sYE70KeWnrFViCOX5MTVvJgPE8ClugNl8RWth/tU849DvM9sT7vFgfVSHcAS2yDRyDlueii+8nF2ym8XWAPltFVCyLHRsyBp5YPqK8JFYIa1eybKsY3hEAxRCA+/7bq8et+Gj3coOsuRmrehav7rE6N12Pb80I6ofa6SM5XNYq4Xk0iYNx7R3kdz0Jj9XgZYWjAHjJmT0gTRoOnt6upOuxK7xI/ykWrllgpXrCPu3Ymz+c+ujaqcxDopnAl2lmf69/J1
                    path: '/home/{your-username}/.ssh/authorized_keys'
          storage_profile:
            image_reference:
              offer: '{image_offer}'
              publisher: '{image_publisher}'
              sku: '{image_sku}'
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

    - name: Update a VM by detaching data disk
      azure_rm_virtualmachine: 
        resource_group_name: myResourceGroup
        vm_name: myVM
        properties:
          hardware_profile:
            vm_size: Standard_D2_v2
          network_profile:
            network_interfaces:
              - id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkInterfaces/{existing-nic-name}
                properties:
                  primary: true
          os_profile:
            admin_password: '{your-password}'
            admin_username: '{your-username}'
            computer_name: myVM
          storage_profile:
            data_disks:
              - create_option: Empty
                disk_size_gb: 1023
                lun: 0
                to_be_detached: true
              - create_option: Empty
                disk_size_gb: 1023
                lun: 1
                to_be_detached: false
            image_reference:
              offer: WindowsServer
              publisher: MicrosoftWindowsServer
              sku: 2016-Datacenter
              version: latest
            os_disk:
              caching: ReadWrite
              create_option: FromImage
              managed_disk:
                storage_account_type: Standard_LRS
              name: myVMosdisk
        

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
plan:
    description:
        - >-
            Specifies information about the marketplace image used to create the
            virtual machine. This element is only used for marketplace images. Before
            you can use a marketplace image from an API, you must enable the image for
            programmatic use.  In the Azure portal, find the marketplace image that
            you want to use and then click **Want to deploy programmatically, Get
            Started ->**. Enter any required information and then click **Save**.
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
                - >-
                    Specifies the product of the image from the marketplace. This is the
                    same value as Offer under the imageReference element.
            returned: always
            type: str
            sample: null
        promotion_code:
            description:
                - The promotion code.
            returned: always
            type: str
            sample: null
resources:
    description:
        - The virtual machine child extension resources.
    returned: always
    type: list
    sample: null
    contains:
        force_update_tag:
            description:
                - >-
                    How the extension handler should be forced to update even if the
                    extension configuration has not changed.
            returned: always
            type: str
            sample: null
        publisher:
            description:
                - The name of the extension handler publisher.
            returned: always
            type: str
            sample: null
        type_properties_type:
            description:
                - >-
                    Specifies the type of the extension; an example is
                    "CustomScriptExtension".
            returned: always
            type: str
            sample: null
        type_handler_version:
            description:
                - Specifies the version of the script handler.
            returned: always
            type: str
            sample: null
        auto_upgrade_minor_version:
            description:
                - >-
                    Indicates whether the extension should use a newer minor version if
                    one is available at deployment time. Once deployed, however, the
                    extension will not upgrade minor versions unless redeployed, even with
                    this property set to true.
            returned: always
            type: bool
            sample: null
        enable_automatic_upgrade:
            description:
                - >-
                    Indicates whether the extension should be automatically upgraded by
                    the platform if there is a newer version of the extension available.
            returned: always
            type: bool
            sample: null
        settings:
            description:
                - Json formatted public settings for the extension.
            returned: always
            type: any
            sample: null
        protected_settings:
            description:
                - >-
                    The extension can contain either protectedSettings or
                    protectedSettingsFromKeyVault or no protected settings at all.
            returned: always
            type: any
            sample: null
        instance_view:
            description:
                - The virtual machine extension instance view.
            returned: always
            type: dict
            sample: null
            contains:
                name:
                    description:
                        - The virtual machine extension name.
                    returned: always
                    type: str
                    sample: null
                type:
                    description:
                        - >-
                            Specifies the type of the extension; an example is
                            "CustomScriptExtension".
                    returned: always
                    type: str
                    sample: null
                type_handler_version:
                    description:
                        - Specifies the version of the script handler.
                    returned: always
                    type: str
                    sample: null
                substatuses:
                    description:
                        - The resource status information.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            returned: always
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            returned: always
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            returned: always
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            returned: always
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            returned: always
                            type: str
                            sample: null
                statuses:
                    description:
                        - The resource status information.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            returned: always
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            returned: always
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            returned: always
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            returned: always
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            returned: always
                            type: str
                            sample: null
identity:
    description:
        - 'The identity of the virtual machine, if configured.'
    returned: always
    type: dict
    sample: null
    contains:
        type:
            description:
                - >-
                    The type of identity used for the virtual machine. The type
                    'SystemAssigned, UserAssigned' includes both an implicitly created
                    identity and a set of user assigned identities. The type 'None' will
                    remove any identities from the virtual machine.
            returned: always
            type: sealed-choice
            sample: null
        user_assigned_identities:
            description:
                - >-
                    The list of user identities associated with the Virtual Machine. The
                    user identity dictionary key references will be ARM resource ids in
                    the form:
                    '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
            returned: always
            type: dict
            sample: null
zones:
    description:
        - The virtual machine zones.
    returned: always
    type: list
    sample: null
hardware_profile:
    description:
        - Specifies the hardware settings for the virtual machine.
    returned: always
    type: dict
    sample: null
    contains:
        vm_size:
            description:
                - >-
                    Specifies the size of the virtual machine. For more information about
                    virtual machine sizes, see `Sizes for virtual machines
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-sizes?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                    :code:`<br>`:code:`<br>` The available VM sizes depend on region and
                    availability set. For a list of available sizes use these APIs: 
                    :code:`<br>`:code:`<br>` `List all available virtual machine sizes in
                    an availability set
                    <https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes>`_
                    :code:`<br>`:code:`<br>` `List all available virtual machine sizes in
                    a region
                    <https://docs.microsoft.com/rest/api/compute/virtualmachinesizes/list>`_
                    :code:`<br>`:code:`<br>` `List all available virtual machine sizes for
                    resizing
                    <https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes>`_
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
        image_reference:
            description:
                - >-
                    Specifies information about the image to use. You can specify
                    information about platform images, marketplace images, or virtual
                    machine images. This element is required when you want to use a
                    platform image, marketplace image, or virtual machine image, but is
                    not used in other creation operations.
            returned: always
            type: dict
            sample: null
            contains:
                publisher:
                    description:
                        - The image publisher.
                    returned: always
                    type: str
                    sample: null
                offer:
                    description:
                        - >-
                            Specifies the offer of the platform image or marketplace image
                            used to create the virtual machine.
                    returned: always
                    type: str
                    sample: null
                sku:
                    description:
                        - The image SKU.
                    returned: always
                    type: str
                    sample: null
                version:
                    description:
                        - >-
                            Specifies the version of the platform image or marketplace image
                            used to create the virtual machine. The allowed formats are
                            Major.Minor.Build or 'latest'. Major, Minor, and Build are decimal
                            numbers. Specify 'latest' to use the latest version of an image
                            available at deploy time. Even if you use 'latest', the VM image
                            will not automatically update after deploy time even if a new
                            version becomes available.
                    returned: always
                    type: str
                    sample: null
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
                            included in the disk if creating a VM from user-image or a
                            specialized VHD. :code:`<br>`:code:`<br>` Possible values are:
                            :code:`<br>`:code:`<br>` **Windows** :code:`<br>`:code:`<br>`
                            **Linux**
                    returned: always
                    type: sealed-choice
                    sample: null
                encryption_settings:
                    description:
                        - >-
                            Specifies the encryption settings for the OS Disk.
                            :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        disk_encryption_key:
                            description:
                                - >-
                                    Specifies the location of the disk encryption key, which is a
                                    Key Vault Secret.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                secret_url:
                                    description:
                                        - The URL referencing a secret in a Key Vault.
                                    returned: always
                                    type: str
                                    sample: null
                                source_vault:
                                    description:
                                        - The relative URL of the Key Vault containing the secret.
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
                        key_encryption_key:
                            description:
                                - Specifies the location of the key encryption key in Key Vault.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                key_url:
                                    description:
                                        - The URL referencing a key encryption key in Key Vault.
                                    returned: always
                                    type: str
                                    sample: null
                                source_vault:
                                    description:
                                        - The relative URL of the Key Vault containing the key.
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
                        enabled:
                            description:
                                - >-
                                    Specifies whether disk encryption should be enabled on the
                                    virtual machine.
                            returned: always
                            type: bool
                            sample: null
                name:
                    description:
                        - The disk name.
                    returned: always
                    type: str
                    sample: null
                vhd:
                    description:
                        - The virtual hard disk.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        uri:
                            description:
                                - Specifies the virtual hard disk's uri.
                            returned: always
                            type: str
                            sample: null
                image:
                    description:
                        - >-
                            The source user image virtual hard disk. The virtual hard disk
                            will be copied before being attached to the virtual machine. If
                            SourceImage is provided, the destination virtual hard drive must
                            not exist.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        uri:
                            description:
                                - Specifies the virtual hard disk's uri.
                            returned: always
                            type: str
                            sample: null
                caching:
                    description:
                        - >-
                            Specifies the caching requirements. :code:`<br>`:code:`<br>`
                            Possible values are: :code:`<br>`:code:`<br>` **None**
                            :code:`<br>`:code:`<br>` **ReadOnly** :code:`<br>`:code:`<br>`
                            **ReadWrite** :code:`<br>`:code:`<br>` Default: **None** for
                            Standard storage. **ReadOnly** for Premium storage.
                    returned: always
                    type: sealed-choice
                    sample: null
                write_accelerator_enabled:
                    description:
                        - >-
                            Specifies whether writeAccelerator should be enabled or disabled
                            on the disk.
                    returned: always
                    type: bool
                    sample: null
                diff_disk_settings:
                    description:
                        - >-
                            Specifies the ephemeral Disk Settings for the operating system
                            disk used by the virtual machine.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        option:
                            description:
                                - >-
                                    Specifies the ephemeral disk settings for operating system
                                    disk.
                            returned: always
                            type: str
                            sample: null
                        placement:
                            description:
                                - >-
                                    Specifies the ephemeral disk placement for operating system
                                    disk.:code:`<br>`:code:`<br>` Possible values are:
                                    :code:`<br>`:code:`<br>` **CacheDisk**
                                    :code:`<br>`:code:`<br>` **ResourceDisk**
                                    :code:`<br>`:code:`<br>` Default: **CacheDisk** if one is
                                    configured for the VM size otherwise **ResourceDisk** is
                                    used.:code:`<br>`:code:`<br>` Refer to VM size documentation
                                    for Windows VM at
                                    https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
                                    and Linux VM at
                                    https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes
                                    to check which VM sizes exposes a cache disk.
                            returned: always
                            type: str
                            sample: null
                create_option:
                    description:
                        - >-
                            Specifies how the virtual machine should be
                            created.:code:`<br>`:code:`<br>` Possible values
                            are::code:`<br>`:code:`<br>` **Attach** \u2013 This value is used
                            when you are using a specialized disk to create the virtual
                            machine.:code:`<br>`:code:`<br>` **FromImage** \u2013 This value
                            is used when you are using an image to create the virtual machine.
                            If you are using a platform image, you also use the imageReference
                            element described above. If you are using a marketplace image,
                            you  also use the plan element previously described.
                    returned: always
                    type: str
                    sample: null
                disk_size_gb:
                    description:
                        - >-
                            Specifies the size of an empty data disk in gigabytes. This
                            element can be used to overwrite the size of the disk in a virtual
                            machine image. :code:`<br>`:code:`<br>` This value cannot be
                            larger than 1023 GB
                    returned: always
                    type: int
                    sample: null
                managed_disk:
                    description:
                        - The managed disk parameters.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        storage_account_type:
                            description:
                                - >-
                                    Specifies the storage account type for the managed disk. NOTE:
                                    UltraSSD_LRS can only be used with data disks, it cannot be
                                    used with OS Disk.
                            returned: always
                            type: str
                            sample: null
                        disk_encryption_set:
                            description:
                                - >-
                                    Specifies the customer managed disk encryption set resource id
                                    for the managed disk.
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
                name:
                    description:
                        - The disk name.
                    returned: always
                    type: str
                    sample: null
                vhd:
                    description:
                        - The virtual hard disk.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        uri:
                            description:
                                - Specifies the virtual hard disk's uri.
                            returned: always
                            type: str
                            sample: null
                image:
                    description:
                        - >-
                            The source user image virtual hard disk. The virtual hard disk
                            will be copied before being attached to the virtual machine. If
                            SourceImage is provided, the destination virtual hard drive must
                            not exist.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        uri:
                            description:
                                - Specifies the virtual hard disk's uri.
                            returned: always
                            type: str
                            sample: null
                caching:
                    description:
                        - >-
                            Specifies the caching requirements. :code:`<br>`:code:`<br>`
                            Possible values are: :code:`<br>`:code:`<br>` **None**
                            :code:`<br>`:code:`<br>` **ReadOnly** :code:`<br>`:code:`<br>`
                            **ReadWrite** :code:`<br>`:code:`<br>` Default: **None for
                            Standard storage. ReadOnly for Premium storage**
                    returned: always
                    type: sealed-choice
                    sample: null
                write_accelerator_enabled:
                    description:
                        - >-
                            Specifies whether writeAccelerator should be enabled or disabled
                            on the disk.
                    returned: always
                    type: bool
                    sample: null
                create_option:
                    description:
                        - >-
                            Specifies how the virtual machine should be
                            created.:code:`<br>`:code:`<br>` Possible values
                            are::code:`<br>`:code:`<br>` **Attach** \u2013 This value is used
                            when you are using a specialized disk to create the virtual
                            machine.:code:`<br>`:code:`<br>` **FromImage** \u2013 This value
                            is used when you are using an image to create the virtual machine.
                            If you are using a platform image, you also use the imageReference
                            element described above. If you are using a marketplace image,
                            you  also use the plan element previously described.
                    returned: always
                    type: str
                    sample: null
                disk_size_gb:
                    description:
                        - >-
                            Specifies the size of an empty data disk in gigabytes. This
                            element can be used to overwrite the size of the disk in a virtual
                            machine image. :code:`<br>`:code:`<br>` This value cannot be
                            larger than 1023 GB
                    returned: always
                    type: int
                    sample: null
                managed_disk:
                    description:
                        - The managed disk parameters.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        storage_account_type:
                            description:
                                - >-
                                    Specifies the storage account type for the managed disk. NOTE:
                                    UltraSSD_LRS can only be used with data disks, it cannot be
                                    used with OS Disk.
                            returned: always
                            type: str
                            sample: null
                        disk_encryption_set:
                            description:
                                - >-
                                    Specifies the customer managed disk encryption set resource id
                                    for the managed disk.
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
                to_be_detached:
                    description:
                        - >-
                            Specifies whether the data disk is in process of detachment from
                            the VirtualMachine/VirtualMachineScaleset
                    returned: always
                    type: bool
                    sample: null
additional_capabilities:
    description:
        - >-
            Specifies additional capabilities enabled or disabled on the virtual
            machine.
    returned: always
    type: dict
    sample: null
    contains:
        ultra_ssd_enabled:
            description:
                - >-
                    The flag that enables or disables a capability to have one or more
                    managed data disks with UltraSSD_LRS storage account type on the VM or
                    VMSS. Managed disks with storage account type UltraSSD_LRS can be
                    added to a virtual machine or virtual machine scale set only if this
                    property is enabled.
            returned: always
            type: bool
            sample: null
os_profile:
    description:
        - >-
            Specifies the operating system settings used while creating the virtual
            machine. Some of the settings cannot be changed once VM is provisioned.
    returned: always
    type: dict
    sample: null
    contains:
        computer_name:
            description:
                - >-
                    Specifies the host OS name of the virtual machine.
                    :code:`<br>`:code:`<br>` This name cannot be updated after the VM is
                    created. :code:`<br>`:code:`<br>` **Max-length (Windows):** 15
                    characters :code:`<br>`:code:`<br>` **Max-length (Linux):** 64
                    characters. :code:`<br>`:code:`<br>` For naming conventions and
                    restrictions see `Azure infrastructure services implementation
                    guidelines
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-infrastructure-subscription-accounts-guidelines?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#1-naming-conventions>`_.
            returned: always
            type: str
            sample: null
        admin_username:
            description:
                - >-
                    Specifies the name of the administrator account.
                    :code:`<br>`:code:`<br>` This property cannot be updated after the VM
                    is created. :code:`<br>`:code:`<br>` **Windows-only restriction:**
                    Cannot end in "." :code:`<br>`:code:`<br>` **Disallowed values:**
                    "administrator", "admin", "user", "user1", "test", "user2", "test1",
                    "user3", "admin1", "1", "123", "a", "actuser", "adm", "admin2",
                    "aspnet", "backup", "console", "david", "guest", "john", "owner",
                    "root", "server", "sql", "support", "support_388945a0", "sys",
                    "test2", "test3", "user4", "user5". :code:`<br>`:code:`<br>`
                    **Minimum-length (Linux):** 1  character :code:`<br>`:code:`<br>`
                    **Max-length (Linux):** 64 characters :code:`<br>`:code:`<br>`
                    **Max-length (Windows):** 20 characters 
                    :code:`<br>`:code:`<br>`:code:`<li>` For root access to the Linux VM,
                    see `Using root privileges on Linux virtual machines in Azure
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_\
                    :code:`<br>`:code:`<li>` For a list of built-in system users on Linux
                    that should not be used in this field, see `Selecting User Names for
                    Linux on Azure
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-usernames?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
            returned: always
            type: str
            sample: null
        admin_password:
            description:
                - >-
                    Specifies the password of the administrator account.
                    :code:`<br>`:code:`<br>` **Minimum-length (Windows):** 8 characters
                    :code:`<br>`:code:`<br>` **Minimum-length (Linux):** 6 characters
                    :code:`<br>`:code:`<br>` **Max-length (Windows):** 123 characters
                    :code:`<br>`:code:`<br>` **Max-length (Linux):** 72 characters
                    :code:`<br>`:code:`<br>` **Complexity requirements:** 3 out of 4
                    conditions below need to be fulfilled :code:`<br>` Has lower
                    characters :code:`<br>`Has upper characters :code:`<br>` Has a digit
                    :code:`<br>` Has a special character (Regex match [\W_])
                    :code:`<br>`:code:`<br>` **Disallowed values:** "abc@123", "P@$$w0rd",
                    "P@ssw0rd", "P@ssword123", "Pa$$word", "pass@word1", "Password!",
                    "Password1", "Password22", "iloveyou!" :code:`<br>`:code:`<br>` For
                    resetting the password, see `How to reset the Remote Desktop service
                    or its login password in a Windows VM
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                    :code:`<br>`:code:`<br>` For resetting root password, see `Manage
                    users, SSH, and check or repair disks on Azure Linux VMs using the
                    VMAccess Extension
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password>`_
            returned: always
            type: str
            sample: null
        custom_data:
            description:
                - >-
                    Specifies a base-64 encoded string of custom data. The base-64 encoded
                    string is decoded to a binary array that is saved as a file on the
                    Virtual Machine. The maximum length of the binary array is 65535
                    bytes. :code:`<br>`:code:`<br>` **Note: Do not pass any secrets or
                    passwords in customData property** :code:`<br>`:code:`<br>` This
                    property cannot be updated after the VM is created.
                    :code:`<br>`:code:`<br>` customData is passed to the VM to be saved as
                    a file, for more information see `Custom Data on Azure VMs
                    <https://azure.microsoft.com/en-us/blog/custom-data-and-cloud-init-on-windows-azure/>`_
                    :code:`<br>`:code:`<br>` For using cloud-init for your Linux VM, see
                    `Using cloud-init to customize a Linux VM during creation
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
            returned: always
            type: str
            sample: null
        windows_configuration:
            description:
                - Specifies Windows operating system settings on the virtual machine.
            returned: always
            type: dict
            sample: null
            contains:
                provision_vm_agent:
                    description:
                        - >-
                            Indicates whether virtual machine agent should be provisioned on
                            the virtual machine. :code:`<br>`:code:`<br>` When this property
                            is not specified in the request body, default behavior is to set
                            it to true.  This will ensure that VM Agent is installed on the VM
                            so that extensions can be added to the VM later.
                    returned: always
                    type: bool
                    sample: null
                enable_automatic_updates:
                    description:
                        - >-
                            Indicates whether Automatic Updates is enabled for the Windows
                            virtual machine. Default value is true. :code:`<br>`:code:`<br>`
                            For virtual machine scale sets, this property can be updated and
                            updates will take effect on OS reprovisioning.
                    returned: always
                    type: bool
                    sample: null
                time_zone:
                    description:
                        - >-
                            Specifies the time zone of the virtual machine. e.g. "Pacific
                            Standard Time". :code:`<br>`:code:`<br>` Possible values can be
                            `TimeZoneInfo.Id
                            <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.id?#System_TimeZoneInfo_Id>`_
                            value from time zones returned by `TimeZoneInfo.GetSystemTimeZones
                            <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.getsystemtimezones>`_.
                    returned: always
                    type: str
                    sample: null
                additional_unattend_content:
                    description:
                        - >-
                            Specifies additional base-64 encoded XML formatted information
                            that can be included in the Unattend.xml file, which is used by
                            Windows Setup.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        pass_name:
                            description:
                                - >-
                                    The pass name. Currently, the only allowable value is
                                    OobeSystem.
                            returned: always
                            type: constant
                            sample: null
                        component_name:
                            description:
                                - >-
                                    The component name. Currently, the only allowable value is
                                    Microsoft-Windows-Shell-Setup.
                            returned: always
                            type: constant
                            sample: null
                        setting_name:
                            description:
                                - >-
                                    Specifies the name of the setting to which the content
                                    applies. Possible values are: FirstLogonCommands and
                                    AutoLogon.
                            returned: always
                            type: sealed-choice
                            sample: null
                        content:
                            description:
                                - >-
                                    Specifies the XML formatted content that is added to the
                                    unattend.xml file for the specified path and component. The
                                    XML must be less than 4KB and must include the root element
                                    for the setting or feature that is being inserted.
                            returned: always
                            type: str
                            sample: null
                patch_settings:
                    description:
                        - Specifies settings related to in-guest patching (KBs).
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        patch_mode:
                            description:
                                - >-
                                    Specifies the mode of in-guest patching to IaaS virtual
                                    machine.:code:`<br />`:code:`<br />` Possible values
                                    are::code:`<br />`:code:`<br />` **Manual** - You  control the
                                    application of patches to a virtual machine. You do this by
                                    applying patches manually inside the VM. In this mode,
                                    automatic updates are disabled; the property
                                    WindowsConfiguration.enableAutomaticUpdates must be
                                    false:code:`<br />`:code:`<br />` **AutomaticByOS** - The
                                    virtual machine will automatically be updated by the OS. The
                                    property WindowsConfiguration.enableAutomaticUpdates must be
                                    true. :code:`<br />`:code:`<br />` ** AutomaticByPlatform** -
                                    the virtual machine will automatically updated by the
                                    platform. The properties provisionVMAgent and
                                    WindowsConfiguration.enableAutomaticUpdates must be true
                            returned: always
                            type: str
                            sample: null
                win_rm:
                    description:
                        - >-
                            Specifies the Windows Remote Management listeners. This enables
                            remote Windows PowerShell.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        listeners:
                            description:
                                - The list of Windows Remote Management listeners
                            returned: always
                            type: list
                            sample: null
                            contains:
                                protocol:
                                    description:
                                        - >-
                                            Specifies the protocol of WinRM listener.
                                            :code:`<br>`:code:`<br>` Possible values are:
                                            :code:`<br>`\ **http** :code:`<br>`:code:`<br>` **https**
                                    returned: always
                                    type: sealed-choice
                                    sample: null
                                certificate_url:
                                    description:
                                        - >-
                                            This is the URL of a certificate that has been uploaded to
                                            Key Vault as a secret. For adding a secret to the Key
                                            Vault, see `Add a key or secret to the key vault
                                            <https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add>`_.
                                            In this case, your certificate needs to be It is the
                                            Base64 encoding of the following JSON Object which is
                                            encoded in UTF-8: :code:`<br>`:code:`<br>` {:code:`<br>` 
                                            "data":":code:`<Base64-encoded-certificate>`",:code:`<br>` 
                                            "dataType":"pfx",:code:`<br>` 
                                            "password":":code:`<pfx-file-password>`":code:`<br>`}
                                    returned: always
                                    type: str
                                    sample: null
        linux_configuration:
            description:
                - >-
                    Specifies the Linux operating system settings on the virtual machine.
                    :code:`<br>`:code:`<br>`For a list of supported Linux distributions,
                    see `Linux on Azure-Endorsed Distributions
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-endorsed-distros?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                    :code:`<br>`:code:`<br>` For running non-endorsed distributions, see
                    `Information for Non-Endorsed Distributions
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-create-upload-generic?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
            returned: always
            type: dict
            sample: null
            contains:
                disable_password_authentication:
                    description:
                        - Specifies whether password authentication should be disabled.
                    returned: always
                    type: bool
                    sample: null
                ssh:
                    description:
                        - Specifies the ssh key configuration for a Linux OS.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        public_keys:
                            description:
                                - >-
                                    The list of SSH public keys used to authenticate with linux
                                    based VMs.
                            returned: always
                            type: list
                            sample: null
                            contains:
                                path:
                                    description:
                                        - >-
                                            Specifies the full path on the created VM where ssh public
                                            key is stored. If the file already exists, the specified
                                            key is appended to the file. Example:
                                            /home/user/.ssh/authorized_keys
                                    returned: always
                                    type: str
                                    sample: null
                                key_data:
                                    description:
                                        - >-
                                            SSH public key certificate used to authenticate with the
                                            VM through ssh. The key needs to be at least 2048-bit and
                                            in ssh-rsa format. :code:`<br>`:code:`<br>` For creating
                                            ssh keys, see `Create SSH keys on Linux and Mac for Linux
                                            VMs in Azure
                                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-mac-create-ssh-keys?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
                                    returned: always
                                    type: str
                                    sample: null
                provision_vm_agent:
                    description:
                        - >-
                            Indicates whether virtual machine agent should be provisioned on
                            the virtual machine. :code:`<br>`:code:`<br>` When this property
                            is not specified in the request body, default behavior is to set
                            it to true.  This will ensure that VM Agent is installed on the VM
                            so that extensions can be added to the VM later.
                    returned: always
                    type: bool
                    sample: null
        secrets:
            description:
                - >-
                    Specifies set of certificates that should be installed onto the
                    virtual machine.
            returned: always
            type: list
            sample: null
            contains:
                source_vault:
                    description:
                        - >-
                            The relative URL of the Key Vault containing all of the
                            certificates in VaultCertificates.
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
                vault_certificates:
                    description:
                        - >-
                            The list of key vault references in SourceVault which contain
                            certificates.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        certificate_url:
                            description:
                                - >-
                                    This is the URL of a certificate that has been uploaded to Key
                                    Vault as a secret. For adding a secret to the Key Vault, see
                                    `Add a key or secret to the key vault
                                    <https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add>`_.
                                    In this case, your certificate needs to be It is the Base64
                                    encoding of the following JSON Object which is encoded in
                                    UTF-8: :code:`<br>`:code:`<br>` {:code:`<br>` 
                                    "data":":code:`<Base64-encoded-certificate>`",:code:`<br>` 
                                    "dataType":"pfx",:code:`<br>` 
                                    "password":":code:`<pfx-file-password>`":code:`<br>`}
                            returned: always
                            type: str
                            sample: null
                        certificate_store:
                            description:
                                - >-
                                    For Windows VMs, specifies the certificate store on the
                                    Virtual Machine to which the certificate should be added. The
                                    specified certificate store is implicitly in the LocalMachine
                                    account. :code:`<br>`:code:`<br>`For Linux VMs, the
                                    certificate file is placed under the /var/lib/waagent
                                    directory, with the file name &lt;UppercaseThumbprint&gt;.crt
                                    for the X509 certificate file and
                                    &lt;UppercaseThumbprint&gt;.prv for private key. Both of these
                                    files are .pem formatted.
                            returned: always
                            type: str
                            sample: null
        allow_extension_operations:
            description:
                - >-
                    Specifies whether extension operations should be allowed on the
                    virtual machine. :code:`<br>`:code:`<br>`This may only be set to False
                    when no extensions are present on the virtual machine.
            returned: always
            type: bool
            sample: null
        require_guest_provision_signal:
            description:
                - >-
                    Specifies whether the guest provision signal is required to infer
                    provision success of the virtual machine.  **Note: This property is
                    for private testing only, and all customers must not set the property
                    to false.**
            returned: always
            type: bool
            sample: null
network_profile:
    description:
        - Specifies the network interfaces of the virtual machine.
    returned: always
    type: dict
    sample: null
    contains:
        network_interfaces:
            description:
                - >-
                    Specifies the list of resource Ids for the network interfaces
                    associated with the virtual machine.
            returned: always
            type: list
            sample: null
            contains:
                primary:
                    description:
                        - >-
                            Specifies the primary network interface in case the virtual
                            machine has more than 1 network interface.
                    returned: always
                    type: bool
                    sample: null
security_profile:
    description:
        - Specifies the Security related profile settings for the virtual machine.
    returned: always
    type: dict
    sample: null
    contains:
        encryption_at_host:
            description:
                - >-
                    This property can be used by user in the request to enable or disable
                    the Host Encryption for the virtual machine or virtual machine scale
                    set. This will enable the encryption for all the disks including
                    Resource/Temp disk at host itself. :code:`<br>`:code:`<br>` Default:
                    The Encryption at host will be disabled unless this property is set to
                    true for the resource.
            returned: always
            type: bool
            sample: null
diagnostics_profile:
    description:
        - >-
            Specifies the boot diagnostic settings state.
            :code:`<br>`:code:`<br>`Minimum api-version: 2015-06-15.
    returned: always
    type: dict
    sample: null
    contains:
        boot_diagnostics:
            description:
                - >-
                    Boot Diagnostics is a debugging feature which allows you to view
                    Console Output and Screenshot to diagnose VM status.
                    :code:`<br>`:code:`<br>` You can easily view the output of your
                    console log. :code:`<br>`:code:`<br>` Azure also enables you to see a
                    screenshot of the VM from the hypervisor.
            returned: always
            type: dict
            sample: null
            contains:
                enabled:
                    description:
                        - Whether boot diagnostics should be enabled on the Virtual Machine.
                    returned: always
                    type: bool
                    sample: null
                storage_uri:
                    description:
                        - >-
                            Uri of the storage account to use for placing the console output
                            and screenshot. :code:`<br>`:code:`<br>`If storageUri is not
                            specified while enabling boot diagnostics, managed storage will be
                            used.
                    returned: always
                    type: str
                    sample: null
availability_set:
    description:
        - >-
            Specifies information about the availability set that the virtual machine
            should be assigned to. Virtual machines specified in the same availability
            set are allocated to different nodes to maximize availability. For more
            information about availability sets, see `Manage the availability of
            virtual machines
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-manage-availability?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
            :code:`<br>`:code:`<br>` For more information on Azure planned
            maintenance, see `Planned maintenance for virtual machines in Azure
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-planned-maintenance?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
            :code:`<br>`:code:`<br>` Currently, a VM can only be added to availability
            set at creation time. The availability set to which the VM is being added
            should be under the same resource group as the availability set resource.
            An existing VM cannot be added to an availability set.
            :code:`<br>`:code:`<br>`This property cannot exist along with a non-null
            properties.virtualMachineScaleSet reference.
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
virtual_machine_scale_set:
    description:
        - >-
            Specifies information about the virtual machine scale set that the virtual
            machine should be assigned to. Virtual machines specified in the same
            virtual machine scale set are allocated to different nodes to maximize
            availability. Currently, a VM can only be added to virtual machine scale
            set at creation time. An existing VM cannot be added to a virtual machine
            scale set. :code:`<br>`:code:`<br>`This property cannot exist along with a
            non-null properties.availabilitySet reference.
            :code:`<br>`:code:`<br>`Minimum api‐version: 2019‐03‐01
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
proximity_placement_group:
    description:
        - >-
            Specifies information about the proximity placement group that the virtual
            machine should be assigned to. :code:`<br>`:code:`<br>`Minimum
            api-version: 2018-04-01.
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
priority:
    description:
        - >-
            Specifies the priority for the virtual machine.
            :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01
    returned: always
    type: str
    sample: null
eviction_policy:
    description:
        - >-
            Specifies the eviction policy for the Azure Spot virtual machine and Azure
            Spot scale set. :code:`<br>`:code:`<br>`For Azure Spot virtual machines,
            both 'Deallocate' and 'Delete' are supported and the minimum api-version
            is 2019-03-01. :code:`<br>`:code:`<br>`For Azure Spot scale sets, both
            'Deallocate' and 'Delete' are supported and the minimum api-version is
            2017-10-30-preview.
    returned: always
    type: str
    sample: null
billing_profile:
    description:
        - >-
            Specifies the billing related details of a Azure Spot virtual machine.
            :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
    returned: always
    type: dict
    sample: null
    contains:
        max_price:
            description:
                - >-
                    Specifies the maximum price you are willing to pay for a Azure Spot
                    VM/VMSS. This price is in US Dollars. :code:`<br>`:code:`<br>` This
                    price will be compared with the current Azure Spot price for the VM
                    size. Also, the prices are compared at the time of create/update of
                    Azure Spot VM/VMSS and the operation will only succeed if  the
                    maxPrice is greater than the current Azure Spot price.
                    :code:`<br>`:code:`<br>` The maxPrice will also be used for evicting a
                    Azure Spot VM/VMSS if the current Azure Spot price goes beyond the
                    maxPrice after creation of VM/VMSS. :code:`<br>`:code:`<br>` Possible
                    values are: :code:`<br>`:code:`<br>` - Any decimal value greater than
                    zero. Example: 0.01538 :code:`<br>`:code:`<br>` -1 – indicates default
                    price to be up-to on-demand. :code:`<br>`:code:`<br>` You can set the
                    maxPrice to -1 to indicate that the Azure Spot VM/VMSS should not be
                    evicted for price reasons. Also, the default max price is -1 if it is
                    not provided by you. :code:`<br>`:code:`<br>`Minimum api-version:
                    2019-03-01.
            returned: always
            type: number
            sample: null
host:
    description:
        - >-
            Specifies information about the dedicated host that the virtual machine
            resides in. :code:`<br>`:code:`<br>`Minimum api-version: 2018-10-01.
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
host_group:
    description:
        - >-
            Specifies information about the dedicated host group that the virtual
            machine resides in. :code:`<br>`:code:`<br>`Minimum api-version:
            2020-06-01. :code:`<br>`:code:`<br>`NOTE: User cannot specify both host
            and hostGroup properties.
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
provisioning_state:
    description:
        - 'The provisioning state, which only appears in the response.'
    returned: always
    type: str
    sample: null
instance_view:
    description:
        - The virtual machine instance view.
    returned: always
    type: dict
    sample: null
    contains:
        platform_update_domain:
            description:
                - Specifies the update domain of the virtual machine.
            returned: always
            type: int
            sample: null
        platform_fault_domain:
            description:
                - Specifies the fault domain of the virtual machine.
            returned: always
            type: int
            sample: null
        computer_name:
            description:
                - The computer name assigned to the virtual machine.
            returned: always
            type: str
            sample: null
        os_name:
            description:
                - The Operating System running on the virtual machine.
            returned: always
            type: str
            sample: null
        os_version:
            description:
                - The version of Operating System running on the virtual machine.
            returned: always
            type: str
            sample: null
        hyper_v_generation:
            description:
                - Specifies the HyperVGeneration Type associated with a resource
            returned: always
            type: str
            sample: null
        rdp_thumb_print:
            description:
                - The Remote desktop certificate thumbprint.
            returned: always
            type: str
            sample: null
        vm_agent:
            description:
                - The VM Agent running on the virtual machine.
            returned: always
            type: dict
            sample: null
            contains:
                vm_agent_version:
                    description:
                        - The VM Agent full version.
                    returned: always
                    type: str
                    sample: null
                extension_handlers:
                    description:
                        - The virtual machine extension handler instance view.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        type:
                            description:
                                - >-
                                    Specifies the type of the extension; an example is
                                    "CustomScriptExtension".
                            returned: always
                            type: str
                            sample: null
                        type_handler_version:
                            description:
                                - Specifies the version of the script handler.
                            returned: always
                            type: str
                            sample: null
                        status:
                            description:
                                - The extension handler status.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    returned: always
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    returned: always
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    returned: always
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    returned: always
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    returned: always
                                    type: str
                                    sample: null
                statuses:
                    description:
                        - The resource status information.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            returned: always
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            returned: always
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            returned: always
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            returned: always
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            returned: always
                            type: str
                            sample: null
        maintenance_redeploy_status:
            description:
                - The Maintenance Operation status on the virtual machine.
            returned: always
            type: dict
            sample: null
            contains:
                is_customer_initiated_maintenance_allowed:
                    description:
                        - 'True, if customer is allowed to perform Maintenance.'
                    returned: always
                    type: bool
                    sample: null
                pre_maintenance_window_start_time:
                    description:
                        - Start Time for the Pre Maintenance Window.
                    returned: always
                    type: str
                    sample: null
                pre_maintenance_window_end_time:
                    description:
                        - End Time for the Pre Maintenance Window.
                    returned: always
                    type: str
                    sample: null
                maintenance_window_start_time:
                    description:
                        - Start Time for the Maintenance Window.
                    returned: always
                    type: str
                    sample: null
                maintenance_window_end_time:
                    description:
                        - End Time for the Maintenance Window.
                    returned: always
                    type: str
                    sample: null
                last_operation_result_code:
                    description:
                        - The Last Maintenance Operation Result Code.
                    returned: always
                    type: sealed-choice
                    sample: null
                last_operation_message:
                    description:
                        - Message returned for the last Maintenance Operation.
                    returned: always
                    type: str
                    sample: null
        disks:
            description:
                - The virtual machine disk information.
            returned: always
            type: list
            sample: null
            contains:
                name:
                    description:
                        - The disk name.
                    returned: always
                    type: str
                    sample: null
                encryption_settings:
                    description:
                        - >-
                            Specifies the encryption settings for the OS Disk.
                            :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
                    returned: always
                    type: list
                    sample: null
                    contains:
                        disk_encryption_key:
                            description:
                                - >-
                                    Specifies the location of the disk encryption key, which is a
                                    Key Vault Secret.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                secret_url:
                                    description:
                                        - The URL referencing a secret in a Key Vault.
                                    returned: always
                                    type: str
                                    sample: null
                                source_vault:
                                    description:
                                        - The relative URL of the Key Vault containing the secret.
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
                        key_encryption_key:
                            description:
                                - Specifies the location of the key encryption key in Key Vault.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                key_url:
                                    description:
                                        - The URL referencing a key encryption key in Key Vault.
                                    returned: always
                                    type: str
                                    sample: null
                                source_vault:
                                    description:
                                        - The relative URL of the Key Vault containing the key.
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
                        enabled:
                            description:
                                - >-
                                    Specifies whether disk encryption should be enabled on the
                                    virtual machine.
                            returned: always
                            type: bool
                            sample: null
                statuses:
                    description:
                        - The resource status information.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            returned: always
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            returned: always
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            returned: always
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            returned: always
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            returned: always
                            type: str
                            sample: null
        extensions:
            description:
                - The extensions information.
            returned: always
            type: list
            sample: null
            contains:
                name:
                    description:
                        - The virtual machine extension name.
                    returned: always
                    type: str
                    sample: null
                type:
                    description:
                        - >-
                            Specifies the type of the extension; an example is
                            "CustomScriptExtension".
                    returned: always
                    type: str
                    sample: null
                type_handler_version:
                    description:
                        - Specifies the version of the script handler.
                    returned: always
                    type: str
                    sample: null
                substatuses:
                    description:
                        - The resource status information.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            returned: always
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            returned: always
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            returned: always
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            returned: always
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            returned: always
                            type: str
                            sample: null
                statuses:
                    description:
                        - The resource status information.
                    returned: always
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            returned: always
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            returned: always
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            returned: always
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            returned: always
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            returned: always
                            type: str
                            sample: null
        vm_health:
            description:
                - The health status for the VM.
            returned: always
            type: dict
            sample: null
            contains:
                status:
                    description:
                        - The health status information for the VM.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            returned: always
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            returned: always
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            returned: always
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            returned: always
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            returned: always
                            type: str
                            sample: null
        boot_diagnostics:
            description:
                - >-
                    Boot Diagnostics is a debugging feature which allows you to view
                    Console Output and Screenshot to diagnose VM status.
                    :code:`<br>`:code:`<br>` You can easily view the output of your
                    console log. :code:`<br>`:code:`<br>` Azure also enables you to see a
                    screenshot of the VM from the hypervisor.
            returned: always
            type: dict
            sample: null
            contains:
                status:
                    description:
                        - >-
                            The boot diagnostics status information for the VM.
                            :code:`<br>`:code:`<br>` NOTE: It will be set only if there are
                            errors encountered in enabling boot diagnostics.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            returned: always
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            returned: always
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            returned: always
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            returned: always
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            returned: always
                            type: str
                            sample: null
        statuses:
            description:
                - The resource status information.
            returned: always
            type: list
            sample: null
            contains:
                code:
                    description:
                        - The status code.
                    returned: always
                    type: str
                    sample: null
                level:
                    description:
                        - The level code.
                    returned: always
                    type: sealed-choice
                    sample: null
                display_status:
                    description:
                        - The short localizable label for the status.
                    returned: always
                    type: str
                    sample: null
                message:
                    description:
                        - >-
                            The detailed status message, including for alerts and error
                            messages.
                    returned: always
                    type: str
                    sample: null
                time:
                    description:
                        - The time of the status.
                    returned: always
                    type: str
                    sample: null
        patch_status:
            description:
                - The status of virtual machine patch operations.
            returned: always
            type: dict
            sample: null
            contains:
                available_patch_summary:
                    description:
                        - >-
                            The available patch summary of the latest assessment operation for
                            the virtual machine.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        error:
                            description:
                                - >-
                                    The errors that were encountered during execution of the
                                    operation. The details array contains the list of them.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                details:
                                    description:
                                        - The Api error details
                                    returned: always
                                    type: list
                                    sample: null
                                    contains:
                                        code:
                                            description:
                                                - The error code.
                                            returned: always
                                            type: str
                                            sample: null
                                        target:
                                            description:
                                                - The target of the particular error.
                                            returned: always
                                            type: str
                                            sample: null
                                        message:
                                            description:
                                                - The error message.
                                            returned: always
                                            type: str
                                            sample: null
                                innererror:
                                    description:
                                        - The Api inner error
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        exceptiontype:
                                            description:
                                                - The exception type.
                                            returned: always
                                            type: str
                                            sample: null
                                        errordetail:
                                            description:
                                                - The internal error message or exception dump.
                                            returned: always
                                            type: str
                                            sample: null
                                code:
                                    description:
                                        - The error code.
                                    returned: always
                                    type: str
                                    sample: null
                                target:
                                    description:
                                        - The target of the particular error.
                                    returned: always
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - The error message.
                                    returned: always
                                    type: str
                                    sample: null
                last_patch_installation_summary:
                    description:
                        - >-
                            The installation summary of the latest installation operation for
                            the virtual machine.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        error:
                            description:
                                - >-
                                    The errors that were encountered during execution of the
                                    operation. The details array contains the list of them.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                details:
                                    description:
                                        - The Api error details
                                    returned: always
                                    type: list
                                    sample: null
                                    contains:
                                        code:
                                            description:
                                                - The error code.
                                            returned: always
                                            type: str
                                            sample: null
                                        target:
                                            description:
                                                - The target of the particular error.
                                            returned: always
                                            type: str
                                            sample: null
                                        message:
                                            description:
                                                - The error message.
                                            returned: always
                                            type: str
                                            sample: null
                                innererror:
                                    description:
                                        - The Api inner error
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        exceptiontype:
                                            description:
                                                - The exception type.
                                            returned: always
                                            type: str
                                            sample: null
                                        errordetail:
                                            description:
                                                - The internal error message or exception dump.
                                            returned: always
                                            type: str
                                            sample: null
                                code:
                                    description:
                                        - The error code.
                                    returned: always
                                    type: str
                                    sample: null
                                target:
                                    description:
                                        - The target of the particular error.
                                    returned: always
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - The error message.
                                    returned: always
                                    type: str
                                    sample: null
license_type:
    description:
        - >-
            Specifies that the image or disk that is being used was licensed
            on-premises. This element is only used for images that contain the Windows
            Server operating system. :code:`<br>`:code:`<br>` Possible values are:
            :code:`<br>`:code:`<br>` Windows_Client :code:`<br>`:code:`<br>`
            Windows_Server :code:`<br>`:code:`<br>` If this element is included in a
            request for an update, the value must match the initial value. This value
            cannot be updated. :code:`<br>`:code:`<br>` For more information, see
            `Azure Hybrid Use Benefit for Windows Server
            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
            :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
    returned: always
    type: str
    sample: null
vm_id:
    description:
        - >-
            Specifies the VM unique ID which is a 128-bits identifier that is encoded
            and stored in all Azure IaaS VMs SMBIOS and can be read using platform
            BIOS commands.
    returned: always
    type: str
    sample: null
extensions_time_budget:
    description:
        - >-
            Specifies the time alloted for all extensions to start. The time duration
            should be between 15 minutes and 120 minutes (inclusive) and should be
            specified in ISO 8601 format. The default value is 90 minutes (PT1H30M).
            :code:`<br>`:code:`<br>` Minimum api-version: 2020-06-01
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


class AzureRMVirtualMachine(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            vm_name=dict(
                type='str',
                required=True
            ),
            plan=dict(
                type='dict',
                disposition='/plan',
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
                    ),
                    promotion_code=dict(
                        type='str',
                        disposition='promotion_code'
                    )
                )
            ),
            resources=dict(
                type='list',
                updatable=False,
                disposition='/resources',
                elements='dict',
                options=dict(
                    force_update_tag=dict(
                        type='str',
                        disposition='force_update_tag'
                    ),
                    publisher=dict(
                        type='str',
                        disposition='publisher'
                    ),
                    type_properties_type=dict(
                        type='str',
                        disposition='type_properties_type'
                    ),
                    type_handler_version=dict(
                        type='str',
                        disposition='type_handler_version'
                    ),
                    auto_upgrade_minor_version=dict(
                        type='bool',
                        disposition='auto_upgrade_minor_version'
                    ),
                    enable_automatic_upgrade=dict(
                        type='bool',
                        disposition='enable_automatic_upgrade'
                    ),
                    settings=dict(
                        type='any',
                        disposition='settings'
                    ),
                    protected_settings=dict(
                        type='any',
                        disposition='protected_settings'
                    ),
                    instance_view=dict(
                        type='dict',
                        disposition='instance_view',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            type=dict(
                                type='str',
                                disposition='type'
                            ),
                            type_handler_version=dict(
                                type='str',
                                disposition='type_handler_version'
                            ),
                            substatuses=dict(
                                type='list',
                                disposition='substatuses',
                                elements='dict',
                                options=dict(
                                    code=dict(
                                        type='str',
                                        disposition='code'
                                    ),
                                    level=dict(
                                        type='sealed-choice',
                                        disposition='level'
                                    ),
                                    display_status=dict(
                                        type='str',
                                        disposition='display_status'
                                    ),
                                    message=dict(
                                        type='str',
                                        disposition='message'
                                    ),
                                    time=dict(
                                        type='str',
                                        disposition='time'
                                    )
                                )
                            ),
                            statuses=dict(
                                type='list',
                                disposition='statuses',
                                elements='dict',
                                options=dict(
                                    code=dict(
                                        type='str',
                                        disposition='code'
                                    ),
                                    level=dict(
                                        type='sealed-choice',
                                        disposition='level'
                                    ),
                                    display_status=dict(
                                        type='str',
                                        disposition='display_status'
                                    ),
                                    message=dict(
                                        type='str',
                                        disposition='message'
                                    ),
                                    time=dict(
                                        type='str',
                                        disposition='time'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            identity=dict(
                type='dict',
                disposition='/identity',
                options=dict(
                    type=dict(
                        type='sealed-choice',
                        disposition='type'
                    ),
                    user_assigned_identities=dict(
                        type='dict',
                        disposition='user_assigned_identities'
                    )
                )
            ),
            zones=dict(
                type='list',
                disposition='/zones',
                elements='str'
            ),
            hardware_profile=dict(
                type='dict',
                disposition='/hardware_profile',
                options=dict(
                    vm_size=dict(
                        type='str',
                        disposition='vm_size',
                        choices=['Basic_A0',
                                 'Basic_A1',
                                 'Basic_A2',
                                 'Basic_A3',
                                 'Basic_A4',
                                 'Standard_A0',
                                 'Standard_A1',
                                 'Standard_A2',
                                 'Standard_A3',
                                 'Standard_A4',
                                 'Standard_A5',
                                 'Standard_A6',
                                 'Standard_A7',
                                 'Standard_A8',
                                 'Standard_A9',
                                 'Standard_A10',
                                 'Standard_A11',
                                 'Standard_A1_v2',
                                 'Standard_A2_v2',
                                 'Standard_A4_v2',
                                 'Standard_A8_v2',
                                 'Standard_A2m_v2',
                                 'Standard_A4m_v2',
                                 'Standard_A8m_v2',
                                 'Standard_B1s',
                                 'Standard_B1ms',
                                 'Standard_B2s',
                                 'Standard_B2ms',
                                 'Standard_B4ms',
                                 'Standard_B8ms',
                                 'Standard_D1',
                                 'Standard_D2',
                                 'Standard_D3',
                                 'Standard_D4',
                                 'Standard_D11',
                                 'Standard_D12',
                                 'Standard_D13',
                                 'Standard_D14',
                                 'Standard_D1_v2',
                                 'Standard_D2_v2',
                                 'Standard_D3_v2',
                                 'Standard_D4_v2',
                                 'Standard_D5_v2',
                                 'Standard_D2_v3',
                                 'Standard_D4_v3',
                                 'Standard_D8_v3',
                                 'Standard_D16_v3',
                                 'Standard_D32_v3',
                                 'Standard_D64_v3',
                                 'Standard_D2s_v3',
                                 'Standard_D4s_v3',
                                 'Standard_D8s_v3',
                                 'Standard_D16s_v3',
                                 'Standard_D32s_v3',
                                 'Standard_D64s_v3',
                                 'Standard_D11_v2',
                                 'Standard_D12_v2',
                                 'Standard_D13_v2',
                                 'Standard_D14_v2',
                                 'Standard_D15_v2',
                                 'Standard_DS1',
                                 'Standard_DS2',
                                 'Standard_DS3',
                                 'Standard_DS4',
                                 'Standard_DS11',
                                 'Standard_DS12',
                                 'Standard_DS13',
                                 'Standard_DS14',
                                 'Standard_DS1_v2',
                                 'Standard_DS2_v2',
                                 'Standard_DS3_v2',
                                 'Standard_DS4_v2',
                                 'Standard_DS5_v2',
                                 'Standard_DS11_v2',
                                 'Standard_DS12_v2',
                                 'Standard_DS13_v2',
                                 'Standard_DS14_v2',
                                 'Standard_DS15_v2',
                                 'Standard_DS13-4_v2',
                                 'Standard_DS13-2_v2',
                                 'Standard_DS14-8_v2',
                                 'Standard_DS14-4_v2',
                                 'Standard_E2_v3',
                                 'Standard_E4_v3',
                                 'Standard_E8_v3',
                                 'Standard_E16_v3',
                                 'Standard_E32_v3',
                                 'Standard_E64_v3',
                                 'Standard_E2s_v3',
                                 'Standard_E4s_v3',
                                 'Standard_E8s_v3',
                                 'Standard_E16s_v3',
                                 'Standard_E32s_v3',
                                 'Standard_E64s_v3',
                                 'Standard_E32-16_v3',
                                 'Standard_E32-8s_v3',
                                 'Standard_E64-32s_v3',
                                 'Standard_E64-16s_v3',
                                 'Standard_F1',
                                 'Standard_F2',
                                 'Standard_F4',
                                 'Standard_F8',
                                 'Standard_F16',
                                 'Standard_F1s',
                                 'Standard_F2s',
                                 'Standard_F4s',
                                 'Standard_F8s',
                                 'Standard_F16s',
                                 'Standard_F2s_v2',
                                 'Standard_F4s_v2',
                                 'Standard_F8s_v2',
                                 'Standard_F16s_v2',
                                 'Standard_F32s_v2',
                                 'Standard_F64s_v2',
                                 'Standard_F72s_v2',
                                 'Standard_G1',
                                 'Standard_G2',
                                 'Standard_G3',
                                 'Standard_G4',
                                 'Standard_G5',
                                 'Standard_GS1',
                                 'Standard_GS2',
                                 'Standard_GS3',
                                 'Standard_GS4',
                                 'Standard_GS5',
                                 'Standard_GS4-8',
                                 'Standard_GS4-4',
                                 'Standard_GS5-16',
                                 'Standard_GS5-8',
                                 'Standard_H8',
                                 'Standard_H16',
                                 'Standard_H8m',
                                 'Standard_H16m',
                                 'Standard_H16r',
                                 'Standard_H16mr',
                                 'Standard_L4s',
                                 'Standard_L8s',
                                 'Standard_L16s',
                                 'Standard_L32s',
                                 'Standard_M64s',
                                 'Standard_M64ms',
                                 'Standard_M128s',
                                 'Standard_M128ms',
                                 'Standard_M64-32ms',
                                 'Standard_M64-16ms',
                                 'Standard_M128-64ms',
                                 'Standard_M128-32ms',
                                 'Standard_NC6',
                                 'Standard_NC12',
                                 'Standard_NC24',
                                 'Standard_NC24r',
                                 'Standard_NC6s_v2',
                                 'Standard_NC12s_v2',
                                 'Standard_NC24s_v2',
                                 'Standard_NC24rs_v2',
                                 'Standard_NC6s_v3',
                                 'Standard_NC12s_v3',
                                 'Standard_NC24s_v3',
                                 'Standard_NC24rs_v3',
                                 'Standard_ND6s',
                                 'Standard_ND12s',
                                 'Standard_ND24s',
                                 'Standard_ND24rs',
                                 'Standard_NV6',
                                 'Standard_NV12',
                                 'Standard_NV24']
                    )
                )
            ),
            storage_profile=dict(
                type='dict',
                disposition='/storage_profile',
                options=dict(
                    image_reference=dict(
                        type='dict',
                        disposition='image_reference',
                        options=dict(
                            publisher=dict(
                                type='str',
                                disposition='publisher'
                            ),
                            offer=dict(
                                type='str',
                                disposition='offer'
                            ),
                            sku=dict(
                                type='str',
                                disposition='sku'
                            ),
                            version=dict(
                                type='str',
                                disposition='version'
                            )
                        )
                    ),
                    os_disk=dict(
                        type='dict',
                        disposition='os_disk',
                        options=dict(
                            os_type=dict(
                                type='sealed-choice',
                                disposition='os_type'
                            ),
                            encryption_settings=dict(
                                type='dict',
                                disposition='encryption_settings',
                                options=dict(
                                    disk_encryption_key=dict(
                                        type='dict',
                                        disposition='disk_encryption_key',
                                        options=dict(
                                            secret_url=dict(
                                                type='str',
                                                disposition='secret_url',
                                                required=True
                                            ),
                                            source_vault=dict(
                                                type='dict',
                                                disposition='source_vault',
                                                required=True,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    key_encryption_key=dict(
                                        type='dict',
                                        disposition='key_encryption_key',
                                        options=dict(
                                            key_url=dict(
                                                type='str',
                                                disposition='key_url',
                                                required=True
                                            ),
                                            source_vault=dict(
                                                type='dict',
                                                disposition='source_vault',
                                                required=True,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    enabled=dict(
                                        type='bool',
                                        disposition='enabled'
                                    )
                                )
                            ),
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            vhd=dict(
                                type='dict',
                                disposition='vhd',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='uri'
                                    )
                                )
                            ),
                            image=dict(
                                type='dict',
                                disposition='image',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='uri'
                                    )
                                )
                            ),
                            caching=dict(
                                type='sealed-choice',
                                disposition='caching'
                            ),
                            write_accelerator_enabled=dict(
                                type='bool',
                                disposition='write_accelerator_enabled'
                            ),
                            diff_disk_settings=dict(
                                type='dict',
                                disposition='diff_disk_settings',
                                options=dict(
                                    option=dict(
                                        type='str',
                                        disposition='option',
                                        choices=['Local']
                                    ),
                                    placement=dict(
                                        type='str',
                                        disposition='placement',
                                        choices=['CacheDisk',
                                                 'ResourceDisk']
                                    )
                                )
                            ),
                            create_option=dict(
                                type='str',
                                disposition='create_option',
                                choices=['FromImage',
                                         'Empty',
                                         'Attach'],
                                required=True
                            ),
                            disk_size_gb=dict(
                                type='int',
                                disposition='disk_size_gb'
                            ),
                            managed_disk=dict(
                                type='dict',
                                disposition='managed_disk',
                                options=dict(
                                    storage_account_type=dict(
                                        type='str',
                                        disposition='storage_account_type',
                                        choices=['Standard_LRS',
                                                 'Premium_LRS',
                                                 'StandardSSD_LRS',
                                                 'UltraSSD_LRS']
                                    ),
                                    disk_encryption_set=dict(
                                        type='dict',
                                        disposition='disk_encryption_set',
                                        options=dict(
                                            id=dict(
                                                type='str',
                                                disposition='id'
                                            )
                                        )
                                    )
                                )
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
                            ),
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            vhd=dict(
                                type='dict',
                                disposition='vhd',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='uri'
                                    )
                                )
                            ),
                            image=dict(
                                type='dict',
                                disposition='image',
                                options=dict(
                                    uri=dict(
                                        type='str',
                                        disposition='uri'
                                    )
                                )
                            ),
                            caching=dict(
                                type='sealed-choice',
                                disposition='caching'
                            ),
                            write_accelerator_enabled=dict(
                                type='bool',
                                disposition='write_accelerator_enabled'
                            ),
                            create_option=dict(
                                type='str',
                                disposition='create_option',
                                choices=['FromImage',
                                         'Empty',
                                         'Attach'],
                                required=True
                            ),
                            disk_size_gb=dict(
                                type='int',
                                disposition='disk_size_gb'
                            ),
                            managed_disk=dict(
                                type='dict',
                                disposition='managed_disk',
                                options=dict(
                                    storage_account_type=dict(
                                        type='str',
                                        disposition='storage_account_type',
                                        choices=['Standard_LRS',
                                                 'Premium_LRS',
                                                 'StandardSSD_LRS',
                                                 'UltraSSD_LRS']
                                    ),
                                    disk_encryption_set=dict(
                                        type='dict',
                                        disposition='disk_encryption_set',
                                        options=dict(
                                            id=dict(
                                                type='str',
                                                disposition='id'
                                            )
                                        )
                                    )
                                )
                            ),
                            to_be_detached=dict(
                                type='bool',
                                disposition='to_be_detached'
                            )
                        )
                    )
                )
            ),
            additional_capabilities=dict(
                type='dict',
                disposition='/additional_capabilities',
                options=dict(
                    ultra_ssd_enabled=dict(
                        type='bool',
                        disposition='ultra_ssd_enabled'
                    )
                )
            ),
            os_profile=dict(
                type='dict',
                disposition='/os_profile',
                options=dict(
                    computer_name=dict(
                        type='str',
                        disposition='computer_name'
                    ),
                    admin_username=dict(
                        type='str',
                        disposition='admin_username'
                    ),
                    admin_password=dict(
                        type='str',
                        disposition='admin_password'
                    ),
                    custom_data=dict(
                        type='str',
                        disposition='custom_data'
                    ),
                    windows_configuration=dict(
                        type='dict',
                        disposition='windows_configuration',
                        options=dict(
                            provision_vm_agent=dict(
                                type='bool',
                                disposition='provision_vm_agent'
                            ),
                            enable_automatic_updates=dict(
                                type='bool',
                                disposition='enable_automatic_updates'
                            ),
                            time_zone=dict(
                                type='str',
                                disposition='time_zone'
                            ),
                            additional_unattend_content=dict(
                                type='list',
                                disposition='additional_unattend_content',
                                elements='dict',
                                options=dict(
                                    pass_name=dict(
                                        type='constant',
                                        disposition='pass_name'
                                    ),
                                    component_name=dict(
                                        type='constant',
                                        disposition='component_name'
                                    ),
                                    setting_name=dict(
                                        type='sealed-choice',
                                        disposition='setting_name'
                                    ),
                                    content=dict(
                                        type='str',
                                        disposition='content'
                                    )
                                )
                            ),
                            patch_settings=dict(
                                type='dict',
                                disposition='patch_settings',
                                options=dict(
                                    patch_mode=dict(
                                        type='str',
                                        disposition='patch_mode',
                                        choices=['Manual',
                                                 'AutomaticByOS',
                                                 'AutomaticByPlatform']
                                    )
                                )
                            ),
                            win_rm=dict(
                                type='dict',
                                disposition='win_rm',
                                options=dict(
                                    listeners=dict(
                                        type='list',
                                        disposition='listeners',
                                        elements='dict',
                                        options=dict(
                                            protocol=dict(
                                                type='sealed-choice',
                                                disposition='protocol'
                                            ),
                                            certificate_url=dict(
                                                type='str',
                                                disposition='certificate_url'
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    linux_configuration=dict(
                        type='dict',
                        disposition='linux_configuration',
                        options=dict(
                            disable_password_authentication=dict(
                                type='bool',
                                disposition='disable_password_authentication'
                            ),
                            ssh=dict(
                                type='dict',
                                disposition='ssh',
                                options=dict(
                                    public_keys=dict(
                                        type='list',
                                        disposition='public_keys',
                                        elements='dict',
                                        options=dict(
                                            path=dict(
                                                type='str',
                                                disposition='path'
                                            ),
                                            key_data=dict(
                                                type='str',
                                                disposition='key_data'
                                            )
                                        )
                                    )
                                )
                            ),
                            provision_vm_agent=dict(
                                type='bool',
                                disposition='provision_vm_agent'
                            )
                        )
                    ),
                    secrets=dict(
                        type='list',
                        disposition='secrets',
                        elements='dict',
                        options=dict(
                            source_vault=dict(
                                type='dict',
                                disposition='source_vault',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            vault_certificates=dict(
                                type='list',
                                disposition='vault_certificates',
                                elements='dict',
                                options=dict(
                                    certificate_url=dict(
                                        type='str',
                                        disposition='certificate_url'
                                    ),
                                    certificate_store=dict(
                                        type='str',
                                        disposition='certificate_store'
                                    )
                                )
                            )
                        )
                    ),
                    allow_extension_operations=dict(
                        type='bool',
                        disposition='allow_extension_operations'
                    ),
                    require_guest_provision_signal=dict(
                        type='bool',
                        disposition='require_guest_provision_signal'
                    )
                )
            ),
            network_profile=dict(
                type='dict',
                disposition='/network_profile',
                options=dict(
                    network_interfaces=dict(
                        type='list',
                        disposition='network_interfaces',
                        elements='dict',
                        options=dict(
                            primary=dict(
                                type='bool',
                                disposition='primary'
                            )
                        )
                    )
                )
            ),
            security_profile=dict(
                type='dict',
                disposition='/security_profile',
                options=dict(
                    encryption_at_host=dict(
                        type='bool',
                        disposition='encryption_at_host'
                    )
                )
            ),
            diagnostics_profile=dict(
                type='dict',
                disposition='/diagnostics_profile',
                options=dict(
                    boot_diagnostics=dict(
                        type='dict',
                        disposition='boot_diagnostics',
                        options=dict(
                            enabled=dict(
                                type='bool',
                                disposition='enabled'
                            ),
                            storage_uri=dict(
                                type='str',
                                disposition='storage_uri'
                            )
                        )
                    )
                )
            ),
            availability_set=dict(
                type='dict',
                disposition='/availability_set',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            virtual_machine_scale_set=dict(
                type='dict',
                disposition='/virtual_machine_scale_set',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            proximity_placement_group=dict(
                type='dict',
                disposition='/proximity_placement_group',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            priority=dict(
                type='str',
                disposition='/priority',
                choices=['Regular',
                         'Low',
                         'Spot']
            ),
            eviction_policy=dict(
                type='str',
                disposition='/eviction_policy',
                choices=['Deallocate',
                         'Delete']
            ),
            billing_profile=dict(
                type='dict',
                disposition='/billing_profile',
                options=dict(
                    max_price=dict(
                        type='number',
                        disposition='max_price'
                    )
                )
            ),
            host=dict(
                type='dict',
                disposition='/host',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            host_group=dict(
                type='dict',
                disposition='/host_group',
                options=dict(
                    id=dict(
                        type='str',
                        disposition='id'
                    )
                )
            ),
            instance_view=dict(
                type='dict',
                updatable=False,
                disposition='/instance_view',
                options=dict(
                    platform_update_domain=dict(
                        type='int',
                        disposition='platform_update_domain'
                    ),
                    platform_fault_domain=dict(
                        type='int',
                        disposition='platform_fault_domain'
                    ),
                    computer_name=dict(
                        type='str',
                        disposition='computer_name'
                    ),
                    os_name=dict(
                        type='str',
                        disposition='os_name'
                    ),
                    os_version=dict(
                        type='str',
                        disposition='os_version'
                    ),
                    hyper_v_generation=dict(
                        type='str',
                        disposition='hyper_v_generation',
                        choices=['V1',
                                 'V2']
                    ),
                    rdp_thumb_print=dict(
                        type='str',
                        disposition='rdp_thumb_print'
                    ),
                    vm_agent=dict(
                        type='dict',
                        disposition='vm_agent',
                        options=dict(
                            vm_agent_version=dict(
                                type='str',
                                disposition='vm_agent_version'
                            ),
                            extension_handlers=dict(
                                type='list',
                                disposition='extension_handlers',
                                elements='dict',
                                options=dict(
                                    type=dict(
                                        type='str',
                                        disposition='type'
                                    ),
                                    type_handler_version=dict(
                                        type='str',
                                        disposition='type_handler_version'
                                    ),
                                    status=dict(
                                        type='dict',
                                        disposition='status',
                                        options=dict(
                                            code=dict(
                                                type='str',
                                                disposition='code'
                                            ),
                                            level=dict(
                                                type='sealed-choice',
                                                disposition='level'
                                            ),
                                            display_status=dict(
                                                type='str',
                                                disposition='display_status'
                                            ),
                                            message=dict(
                                                type='str',
                                                disposition='message'
                                            ),
                                            time=dict(
                                                type='str',
                                                disposition='time'
                                            )
                                        )
                                    )
                                )
                            ),
                            statuses=dict(
                                type='list',
                                disposition='statuses',
                                elements='dict',
                                options=dict(
                                    code=dict(
                                        type='str',
                                        disposition='code'
                                    ),
                                    level=dict(
                                        type='sealed-choice',
                                        disposition='level'
                                    ),
                                    display_status=dict(
                                        type='str',
                                        disposition='display_status'
                                    ),
                                    message=dict(
                                        type='str',
                                        disposition='message'
                                    ),
                                    time=dict(
                                        type='str',
                                        disposition='time'
                                    )
                                )
                            )
                        )
                    ),
                    maintenance_redeploy_status=dict(
                        type='dict',
                        disposition='maintenance_redeploy_status',
                        options=dict(
                            is_customer_initiated_maintenance_allowed=dict(
                                type='bool',
                                disposition='is_customer_initiated_maintenance_allowed'
                            ),
                            pre_maintenance_window_start_time=dict(
                                type='str',
                                disposition='pre_maintenance_window_start_time'
                            ),
                            pre_maintenance_window_end_time=dict(
                                type='str',
                                disposition='pre_maintenance_window_end_time'
                            ),
                            maintenance_window_start_time=dict(
                                type='str',
                                disposition='maintenance_window_start_time'
                            ),
                            maintenance_window_end_time=dict(
                                type='str',
                                disposition='maintenance_window_end_time'
                            ),
                            last_operation_result_code=dict(
                                type='sealed-choice',
                                disposition='last_operation_result_code'
                            ),
                            last_operation_message=dict(
                                type='str',
                                disposition='last_operation_message'
                            )
                        )
                    ),
                    disks=dict(
                        type='list',
                        disposition='disks',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            encryption_settings=dict(
                                type='list',
                                disposition='encryption_settings',
                                elements='dict',
                                options=dict(
                                    disk_encryption_key=dict(
                                        type='dict',
                                        disposition='disk_encryption_key',
                                        options=dict(
                                            secret_url=dict(
                                                type='str',
                                                disposition='secret_url',
                                                required=True
                                            ),
                                            source_vault=dict(
                                                type='dict',
                                                disposition='source_vault',
                                                required=True,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    key_encryption_key=dict(
                                        type='dict',
                                        disposition='key_encryption_key',
                                        options=dict(
                                            key_url=dict(
                                                type='str',
                                                disposition='key_url',
                                                required=True
                                            ),
                                            source_vault=dict(
                                                type='dict',
                                                disposition='source_vault',
                                                required=True,
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    enabled=dict(
                                        type='bool',
                                        disposition='enabled'
                                    )
                                )
                            ),
                            statuses=dict(
                                type='list',
                                disposition='statuses',
                                elements='dict',
                                options=dict(
                                    code=dict(
                                        type='str',
                                        disposition='code'
                                    ),
                                    level=dict(
                                        type='sealed-choice',
                                        disposition='level'
                                    ),
                                    display_status=dict(
                                        type='str',
                                        disposition='display_status'
                                    ),
                                    message=dict(
                                        type='str',
                                        disposition='message'
                                    ),
                                    time=dict(
                                        type='str',
                                        disposition='time'
                                    )
                                )
                            )
                        )
                    ),
                    extensions=dict(
                        type='list',
                        disposition='extensions',
                        elements='dict',
                        options=dict(
                            name=dict(
                                type='str',
                                disposition='name'
                            ),
                            type=dict(
                                type='str',
                                disposition='type'
                            ),
                            type_handler_version=dict(
                                type='str',
                                disposition='type_handler_version'
                            ),
                            substatuses=dict(
                                type='list',
                                disposition='substatuses',
                                elements='dict',
                                options=dict(
                                    code=dict(
                                        type='str',
                                        disposition='code'
                                    ),
                                    level=dict(
                                        type='sealed-choice',
                                        disposition='level'
                                    ),
                                    display_status=dict(
                                        type='str',
                                        disposition='display_status'
                                    ),
                                    message=dict(
                                        type='str',
                                        disposition='message'
                                    ),
                                    time=dict(
                                        type='str',
                                        disposition='time'
                                    )
                                )
                            ),
                            statuses=dict(
                                type='list',
                                disposition='statuses',
                                elements='dict',
                                options=dict(
                                    code=dict(
                                        type='str',
                                        disposition='code'
                                    ),
                                    level=dict(
                                        type='sealed-choice',
                                        disposition='level'
                                    ),
                                    display_status=dict(
                                        type='str',
                                        disposition='display_status'
                                    ),
                                    message=dict(
                                        type='str',
                                        disposition='message'
                                    ),
                                    time=dict(
                                        type='str',
                                        disposition='time'
                                    )
                                )
                            )
                        )
                    ),
                    vm_health=dict(
                        type='dict',
                        updatable=False,
                        disposition='vm_health',
                        options=dict(
                            status=dict(
                                type='dict',
                                updatable=False,
                                disposition='status',
                                options=dict(
                                    code=dict(
                                        type='str',
                                        disposition='code'
                                    ),
                                    level=dict(
                                        type='sealed-choice',
                                        disposition='level'
                                    ),
                                    display_status=dict(
                                        type='str',
                                        disposition='display_status'
                                    ),
                                    message=dict(
                                        type='str',
                                        disposition='message'
                                    ),
                                    time=dict(
                                        type='str',
                                        disposition='time'
                                    )
                                )
                            )
                        )
                    ),
                    boot_diagnostics=dict(
                        type='dict',
                        disposition='boot_diagnostics',
                        options=dict(
                            status=dict(
                                type='dict',
                                updatable=False,
                                disposition='status',
                                options=dict(
                                    code=dict(
                                        type='str',
                                        disposition='code'
                                    ),
                                    level=dict(
                                        type='sealed-choice',
                                        disposition='level'
                                    ),
                                    display_status=dict(
                                        type='str',
                                        disposition='display_status'
                                    ),
                                    message=dict(
                                        type='str',
                                        disposition='message'
                                    ),
                                    time=dict(
                                        type='str',
                                        disposition='time'
                                    )
                                )
                            )
                        )
                    ),
                    statuses=dict(
                        type='list',
                        disposition='statuses',
                        elements='dict',
                        options=dict(
                            code=dict(
                                type='str',
                                disposition='code'
                            ),
                            level=dict(
                                type='sealed-choice',
                                disposition='level'
                            ),
                            display_status=dict(
                                type='str',
                                disposition='display_status'
                            ),
                            message=dict(
                                type='str',
                                disposition='message'
                            ),
                            time=dict(
                                type='str',
                                disposition='time'
                            )
                        )
                    ),
                    patch_status=dict(
                        type='dict',
                        disposition='patch_status',
                        options=dict(
                            available_patch_summary=dict(
                                type='dict',
                                disposition='available_patch_summary',
                                options=dict(
                                    error=dict(
                                        type='dict',
                                        updatable=False,
                                        disposition='error',
                                        options=dict(
                                            details=dict(
                                                type='list',
                                                disposition='details',
                                                elements='dict',
                                                options=dict(
                                                    code=dict(
                                                        type='str',
                                                        disposition='code'
                                                    ),
                                                    target=dict(
                                                        type='str',
                                                        disposition='target'
                                                    ),
                                                    message=dict(
                                                        type='str',
                                                        disposition='message'
                                                    )
                                                )
                                            ),
                                            innererror=dict(
                                                type='dict',
                                                disposition='innererror',
                                                options=dict(
                                                    exceptiontype=dict(
                                                        type='str',
                                                        disposition='exceptiontype'
                                                    ),
                                                    errordetail=dict(
                                                        type='str',
                                                        disposition='errordetail'
                                                    )
                                                )
                                            ),
                                            code=dict(
                                                type='str',
                                                disposition='code'
                                            ),
                                            target=dict(
                                                type='str',
                                                disposition='target'
                                            ),
                                            message=dict(
                                                type='str',
                                                disposition='message'
                                            )
                                        )
                                    )
                                )
                            ),
                            last_patch_installation_summary=dict(
                                type='dict',
                                disposition='last_patch_installation_summary',
                                options=dict(
                                    error=dict(
                                        type='dict',
                                        updatable=False,
                                        disposition='error',
                                        options=dict(
                                            details=dict(
                                                type='list',
                                                disposition='details',
                                                elements='dict',
                                                options=dict(
                                                    code=dict(
                                                        type='str',
                                                        disposition='code'
                                                    ),
                                                    target=dict(
                                                        type='str',
                                                        disposition='target'
                                                    ),
                                                    message=dict(
                                                        type='str',
                                                        disposition='message'
                                                    )
                                                )
                                            ),
                                            innererror=dict(
                                                type='dict',
                                                disposition='innererror',
                                                options=dict(
                                                    exceptiontype=dict(
                                                        type='str',
                                                        disposition='exceptiontype'
                                                    ),
                                                    errordetail=dict(
                                                        type='str',
                                                        disposition='errordetail'
                                                    )
                                                )
                                            ),
                                            code=dict(
                                                type='str',
                                                disposition='code'
                                            ),
                                            target=dict(
                                                type='str',
                                                disposition='target'
                                            ),
                                            message=dict(
                                                type='str',
                                                disposition='message'
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            license_type=dict(
                type='str',
                disposition='/license_type'
            ),
            extensions_time_budget=dict(
                type='str',
                disposition='/extensions_time_budget'
            ),
            force_deletion=dict(
                type='bool'
            ),
            expand=dict(
                type='constant'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.vm_name = None
        self.force_deletion = None
        self.expand = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachine, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            self.result['state'] = response

        return self.results

    def create_update_resource(self):
        try:
            response = self.mgmt_client.virtual_machines.create_or_update(resource_group=self.resource_group,
                                                                          vm_name=self.vm_name,
                                                                          parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachine instance.')
            self.fail('Error creating the VirtualMachine instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machines.delete(resource_group=self.resource_group,
                                                                vm_name=self.vm_name,
                                                                force_deletion=self.force_deletion)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachine instance.')
            self.fail('Error deleting the VirtualMachine instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_machines.get(resource_group=self.resource_group,
                                                             vm_name=self.vm_name,
                                                             expand=self.expand)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachine()


if __name__ == '__main__':
    main()
