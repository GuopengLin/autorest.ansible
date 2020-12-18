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
module: azure_rm_virtualmachinescalesetvm_info
version_added: '2.9'
short_description: Get VirtualMachineScaleSetVM info.
description:
    - Get info of VirtualMachineScaleSetVM.
options:
    resource_group:
        description:
            - The name of the resource group.
        required: true
        type: str
    vm_scale_set_name:
        description:
            - The name of the VM scale set.
        type: str
    instance_id:
        description:
            - The instance ID of the virtual machine.
        type: str
    expand:
        description:
            - The expand expression to apply on the operation.
            - >-
                The expand expression to apply to the operation. Allowed values are
                'instanceView'.
        type: constant
    virtual_machine_scale_set_name:
        description:
            - The name of the VM scale set.
        type: str
    filter:
        description:
            - >-
                The filter to apply to the operation. Allowed values are
                'startswith(instanceView/statuses/code, 'PowerState') eq true',
                'properties/latestModelApplied eq true', 'properties/latestModelApplied
                eq false'.
        type: str
    select:
        description:
            - >-
                The list parameters. Allowed values are 'instanceView',
                'instanceView/statuses'.
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get instance view of a virtual machine from a VM scale set placed on a dedicated host group through automatic placement.
      azure_rm_virtualmachinescalesetvm_info: 
        instance_id: '0'
        resource_group_name: myResourceGroup
        vm_scale_set_name: myVirtualMachineScaleSet

'''

RETURN = '''
virtual_machine_scale_set_vms:
    description: >-
        A list of dict results where the key is the name of the
        VirtualMachineScaleSetVM and the values are the facts for that
        VirtualMachineScaleSetVM.
    returned: always
    type: complex
    contains:
        id:
            description:
                - Resource Id
            type: str
            sample: null
        name:
            description:
                - Resource name
            type: str
            sample: null
        type:
            description:
                - Resource type
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
            type: dict
            sample: null
        instance_id:
            description:
                - The virtual machine instance ID.
            type: str
            sample: null
        sku:
            description:
                - The virtual machine SKU.
            type: dict
            sample: null
            contains:
                name:
                    description:
                        - The sku name.
                    type: str
                    sample: null
                tier:
                    description:
                        - >-
                            Specifies the tier of virtual machines in a scale set.:code:`<br
                            />`:code:`<br />` Possible Values::code:`<br />`:code:`<br />`
                            **Standard**\ :code:`<br />`:code:`<br />` **Basic**
                    type: str
                    sample: null
                capacity:
                    description:
                        - Specifies the number of virtual machines in the scale set.
                    type: int
                    sample: null
        plan:
            description:
                - >-
                    Specifies information about the marketplace image used to create the
                    virtual machine. This element is only used for marketplace images.
                    Before you can use a marketplace image from an API, you must enable
                    the image for programmatic use.  In the Azure portal, find the
                    marketplace image that you want to use and then click **Want to deploy
                    programmatically, Get Started ->**. Enter any required information and
                    then click **Save**.
            type: dict
            sample: null
            contains:
                name:
                    description:
                        - The plan ID.
                    type: str
                    sample: null
                publisher:
                    description:
                        - The publisher ID.
                    type: str
                    sample: null
                product:
                    description:
                        - >-
                            Specifies the product of the image from the marketplace. This is
                            the same value as Offer under the imageReference element.
                    type: str
                    sample: null
                promotion_code:
                    description:
                        - The promotion code.
                    type: str
                    sample: null
        resources:
            description:
                - The virtual machine child extension resources.
            type: list
            sample: null
            contains:
                force_update_tag:
                    description:
                        - >-
                            How the extension handler should be forced to update even if the
                            extension configuration has not changed.
                    type: str
                    sample: null
                publisher:
                    description:
                        - The name of the extension handler publisher.
                    type: str
                    sample: null
                type_properties_type:
                    description:
                        - >-
                            Specifies the type of the extension; an example is
                            "CustomScriptExtension".
                    type: str
                    sample: null
                type_handler_version:
                    description:
                        - Specifies the version of the script handler.
                    type: str
                    sample: null
                auto_upgrade_minor_version:
                    description:
                        - >-
                            Indicates whether the extension should use a newer minor version
                            if one is available at deployment time. Once deployed, however,
                            the extension will not upgrade minor versions unless redeployed,
                            even with this property set to true.
                    type: bool
                    sample: null
                enable_automatic_upgrade:
                    description:
                        - >-
                            Indicates whether the extension should be automatically upgraded
                            by the platform if there is a newer version of the extension
                            available.
                    type: bool
                    sample: null
                settings:
                    description:
                        - Json formatted public settings for the extension.
                    type: any
                    sample: null
                protected_settings:
                    description:
                        - >-
                            The extension can contain either protectedSettings or
                            protectedSettingsFromKeyVault or no protected settings at all.
                    type: any
                    sample: null
                instance_view:
                    description:
                        - The virtual machine extension instance view.
                    type: dict
                    sample: null
                    contains:
                        name:
                            description:
                                - The virtual machine extension name.
                            type: str
                            sample: null
                        type:
                            description:
                                - >-
                                    Specifies the type of the extension; an example is
                                    "CustomScriptExtension".
                            type: str
                            sample: null
                        type_handler_version:
                            description:
                                - Specifies the version of the script handler.
                            type: str
                            sample: null
                        substatuses:
                            description:
                                - The resource status information.
                            type: list
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null
                        statuses:
                            description:
                                - The resource status information.
                            type: list
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null
        zones:
            description:
                - The virtual machine zones.
            type: list
            sample: null
        latest_model_applied:
            description:
                - >-
                    Specifies whether the latest model has been applied to the virtual
                    machine.
            type: bool
            sample: null
        vm_id:
            description:
                - Azure VM unique ID.
            type: str
            sample: null
        instance_view:
            description:
                - The virtual machine instance view.
            type: dict
            sample: null
            contains:
                platform_update_domain:
                    description:
                        - The Update Domain count.
                    type: int
                    sample: null
                platform_fault_domain:
                    description:
                        - The Fault Domain count.
                    type: int
                    sample: null
                rdp_thumb_print:
                    description:
                        - The Remote desktop certificate thumbprint.
                    type: str
                    sample: null
                vm_agent:
                    description:
                        - The VM Agent running on the virtual machine.
                    type: dict
                    sample: null
                    contains:
                        vm_agent_version:
                            description:
                                - The VM Agent full version.
                            type: str
                            sample: null
                        extension_handlers:
                            description:
                                - The virtual machine extension handler instance view.
                            type: list
                            sample: null
                            contains:
                                type:
                                    description:
                                        - >-
                                            Specifies the type of the extension; an example is
                                            "CustomScriptExtension".
                                    type: str
                                    sample: null
                                type_handler_version:
                                    description:
                                        - Specifies the version of the script handler.
                                    type: str
                                    sample: null
                                status:
                                    description:
                                        - The extension handler status.
                                    type: dict
                                    sample: null
                                    contains:
                                        code:
                                            description:
                                                - The status code.
                                            type: str
                                            sample: null
                                        level:
                                            description:
                                                - The level code.
                                            type: sealed-choice
                                            sample: null
                                        display_status:
                                            description:
                                                - The short localizable label for the status.
                                            type: str
                                            sample: null
                                        message:
                                            description:
                                                - >-
                                                    The detailed status message, including for alerts and
                                                    error messages.
                                            type: str
                                            sample: null
                                        time:
                                            description:
                                                - The time of the status.
                                            type: str
                                            sample: null
                        statuses:
                            description:
                                - The resource status information.
                            type: list
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null
                maintenance_redeploy_status:
                    description:
                        - The Maintenance Operation status on the virtual machine.
                    type: dict
                    sample: null
                    contains:
                        is_customer_initiated_maintenance_allowed:
                            description:
                                - 'True, if customer is allowed to perform Maintenance.'
                            type: bool
                            sample: null
                        pre_maintenance_window_start_time:
                            description:
                                - Start Time for the Pre Maintenance Window.
                            type: str
                            sample: null
                        pre_maintenance_window_end_time:
                            description:
                                - End Time for the Pre Maintenance Window.
                            type: str
                            sample: null
                        maintenance_window_start_time:
                            description:
                                - Start Time for the Maintenance Window.
                            type: str
                            sample: null
                        maintenance_window_end_time:
                            description:
                                - End Time for the Maintenance Window.
                            type: str
                            sample: null
                        last_operation_result_code:
                            description:
                                - The Last Maintenance Operation Result Code.
                            type: sealed-choice
                            sample: null
                        last_operation_message:
                            description:
                                - Message returned for the last Maintenance Operation.
                            type: str
                            sample: null
                disks:
                    description:
                        - The disks information.
                    type: list
                    sample: null
                    contains:
                        name:
                            description:
                                - The disk name.
                            type: str
                            sample: null
                        encryption_settings:
                            description:
                                - >-
                                    Specifies the encryption settings for the OS Disk.
                                    :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
                            type: list
                            sample: null
                            contains:
                                disk_encryption_key:
                                    description:
                                        - >-
                                            Specifies the location of the disk encryption key, which
                                            is a Key Vault Secret.
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
                                                - >-
                                                    The relative URL of the Key Vault containing the
                                                    secret.
                                            returned: always
                                            type: dict
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    type: str
                                                    sample: null
                                key_encryption_key:
                                    description:
                                        - >-
                                            Specifies the location of the key encryption key in Key
                                            Vault.
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
                                                    type: str
                                                    sample: null
                                enabled:
                                    description:
                                        - >-
                                            Specifies whether disk encryption should be enabled on the
                                            virtual machine.
                                    type: bool
                                    sample: null
                        statuses:
                            description:
                                - The resource status information.
                            type: list
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null
                extensions:
                    description:
                        - The extensions information.
                    type: list
                    sample: null
                    contains:
                        name:
                            description:
                                - The virtual machine extension name.
                            type: str
                            sample: null
                        type:
                            description:
                                - >-
                                    Specifies the type of the extension; an example is
                                    "CustomScriptExtension".
                            type: str
                            sample: null
                        type_handler_version:
                            description:
                                - Specifies the version of the script handler.
                            type: str
                            sample: null
                        substatuses:
                            description:
                                - The resource status information.
                            type: list
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null
                        statuses:
                            description:
                                - The resource status information.
                            type: list
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null
                vm_health:
                    description:
                        - The health status for the VM.
                    type: dict
                    sample: null
                    contains:
                        status:
                            description:
                                - The health status information for the VM.
                            type: dict
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null
                boot_diagnostics:
                    description:
                        - >-
                            Boot Diagnostics is a debugging feature which allows you to view
                            Console Output and Screenshot to diagnose VM status.
                            :code:`<br>`:code:`<br>` You can easily view the output of your
                            console log. :code:`<br>`:code:`<br>` Azure also enables you to
                            see a screenshot of the VM from the hypervisor.
                    type: dict
                    sample: null
                    contains:
                        status:
                            description:
                                - >-
                                    The boot diagnostics status information for the VM.
                                    :code:`<br>`:code:`<br>` NOTE: It will be set only if there
                                    are errors encountered in enabling boot diagnostics.
                            type: dict
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null
                statuses:
                    description:
                        - The resource status information.
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            type: str
                            sample: null
                placement_group_id:
                    description:
                        - >-
                            The placement group in which the VM is running. If the VM is
                            deallocated it will not have a placementGroupId.
                    type: str
                    sample: null
        hardware_profile:
            description:
                - Specifies the hardware settings for the virtual machine.
            type: dict
            sample: null
            contains:
                vm_size:
                    description:
                        - >-
                            Specifies the size of the virtual machine. For more information
                            about virtual machine sizes, see `Sizes for virtual machines
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-sizes?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                            :code:`<br>`:code:`<br>` The available VM sizes depend on region
                            and availability set. For a list of available sizes use these
                            APIs:  :code:`<br>`:code:`<br>` `List all available virtual
                            machine sizes in an availability set
                            <https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes>`_
                            :code:`<br>`:code:`<br>` `List all available virtual machine sizes
                            in a region
                            <https://docs.microsoft.com/rest/api/compute/virtualmachinesizes/list>`_
                            :code:`<br>`:code:`<br>` `List all available virtual machine sizes
                            for resizing
                            <https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes>`_
                    type: str
                    sample: null
        storage_profile:
            description:
                - Specifies the storage settings for the virtual machine disks.
            type: dict
            sample: null
            contains:
                image_reference:
                    description:
                        - >-
                            Specifies information about the image to use. You can specify
                            information about platform images, marketplace images, or virtual
                            machine images. This element is required when you want to use a
                            platform image, marketplace image, or virtual machine image, but
                            is not used in other creation operations.
                    type: dict
                    sample: null
                    contains:
                        publisher:
                            description:
                                - The image publisher.
                            type: str
                            sample: null
                        offer:
                            description:
                                - >-
                                    Specifies the offer of the platform image or marketplace image
                                    used to create the virtual machine.
                            type: str
                            sample: null
                        sku:
                            description:
                                - The image SKU.
                            type: str
                            sample: null
                        version:
                            description:
                                - >-
                                    Specifies the version of the platform image or marketplace
                                    image used to create the virtual machine. The allowed formats
                                    are Major.Minor.Build or 'latest'. Major, Minor, and Build are
                                    decimal numbers. Specify 'latest' to use the latest version of
                                    an image available at deploy time. Even if you use 'latest',
                                    the VM image will not automatically update after deploy time
                                    even if a new version becomes available.
                            type: str
                            sample: null
                os_disk:
                    description:
                        - >-
                            Specifies information about the operating system disk used by the
                            virtual machine. :code:`<br>`:code:`<br>` For more information
                            about disks, see `About disks and VHDs for Azure virtual machines
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
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
                            type: sealed-choice
                            sample: null
                        encryption_settings:
                            description:
                                - >-
                                    Specifies the encryption settings for the OS Disk.
                                    :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
                            type: dict
                            sample: null
                            contains:
                                disk_encryption_key:
                                    description:
                                        - >-
                                            Specifies the location of the disk encryption key, which
                                            is a Key Vault Secret.
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
                                                - >-
                                                    The relative URL of the Key Vault containing the
                                                    secret.
                                            returned: always
                                            type: dict
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    type: str
                                                    sample: null
                                key_encryption_key:
                                    description:
                                        - >-
                                            Specifies the location of the key encryption key in Key
                                            Vault.
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
                                                    type: str
                                                    sample: null
                                enabled:
                                    description:
                                        - >-
                                            Specifies whether disk encryption should be enabled on the
                                            virtual machine.
                                    type: bool
                                    sample: null
                        name:
                            description:
                                - The disk name.
                            type: str
                            sample: null
                        vhd:
                            description:
                                - The virtual hard disk.
                            type: dict
                            sample: null
                            contains:
                                uri:
                                    description:
                                        - Specifies the virtual hard disk's uri.
                                    type: str
                                    sample: null
                        image:
                            description:
                                - >-
                                    The source user image virtual hard disk. The virtual hard disk
                                    will be copied before being attached to the virtual machine.
                                    If SourceImage is provided, the destination virtual hard drive
                                    must not exist.
                            type: dict
                            sample: null
                            contains:
                                uri:
                                    description:
                                        - Specifies the virtual hard disk's uri.
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
                            type: sealed-choice
                            sample: null
                        write_accelerator_enabled:
                            description:
                                - >-
                                    Specifies whether writeAccelerator should be enabled or
                                    disabled on the disk.
                            type: bool
                            sample: null
                        diff_disk_settings:
                            description:
                                - >-
                                    Specifies the ephemeral Disk Settings for the operating system
                                    disk used by the virtual machine.
                            type: dict
                            sample: null
                            contains:
                                option:
                                    description:
                                        - >-
                                            Specifies the ephemeral disk settings for operating system
                                            disk.
                                    type: str
                                    sample: null
                                placement:
                                    description:
                                        - >-
                                            Specifies the ephemeral disk placement for operating
                                            system disk.:code:`<br>`:code:`<br>` Possible values are:
                                            :code:`<br>`:code:`<br>` **CacheDisk**
                                            :code:`<br>`:code:`<br>` **ResourceDisk**
                                            :code:`<br>`:code:`<br>` Default: **CacheDisk** if one is
                                            configured for the VM size otherwise **ResourceDisk** is
                                            used.:code:`<br>`:code:`<br>` Refer to VM size
                                            documentation for Windows VM at
                                            https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
                                            and Linux VM at
                                            https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes
                                            to check which VM sizes exposes a cache disk.
                                    type: str
                                    sample: null
                        create_option:
                            description:
                                - >-
                                    Specifies how the virtual machine should be
                                    created.:code:`<br>`:code:`<br>` Possible values
                                    are::code:`<br>`:code:`<br>` **Attach** \u2013 This value is
                                    used when you are using a specialized disk to create the
                                    virtual machine.:code:`<br>`:code:`<br>` **FromImage** \u2013
                                    This value is used when you are using an image to create the
                                    virtual machine. If you are using a platform image, you also
                                    use the imageReference element described above. If you are
                                    using a marketplace image, you  also use the plan element
                                    previously described.
                            returned: always
                            type: str
                            sample: null
                        disk_size_gb:
                            description:
                                - >-
                                    Specifies the size of an empty data disk in gigabytes. This
                                    element can be used to overwrite the size of the disk in a
                                    virtual machine image. :code:`<br>`:code:`<br>` This value
                                    cannot be larger than 1023 GB
                            type: int
                            sample: null
                        managed_disk:
                            description:
                                - The managed disk parameters.
                            type: dict
                            sample: null
                            contains:
                                storage_account_type:
                                    description:
                                        - >-
                                            Specifies the storage account type for the managed disk.
                                            NOTE: UltraSSD_LRS can only be used with data disks, it
                                            cannot be used with OS Disk.
                                    type: str
                                    sample: null
                                disk_encryption_set:
                                    description:
                                        - >-
                                            Specifies the customer managed disk encryption set
                                            resource id for the managed disk.
                                    type: dict
                                    sample: null
                                    contains:
                                        id:
                                            description:
                                                - Resource Id
                                            type: str
                                            sample: null
                data_disks:
                    description:
                        - >-
                            Specifies the parameters that are used to add a data disk to a
                            virtual machine. :code:`<br>`:code:`<br>` For more information
                            about disks, see `About disks and VHDs for Azure virtual machines
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
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
                        name:
                            description:
                                - The disk name.
                            type: str
                            sample: null
                        vhd:
                            description:
                                - The virtual hard disk.
                            type: dict
                            sample: null
                            contains:
                                uri:
                                    description:
                                        - Specifies the virtual hard disk's uri.
                                    type: str
                                    sample: null
                        image:
                            description:
                                - >-
                                    The source user image virtual hard disk. The virtual hard disk
                                    will be copied before being attached to the virtual machine.
                                    If SourceImage is provided, the destination virtual hard drive
                                    must not exist.
                            type: dict
                            sample: null
                            contains:
                                uri:
                                    description:
                                        - Specifies the virtual hard disk's uri.
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
                            type: sealed-choice
                            sample: null
                        write_accelerator_enabled:
                            description:
                                - >-
                                    Specifies whether writeAccelerator should be enabled or
                                    disabled on the disk.
                            type: bool
                            sample: null
                        create_option:
                            description:
                                - >-
                                    Specifies how the virtual machine should be
                                    created.:code:`<br>`:code:`<br>` Possible values
                                    are::code:`<br>`:code:`<br>` **Attach** \u2013 This value is
                                    used when you are using a specialized disk to create the
                                    virtual machine.:code:`<br>`:code:`<br>` **FromImage** \u2013
                                    This value is used when you are using an image to create the
                                    virtual machine. If you are using a platform image, you also
                                    use the imageReference element described above. If you are
                                    using a marketplace image, you  also use the plan element
                                    previously described.
                            returned: always
                            type: str
                            sample: null
                        disk_size_gb:
                            description:
                                - >-
                                    Specifies the size of an empty data disk in gigabytes. This
                                    element can be used to overwrite the size of the disk in a
                                    virtual machine image. :code:`<br>`:code:`<br>` This value
                                    cannot be larger than 1023 GB
                            type: int
                            sample: null
                        managed_disk:
                            description:
                                - The managed disk parameters.
                            type: dict
                            sample: null
                            contains:
                                storage_account_type:
                                    description:
                                        - >-
                                            Specifies the storage account type for the managed disk.
                                            NOTE: UltraSSD_LRS can only be used with data disks, it
                                            cannot be used with OS Disk.
                                    type: str
                                    sample: null
                                disk_encryption_set:
                                    description:
                                        - >-
                                            Specifies the customer managed disk encryption set
                                            resource id for the managed disk.
                                    type: dict
                                    sample: null
                                    contains:
                                        id:
                                            description:
                                                - Resource Id
                                            type: str
                                            sample: null
                        to_be_detached:
                            description:
                                - >-
                                    Specifies whether the data disk is in process of detachment
                                    from the VirtualMachine/VirtualMachineScaleset
                            type: bool
                            sample: null
        additional_capabilities:
            description:
                - >-
                    Specifies additional capabilities enabled or disabled on the virtual
                    machine in the scale set. For instance: whether the virtual machine
                    has the capability to support attaching managed data disks with
                    UltraSSD_LRS storage account type.
            type: dict
            sample: null
            contains:
                ultra_ssd_enabled:
                    description:
                        - >-
                            The flag that enables or disables a capability to have one or more
                            managed data disks with UltraSSD_LRS storage account type on the
                            VM or VMSS. Managed disks with storage account type UltraSSD_LRS
                            can be added to a virtual machine or virtual machine scale set
                            only if this property is enabled.
                    type: bool
                    sample: null
        os_profile:
            description:
                - Specifies the operating system settings for the virtual machine.
            type: dict
            sample: null
            contains:
                computer_name:
                    description:
                        - >-
                            Specifies the host OS name of the virtual machine.
                            :code:`<br>`:code:`<br>` This name cannot be updated after the VM
                            is created. :code:`<br>`:code:`<br>` **Max-length (Windows):** 15
                            characters :code:`<br>`:code:`<br>` **Max-length (Linux):** 64
                            characters. :code:`<br>`:code:`<br>` For naming conventions and
                            restrictions see `Azure infrastructure services implementation
                            guidelines
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-infrastructure-subscription-accounts-guidelines?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#1-naming-conventions>`_.
                    type: str
                    sample: null
                admin_username:
                    description:
                        - >-
                            Specifies the name of the administrator account.
                            :code:`<br>`:code:`<br>` This property cannot be updated after the
                            VM is created. :code:`<br>`:code:`<br>` **Windows-only
                            restriction:** Cannot end in "." :code:`<br>`:code:`<br>`
                            **Disallowed values:** "administrator", "admin", "user", "user1",
                            "test", "user2", "test1", "user3", "admin1", "1", "123", "a",
                            "actuser", "adm", "admin2", "aspnet", "backup", "console",
                            "david", "guest", "john", "owner", "root", "server", "sql",
                            "support", "support_388945a0", "sys", "test2", "test3", "user4",
                            "user5". :code:`<br>`:code:`<br>` **Minimum-length (Linux):** 1 
                            character :code:`<br>`:code:`<br>` **Max-length (Linux):** 64
                            characters :code:`<br>`:code:`<br>` **Max-length (Windows):** 20
                            characters  :code:`<br>`:code:`<br>`:code:`<li>` For root access
                            to the Linux VM, see `Using root privileges on Linux virtual
                            machines in Azure
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_\
                            :code:`<br>`:code:`<li>` For a list of built-in system users on
                            Linux that should not be used in this field, see `Selecting User
                            Names for Linux on Azure
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-usernames?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                    type: str
                    sample: null
                admin_password:
                    description:
                        - >-
                            Specifies the password of the administrator account.
                            :code:`<br>`:code:`<br>` **Minimum-length (Windows):** 8
                            characters :code:`<br>`:code:`<br>` **Minimum-length (Linux):** 6
                            characters :code:`<br>`:code:`<br>` **Max-length (Windows):** 123
                            characters :code:`<br>`:code:`<br>` **Max-length (Linux):** 72
                            characters :code:`<br>`:code:`<br>` **Complexity requirements:** 3
                            out of 4 conditions below need to be fulfilled :code:`<br>` Has
                            lower characters :code:`<br>`Has upper characters :code:`<br>` Has
                            a digit :code:`<br>` Has a special character (Regex match [\W_])
                            :code:`<br>`:code:`<br>` **Disallowed values:** "abc@123",
                            "P@$$w0rd", "P@ssw0rd", "P@ssword123", "Pa$$word", "pass@word1",
                            "Password!", "Password1", "Password22", "iloveyou!"
                            :code:`<br>`:code:`<br>` For resetting the password, see `How to
                            reset the Remote Desktop service or its login password in a
                            Windows VM
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                            :code:`<br>`:code:`<br>` For resetting root password, see `Manage
                            users, SSH, and check or repair disks on Azure Linux VMs using the
                            VMAccess Extension
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password>`_
                    type: str
                    sample: null
                custom_data:
                    description:
                        - >-
                            Specifies a base-64 encoded string of custom data. The base-64
                            encoded string is decoded to a binary array that is saved as a
                            file on the Virtual Machine. The maximum length of the binary
                            array is 65535 bytes. :code:`<br>`:code:`<br>` **Note: Do not pass
                            any secrets or passwords in customData property**
                            :code:`<br>`:code:`<br>` This property cannot be updated after the
                            VM is created. :code:`<br>`:code:`<br>` customData is passed to
                            the VM to be saved as a file, for more information see `Custom
                            Data on Azure VMs
                            <https://azure.microsoft.com/en-us/blog/custom-data-and-cloud-init-on-windows-azure/>`_
                            :code:`<br>`:code:`<br>` For using cloud-init for your Linux VM,
                            see `Using cloud-init to customize a Linux VM during creation
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                    type: str
                    sample: null
                windows_configuration:
                    description:
                        - >-
                            Specifies Windows operating system settings on the virtual
                            machine.
                    type: dict
                    sample: null
                    contains:
                        provision_vm_agent:
                            description:
                                - >-
                                    Indicates whether virtual machine agent should be provisioned
                                    on the virtual machine. :code:`<br>`:code:`<br>` When this
                                    property is not specified in the request body, default
                                    behavior is to set it to true.  This will ensure that VM Agent
                                    is installed on the VM so that extensions can be added to the
                                    VM later.
                            type: bool
                            sample: null
                        enable_automatic_updates:
                            description:
                                - >-
                                    Indicates whether Automatic Updates is enabled for the Windows
                                    virtual machine. Default value is true.
                                    :code:`<br>`:code:`<br>` For virtual machine scale sets, this
                                    property can be updated and updates will take effect on OS
                                    reprovisioning.
                            type: bool
                            sample: null
                        time_zone:
                            description:
                                - >-
                                    Specifies the time zone of the virtual machine. e.g. "Pacific
                                    Standard Time". :code:`<br>`:code:`<br>` Possible values can
                                    be `TimeZoneInfo.Id
                                    <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.id?#System_TimeZoneInfo_Id>`_
                                    value from time zones returned by
                                    `TimeZoneInfo.GetSystemTimeZones
                                    <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.getsystemtimezones>`_.
                            type: str
                            sample: null
                        additional_unattend_content:
                            description:
                                - >-
                                    Specifies additional base-64 encoded XML formatted information
                                    that can be included in the Unattend.xml file, which is used
                                    by Windows Setup.
                            type: list
                            sample: null
                            contains:
                                pass_name:
                                    description:
                                        - >-
                                            The pass name. Currently, the only allowable value is
                                            OobeSystem.
                                    type: constant
                                    sample: null
                                component_name:
                                    description:
                                        - >-
                                            The component name. Currently, the only allowable value is
                                            Microsoft-Windows-Shell-Setup.
                                    type: constant
                                    sample: null
                                setting_name:
                                    description:
                                        - >-
                                            Specifies the name of the setting to which the content
                                            applies. Possible values are: FirstLogonCommands and
                                            AutoLogon.
                                    type: sealed-choice
                                    sample: null
                                content:
                                    description:
                                        - >-
                                            Specifies the XML formatted content that is added to the
                                            unattend.xml file for the specified path and component.
                                            The XML must be less than 4KB and must include the root
                                            element for the setting or feature that is being inserted.
                                    type: str
                                    sample: null
                        patch_settings:
                            description:
                                - Specifies settings related to in-guest patching (KBs).
                            type: dict
                            sample: null
                            contains:
                                patch_mode:
                                    description:
                                        - >-
                                            Specifies the mode of in-guest patching to IaaS virtual
                                            machine.:code:`<br />`:code:`<br />` Possible values
                                            are::code:`<br />`:code:`<br />` **Manual** - You  control
                                            the application of patches to a virtual machine. You do
                                            this by applying patches manually inside the VM. In this
                                            mode, automatic updates are disabled; the property
                                            WindowsConfiguration.enableAutomaticUpdates must be
                                            false:code:`<br />`:code:`<br />` **AutomaticByOS** - The
                                            virtual machine will automatically be updated by the OS.
                                            The property WindowsConfiguration.enableAutomaticUpdates
                                            must be true. :code:`<br />`:code:`<br />` **
                                            AutomaticByPlatform** - the virtual machine will
                                            automatically updated by the platform. The properties
                                            provisionVMAgent and
                                            WindowsConfiguration.enableAutomaticUpdates must be true
                                    type: str
                                    sample: null
                        win_rm:
                            description:
                                - >-
                                    Specifies the Windows Remote Management listeners. This
                                    enables remote Windows PowerShell.
                            type: dict
                            sample: null
                            contains:
                                listeners:
                                    description:
                                        - The list of Windows Remote Management listeners
                                    type: list
                                    sample: null
                                    contains:
                                        protocol:
                                            description:
                                                - >-
                                                    Specifies the protocol of WinRM listener.
                                                    :code:`<br>`:code:`<br>` Possible values are:
                                                    :code:`<br>`\ **http** :code:`<br>`:code:`<br>`
                                                    **https**
                                            type: sealed-choice
                                            sample: null
                                        certificate_url:
                                            description:
                                                - >-
                                                    This is the URL of a certificate that has been
                                                    uploaded to Key Vault as a secret. For adding a secret
                                                    to the Key Vault, see `Add a key or secret to the key
                                                    vault
                                                    <https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add>`_.
                                                    In this case, your certificate needs to be It is the
                                                    Base64 encoding of the following JSON Object which is
                                                    encoded in UTF-8: :code:`<br>`:code:`<br>`
                                                    {:code:`<br>` 
                                                    "data":":code:`<Base64-encoded-certificate>`",:code:`<br>` 
                                                    "dataType":"pfx",:code:`<br>` 
                                                    "password":":code:`<pfx-file-password>`":code:`<br>`}
                                            type: str
                                            sample: null
                linux_configuration:
                    description:
                        - >-
                            Specifies the Linux operating system settings on the virtual
                            machine. :code:`<br>`:code:`<br>`For a list of supported Linux
                            distributions, see `Linux on Azure-Endorsed Distributions
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-endorsed-distros?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                            :code:`<br>`:code:`<br>` For running non-endorsed distributions,
                            see `Information for Non-Endorsed Distributions
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-create-upload-generic?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
                    type: dict
                    sample: null
                    contains:
                        disable_password_authentication:
                            description:
                                - Specifies whether password authentication should be disabled.
                            type: bool
                            sample: null
                        ssh:
                            description:
                                - Specifies the ssh key configuration for a Linux OS.
                            type: dict
                            sample: null
                            contains:
                                public_keys:
                                    description:
                                        - >-
                                            The list of SSH public keys used to authenticate with
                                            linux based VMs.
                                    type: list
                                    sample: null
                                    contains:
                                        path:
                                            description:
                                                - >-
                                                    Specifies the full path on the created VM where ssh
                                                    public key is stored. If the file already exists, the
                                                    specified key is appended to the file. Example:
                                                    /home/user/.ssh/authorized_keys
                                            type: str
                                            sample: null
                                        key_data:
                                            description:
                                                - >-
                                                    SSH public key certificate used to authenticate with
                                                    the VM through ssh. The key needs to be at least
                                                    2048-bit and in ssh-rsa format.
                                                    :code:`<br>`:code:`<br>` For creating ssh keys, see
                                                    `Create SSH keys on Linux and Mac for Linux VMs in
                                                    Azure
                                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-mac-create-ssh-keys?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
                                            type: str
                                            sample: null
                        provision_vm_agent:
                            description:
                                - >-
                                    Indicates whether virtual machine agent should be provisioned
                                    on the virtual machine. :code:`<br>`:code:`<br>` When this
                                    property is not specified in the request body, default
                                    behavior is to set it to true.  This will ensure that VM Agent
                                    is installed on the VM so that extensions can be added to the
                                    VM later.
                            type: bool
                            sample: null
                secrets:
                    description:
                        - >-
                            Specifies set of certificates that should be installed onto the
                            virtual machine.
                    type: list
                    sample: null
                    contains:
                        source_vault:
                            description:
                                - >-
                                    The relative URL of the Key Vault containing all of the
                                    certificates in VaultCertificates.
                            type: dict
                            sample: null
                            contains:
                                id:
                                    description:
                                        - Resource Id
                                    type: str
                                    sample: null
                        vault_certificates:
                            description:
                                - >-
                                    The list of key vault references in SourceVault which contain
                                    certificates.
                            type: list
                            sample: null
                            contains:
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
                                    type: str
                                    sample: null
                                certificate_store:
                                    description:
                                        - >-
                                            For Windows VMs, specifies the certificate store on the
                                            Virtual Machine to which the certificate should be added.
                                            The specified certificate store is implicitly in the
                                            LocalMachine account. :code:`<br>`:code:`<br>`For Linux
                                            VMs, the certificate file is placed under the
                                            /var/lib/waagent directory, with the file name
                                            &lt;UppercaseThumbprint&gt;.crt for the X509 certificate
                                            file and &lt;UppercaseThumbprint&gt;.prv for private key.
                                            Both of these files are .pem formatted.
                                    type: str
                                    sample: null
                allow_extension_operations:
                    description:
                        - >-
                            Specifies whether extension operations should be allowed on the
                            virtual machine. :code:`<br>`:code:`<br>`This may only be set to
                            False when no extensions are present on the virtual machine.
                    type: bool
                    sample: null
                require_guest_provision_signal:
                    description:
                        - >-
                            Specifies whether the guest provision signal is required to infer
                            provision success of the virtual machine.  **Note: This property
                            is for private testing only, and all customers must not set the
                            property to false.**
                    type: bool
                    sample: null
        security_profile:
            description:
                - >-
                    Specifies the Security related profile settings for the virtual
                    machine.
            type: dict
            sample: null
            contains:
                encryption_at_host:
                    description:
                        - >-
                            This property can be used by user in the request to enable or
                            disable the Host Encryption for the virtual machine or virtual
                            machine scale set. This will enable the encryption for all the
                            disks including Resource/Temp disk at host itself.
                            :code:`<br>`:code:`<br>` Default: The Encryption at host will be
                            disabled unless this property is set to true for the resource.
                    type: bool
                    sample: null
        network_profile:
            description:
                - Specifies the network interfaces of the virtual machine.
            type: dict
            sample: null
            contains:
                network_interfaces:
                    description:
                        - >-
                            Specifies the list of resource Ids for the network interfaces
                            associated with the virtual machine.
                    type: list
                    sample: null
                    contains:
                        primary:
                            description:
                                - >-
                                    Specifies the primary network interface in case the virtual
                                    machine has more than 1 network interface.
                            type: bool
                            sample: null
        network_profile_configuration:
            description:
                - Specifies the network profile configuration of the virtual machine.
            type: dict
            sample: null
            contains:
                network_interface_configurations:
                    description:
                        - The list of network configurations.
                    type: list
                    sample: null
                    contains:
                        name:
                            description:
                                - The network configuration name.
                            returned: always
                            type: str
                            sample: null
                        primary:
                            description:
                                - >-
                                    Specifies the primary network interface in case the virtual
                                    machine has more than 1 network interface.
                            type: bool
                            sample: null
                        enable_accelerated_networking:
                            description:
                                - >-
                                    Specifies whether the network interface is accelerated
                                    networking-enabled.
                            type: bool
                            sample: null
                        network_security_group:
                            description:
                                - The network security group.
                            type: dict
                            sample: null
                            contains:
                                id:
                                    description:
                                        - Resource Id
                                    type: str
                                    sample: null
                        dns_settings:
                            description:
                                - The dns settings to be applied on the network interfaces.
                            type: dict
                            sample: null
                            contains:
                                dns_servers:
                                    description:
                                        - List of DNS servers IP addresses
                                    type: list
                                    sample: null
                        ip_configurations:
                            description:
                                - Specifies the IP configurations of the network interface.
                            type: list
                            sample: null
                            contains:
                                name:
                                    description:
                                        - The IP configuration name.
                                    returned: always
                                    type: str
                                    sample: null
                                subnet:
                                    description:
                                        - Specifies the identifier of the subnet.
                                    type: dict
                                    sample: null
                                    contains:
                                        id:
                                            description:
                                                - >-
                                                    The ARM resource id in the form of
                                                    /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
                                            type: str
                                            sample: null
                                primary:
                                    description:
                                        - >-
                                            Specifies the primary network interface in case the
                                            virtual machine has more than 1 network interface.
                                    type: bool
                                    sample: null
                                public_ip_address_configuration:
                                    description:
                                        - The publicIPAddressConfiguration.
                                    type: dict
                                    sample: null
                                    contains:
                                        name:
                                            description:
                                                - The publicIP address configuration name.
                                            returned: always
                                            type: str
                                            sample: null
                                        idle_timeout_in_minutes:
                                            description:
                                                - The idle timeout of the public IP address.
                                            type: int
                                            sample: null
                                        dns_settings:
                                            description:
                                                - >-
                                                    The dns settings to be applied on the publicIP
                                                    addresses .
                                            type: dict
                                            sample: null
                                            contains:
                                                domain_name_label:
                                                    description:
                                                        - >-
                                                            The Domain name label.The concatenation of the
                                                            domain name label and vm index will be the domain
                                                            name labels of the PublicIPAddress resources that
                                                            will be created
                                                    returned: always
                                                    type: str
                                                    sample: null
                                        ip_tags:
                                            description:
                                                - >-
                                                    The list of IP tags associated with the public IP
                                                    address.
                                            type: list
                                            sample: null
                                            contains:
                                                ip_tag_type:
                                                    description:
                                                        - 'IP tag type. Example: FirstPartyUsage.'
                                                    type: str
                                                    sample: null
                                                tag:
                                                    description:
                                                        - >-
                                                            IP tag associated with the public IP. Example:
                                                            SQL, Storage etc.
                                                    type: str
                                                    sample: null
                                        public_ip_prefix:
                                            description:
                                                - >-
                                                    The PublicIPPrefix from which to allocate publicIP
                                                    addresses.
                                            type: dict
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    type: str
                                                    sample: null
                                        public_ip_address_version:
                                            description:
                                                - >-
                                                    Available from Api-Version 2019-07-01 onwards, it
                                                    represents whether the specific ipconfiguration is
                                                    IPv4 or IPv6. Default is taken as IPv4. Possible
                                                    values are: 'IPv4' and 'IPv6'.
                                            type: str
                                            sample: null
                                private_ip_address_version:
                                    description:
                                        - >-
                                            Available from Api-Version 2017-03-30 onwards, it
                                            represents whether the specific ipconfiguration is IPv4 or
                                            IPv6. Default is taken as IPv4.  Possible values are:
                                            'IPv4' and 'IPv6'.
                                    type: str
                                    sample: null
                                application_gateway_backend_address_pools:
                                    description:
                                        - >-
                                            Specifies an array of references to backend address pools
                                            of application gateways. A scale set can reference backend
                                            address pools of multiple application gateways. Multiple
                                            scale sets cannot use the same application gateway.
                                    type: list
                                    sample: null
                                    contains:
                                        id:
                                            description:
                                                - Resource Id
                                            type: str
                                            sample: null
                                application_security_groups:
                                    description:
                                        - >-
                                            Specifies an array of references to application security
                                            group.
                                    type: list
                                    sample: null
                                    contains:
                                        id:
                                            description:
                                                - Resource Id
                                            type: str
                                            sample: null
                                load_balancer_backend_address_pools:
                                    description:
                                        - >-
                                            Specifies an array of references to backend address pools
                                            of load balancers. A scale set can reference backend
                                            address pools of one public and one internal load
                                            balancer. Multiple scale sets cannot use the same basic
                                            sku load balancer.
                                    type: list
                                    sample: null
                                    contains:
                                        id:
                                            description:
                                                - Resource Id
                                            type: str
                                            sample: null
                                load_balancer_inbound_nat_pools:
                                    description:
                                        - >-
                                            Specifies an array of references to inbound Nat pools of
                                            the load balancers. A scale set can reference inbound nat
                                            pools of one public and one internal load balancer.
                                            Multiple scale sets cannot use the same basic sku load
                                            balancer.
                                    type: list
                                    sample: null
                                    contains:
                                        id:
                                            description:
                                                - Resource Id
                                            type: str
                                            sample: null
                        enable_ip_forwarding:
                            description:
                                - Whether IP forwarding enabled on this NIC.
                            type: bool
                            sample: null
        diagnostics_profile:
            description:
                - >-
                    Specifies the boot diagnostic settings state.
                    :code:`<br>`:code:`<br>`Minimum api-version: 2015-06-15.
            type: dict
            sample: null
            contains:
                boot_diagnostics:
                    description:
                        - >-
                            Boot Diagnostics is a debugging feature which allows you to view
                            Console Output and Screenshot to diagnose VM status.
                            :code:`<br>`:code:`<br>` You can easily view the output of your
                            console log. :code:`<br>`:code:`<br>` Azure also enables you to
                            see a screenshot of the VM from the hypervisor.
                    type: dict
                    sample: null
                    contains:
                        enabled:
                            description:
                                - >-
                                    Whether boot diagnostics should be enabled on the Virtual
                                    Machine.
                            type: bool
                            sample: null
                        storage_uri:
                            description:
                                - >-
                                    Uri of the storage account to use for placing the console
                                    output and screenshot. :code:`<br>`:code:`<br>`If storageUri
                                    is not specified while enabling boot diagnostics, managed
                                    storage will be used.
                            type: str
                            sample: null
        availability_set:
            description:
                - >-
                    Specifies information about the availability set that the virtual
                    machine should be assigned to. Virtual machines specified in the same
                    availability set are allocated to different nodes to maximize
                    availability. For more information about availability sets, see
                    `Manage the availability of virtual machines
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-manage-availability?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                    :code:`<br>`:code:`<br>` For more information on Azure planned
                    maintenance, see `Planned maintenance for virtual machines in Azure
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-planned-maintenance?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                    :code:`<br>`:code:`<br>` Currently, a VM can only be added to
                    availability set at creation time. An existing VM cannot be added to
                    an availability set.
            type: dict
            sample: null
            contains:
                id:
                    description:
                        - Resource Id
                    type: str
                    sample: null
        provisioning_state:
            description:
                - 'The provisioning state, which only appears in the response.'
            type: str
            sample: null
        license_type:
            description:
                - >-
                    Specifies that the image or disk that is being used was licensed
                    on-premises. This element is only used for images that contain the
                    Windows Server operating system. :code:`<br>`:code:`<br>` Possible
                    values are: :code:`<br>`:code:`<br>` Windows_Client
                    :code:`<br>`:code:`<br>` Windows_Server :code:`<br>`:code:`<br>` If
                    this element is included in a request for an update, the value must
                    match the initial value. This value cannot be updated.
                    :code:`<br>`:code:`<br>` For more information, see `Azure Hybrid Use
                    Benefit for Windows Server
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                    :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
            type: str
            sample: null
        model_definition_applied:
            description:
                - >-
                    Specifies whether the model applied to the virtual machine is the
                    model of the virtual machine scale set or the customized model for the
                    virtual machine.
            type: str
            sample: null
        protection_policy:
            description:
                - Specifies the protection policy of the virtual machine.
            type: dict
            sample: null
            contains:
                protect_from_scale_in:
                    description:
                        - >-
                            Indicates that the virtual machine scale set VM shouldn't be
                            considered for deletion during a scale-in operation.
                    type: bool
                    sample: null
                protect_from_scale_set_actions:
                    description:
                        - >-
                            Indicates that model updates or actions (including scale-in)
                            initiated on the virtual machine scale set should not be applied
                            to the virtual machine scale set VM.
                    type: bool
                    sample: null
        platform_update_domain:
            description:
                - The Update Domain count.
            type: int
            sample: null
        platform_fault_domain:
            description:
                - The Fault Domain count.
            type: int
            sample: null
        rdp_thumb_print:
            description:
                - The Remote desktop certificate thumbprint.
            type: str
            sample: null
        vm_agent:
            description:
                - The VM Agent running on the virtual machine.
            type: dict
            sample: null
            contains:
                vm_agent_version:
                    description:
                        - The VM Agent full version.
                    type: str
                    sample: null
                extension_handlers:
                    description:
                        - The virtual machine extension handler instance view.
                    type: list
                    sample: null
                    contains:
                        type:
                            description:
                                - >-
                                    Specifies the type of the extension; an example is
                                    "CustomScriptExtension".
                            type: str
                            sample: null
                        type_handler_version:
                            description:
                                - Specifies the version of the script handler.
                            type: str
                            sample: null
                        status:
                            description:
                                - The extension handler status.
                            type: dict
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null
                statuses:
                    description:
                        - The resource status information.
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            type: str
                            sample: null
        maintenance_redeploy_status:
            description:
                - The Maintenance Operation status on the virtual machine.
            type: dict
            sample: null
            contains:
                is_customer_initiated_maintenance_allowed:
                    description:
                        - 'True, if customer is allowed to perform Maintenance.'
                    type: bool
                    sample: null
                pre_maintenance_window_start_time:
                    description:
                        - Start Time for the Pre Maintenance Window.
                    type: str
                    sample: null
                pre_maintenance_window_end_time:
                    description:
                        - End Time for the Pre Maintenance Window.
                    type: str
                    sample: null
                maintenance_window_start_time:
                    description:
                        - Start Time for the Maintenance Window.
                    type: str
                    sample: null
                maintenance_window_end_time:
                    description:
                        - End Time for the Maintenance Window.
                    type: str
                    sample: null
                last_operation_result_code:
                    description:
                        - The Last Maintenance Operation Result Code.
                    type: sealed-choice
                    sample: null
                last_operation_message:
                    description:
                        - Message returned for the last Maintenance Operation.
                    type: str
                    sample: null
        disks:
            description:
                - The disks information.
            type: list
            sample: null
            contains:
                name:
                    description:
                        - The disk name.
                    type: str
                    sample: null
                encryption_settings:
                    description:
                        - >-
                            Specifies the encryption settings for the OS Disk.
                            :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
                    type: list
                    sample: null
                    contains:
                        disk_encryption_key:
                            description:
                                - >-
                                    Specifies the location of the disk encryption key, which is a
                                    Key Vault Secret.
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
                                            type: str
                                            sample: null
                        key_encryption_key:
                            description:
                                - Specifies the location of the key encryption key in Key Vault.
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
                                            type: str
                                            sample: null
                        enabled:
                            description:
                                - >-
                                    Specifies whether disk encryption should be enabled on the
                                    virtual machine.
                            type: bool
                            sample: null
                statuses:
                    description:
                        - The resource status information.
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            type: str
                            sample: null
        extensions:
            description:
                - The extensions information.
            type: list
            sample: null
            contains:
                name:
                    description:
                        - The virtual machine extension name.
                    type: str
                    sample: null
                type:
                    description:
                        - >-
                            Specifies the type of the extension; an example is
                            "CustomScriptExtension".
                    type: str
                    sample: null
                type_handler_version:
                    description:
                        - Specifies the version of the script handler.
                    type: str
                    sample: null
                substatuses:
                    description:
                        - The resource status information.
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            type: str
                            sample: null
                statuses:
                    description:
                        - The resource status information.
                    type: list
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            type: str
                            sample: null
        vm_health:
            description:
                - The health status for the VM.
            type: dict
            sample: null
            contains:
                status:
                    description:
                        - The health status information for the VM.
                    type: dict
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
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
            type: dict
            sample: null
            contains:
                status:
                    description:
                        - >-
                            The boot diagnostics status information for the VM.
                            :code:`<br>`:code:`<br>` NOTE: It will be set only if there are
                            errors encountered in enabling boot diagnostics.
                    type: dict
                    sample: null
                    contains:
                        code:
                            description:
                                - The status code.
                            type: str
                            sample: null
                        level:
                            description:
                                - The level code.
                            type: sealed-choice
                            sample: null
                        display_status:
                            description:
                                - The short localizable label for the status.
                            type: str
                            sample: null
                        message:
                            description:
                                - >-
                                    The detailed status message, including for alerts and error
                                    messages.
                            type: str
                            sample: null
                        time:
                            description:
                                - The time of the status.
                            type: str
                            sample: null
        statuses:
            description:
                - The resource status information.
            type: list
            sample: null
            contains:
                code:
                    description:
                        - The status code.
                    type: str
                    sample: null
                level:
                    description:
                        - The level code.
                    type: sealed-choice
                    sample: null
                display_status:
                    description:
                        - The short localizable label for the status.
                    type: str
                    sample: null
                message:
                    description:
                        - >-
                            The detailed status message, including for alerts and error
                            messages.
                    type: str
                    sample: null
                time:
                    description:
                        - The time of the status.
                    type: str
                    sample: null
        assigned_host:
            description:
                - >-
                    Resource id of the dedicated host, on which the virtual machine is
                    allocated through automatic placement, when the virtual machine is
                    associated with a dedicated host group that has automatic placement
                    enabled. :code:`<br>`:code:`<br>`Minimum api-version: 2020-06-01.
            type: str
            sample: null
        placement_group_id:
            description:
                - >-
                    The placement group in which the VM is running. If the VM is
                    deallocated it will not have a placementGroupId.
            type: str
            sample: null
        value:
            description:
                - The list of virtual machine scale sets VMs.
            returned: always
            type: list
            sample: null
            contains:
                sku:
                    description:
                        - The virtual machine SKU.
                    type: dict
                    sample: null
                    contains:
                        name:
                            description:
                                - The sku name.
                            type: str
                            sample: null
                        tier:
                            description:
                                - >-
                                    Specifies the tier of virtual machines in a scale
                                    set.:code:`<br />`:code:`<br />` Possible Values::code:`<br
                                    />`:code:`<br />` **Standard**\ :code:`<br />`:code:`<br />`
                                    **Basic**
                            type: str
                            sample: null
                        capacity:
                            description:
                                - Specifies the number of virtual machines in the scale set.
                            type: int
                            sample: null
                plan:
                    description:
                        - >-
                            Specifies information about the marketplace image used to create
                            the virtual machine. This element is only used for marketplace
                            images. Before you can use a marketplace image from an API, you
                            must enable the image for programmatic use.  In the Azure portal,
                            find the marketplace image that you want to use and then click
                            **Want to deploy programmatically, Get Started ->**. Enter any
                            required information and then click **Save**.
                    type: dict
                    sample: null
                    contains:
                        name:
                            description:
                                - The plan ID.
                            type: str
                            sample: null
                        publisher:
                            description:
                                - The publisher ID.
                            type: str
                            sample: null
                        product:
                            description:
                                - >-
                                    Specifies the product of the image from the marketplace. This
                                    is the same value as Offer under the imageReference element.
                            type: str
                            sample: null
                        promotion_code:
                            description:
                                - The promotion code.
                            type: str
                            sample: null
                resources:
                    description:
                        - The virtual machine child extension resources.
                    type: list
                    sample: null
                    contains:
                        force_update_tag:
                            description:
                                - >-
                                    How the extension handler should be forced to update even if
                                    the extension configuration has not changed.
                            type: str
                            sample: null
                        publisher:
                            description:
                                - The name of the extension handler publisher.
                            type: str
                            sample: null
                        type_properties_type:
                            description:
                                - >-
                                    Specifies the type of the extension; an example is
                                    "CustomScriptExtension".
                            type: str
                            sample: null
                        type_handler_version:
                            description:
                                - Specifies the version of the script handler.
                            type: str
                            sample: null
                        auto_upgrade_minor_version:
                            description:
                                - >-
                                    Indicates whether the extension should use a newer minor
                                    version if one is available at deployment time. Once deployed,
                                    however, the extension will not upgrade minor versions unless
                                    redeployed, even with this property set to true.
                            type: bool
                            sample: null
                        enable_automatic_upgrade:
                            description:
                                - >-
                                    Indicates whether the extension should be automatically
                                    upgraded by the platform if there is a newer version of the
                                    extension available.
                            type: bool
                            sample: null
                        settings:
                            description:
                                - Json formatted public settings for the extension.
                            type: any
                            sample: null
                        protected_settings:
                            description:
                                - >-
                                    The extension can contain either protectedSettings or
                                    protectedSettingsFromKeyVault or no protected settings at all.
                            type: any
                            sample: null
                        instance_view:
                            description:
                                - The virtual machine extension instance view.
                            type: dict
                            sample: null
                            contains:
                                name:
                                    description:
                                        - The virtual machine extension name.
                                    type: str
                                    sample: null
                                type:
                                    description:
                                        - >-
                                            Specifies the type of the extension; an example is
                                            "CustomScriptExtension".
                                    type: str
                                    sample: null
                                type_handler_version:
                                    description:
                                        - Specifies the version of the script handler.
                                    type: str
                                    sample: null
                                substatuses:
                                    description:
                                        - The resource status information.
                                    type: list
                                    sample: null
                                    contains:
                                        code:
                                            description:
                                                - The status code.
                                            type: str
                                            sample: null
                                        level:
                                            description:
                                                - The level code.
                                            type: sealed-choice
                                            sample: null
                                        display_status:
                                            description:
                                                - The short localizable label for the status.
                                            type: str
                                            sample: null
                                        message:
                                            description:
                                                - >-
                                                    The detailed status message, including for alerts and
                                                    error messages.
                                            type: str
                                            sample: null
                                        time:
                                            description:
                                                - The time of the status.
                                            type: str
                                            sample: null
                                statuses:
                                    description:
                                        - The resource status information.
                                    type: list
                                    sample: null
                                    contains:
                                        code:
                                            description:
                                                - The status code.
                                            type: str
                                            sample: null
                                        level:
                                            description:
                                                - The level code.
                                            type: sealed-choice
                                            sample: null
                                        display_status:
                                            description:
                                                - The short localizable label for the status.
                                            type: str
                                            sample: null
                                        message:
                                            description:
                                                - >-
                                                    The detailed status message, including for alerts and
                                                    error messages.
                                            type: str
                                            sample: null
                                        time:
                                            description:
                                                - The time of the status.
                                            type: str
                                            sample: null
                zones:
                    description:
                        - The virtual machine zones.
                    type: list
                    sample: null
                instance_view:
                    description:
                        - The virtual machine instance view.
                    type: dict
                    sample: null
                    contains:
                        platform_update_domain:
                            description:
                                - The Update Domain count.
                            type: int
                            sample: null
                        platform_fault_domain:
                            description:
                                - The Fault Domain count.
                            type: int
                            sample: null
                        rdp_thumb_print:
                            description:
                                - The Remote desktop certificate thumbprint.
                            type: str
                            sample: null
                        vm_agent:
                            description:
                                - The VM Agent running on the virtual machine.
                            type: dict
                            sample: null
                            contains:
                                vm_agent_version:
                                    description:
                                        - The VM Agent full version.
                                    type: str
                                    sample: null
                                extension_handlers:
                                    description:
                                        - The virtual machine extension handler instance view.
                                    type: list
                                    sample: null
                                    contains:
                                        type:
                                            description:
                                                - >-
                                                    Specifies the type of the extension; an example is
                                                    "CustomScriptExtension".
                                            type: str
                                            sample: null
                                        type_handler_version:
                                            description:
                                                - Specifies the version of the script handler.
                                            type: str
                                            sample: null
                                        status:
                                            description:
                                                - The extension handler status.
                                            type: dict
                                            sample: null
                                            contains:
                                                code:
                                                    description:
                                                        - The status code.
                                                    type: str
                                                    sample: null
                                                level:
                                                    description:
                                                        - The level code.
                                                    type: sealed-choice
                                                    sample: null
                                                display_status:
                                                    description:
                                                        - The short localizable label for the status.
                                                    type: str
                                                    sample: null
                                                message:
                                                    description:
                                                        - >-
                                                            The detailed status message, including for alerts
                                                            and error messages.
                                                    type: str
                                                    sample: null
                                                time:
                                                    description:
                                                        - The time of the status.
                                                    type: str
                                                    sample: null
                                statuses:
                                    description:
                                        - The resource status information.
                                    type: list
                                    sample: null
                                    contains:
                                        code:
                                            description:
                                                - The status code.
                                            type: str
                                            sample: null
                                        level:
                                            description:
                                                - The level code.
                                            type: sealed-choice
                                            sample: null
                                        display_status:
                                            description:
                                                - The short localizable label for the status.
                                            type: str
                                            sample: null
                                        message:
                                            description:
                                                - >-
                                                    The detailed status message, including for alerts and
                                                    error messages.
                                            type: str
                                            sample: null
                                        time:
                                            description:
                                                - The time of the status.
                                            type: str
                                            sample: null
                        maintenance_redeploy_status:
                            description:
                                - The Maintenance Operation status on the virtual machine.
                            type: dict
                            sample: null
                            contains:
                                is_customer_initiated_maintenance_allowed:
                                    description:
                                        - 'True, if customer is allowed to perform Maintenance.'
                                    type: bool
                                    sample: null
                                pre_maintenance_window_start_time:
                                    description:
                                        - Start Time for the Pre Maintenance Window.
                                    type: str
                                    sample: null
                                pre_maintenance_window_end_time:
                                    description:
                                        - End Time for the Pre Maintenance Window.
                                    type: str
                                    sample: null
                                maintenance_window_start_time:
                                    description:
                                        - Start Time for the Maintenance Window.
                                    type: str
                                    sample: null
                                maintenance_window_end_time:
                                    description:
                                        - End Time for the Maintenance Window.
                                    type: str
                                    sample: null
                                last_operation_result_code:
                                    description:
                                        - The Last Maintenance Operation Result Code.
                                    type: sealed-choice
                                    sample: null
                                last_operation_message:
                                    description:
                                        - Message returned for the last Maintenance Operation.
                                    type: str
                                    sample: null
                        disks:
                            description:
                                - The disks information.
                            type: list
                            sample: null
                            contains:
                                name:
                                    description:
                                        - The disk name.
                                    type: str
                                    sample: null
                                encryption_settings:
                                    description:
                                        - >-
                                            Specifies the encryption settings for the OS Disk.
                                            :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
                                    type: list
                                    sample: null
                                    contains:
                                        disk_encryption_key:
                                            description:
                                                - >-
                                                    Specifies the location of the disk encryption key,
                                                    which is a Key Vault Secret.
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
                                                        - >-
                                                            The relative URL of the Key Vault containing the
                                                            secret.
                                                    returned: always
                                                    type: dict
                                                    sample: null
                                                    contains:
                                                        id:
                                                            description:
                                                                - Resource Id
                                                            type: str
                                                            sample: null
                                        key_encryption_key:
                                            description:
                                                - >-
                                                    Specifies the location of the key encryption key in
                                                    Key Vault.
                                            type: dict
                                            sample: null
                                            contains:
                                                key_url:
                                                    description:
                                                        - >-
                                                            The URL referencing a key encryption key in Key
                                                            Vault.
                                                    returned: always
                                                    type: str
                                                    sample: null
                                                source_vault:
                                                    description:
                                                        - >-
                                                            The relative URL of the Key Vault containing the
                                                            key.
                                                    returned: always
                                                    type: dict
                                                    sample: null
                                                    contains:
                                                        id:
                                                            description:
                                                                - Resource Id
                                                            type: str
                                                            sample: null
                                        enabled:
                                            description:
                                                - >-
                                                    Specifies whether disk encryption should be enabled on
                                                    the virtual machine.
                                            type: bool
                                            sample: null
                                statuses:
                                    description:
                                        - The resource status information.
                                    type: list
                                    sample: null
                                    contains:
                                        code:
                                            description:
                                                - The status code.
                                            type: str
                                            sample: null
                                        level:
                                            description:
                                                - The level code.
                                            type: sealed-choice
                                            sample: null
                                        display_status:
                                            description:
                                                - The short localizable label for the status.
                                            type: str
                                            sample: null
                                        message:
                                            description:
                                                - >-
                                                    The detailed status message, including for alerts and
                                                    error messages.
                                            type: str
                                            sample: null
                                        time:
                                            description:
                                                - The time of the status.
                                            type: str
                                            sample: null
                        extensions:
                            description:
                                - The extensions information.
                            type: list
                            sample: null
                            contains:
                                name:
                                    description:
                                        - The virtual machine extension name.
                                    type: str
                                    sample: null
                                type:
                                    description:
                                        - >-
                                            Specifies the type of the extension; an example is
                                            "CustomScriptExtension".
                                    type: str
                                    sample: null
                                type_handler_version:
                                    description:
                                        - Specifies the version of the script handler.
                                    type: str
                                    sample: null
                                substatuses:
                                    description:
                                        - The resource status information.
                                    type: list
                                    sample: null
                                    contains:
                                        code:
                                            description:
                                                - The status code.
                                            type: str
                                            sample: null
                                        level:
                                            description:
                                                - The level code.
                                            type: sealed-choice
                                            sample: null
                                        display_status:
                                            description:
                                                - The short localizable label for the status.
                                            type: str
                                            sample: null
                                        message:
                                            description:
                                                - >-
                                                    The detailed status message, including for alerts and
                                                    error messages.
                                            type: str
                                            sample: null
                                        time:
                                            description:
                                                - The time of the status.
                                            type: str
                                            sample: null
                                statuses:
                                    description:
                                        - The resource status information.
                                    type: list
                                    sample: null
                                    contains:
                                        code:
                                            description:
                                                - The status code.
                                            type: str
                                            sample: null
                                        level:
                                            description:
                                                - The level code.
                                            type: sealed-choice
                                            sample: null
                                        display_status:
                                            description:
                                                - The short localizable label for the status.
                                            type: str
                                            sample: null
                                        message:
                                            description:
                                                - >-
                                                    The detailed status message, including for alerts and
                                                    error messages.
                                            type: str
                                            sample: null
                                        time:
                                            description:
                                                - The time of the status.
                                            type: str
                                            sample: null
                        vm_health:
                            description:
                                - The health status for the VM.
                            type: dict
                            sample: null
                            contains:
                                status:
                                    description:
                                        - The health status information for the VM.
                                    type: dict
                                    sample: null
                                    contains:
                                        code:
                                            description:
                                                - The status code.
                                            type: str
                                            sample: null
                                        level:
                                            description:
                                                - The level code.
                                            type: sealed-choice
                                            sample: null
                                        display_status:
                                            description:
                                                - The short localizable label for the status.
                                            type: str
                                            sample: null
                                        message:
                                            description:
                                                - >-
                                                    The detailed status message, including for alerts and
                                                    error messages.
                                            type: str
                                            sample: null
                                        time:
                                            description:
                                                - The time of the status.
                                            type: str
                                            sample: null
                        boot_diagnostics:
                            description:
                                - >-
                                    Boot Diagnostics is a debugging feature which allows you to
                                    view Console Output and Screenshot to diagnose VM status.
                                    :code:`<br>`:code:`<br>` You can easily view the output of
                                    your console log. :code:`<br>`:code:`<br>` Azure also enables
                                    you to see a screenshot of the VM from the hypervisor.
                            type: dict
                            sample: null
                            contains:
                                status:
                                    description:
                                        - >-
                                            The boot diagnostics status information for the VM.
                                            :code:`<br>`:code:`<br>` NOTE: It will be set only if
                                            there are errors encountered in enabling boot diagnostics.
                                    type: dict
                                    sample: null
                                    contains:
                                        code:
                                            description:
                                                - The status code.
                                            type: str
                                            sample: null
                                        level:
                                            description:
                                                - The level code.
                                            type: sealed-choice
                                            sample: null
                                        display_status:
                                            description:
                                                - The short localizable label for the status.
                                            type: str
                                            sample: null
                                        message:
                                            description:
                                                - >-
                                                    The detailed status message, including for alerts and
                                                    error messages.
                                            type: str
                                            sample: null
                                        time:
                                            description:
                                                - The time of the status.
                                            type: str
                                            sample: null
                        statuses:
                            description:
                                - The resource status information.
                            type: list
                            sample: null
                            contains:
                                code:
                                    description:
                                        - The status code.
                                    type: str
                                    sample: null
                                level:
                                    description:
                                        - The level code.
                                    type: sealed-choice
                                    sample: null
                                display_status:
                                    description:
                                        - The short localizable label for the status.
                                    type: str
                                    sample: null
                                message:
                                    description:
                                        - >-
                                            The detailed status message, including for alerts and
                                            error messages.
                                    type: str
                                    sample: null
                                time:
                                    description:
                                        - The time of the status.
                                    type: str
                                    sample: null
                        placement_group_id:
                            description:
                                - >-
                                    The placement group in which the VM is running. If the VM is
                                    deallocated it will not have a placementGroupId.
                            type: str
                            sample: null
                hardware_profile:
                    description:
                        - Specifies the hardware settings for the virtual machine.
                    type: dict
                    sample: null
                    contains:
                        vm_size:
                            description:
                                - >-
                                    Specifies the size of the virtual machine. For more
                                    information about virtual machine sizes, see `Sizes for
                                    virtual machines
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-sizes?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                                    :code:`<br>`:code:`<br>` The available VM sizes depend on
                                    region and availability set. For a list of available sizes use
                                    these APIs:  :code:`<br>`:code:`<br>` `List all available
                                    virtual machine sizes in an availability set
                                    <https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes>`_
                                    :code:`<br>`:code:`<br>` `List all available virtual machine
                                    sizes in a region
                                    <https://docs.microsoft.com/rest/api/compute/virtualmachinesizes/list>`_
                                    :code:`<br>`:code:`<br>` `List all available virtual machine
                                    sizes for resizing
                                    <https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes>`_
                            type: str
                            sample: null
                storage_profile:
                    description:
                        - Specifies the storage settings for the virtual machine disks.
                    type: dict
                    sample: null
                    contains:
                        image_reference:
                            description:
                                - >-
                                    Specifies information about the image to use. You can specify
                                    information about platform images, marketplace images, or
                                    virtual machine images. This element is required when you want
                                    to use a platform image, marketplace image, or virtual machine
                                    image, but is not used in other creation operations.
                            type: dict
                            sample: null
                            contains:
                                publisher:
                                    description:
                                        - The image publisher.
                                    type: str
                                    sample: null
                                offer:
                                    description:
                                        - >-
                                            Specifies the offer of the platform image or marketplace
                                            image used to create the virtual machine.
                                    type: str
                                    sample: null
                                sku:
                                    description:
                                        - The image SKU.
                                    type: str
                                    sample: null
                                version:
                                    description:
                                        - >-
                                            Specifies the version of the platform image or marketplace
                                            image used to create the virtual machine. The allowed
                                            formats are Major.Minor.Build or 'latest'. Major, Minor,
                                            and Build are decimal numbers. Specify 'latest' to use the
                                            latest version of an image available at deploy time. Even
                                            if you use 'latest', the VM image will not automatically
                                            update after deploy time even if a new version becomes
                                            available.
                                    type: str
                                    sample: null
                        os_disk:
                            description:
                                - >-
                                    Specifies information about the operating system disk used by
                                    the virtual machine. :code:`<br>`:code:`<br>` For more
                                    information about disks, see `About disks and VHDs for Azure
                                    virtual machines
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                            type: dict
                            sample: null
                            contains:
                                os_type:
                                    description:
                                        - >-
                                            This property allows you to specify the type of the OS
                                            that is included in the disk if creating a VM from
                                            user-image or a specialized VHD. :code:`<br>`:code:`<br>`
                                            Possible values are: :code:`<br>`:code:`<br>` **Windows**
                                            :code:`<br>`:code:`<br>` **Linux**
                                    type: sealed-choice
                                    sample: null
                                encryption_settings:
                                    description:
                                        - >-
                                            Specifies the encryption settings for the OS Disk.
                                            :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
                                    type: dict
                                    sample: null
                                    contains:
                                        disk_encryption_key:
                                            description:
                                                - >-
                                                    Specifies the location of the disk encryption key,
                                                    which is a Key Vault Secret.
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
                                                        - >-
                                                            The relative URL of the Key Vault containing the
                                                            secret.
                                                    returned: always
                                                    type: dict
                                                    sample: null
                                                    contains:
                                                        id:
                                                            description:
                                                                - Resource Id
                                                            type: str
                                                            sample: null
                                        key_encryption_key:
                                            description:
                                                - >-
                                                    Specifies the location of the key encryption key in
                                                    Key Vault.
                                            type: dict
                                            sample: null
                                            contains:
                                                key_url:
                                                    description:
                                                        - >-
                                                            The URL referencing a key encryption key in Key
                                                            Vault.
                                                    returned: always
                                                    type: str
                                                    sample: null
                                                source_vault:
                                                    description:
                                                        - >-
                                                            The relative URL of the Key Vault containing the
                                                            key.
                                                    returned: always
                                                    type: dict
                                                    sample: null
                                                    contains:
                                                        id:
                                                            description:
                                                                - Resource Id
                                                            type: str
                                                            sample: null
                                        enabled:
                                            description:
                                                - >-
                                                    Specifies whether disk encryption should be enabled on
                                                    the virtual machine.
                                            type: bool
                                            sample: null
                                name:
                                    description:
                                        - The disk name.
                                    type: str
                                    sample: null
                                vhd:
                                    description:
                                        - The virtual hard disk.
                                    type: dict
                                    sample: null
                                    contains:
                                        uri:
                                            description:
                                                - Specifies the virtual hard disk's uri.
                                            type: str
                                            sample: null
                                image:
                                    description:
                                        - >-
                                            The source user image virtual hard disk. The virtual hard
                                            disk will be copied before being attached to the virtual
                                            machine. If SourceImage is provided, the destination
                                            virtual hard drive must not exist.
                                    type: dict
                                    sample: null
                                    contains:
                                        uri:
                                            description:
                                                - Specifies the virtual hard disk's uri.
                                            type: str
                                            sample: null
                                caching:
                                    description:
                                        - >-
                                            Specifies the caching requirements.
                                            :code:`<br>`:code:`<br>` Possible values are:
                                            :code:`<br>`:code:`<br>` **None** :code:`<br>`:code:`<br>`
                                            **ReadOnly** :code:`<br>`:code:`<br>` **ReadWrite**
                                            :code:`<br>`:code:`<br>` Default: **None** for Standard
                                            storage. **ReadOnly** for Premium storage.
                                    type: sealed-choice
                                    sample: null
                                write_accelerator_enabled:
                                    description:
                                        - >-
                                            Specifies whether writeAccelerator should be enabled or
                                            disabled on the disk.
                                    type: bool
                                    sample: null
                                diff_disk_settings:
                                    description:
                                        - >-
                                            Specifies the ephemeral Disk Settings for the operating
                                            system disk used by the virtual machine.
                                    type: dict
                                    sample: null
                                    contains:
                                        option:
                                            description:
                                                - >-
                                                    Specifies the ephemeral disk settings for operating
                                                    system disk.
                                            type: str
                                            sample: null
                                        placement:
                                            description:
                                                - >-
                                                    Specifies the ephemeral disk placement for operating
                                                    system disk.:code:`<br>`:code:`<br>` Possible values
                                                    are: :code:`<br>`:code:`<br>` **CacheDisk**
                                                    :code:`<br>`:code:`<br>` **ResourceDisk**
                                                    :code:`<br>`:code:`<br>` Default: **CacheDisk** if one
                                                    is configured for the VM size otherwise
                                                    **ResourceDisk** is used.:code:`<br>`:code:`<br>`
                                                    Refer to VM size documentation for Windows VM at
                                                    https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
                                                    and Linux VM at
                                                    https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes
                                                    to check which VM sizes exposes a cache disk.
                                            type: str
                                            sample: null
                                create_option:
                                    description:
                                        - >-
                                            Specifies how the virtual machine should be
                                            created.:code:`<br>`:code:`<br>` Possible values
                                            are::code:`<br>`:code:`<br>` **Attach** \u2013 This value
                                            is used when you are using a specialized disk to create
                                            the virtual machine.:code:`<br>`:code:`<br>` **FromImage**
                                            \u2013 This value is used when you are using an image to
                                            create the virtual machine. If you are using a platform
                                            image, you also use the imageReference element described
                                            above. If you are using a marketplace image, you  also use
                                            the plan element previously described.
                                    returned: always
                                    type: str
                                    sample: null
                                disk_size_gb:
                                    description:
                                        - >-
                                            Specifies the size of an empty data disk in gigabytes.
                                            This element can be used to overwrite the size of the disk
                                            in a virtual machine image. :code:`<br>`:code:`<br>` This
                                            value cannot be larger than 1023 GB
                                    type: int
                                    sample: null
                                managed_disk:
                                    description:
                                        - The managed disk parameters.
                                    type: dict
                                    sample: null
                                    contains:
                                        storage_account_type:
                                            description:
                                                - >-
                                                    Specifies the storage account type for the managed
                                                    disk. NOTE: UltraSSD_LRS can only be used with data
                                                    disks, it cannot be used with OS Disk.
                                            type: str
                                            sample: null
                                        disk_encryption_set:
                                            description:
                                                - >-
                                                    Specifies the customer managed disk encryption set
                                                    resource id for the managed disk.
                                            type: dict
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    type: str
                                                    sample: null
                        data_disks:
                            description:
                                - >-
                                    Specifies the parameters that are used to add a data disk to a
                                    virtual machine. :code:`<br>`:code:`<br>` For more information
                                    about disks, see `About disks and VHDs for Azure virtual
                                    machines
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
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
                                name:
                                    description:
                                        - The disk name.
                                    type: str
                                    sample: null
                                vhd:
                                    description:
                                        - The virtual hard disk.
                                    type: dict
                                    sample: null
                                    contains:
                                        uri:
                                            description:
                                                - Specifies the virtual hard disk's uri.
                                            type: str
                                            sample: null
                                image:
                                    description:
                                        - >-
                                            The source user image virtual hard disk. The virtual hard
                                            disk will be copied before being attached to the virtual
                                            machine. If SourceImage is provided, the destination
                                            virtual hard drive must not exist.
                                    type: dict
                                    sample: null
                                    contains:
                                        uri:
                                            description:
                                                - Specifies the virtual hard disk's uri.
                                            type: str
                                            sample: null
                                caching:
                                    description:
                                        - >-
                                            Specifies the caching requirements.
                                            :code:`<br>`:code:`<br>` Possible values are:
                                            :code:`<br>`:code:`<br>` **None** :code:`<br>`:code:`<br>`
                                            **ReadOnly** :code:`<br>`:code:`<br>` **ReadWrite**
                                            :code:`<br>`:code:`<br>` Default: **None for Standard
                                            storage. ReadOnly for Premium storage**
                                    type: sealed-choice
                                    sample: null
                                write_accelerator_enabled:
                                    description:
                                        - >-
                                            Specifies whether writeAccelerator should be enabled or
                                            disabled on the disk.
                                    type: bool
                                    sample: null
                                create_option:
                                    description:
                                        - >-
                                            Specifies how the virtual machine should be
                                            created.:code:`<br>`:code:`<br>` Possible values
                                            are::code:`<br>`:code:`<br>` **Attach** \u2013 This value
                                            is used when you are using a specialized disk to create
                                            the virtual machine.:code:`<br>`:code:`<br>` **FromImage**
                                            \u2013 This value is used when you are using an image to
                                            create the virtual machine. If you are using a platform
                                            image, you also use the imageReference element described
                                            above. If you are using a marketplace image, you  also use
                                            the plan element previously described.
                                    returned: always
                                    type: str
                                    sample: null
                                disk_size_gb:
                                    description:
                                        - >-
                                            Specifies the size of an empty data disk in gigabytes.
                                            This element can be used to overwrite the size of the disk
                                            in a virtual machine image. :code:`<br>`:code:`<br>` This
                                            value cannot be larger than 1023 GB
                                    type: int
                                    sample: null
                                managed_disk:
                                    description:
                                        - The managed disk parameters.
                                    type: dict
                                    sample: null
                                    contains:
                                        storage_account_type:
                                            description:
                                                - >-
                                                    Specifies the storage account type for the managed
                                                    disk. NOTE: UltraSSD_LRS can only be used with data
                                                    disks, it cannot be used with OS Disk.
                                            type: str
                                            sample: null
                                        disk_encryption_set:
                                            description:
                                                - >-
                                                    Specifies the customer managed disk encryption set
                                                    resource id for the managed disk.
                                            type: dict
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    type: str
                                                    sample: null
                                to_be_detached:
                                    description:
                                        - >-
                                            Specifies whether the data disk is in process of
                                            detachment from the VirtualMachine/VirtualMachineScaleset
                                    type: bool
                                    sample: null
                additional_capabilities:
                    description:
                        - >-
                            Specifies additional capabilities enabled or disabled on the
                            virtual machine in the scale set. For instance: whether the
                            virtual machine has the capability to support attaching managed
                            data disks with UltraSSD_LRS storage account type.
                    type: dict
                    sample: null
                    contains:
                        ultra_ssd_enabled:
                            description:
                                - >-
                                    The flag that enables or disables a capability to have one or
                                    more managed data disks with UltraSSD_LRS storage account type
                                    on the VM or VMSS. Managed disks with storage account type
                                    UltraSSD_LRS can be added to a virtual machine or virtual
                                    machine scale set only if this property is enabled.
                            type: bool
                            sample: null
                os_profile:
                    description:
                        - Specifies the operating system settings for the virtual machine.
                    type: dict
                    sample: null
                    contains:
                        computer_name:
                            description:
                                - >-
                                    Specifies the host OS name of the virtual machine.
                                    :code:`<br>`:code:`<br>` This name cannot be updated after the
                                    VM is created. :code:`<br>`:code:`<br>` **Max-length
                                    (Windows):** 15 characters :code:`<br>`:code:`<br>`
                                    **Max-length (Linux):** 64 characters.
                                    :code:`<br>`:code:`<br>` For naming conventions and
                                    restrictions see `Azure infrastructure services implementation
                                    guidelines
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-infrastructure-subscription-accounts-guidelines?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#1-naming-conventions>`_.
                            type: str
                            sample: null
                        admin_username:
                            description:
                                - >-
                                    Specifies the name of the administrator account.
                                    :code:`<br>`:code:`<br>` This property cannot be updated after
                                    the VM is created. :code:`<br>`:code:`<br>` **Windows-only
                                    restriction:** Cannot end in "." :code:`<br>`:code:`<br>`
                                    **Disallowed values:** "administrator", "admin", "user",
                                    "user1", "test", "user2", "test1", "user3", "admin1", "1",
                                    "123", "a", "actuser", "adm", "admin2", "aspnet", "backup",
                                    "console", "david", "guest", "john", "owner", "root",
                                    "server", "sql", "support", "support_388945a0", "sys",
                                    "test2", "test3", "user4", "user5". :code:`<br>`:code:`<br>`
                                    **Minimum-length (Linux):** 1  character
                                    :code:`<br>`:code:`<br>` **Max-length (Linux):** 64 characters
                                    :code:`<br>`:code:`<br>` **Max-length (Windows):** 20
                                    characters  :code:`<br>`:code:`<br>`:code:`<li>` For root
                                    access to the Linux VM, see `Using root privileges on Linux
                                    virtual machines in Azure
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_\
                                    :code:`<br>`:code:`<li>` For a list of built-in system users
                                    on Linux that should not be used in this field, see `Selecting
                                    User Names for Linux on Azure
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-usernames?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                            type: str
                            sample: null
                        admin_password:
                            description:
                                - >-
                                    Specifies the password of the administrator account.
                                    :code:`<br>`:code:`<br>` **Minimum-length (Windows):** 8
                                    characters :code:`<br>`:code:`<br>` **Minimum-length
                                    (Linux):** 6 characters :code:`<br>`:code:`<br>` **Max-length
                                    (Windows):** 123 characters :code:`<br>`:code:`<br>`
                                    **Max-length (Linux):** 72 characters :code:`<br>`:code:`<br>`
                                    **Complexity requirements:** 3 out of 4 conditions below need
                                    to be fulfilled :code:`<br>` Has lower characters
                                    :code:`<br>`Has upper characters :code:`<br>` Has a digit
                                    :code:`<br>` Has a special character (Regex match [\W_])
                                    :code:`<br>`:code:`<br>` **Disallowed values:** "abc@123",
                                    "P@$$w0rd", "P@ssw0rd", "P@ssword123", "Pa$$word",
                                    "pass@word1", "Password!", "Password1", "Password22",
                                    "iloveyou!" :code:`<br>`:code:`<br>` For resetting the
                                    password, see `How to reset the Remote Desktop service or its
                                    login password in a Windows VM
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                                    :code:`<br>`:code:`<br>` For resetting root password, see
                                    `Manage users, SSH, and check or repair disks on Azure Linux
                                    VMs using the VMAccess Extension
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password>`_
                            type: str
                            sample: null
                        custom_data:
                            description:
                                - >-
                                    Specifies a base-64 encoded string of custom data. The base-64
                                    encoded string is decoded to a binary array that is saved as a
                                    file on the Virtual Machine. The maximum length of the binary
                                    array is 65535 bytes. :code:`<br>`:code:`<br>` **Note: Do not
                                    pass any secrets or passwords in customData property**
                                    :code:`<br>`:code:`<br>` This property cannot be updated after
                                    the VM is created. :code:`<br>`:code:`<br>` customData is
                                    passed to the VM to be saved as a file, for more information
                                    see `Custom Data on Azure VMs
                                    <https://azure.microsoft.com/en-us/blog/custom-data-and-cloud-init-on-windows-azure/>`_
                                    :code:`<br>`:code:`<br>` For using cloud-init for your Linux
                                    VM, see `Using cloud-init to customize a Linux VM during
                                    creation
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                            type: str
                            sample: null
                        windows_configuration:
                            description:
                                - >-
                                    Specifies Windows operating system settings on the virtual
                                    machine.
                            type: dict
                            sample: null
                            contains:
                                provision_vm_agent:
                                    description:
                                        - >-
                                            Indicates whether virtual machine agent should be
                                            provisioned on the virtual machine.
                                            :code:`<br>`:code:`<br>` When this property is not
                                            specified in the request body, default behavior is to set
                                            it to true.  This will ensure that VM Agent is installed
                                            on the VM so that extensions can be added to the VM later.
                                    type: bool
                                    sample: null
                                enable_automatic_updates:
                                    description:
                                        - >-
                                            Indicates whether Automatic Updates is enabled for the
                                            Windows virtual machine. Default value is true.
                                            :code:`<br>`:code:`<br>` For virtual machine scale sets,
                                            this property can be updated and updates will take effect
                                            on OS reprovisioning.
                                    type: bool
                                    sample: null
                                time_zone:
                                    description:
                                        - >-
                                            Specifies the time zone of the virtual machine. e.g.
                                            "Pacific Standard Time". :code:`<br>`:code:`<br>` Possible
                                            values can be `TimeZoneInfo.Id
                                            <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.id?#System_TimeZoneInfo_Id>`_
                                            value from time zones returned by
                                            `TimeZoneInfo.GetSystemTimeZones
                                            <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.getsystemtimezones>`_.
                                    type: str
                                    sample: null
                                additional_unattend_content:
                                    description:
                                        - >-
                                            Specifies additional base-64 encoded XML formatted
                                            information that can be included in the Unattend.xml file,
                                            which is used by Windows Setup.
                                    type: list
                                    sample: null
                                    contains:
                                        pass_name:
                                            description:
                                                - >-
                                                    The pass name. Currently, the only allowable value is
                                                    OobeSystem.
                                            type: constant
                                            sample: null
                                        component_name:
                                            description:
                                                - >-
                                                    The component name. Currently, the only allowable
                                                    value is Microsoft-Windows-Shell-Setup.
                                            type: constant
                                            sample: null
                                        setting_name:
                                            description:
                                                - >-
                                                    Specifies the name of the setting to which the content
                                                    applies. Possible values are: FirstLogonCommands and
                                                    AutoLogon.
                                            type: sealed-choice
                                            sample: null
                                        content:
                                            description:
                                                - >-
                                                    Specifies the XML formatted content that is added to
                                                    the unattend.xml file for the specified path and
                                                    component. The XML must be less than 4KB and must
                                                    include the root element for the setting or feature
                                                    that is being inserted.
                                            type: str
                                            sample: null
                                patch_settings:
                                    description:
                                        - Specifies settings related to in-guest patching (KBs).
                                    type: dict
                                    sample: null
                                    contains:
                                        patch_mode:
                                            description:
                                                - >-
                                                    Specifies the mode of in-guest patching to IaaS
                                                    virtual machine.:code:`<br />`:code:`<br />` Possible
                                                    values are::code:`<br />`:code:`<br />` **Manual** -
                                                    You  control the application of patches to a virtual
                                                    machine. You do this by applying patches manually
                                                    inside the VM. In this mode, automatic updates are
                                                    disabled; the property
                                                    WindowsConfiguration.enableAutomaticUpdates must be
                                                    false:code:`<br />`:code:`<br />` **AutomaticByOS** -
                                                    The virtual machine will automatically be updated by
                                                    the OS. The property
                                                    WindowsConfiguration.enableAutomaticUpdates must be
                                                    true. :code:`<br />`:code:`<br />` **
                                                    AutomaticByPlatform** - the virtual machine will
                                                    automatically updated by the platform. The properties
                                                    provisionVMAgent and
                                                    WindowsConfiguration.enableAutomaticUpdates must be
                                                    true
                                            type: str
                                            sample: null
                                win_rm:
                                    description:
                                        - >-
                                            Specifies the Windows Remote Management listeners. This
                                            enables remote Windows PowerShell.
                                    type: dict
                                    sample: null
                                    contains:
                                        listeners:
                                            description:
                                                - The list of Windows Remote Management listeners
                                            type: list
                                            sample: null
                                            contains:
                                                protocol:
                                                    description:
                                                        - >-
                                                            Specifies the protocol of WinRM listener.
                                                            :code:`<br>`:code:`<br>` Possible values are:
                                                            :code:`<br>`\ **http** :code:`<br>`:code:`<br>`
                                                            **https**
                                                    type: sealed-choice
                                                    sample: null
                                                certificate_url:
                                                    description:
                                                        - >-
                                                            This is the URL of a certificate that has been
                                                            uploaded to Key Vault as a secret. For adding a
                                                            secret to the Key Vault, see `Add a key or secret
                                                            to the key vault
                                                            <https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add>`_.
                                                            In this case, your certificate needs to be It is
                                                            the Base64 encoding of the following JSON Object
                                                            which is encoded in UTF-8:
                                                            :code:`<br>`:code:`<br>` {:code:`<br>` 
                                                            "data":":code:`<Base64-encoded-certificate>`",:code:`<br>` 
                                                            "dataType":"pfx",:code:`<br>` 
                                                            "password":":code:`<pfx-file-password>`":code:`<br>`}
                                                    type: str
                                                    sample: null
                        linux_configuration:
                            description:
                                - >-
                                    Specifies the Linux operating system settings on the virtual
                                    machine. :code:`<br>`:code:`<br>`For a list of supported Linux
                                    distributions, see `Linux on Azure-Endorsed Distributions
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-endorsed-distros?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                                    :code:`<br>`:code:`<br>` For running non-endorsed
                                    distributions, see `Information for Non-Endorsed Distributions
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-create-upload-generic?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
                            type: dict
                            sample: null
                            contains:
                                disable_password_authentication:
                                    description:
                                        - >-
                                            Specifies whether password authentication should be
                                            disabled.
                                    type: bool
                                    sample: null
                                ssh:
                                    description:
                                        - Specifies the ssh key configuration for a Linux OS.
                                    type: dict
                                    sample: null
                                    contains:
                                        public_keys:
                                            description:
                                                - >-
                                                    The list of SSH public keys used to authenticate with
                                                    linux based VMs.
                                            type: list
                                            sample: null
                                            contains:
                                                path:
                                                    description:
                                                        - >-
                                                            Specifies the full path on the created VM where
                                                            ssh public key is stored. If the file already
                                                            exists, the specified key is appended to the file.
                                                            Example: /home/user/.ssh/authorized_keys
                                                    type: str
                                                    sample: null
                                                key_data:
                                                    description:
                                                        - >-
                                                            SSH public key certificate used to authenticate
                                                            with the VM through ssh. The key needs to be at
                                                            least 2048-bit and in ssh-rsa format.
                                                            :code:`<br>`:code:`<br>` For creating ssh keys,
                                                            see `Create SSH keys on Linux and Mac for Linux
                                                            VMs in Azure
                                                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-mac-create-ssh-keys?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
                                                    type: str
                                                    sample: null
                                provision_vm_agent:
                                    description:
                                        - >-
                                            Indicates whether virtual machine agent should be
                                            provisioned on the virtual machine.
                                            :code:`<br>`:code:`<br>` When this property is not
                                            specified in the request body, default behavior is to set
                                            it to true.  This will ensure that VM Agent is installed
                                            on the VM so that extensions can be added to the VM later.
                                    type: bool
                                    sample: null
                        secrets:
                            description:
                                - >-
                                    Specifies set of certificates that should be installed onto
                                    the virtual machine.
                            type: list
                            sample: null
                            contains:
                                source_vault:
                                    description:
                                        - >-
                                            The relative URL of the Key Vault containing all of the
                                            certificates in VaultCertificates.
                                    type: dict
                                    sample: null
                                    contains:
                                        id:
                                            description:
                                                - Resource Id
                                            type: str
                                            sample: null
                                vault_certificates:
                                    description:
                                        - >-
                                            The list of key vault references in SourceVault which
                                            contain certificates.
                                    type: list
                                    sample: null
                                    contains:
                                        certificate_url:
                                            description:
                                                - >-
                                                    This is the URL of a certificate that has been
                                                    uploaded to Key Vault as a secret. For adding a secret
                                                    to the Key Vault, see `Add a key or secret to the key
                                                    vault
                                                    <https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add>`_.
                                                    In this case, your certificate needs to be It is the
                                                    Base64 encoding of the following JSON Object which is
                                                    encoded in UTF-8: :code:`<br>`:code:`<br>`
                                                    {:code:`<br>` 
                                                    "data":":code:`<Base64-encoded-certificate>`",:code:`<br>` 
                                                    "dataType":"pfx",:code:`<br>` 
                                                    "password":":code:`<pfx-file-password>`":code:`<br>`}
                                            type: str
                                            sample: null
                                        certificate_store:
                                            description:
                                                - >-
                                                    For Windows VMs, specifies the certificate store on
                                                    the Virtual Machine to which the certificate should be
                                                    added. The specified certificate store is implicitly
                                                    in the LocalMachine account.
                                                    :code:`<br>`:code:`<br>`For Linux VMs, the certificate
                                                    file is placed under the /var/lib/waagent directory,
                                                    with the file name &lt;UppercaseThumbprint&gt;.crt for
                                                    the X509 certificate file and
                                                    &lt;UppercaseThumbprint&gt;.prv for private key. Both
                                                    of these files are .pem formatted.
                                            type: str
                                            sample: null
                        allow_extension_operations:
                            description:
                                - >-
                                    Specifies whether extension operations should be allowed on
                                    the virtual machine. :code:`<br>`:code:`<br>`This may only be
                                    set to False when no extensions are present on the virtual
                                    machine.
                            type: bool
                            sample: null
                        require_guest_provision_signal:
                            description:
                                - >-
                                    Specifies whether the guest provision signal is required to
                                    infer provision success of the virtual machine.  **Note: This
                                    property is for private testing only, and all customers must
                                    not set the property to false.**
                            type: bool
                            sample: null
                security_profile:
                    description:
                        - >-
                            Specifies the Security related profile settings for the virtual
                            machine.
                    type: dict
                    sample: null
                    contains:
                        encryption_at_host:
                            description:
                                - >-
                                    This property can be used by user in the request to enable or
                                    disable the Host Encryption for the virtual machine or virtual
                                    machine scale set. This will enable the encryption for all the
                                    disks including Resource/Temp disk at host itself.
                                    :code:`<br>`:code:`<br>` Default: The Encryption at host will
                                    be disabled unless this property is set to true for the
                                    resource.
                            type: bool
                            sample: null
                network_profile:
                    description:
                        - Specifies the network interfaces of the virtual machine.
                    type: dict
                    sample: null
                    contains:
                        network_interfaces:
                            description:
                                - >-
                                    Specifies the list of resource Ids for the network interfaces
                                    associated with the virtual machine.
                            type: list
                            sample: null
                            contains:
                                primary:
                                    description:
                                        - >-
                                            Specifies the primary network interface in case the
                                            virtual machine has more than 1 network interface.
                                    type: bool
                                    sample: null
                network_profile_configuration:
                    description:
                        - >-
                            Specifies the network profile configuration of the virtual
                            machine.
                    type: dict
                    sample: null
                    contains:
                        network_interface_configurations:
                            description:
                                - The list of network configurations.
                            type: list
                            sample: null
                            contains:
                                name:
                                    description:
                                        - The network configuration name.
                                    returned: always
                                    type: str
                                    sample: null
                                primary:
                                    description:
                                        - >-
                                            Specifies the primary network interface in case the
                                            virtual machine has more than 1 network interface.
                                    type: bool
                                    sample: null
                                enable_accelerated_networking:
                                    description:
                                        - >-
                                            Specifies whether the network interface is accelerated
                                            networking-enabled.
                                    type: bool
                                    sample: null
                                network_security_group:
                                    description:
                                        - The network security group.
                                    type: dict
                                    sample: null
                                    contains:
                                        id:
                                            description:
                                                - Resource Id
                                            type: str
                                            sample: null
                                dns_settings:
                                    description:
                                        - The dns settings to be applied on the network interfaces.
                                    type: dict
                                    sample: null
                                    contains:
                                        dns_servers:
                                            description:
                                                - List of DNS servers IP addresses
                                            type: list
                                            sample: null
                                ip_configurations:
                                    description:
                                        - Specifies the IP configurations of the network interface.
                                    type: list
                                    sample: null
                                    contains:
                                        name:
                                            description:
                                                - The IP configuration name.
                                            returned: always
                                            type: str
                                            sample: null
                                        subnet:
                                            description:
                                                - Specifies the identifier of the subnet.
                                            type: dict
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - >-
                                                            The ARM resource id in the form of
                                                            /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
                                                    type: str
                                                    sample: null
                                        primary:
                                            description:
                                                - >-
                                                    Specifies the primary network interface in case the
                                                    virtual machine has more than 1 network interface.
                                            type: bool
                                            sample: null
                                        public_ip_address_configuration:
                                            description:
                                                - The publicIPAddressConfiguration.
                                            type: dict
                                            sample: null
                                            contains:
                                                name:
                                                    description:
                                                        - The publicIP address configuration name.
                                                    returned: always
                                                    type: str
                                                    sample: null
                                                idle_timeout_in_minutes:
                                                    description:
                                                        - The idle timeout of the public IP address.
                                                    type: int
                                                    sample: null
                                                dns_settings:
                                                    description:
                                                        - >-
                                                            The dns settings to be applied on the publicIP
                                                            addresses .
                                                    type: dict
                                                    sample: null
                                                    contains:
                                                        domain_name_label:
                                                            description:
                                                                - >-
                                                                    The Domain name label.The concatenation of the
                                                                    domain name label and vm index will be the
                                                                    domain name labels of the PublicIPAddress
                                                                    resources that will be created
                                                            returned: always
                                                            type: str
                                                            sample: null
                                                ip_tags:
                                                    description:
                                                        - >-
                                                            The list of IP tags associated with the public IP
                                                            address.
                                                    type: list
                                                    sample: null
                                                    contains:
                                                        ip_tag_type:
                                                            description:
                                                                - 'IP tag type. Example: FirstPartyUsage.'
                                                            type: str
                                                            sample: null
                                                        tag:
                                                            description:
                                                                - >-
                                                                    IP tag associated with the public IP. Example:
                                                                    SQL, Storage etc.
                                                            type: str
                                                            sample: null
                                                public_ip_prefix:
                                                    description:
                                                        - >-
                                                            The PublicIPPrefix from which to allocate publicIP
                                                            addresses.
                                                    type: dict
                                                    sample: null
                                                    contains:
                                                        id:
                                                            description:
                                                                - Resource Id
                                                            type: str
                                                            sample: null
                                                public_ip_address_version:
                                                    description:
                                                        - >-
                                                            Available from Api-Version 2019-07-01 onwards, it
                                                            represents whether the specific ipconfiguration is
                                                            IPv4 or IPv6. Default is taken as IPv4. Possible
                                                            values are: 'IPv4' and 'IPv6'.
                                                    type: str
                                                    sample: null
                                        private_ip_address_version:
                                            description:
                                                - >-
                                                    Available from Api-Version 2017-03-30 onwards, it
                                                    represents whether the specific ipconfiguration is
                                                    IPv4 or IPv6. Default is taken as IPv4.  Possible
                                                    values are: 'IPv4' and 'IPv6'.
                                            type: str
                                            sample: null
                                        application_gateway_backend_address_pools:
                                            description:
                                                - >-
                                                    Specifies an array of references to backend address
                                                    pools of application gateways. A scale set can
                                                    reference backend address pools of multiple
                                                    application gateways. Multiple scale sets cannot use
                                                    the same application gateway.
                                            type: list
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    type: str
                                                    sample: null
                                        application_security_groups:
                                            description:
                                                - >-
                                                    Specifies an array of references to application
                                                    security group.
                                            type: list
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    type: str
                                                    sample: null
                                        load_balancer_backend_address_pools:
                                            description:
                                                - >-
                                                    Specifies an array of references to backend address
                                                    pools of load balancers. A scale set can reference
                                                    backend address pools of one public and one internal
                                                    load balancer. Multiple scale sets cannot use the same
                                                    basic sku load balancer.
                                            type: list
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    type: str
                                                    sample: null
                                        load_balancer_inbound_nat_pools:
                                            description:
                                                - >-
                                                    Specifies an array of references to inbound Nat pools
                                                    of the load balancers. A scale set can reference
                                                    inbound nat pools of one public and one internal load
                                                    balancer. Multiple scale sets cannot use the same
                                                    basic sku load balancer.
                                            type: list
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    type: str
                                                    sample: null
                                enable_ip_forwarding:
                                    description:
                                        - Whether IP forwarding enabled on this NIC.
                                    type: bool
                                    sample: null
                diagnostics_profile:
                    description:
                        - >-
                            Specifies the boot diagnostic settings state.
                            :code:`<br>`:code:`<br>`Minimum api-version: 2015-06-15.
                    type: dict
                    sample: null
                    contains:
                        boot_diagnostics:
                            description:
                                - >-
                                    Boot Diagnostics is a debugging feature which allows you to
                                    view Console Output and Screenshot to diagnose VM status.
                                    :code:`<br>`:code:`<br>` You can easily view the output of
                                    your console log. :code:`<br>`:code:`<br>` Azure also enables
                                    you to see a screenshot of the VM from the hypervisor.
                            type: dict
                            sample: null
                            contains:
                                enabled:
                                    description:
                                        - >-
                                            Whether boot diagnostics should be enabled on the Virtual
                                            Machine.
                                    type: bool
                                    sample: null
                                storage_uri:
                                    description:
                                        - >-
                                            Uri of the storage account to use for placing the console
                                            output and screenshot. :code:`<br>`:code:`<br>`If
                                            storageUri is not specified while enabling boot
                                            diagnostics, managed storage will be used.
                                    type: str
                                    sample: null
                availability_set:
                    description:
                        - >-
                            Specifies information about the availability set that the virtual
                            machine should be assigned to. Virtual machines specified in the
                            same availability set are allocated to different nodes to maximize
                            availability. For more information about availability sets, see
                            `Manage the availability of virtual machines
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-manage-availability?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                            :code:`<br>`:code:`<br>` For more information on Azure planned
                            maintenance, see `Planned maintenance for virtual machines in
                            Azure
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-planned-maintenance?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                            :code:`<br>`:code:`<br>` Currently, a VM can only be added to
                            availability set at creation time. An existing VM cannot be added
                            to an availability set.
                    type: dict
                    sample: null
                    contains:
                        id:
                            description:
                                - Resource Id
                            type: str
                            sample: null
                license_type:
                    description:
                        - >-
                            Specifies that the image or disk that is being used was licensed
                            on-premises. This element is only used for images that contain the
                            Windows Server operating system. :code:`<br>`:code:`<br>` Possible
                            values are: :code:`<br>`:code:`<br>` Windows_Client
                            :code:`<br>`:code:`<br>` Windows_Server :code:`<br>`:code:`<br>`
                            If this element is included in a request for an update, the value
                            must match the initial value. This value cannot be updated.
                            :code:`<br>`:code:`<br>` For more information, see `Azure Hybrid
                            Use Benefit for Windows Server
                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                            :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
                    type: str
                    sample: null
                protection_policy:
                    description:
                        - Specifies the protection policy of the virtual machine.
                    type: dict
                    sample: null
                    contains:
                        protect_from_scale_in:
                            description:
                                - >-
                                    Indicates that the virtual machine scale set VM shouldn't be
                                    considered for deletion during a scale-in operation.
                            type: bool
                            sample: null
                        protect_from_scale_set_actions:
                            description:
                                - >-
                                    Indicates that model updates or actions (including scale-in)
                                    initiated on the virtual machine scale set should not be
                                    applied to the virtual machine scale set VM.
                            type: bool
                            sample: null
        next_link:
            description:
                - >-
                    The uri to fetch the next page of Virtual Machine Scale Set VMs. Call
                    ListNext() with this to fetch the next page of VMSS VMs
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


class AzureRMVirtualMachineScaleSetVMInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            vm_scale_set_name=dict(
                type='str'
            ),
            instance_id=dict(
                type='str'
            ),
            expand=dict(
                type='constant'
            ),
            virtual_machine_scale_set_name=dict(
                type='str'
            ),
            filter=dict(
                type='str'
            ),
            select=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.vm_scale_set_name = None
        self.instance_id = None
        self.expand = None
        self.virtual_machine_scale_set_name = None
        self.filter = None
        self.select = None

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
        super(AzureRMVirtualMachineScaleSetVMInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.vm_scale_set_name is not None and
            self.instance_id is not None):
            self.results['virtual_machine_scale_set_vms'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.vm_scale_set_name is not None and
              self.instance_id is not None):
            self.results['virtual_machine_scale_set_vms'] = self.format_item(self.get_instance_view())
        elif (self.resource_group is not None and
              self.virtual_machine_scale_set_name is not None):
            self.results['virtual_machine_scale_set_vms'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vms.get(resource_group=self.resource_group,
                                                                          vm_scale_set_name=self.vm_scale_set_name,
                                                                          instance_id=self.instance_id,
                                                                          expand=self.expand)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get_instance_view(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vms.get_instance_view(resource_group=self.resource_group,
                                                                                        vm_scale_set_name=self.vm_scale_set_name,
                                                                                        instance_id=self.instance_id)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_set_vms.list(resource_group=self.resource_group,
                                                                           virtual_machine_scale_set_name=self.virtual_machine_scale_set_name,
                                                                           filter=self.filter,
                                                                           select=self.select,
                                                                           expand=self.expand)
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
    AzureRMVirtualMachineScaleSetVMInfo()


if __name__ == '__main__':
    main()
