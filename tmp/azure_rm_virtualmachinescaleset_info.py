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
module: azure_rm_virtualmachinescaleset_info
version_added: '2.9'
short_description: Get VirtualMachineScaleSet info.
description:
    - Get info of VirtualMachineScaleSet.
options:
    resource_group:
        description:
            - The name of the resource group.
        type: str
    vm_scale_set_name:
        description:
            - The name of the VM scale set.
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get a virtual machine scale set placed on a dedicated host group through automatic placement.
      azure_rm_virtualmachinescaleset_info: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: myVirtualMachineScaleSet
        

'''

RETURN = '''
virtual_machine_scale_sets:
    description: >-
        A list of dict results where the key is the name of the
        VirtualMachineScaleSet and the values are the facts for that
        VirtualMachineScaleSet.
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
        sku:
            description:
                - The virtual machine scale set sku.
            returned: always
            type: dict
            sample: null
            contains:
                name:
                    description:
                        - The sku name.
                    returned: always
                    type: str
                    sample: null
                tier:
                    description:
                        - >-
                            Specifies the tier of virtual machines in a scale set.:code:`<br
                            />`:code:`<br />` Possible Values::code:`<br />`:code:`<br />`
                            **Standard**\ :code:`<br />`:code:`<br />` **Basic**
                    returned: always
                    type: str
                    sample: null
                capacity:
                    description:
                        - Specifies the number of virtual machines in the scale set.
                    returned: always
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
                            Specifies the product of the image from the marketplace. This is
                            the same value as Offer under the imageReference element.
                    returned: always
                    type: str
                    sample: null
                promotion_code:
                    description:
                        - The promotion code.
                    returned: always
                    type: str
                    sample: null
        identity:
            description:
                - 'The identity of the virtual machine scale set, if configured.'
            returned: always
            type: dict
            sample: null
            contains:
                type:
                    description:
                        - >-
                            The type of identity used for the virtual machine scale set. The
                            type 'SystemAssigned, UserAssigned' includes both an implicitly
                            created identity and a set of user assigned identities. The type
                            'None' will remove any identities from the virtual machine scale
                            set.
                    returned: always
                    type: sealed-choice
                    sample: null
                user_assigned_identities:
                    description:
                        - >-
                            The list of user identities associated with the virtual machine
                            scale set. The user identity dictionary key references will be ARM
                            resource ids in the form:
                            '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
                    returned: always
                    type: dict
                    sample: null
        zones:
            description:
                - >-
                    The virtual machine scale set zones. NOTE: Availability zones can only
                    be set when you create the scale set
            returned: always
            type: list
            sample: null
        upgrade_policy:
            description:
                - The upgrade policy.
            returned: always
            type: dict
            sample: null
            contains:
                mode:
                    description:
                        - >-
                            Specifies the mode of an upgrade to virtual machines in the scale
                            set.:code:`<br />`:code:`<br />` Possible values are::code:`<br
                            />`:code:`<br />` **Manual** - You  control the application of
                            updates to virtual machines in the scale set. You do this by using
                            the manualUpgrade action.:code:`<br />`:code:`<br />`
                            **Automatic** - All virtual machines in the scale set are 
                            automatically updated at the same time.
                    returned: always
                    type: sealed-choice
                    sample: null
                rolling_upgrade_policy:
                    description:
                        - >-
                            The configuration parameters used while performing a rolling
                            upgrade.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        max_batch_instance_percent:
                            description:
                                - >-
                                    The maximum percent of total virtual machine instances that
                                    will be upgraded simultaneously by the rolling upgrade in one
                                    batch. As this is a maximum, unhealthy instances in previous
                                    or future batches can cause the percentage of instances in a
                                    batch to decrease to ensure higher reliability. The default
                                    value for this parameter is 20%.
                            returned: always
                            type: int
                            sample: null
                        max_unhealthy_instance_percent:
                            description:
                                - >-
                                    The maximum percentage of the total virtual machine instances
                                    in the scale set that can be simultaneously unhealthy, either
                                    as a result of being upgraded, or by being found in an
                                    unhealthy state by the virtual machine health checks before
                                    the rolling upgrade aborts. This constraint will be checked
                                    prior to starting any batch. The default value for this
                                    parameter is 20%.
                            returned: always
                            type: int
                            sample: null
                        max_unhealthy_upgraded_instance_percent:
                            description:
                                - >-
                                    The maximum percentage of upgraded virtual machine instances
                                    that can be found to be in an unhealthy state. This check will
                                    happen after each batch is upgraded. If this percentage is
                                    ever exceeded, the rolling update aborts. The default value
                                    for this parameter is 20%.
                            returned: always
                            type: int
                            sample: null
                        pause_time_between_batches:
                            description:
                                - >-
                                    The wait time between completing the update for all virtual
                                    machines in one batch and starting the next batch. The time
                                    duration should be specified in ISO 8601 format. The default
                                    value is 0 seconds (PT0S).
                            returned: always
                            type: str
                            sample: null
                automatic_os_upgrade_policy:
                    description:
                        - Configuration parameters used for performing automatic OS Upgrade.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        enable_automatic_os_upgrade:
                            description:
                                - >-
                                    Indicates whether OS upgrades should automatically be applied
                                    to scale set instances in a rolling fashion when a newer
                                    version of the OS image becomes available. Default value is
                                    false. :code:`<br>`:code:`<br>` If this is set to true for
                                    Windows based scale sets, `enableAutomaticUpdates
                                    <https://docs.microsoft.com/dotnet/api/microsoft.azure.management.compute.models.windowsconfiguration.enableautomaticupdates?view=azure-dotnet>`_
                                    is automatically set to false and cannot be set to true.
                            returned: always
                            type: bool
                            sample: null
                        disable_automatic_rollback:
                            description:
                                - >-
                                    Whether OS image rollback feature should be disabled. Default
                                    value is false.
                            returned: always
                            type: bool
                            sample: null
        automatic_repairs_policy:
            description:
                - Policy for automatic repairs.
            returned: always
            type: dict
            sample: null
            contains:
                enabled:
                    description:
                        - >-
                            Specifies whether automatic repairs should be enabled on the
                            virtual machine scale set. The default value is false.
                    returned: always
                    type: bool
                    sample: null
                grace_period:
                    description:
                        - >-
                            The amount of time for which automatic repairs are suspended due
                            to a state change on VM. The grace time starts after the state
                            change has completed. This helps avoid premature or accidental
                            repairs. The time duration should be specified in ISO 8601 format.
                            The minimum allowed grace period is 30 minutes (PT30M), which is
                            also the default value. The maximum allowed grace period is 90
                            minutes (PT90M).
                    returned: always
                    type: str
                    sample: null
        virtual_machine_profile:
            description:
                - The virtual machine profile.
            returned: always
            type: dict
            sample: null
            contains:
                os_profile:
                    description:
                        - >-
                            Specifies the operating system settings for the virtual machines
                            in the scale set.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        computer_name_prefix:
                            description:
                                - >-
                                    Specifies the computer name prefix for all of the virtual
                                    machines in the scale set. Computer name prefixes must be 1 to
                                    15 characters long.
                            returned: always
                            type: str
                            sample: null
                        admin_username:
                            description:
                                - >-
                                    Specifies the name of the administrator account.
                                    :code:`<br>`:code:`<br>` **Windows-only restriction:** Cannot
                                    end in "." :code:`<br>`:code:`<br>` **Disallowed values:**
                                    "administrator", "admin", "user", "user1", "test", "user2",
                                    "test1", "user3", "admin1", "1", "123", "a", "actuser", "adm",
                                    "admin2", "aspnet", "backup", "console", "david", "guest",
                                    "john", "owner", "root", "server", "sql", "support",
                                    "support_388945a0", "sys", "test2", "test3", "user4", "user5".
                                    :code:`<br>`:code:`<br>` **Minimum-length (Linux):** 1 
                                    character :code:`<br>`:code:`<br>` **Max-length (Linux):** 64
                                    characters :code:`<br>`:code:`<br>` **Max-length (Windows):**
                                    20 characters  :code:`<br>`:code:`<br>`:code:`<li>` For root
                                    access to the Linux VM, see `Using root privileges on Linux
                                    virtual machines in Azure
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_\
                                    :code:`<br>`:code:`<li>` For a list of built-in system users
                                    on Linux that should not be used in this field, see `Selecting
                                    User Names for Linux on Azure
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-usernames?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                            returned: always
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
                            returned: always
                            type: str
                            sample: null
                        custom_data:
                            description:
                                - >-
                                    Specifies a base-64 encoded string of custom data. The base-64
                                    encoded string is decoded to a binary array that is saved as a
                                    file on the Virtual Machine. The maximum length of the binary
                                    array is 65535 bytes. :code:`<br>`:code:`<br>` For using
                                    cloud-init for your VM, see `Using cloud-init to customize a
                                    Linux VM during creation
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                            returned: always
                            type: str
                            sample: null
                        windows_configuration:
                            description:
                                - >-
                                    Specifies Windows operating system settings on the virtual
                                    machine.
                            returned: always
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
                                    returned: always
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
                                    returned: always
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
                                    returned: always
                                    type: str
                                    sample: null
                                additional_unattend_content:
                                    description:
                                        - >-
                                            Specifies additional base-64 encoded XML formatted
                                            information that can be included in the Unattend.xml file,
                                            which is used by Windows Setup.
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
                                                    The component name. Currently, the only allowable
                                                    value is Microsoft-Windows-Shell-Setup.
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
                                                    Specifies the XML formatted content that is added to
                                                    the unattend.xml file for the specified path and
                                                    component. The XML must be less than 4KB and must
                                                    include the root element for the setting or feature
                                                    that is being inserted.
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
                                            returned: always
                                            type: str
                                            sample: null
                                win_rm:
                                    description:
                                        - >-
                                            Specifies the Windows Remote Management listeners. This
                                            enables remote Windows PowerShell.
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
                                                            :code:`<br>`\ **http** :code:`<br>`:code:`<br>`
                                                            **https**
                                                    returned: always
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
                                                    returned: always
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
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                disable_password_authentication:
                                    description:
                                        - >-
                                            Specifies whether password authentication should be
                                            disabled.
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
                                                    The list of SSH public keys used to authenticate with
                                                    linux based VMs.
                                            returned: always
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
                                                    returned: always
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
                                                    returned: always
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
                                    returned: always
                                    type: bool
                                    sample: null
                        secrets:
                            description:
                                - >-
                                    Specifies set of certificates that should be installed onto
                                    the virtual machines in the scale set.
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
                                            The list of key vault references in SourceVault which
                                            contain certificates.
                                    returned: always
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
                                            returned: always
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
                                    information about platform images, marketplace images, or
                                    virtual machine images. This element is required when you want
                                    to use a platform image, marketplace image, or virtual machine
                                    image, but is not used in other creation operations.
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
                                            Specifies the offer of the platform image or marketplace
                                            image used to create the virtual machine.
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
                                            Specifies the version of the platform image or marketplace
                                            image used to create the virtual machine. The allowed
                                            formats are Major.Minor.Build or 'latest'. Major, Minor,
                                            and Build are decimal numbers. Specify 'latest' to use the
                                            latest version of an image available at deploy time. Even
                                            if you use 'latest', the VM image will not automatically
                                            update after deploy time even if a new version becomes
                                            available.
                                    returned: always
                                    type: str
                                    sample: null
                        os_disk:
                            description:
                                - >-
                                    Specifies information about the operating system disk used by
                                    the virtual machines in the scale set.
                                    :code:`<br>`:code:`<br>` For more information about disks, see
                                    `About disks and VHDs for Azure virtual machines
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                name:
                                    description:
                                        - The disk name.
                                    returned: always
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
                                    returned: always
                                    type: sealed-choice
                                    sample: null
                                write_accelerator_enabled:
                                    description:
                                        - >-
                                            Specifies whether writeAccelerator should be enabled or
                                            disabled on the disk.
                                    returned: always
                                    type: bool
                                    sample: null
                                create_option:
                                    description:
                                        - >-
                                            Specifies how the virtual machines in the scale set should
                                            be created.:code:`<br>`:code:`<br>` The only allowed value
                                            is: **FromImage** \u2013 This value is used when you are
                                            using an image to create the virtual machine. If you are
                                            using a platform image, you also use the imageReference
                                            element described above. If you are using a marketplace
                                            image, you  also use the plan element previously
                                            described.
                                    returned: always
                                    type: str
                                    sample: null
                                diff_disk_settings:
                                    description:
                                        - >-
                                            Specifies the ephemeral disk Settings for the operating
                                            system disk used by the virtual machine scale set.
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        option:
                                            description:
                                                - >-
                                                    Specifies the ephemeral disk settings for operating
                                                    system disk.
                                            returned: always
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
                                            returned: always
                                            type: str
                                            sample: null
                                disk_size_gb:
                                    description:
                                        - >-
                                            Specifies the size of the operating system disk in
                                            gigabytes. This element can be used to overwrite the size
                                            of the disk in a virtual machine image.
                                            :code:`<br>`:code:`<br>` This value cannot be larger than
                                            1023 GB
                                    returned: always
                                    type: int
                                    sample: null
                                os_type:
                                    description:
                                        - >-
                                            This property allows you to specify the type of the OS
                                            that is included in the disk if creating a VM from
                                            user-image or a specialized VHD. :code:`<br>`:code:`<br>`
                                            Possible values are: :code:`<br>`:code:`<br>` **Windows**
                                            :code:`<br>`:code:`<br>` **Linux**
                                    returned: always
                                    type: sealed-choice
                                    sample: null
                                image:
                                    description:
                                        - >-
                                            Specifies information about the unmanaged user image to
                                            base the scale set on.
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
                                vhd_containers:
                                    description:
                                        - >-
                                            Specifies the container urls that are used to store
                                            operating system disks for the scale set.
                                    returned: always
                                    type: list
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
                                                    Specifies the storage account type for the managed
                                                    disk. NOTE: UltraSSD_LRS can only be used with data
                                                    disks, it cannot be used with OS Disk.
                                            returned: always
                                            type: str
                                            sample: null
                                        disk_encryption_set:
                                            description:
                                                - >-
                                                    Specifies the customer managed disk encryption set
                                                    resource id for the managed disk.
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
                                    Specifies the parameters that are used to add data disks to
                                    the virtual machines in the scale set.
                                    :code:`<br>`:code:`<br>` For more information about disks, see
                                    `About disks and VHDs for Azure virtual machines
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
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
                                caching:
                                    description:
                                        - >-
                                            Specifies the caching requirements.
                                            :code:`<br>`:code:`<br>` Possible values are:
                                            :code:`<br>`:code:`<br>` **None** :code:`<br>`:code:`<br>`
                                            **ReadOnly** :code:`<br>`:code:`<br>` **ReadWrite**
                                            :code:`<br>`:code:`<br>` Default: **None for Standard
                                            storage. ReadOnly for Premium storage**
                                    returned: always
                                    type: sealed-choice
                                    sample: null
                                write_accelerator_enabled:
                                    description:
                                        - >-
                                            Specifies whether writeAccelerator should be enabled or
                                            disabled on the disk.
                                    returned: always
                                    type: bool
                                    sample: null
                                create_option:
                                    description:
                                        - The create option.
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
                                                    Specifies the storage account type for the managed
                                                    disk. NOTE: UltraSSD_LRS can only be used with data
                                                    disks, it cannot be used with OS Disk.
                                            returned: always
                                            type: str
                                            sample: null
                                        disk_encryption_set:
                                            description:
                                                - >-
                                                    Specifies the customer managed disk encryption set
                                                    resource id for the managed disk.
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
                                disk_iops_read_write:
                                    description:
                                        - >-
                                            Specifies the Read-Write IOPS for the managed disk. Should
                                            be used only when StorageAccountType is UltraSSD_LRS. If
                                            not specified, a default value would be assigned based on
                                            diskSizeGB.
                                    returned: always
                                    type: int
                                    sample: null
                                disk_m_bps_read_write:
                                    description:
                                        - >-
                                            Specifies the bandwidth in MB per second for the managed
                                            disk. Should be used only when StorageAccountType is
                                            UltraSSD_LRS. If not specified, a default value would be
                                            assigned based on diskSizeGB.
                                    returned: always
                                    type: int
                                    sample: null
                network_profile:
                    description:
                        - >-
                            Specifies properties of the network interfaces of the virtual
                            machines in the scale set.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        health_probe:
                            description:
                                - >-
                                    A reference to a load balancer probe used to determine the
                                    health of an instance in the virtual machine scale set. The
                                    reference will be in the form:
                                    '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/probes/{probeName}'.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                id:
                                    description:
                                        - >-
                                            The ARM resource id in the form of
                                            /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
                                    returned: always
                                    type: str
                                    sample: null
                        network_interface_configurations:
                            description:
                                - The list of network configurations.
                            returned: always
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
                                    returned: always
                                    type: bool
                                    sample: null
                                enable_accelerated_networking:
                                    description:
                                        - >-
                                            Specifies whether the network interface is accelerated
                                            networking-enabled.
                                    returned: always
                                    type: bool
                                    sample: null
                                network_security_group:
                                    description:
                                        - The network security group.
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
                                dns_settings:
                                    description:
                                        - The dns settings to be applied on the network interfaces.
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        dns_servers:
                                            description:
                                                - List of DNS servers IP addresses
                                            returned: always
                                            type: list
                                            sample: null
                                ip_configurations:
                                    description:
                                        - Specifies the IP configurations of the network interface.
                                    returned: always
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
                                            returned: always
                                            type: dict
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - >-
                                                            The ARM resource id in the form of
                                                            /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
                                                    returned: always
                                                    type: str
                                                    sample: null
                                        primary:
                                            description:
                                                - >-
                                                    Specifies the primary network interface in case the
                                                    virtual machine has more than 1 network interface.
                                            returned: always
                                            type: bool
                                            sample: null
                                        public_ip_address_configuration:
                                            description:
                                                - The publicIPAddressConfiguration.
                                            returned: always
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
                                                    returned: always
                                                    type: int
                                                    sample: null
                                                dns_settings:
                                                    description:
                                                        - >-
                                                            The dns settings to be applied on the publicIP
                                                            addresses .
                                                    returned: always
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
                                                    returned: always
                                                    type: list
                                                    sample: null
                                                    contains:
                                                        ip_tag_type:
                                                            description:
                                                                - 'IP tag type. Example: FirstPartyUsage.'
                                                            returned: always
                                                            type: str
                                                            sample: null
                                                        tag:
                                                            description:
                                                                - >-
                                                                    IP tag associated with the public IP. Example:
                                                                    SQL, Storage etc.
                                                            returned: always
                                                            type: str
                                                            sample: null
                                                public_ip_prefix:
                                                    description:
                                                        - >-
                                                            The PublicIPPrefix from which to allocate publicIP
                                                            addresses.
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
                                                public_ip_address_version:
                                                    description:
                                                        - >-
                                                            Available from Api-Version 2019-07-01 onwards, it
                                                            represents whether the specific ipconfiguration is
                                                            IPv4 or IPv6. Default is taken as IPv4. Possible
                                                            values are: 'IPv4' and 'IPv6'.
                                                    returned: always
                                                    type: str
                                                    sample: null
                                        private_ip_address_version:
                                            description:
                                                - >-
                                                    Available from Api-Version 2017-03-30 onwards, it
                                                    represents whether the specific ipconfiguration is
                                                    IPv4 or IPv6. Default is taken as IPv4.  Possible
                                                    values are: 'IPv4' and 'IPv6'.
                                            returned: always
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
                                            returned: always
                                            type: list
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    returned: always
                                                    type: str
                                                    sample: null
                                        application_security_groups:
                                            description:
                                                - >-
                                                    Specifies an array of references to application
                                                    security group.
                                            returned: always
                                            type: list
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    returned: always
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
                                            returned: always
                                            type: list
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    returned: always
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
                                            returned: always
                                            type: list
                                            sample: null
                                            contains:
                                                id:
                                                    description:
                                                        - Resource Id
                                                    returned: always
                                                    type: str
                                                    sample: null
                                enable_ip_forwarding:
                                    description:
                                        - Whether IP forwarding enabled on this NIC.
                                    returned: always
                                    type: bool
                                    sample: null
                security_profile:
                    description:
                        - >-
                            Specifies the Security related profile settings for the virtual
                            machines in the scale set.
                    returned: always
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
                                    Boot Diagnostics is a debugging feature which allows you to
                                    view Console Output and Screenshot to diagnose VM status.
                                    :code:`<br>`:code:`<br>` You can easily view the output of
                                    your console log. :code:`<br>`:code:`<br>` Azure also enables
                                    you to see a screenshot of the VM from the hypervisor.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                enabled:
                                    description:
                                        - >-
                                            Whether boot diagnostics should be enabled on the Virtual
                                            Machine.
                                    returned: always
                                    type: bool
                                    sample: null
                                storage_uri:
                                    description:
                                        - >-
                                            Uri of the storage account to use for placing the console
                                            output and screenshot. :code:`<br>`:code:`<br>`If
                                            storageUri is not specified while enabling boot
                                            diagnostics, managed storage will be used.
                                    returned: always
                                    type: str
                                    sample: null
                extension_profile:
                    description:
                        - >-
                            Specifies a collection of settings for extensions installed on
                            virtual machines in the scale set.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        extensions:
                            description:
                                - The virtual machine scale set child extension resources.
                            returned: always
                            type: list
                            sample: null
                            contains:
                                name:
                                    description:
                                        - The name of the extension.
                                    returned: always
                                    type: str
                                    sample: null
                                force_update_tag:
                                    description:
                                        - >-
                                            If a value is provided and is different from the previous
                                            value, the extension handler will be forced to update even
                                            if the extension configuration has not changed.
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
                                            Indicates whether the extension should use a newer minor
                                            version if one is available at deployment time. Once
                                            deployed, however, the extension will not upgrade minor
                                            versions unless redeployed, even with this property set to
                                            true.
                                    returned: always
                                    type: bool
                                    sample: null
                                enable_automatic_upgrade:
                                    description:
                                        - >-
                                            Indicates whether the extension should be automatically
                                            upgraded by the platform if there is a newer version of
                                            the extension available.
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
                                            protectedSettingsFromKeyVault or no protected settings at
                                            all.
                                    returned: always
                                    type: any
                                    sample: null
                                provision_after_extensions:
                                    description:
                                        - >-
                                            Collection of extension names after which this extension
                                            needs to be provisioned.
                                    returned: always
                                    type: list
                                    sample: null
                        extensions_time_budget:
                            description:
                                - >-
                                    Specifies the time alloted for all extensions to start. The
                                    time duration should be between 15 minutes and 120 minutes
                                    (inclusive) and should be specified in ISO 8601 format. The
                                    default value is 90 minutes (PT1H30M).
                                    :code:`<br>`:code:`<br>` Minimum api-version: 2020-06-01
                            returned: always
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
                    returned: always
                    type: str
                    sample: null
                priority:
                    description:
                        - >-
                            Specifies the priority for the virtual machines in the scale set.
                            :code:`<br>`:code:`<br>`Minimum api-version: 2017-10-30-preview
                    returned: always
                    type: str
                    sample: null
                eviction_policy:
                    description:
                        - >-
                            Specifies the eviction policy for the Azure Spot virtual machine
                            and Azure Spot scale set. :code:`<br>`:code:`<br>`For Azure Spot
                            virtual machines, both 'Deallocate' and 'Delete' are supported and
                            the minimum api-version is 2019-03-01. :code:`<br>`:code:`<br>`For
                            Azure Spot scale sets, both 'Deallocate' and 'Delete' are
                            supported and the minimum api-version is 2017-10-30-preview.
                    returned: always
                    type: str
                    sample: null
                billing_profile:
                    description:
                        - >-
                            Specifies the billing related details of a Azure Spot VMSS.
                            :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        max_price:
                            description:
                                - >-
                                    Specifies the maximum price you are willing to pay for a Azure
                                    Spot VM/VMSS. This price is in US Dollars.
                                    :code:`<br>`:code:`<br>` This price will be compared with the
                                    current Azure Spot price for the VM size. Also, the prices are
                                    compared at the time of create/update of Azure Spot VM/VMSS
                                    and the operation will only succeed if  the maxPrice is
                                    greater than the current Azure Spot price.
                                    :code:`<br>`:code:`<br>` The maxPrice will also be used for
                                    evicting a Azure Spot VM/VMSS if the current Azure Spot price
                                    goes beyond the maxPrice after creation of VM/VMSS.
                                    :code:`<br>`:code:`<br>` Possible values are:
                                    :code:`<br>`:code:`<br>` - Any decimal value greater than
                                    zero. Example: 0.01538 :code:`<br>`:code:`<br>` -1 – indicates
                                    default price to be up-to on-demand. :code:`<br>`:code:`<br>`
                                    You can set the maxPrice to -1 to indicate that the Azure Spot
                                    VM/VMSS should not be evicted for price reasons. Also, the
                                    default max price is -1 if it is not provided by you.
                                    :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
                            returned: always
                            type: number
                            sample: null
                scheduled_events_profile:
                    description:
                        - Specifies Scheduled Event related configurations.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        terminate_notification_profile:
                            description:
                                - Specifies Terminate Scheduled Event related configurations.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                not_before_timeout:
                                    description:
                                        - >-
                                            Configurable length of time a Virtual Machine being
                                            deleted will have to potentially approve the Terminate
                                            Scheduled Event before the event is auto approved (timed
                                            out). The configuration must be specified in ISO 8601
                                            format, the default value is 5 minutes (PT5M)
                                    returned: always
                                    type: str
                                    sample: null
                                enable:
                                    description:
                                        - >-
                                            Specifies whether the Terminate Scheduled event is enabled
                                            or disabled.
                                    returned: always
                                    type: bool
                                    sample: null
        provisioning_state:
            description:
                - 'The provisioning state, which only appears in the response.'
            returned: always
            type: str
            sample: null
        overprovision:
            description:
                - >-
                    Specifies whether the Virtual Machine Scale Set should be
                    overprovisioned.
            returned: always
            type: bool
            sample: null
        do_not_run_extensions_on_overprovisioned_v_ms:
            description:
                - >-
                    When Overprovision is enabled, extensions are launched only on the
                    requested number of VMs which are finally kept. This property will
                    hence ensure that the extensions do not run on the extra
                    overprovisioned VMs.
            returned: always
            type: bool
            sample: null
        unique_id:
            description:
                - >-
                    Specifies the ID which uniquely identifies a Virtual Machine Scale
                    Set.
            returned: always
            type: str
            sample: null
        single_placement_group:
            description:
                - >-
                    When true this limits the scale set to a single placement group, of
                    max size 100 virtual machines. NOTE: If singlePlacementGroup is true,
                    it may be modified to false. However, if singlePlacementGroup is
                    false, it may not be modified to true.
            returned: always
            type: bool
            sample: null
        zone_balance:
            description:
                - >-
                    Whether to force strictly even Virtual Machine distribution cross
                    x-zones in case there is zone outage.
            returned: always
            type: bool
            sample: null
        platform_fault_domain_count:
            description:
                - Fault Domain count for each placement group.
            returned: always
            type: int
            sample: null
        proximity_placement_group:
            description:
                - >-
                    Specifies information about the proximity placement group that the
                    virtual machine scale set should be assigned to.
                    :code:`<br>`:code:`<br>`Minimum api-version: 2018-04-01.
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
                    machine scale set resides in. :code:`<br>`:code:`<br>`Minimum
                    api-version: 2020-06-01.
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
        additional_capabilities:
            description:
                - >-
                    Specifies additional capabilities enabled or disabled on the Virtual
                    Machines in the Virtual Machine Scale Set. For instance: whether the
                    Virtual Machines have the capability to support attaching managed data
                    disks with UltraSSD_LRS storage account type.
            returned: always
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
                    returned: always
                    type: bool
                    sample: null
        scale_in_policy:
            description:
                - >-
                    Specifies the scale-in policy that decides which virtual machines are
                    chosen for removal when a Virtual Machine Scale Set is scaled-in.
            returned: always
            type: dict
            sample: null
            contains:
                rules:
                    description:
                        - >-
                            The rules to be followed when scaling-in a virtual machine scale
                            set. :code:`<br>`:code:`<br>` Possible values are:
                            :code:`<br>`:code:`<br>` **Default** When a virtual machine scale
                            set is scaled in, the scale set will first be balanced across
                            zones if it is a zonal scale set. Then, it will be balanced across
                            Fault Domains as far as possible. Within each Fault Domain, the
                            virtual machines chosen for removal will be the newest ones that
                            are not protected from scale-in. :code:`<br>`:code:`<br>`
                            **OldestVM** When a virtual machine scale set is being scaled-in,
                            the oldest virtual machines that are not protected from scale-in
                            will be chosen for removal. For zonal virtual machine scale sets,
                            the scale set will first be balanced across zones. Within each
                            zone, the oldest virtual machines that are not protected will be
                            chosen for removal. :code:`<br>`:code:`<br>` **NewestVM** When a
                            virtual machine scale set is being scaled-in, the newest virtual
                            machines that are not protected from scale-in will be chosen for
                            removal. For zonal virtual machine scale sets, the scale set will
                            first be balanced across zones. Within each zone, the newest
                            virtual machines that are not protected will be chosen for
                            removal. :code:`<br>`:code:`<br>`
                    returned: always
                    type: list
                    sample: null
        virtual_machine:
            description:
                - The instance view status summary for the virtual machine scale set.
            returned: always
            type: dict
            sample: null
        extensions:
            description:
                - The extensions information.
            returned: always
            type: list
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
        orchestration_services:
            description:
                - The orchestration services information.
            returned: always
            type: list
            sample: null
        value:
            description:
                - |-
                    The list of virtual machine scale sets.
                    The list of skus available for the virtual machine scale set.
                    The list of OS upgrades performed on the virtual machine scale set.
            returned: always
            type: list
            sample: null
            contains:
                sku:
                    description:
                        - The virtual machine scale set sku.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        name:
                            description:
                                - The sku name.
                            returned: always
                            type: str
                            sample: null
                        tier:
                            description:
                                - >-
                                    Specifies the tier of virtual machines in a scale
                                    set.:code:`<br />`:code:`<br />` Possible Values::code:`<br
                                    />`:code:`<br />` **Standard**\ :code:`<br />`:code:`<br />`
                                    **Basic**
                            returned: always
                            type: str
                            sample: null
                        capacity:
                            description:
                                - Specifies the number of virtual machines in the scale set.
                            returned: always
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
                                    Specifies the product of the image from the marketplace. This
                                    is the same value as Offer under the imageReference element.
                            returned: always
                            type: str
                            sample: null
                        promotion_code:
                            description:
                                - The promotion code.
                            returned: always
                            type: str
                            sample: null
                identity:
                    description:
                        - 'The identity of the virtual machine scale set, if configured.'
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        type:
                            description:
                                - >-
                                    The type of identity used for the virtual machine scale set.
                                    The type 'SystemAssigned, UserAssigned' includes both an
                                    implicitly created identity and a set of user assigned
                                    identities. The type 'None' will remove any identities from
                                    the virtual machine scale set.
                            returned: always
                            type: sealed-choice
                            sample: null
                        user_assigned_identities:
                            description:
                                - >-
                                    The list of user identities associated with the virtual
                                    machine scale set. The user identity dictionary key references
                                    will be ARM resource ids in the form:
                                    '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
                            returned: always
                            type: dict
                            sample: null
                zones:
                    description:
                        - >-
                            The virtual machine scale set zones. NOTE: Availability zones can
                            only be set when you create the scale set
                    returned: always
                    type: list
                    sample: null
                upgrade_policy:
                    description:
                        - The upgrade policy.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        mode:
                            description:
                                - >-
                                    Specifies the mode of an upgrade to virtual machines in the
                                    scale set.:code:`<br />`:code:`<br />` Possible values
                                    are::code:`<br />`:code:`<br />` **Manual** - You  control the
                                    application of updates to virtual machines in the scale set.
                                    You do this by using the manualUpgrade action.:code:`<br
                                    />`:code:`<br />` **Automatic** - All virtual machines in the
                                    scale set are  automatically updated at the same time.
                            returned: always
                            type: sealed-choice
                            sample: null
                        rolling_upgrade_policy:
                            description:
                                - >-
                                    The configuration parameters used while performing a rolling
                                    upgrade.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                max_batch_instance_percent:
                                    description:
                                        - >-
                                            The maximum percent of total virtual machine instances
                                            that will be upgraded simultaneously by the rolling
                                            upgrade in one batch. As this is a maximum, unhealthy
                                            instances in previous or future batches can cause the
                                            percentage of instances in a batch to decrease to ensure
                                            higher reliability. The default value for this parameter
                                            is 20%.
                                    returned: always
                                    type: int
                                    sample: null
                                max_unhealthy_instance_percent:
                                    description:
                                        - >-
                                            The maximum percentage of the total virtual machine
                                            instances in the scale set that can be simultaneously
                                            unhealthy, either as a result of being upgraded, or by
                                            being found in an unhealthy state by the virtual machine
                                            health checks before the rolling upgrade aborts. This
                                            constraint will be checked prior to starting any batch.
                                            The default value for this parameter is 20%.
                                    returned: always
                                    type: int
                                    sample: null
                                max_unhealthy_upgraded_instance_percent:
                                    description:
                                        - >-
                                            The maximum percentage of upgraded virtual machine
                                            instances that can be found to be in an unhealthy state.
                                            This check will happen after each batch is upgraded. If
                                            this percentage is ever exceeded, the rolling update
                                            aborts. The default value for this parameter is 20%.
                                    returned: always
                                    type: int
                                    sample: null
                                pause_time_between_batches:
                                    description:
                                        - >-
                                            The wait time between completing the update for all
                                            virtual machines in one batch and starting the next batch.
                                            The time duration should be specified in ISO 8601 format.
                                            The default value is 0 seconds (PT0S).
                                    returned: always
                                    type: str
                                    sample: null
                        automatic_os_upgrade_policy:
                            description:
                                - >-
                                    Configuration parameters used for performing automatic OS
                                    Upgrade.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                enable_automatic_os_upgrade:
                                    description:
                                        - >-
                                            Indicates whether OS upgrades should automatically be
                                            applied to scale set instances in a rolling fashion when a
                                            newer version of the OS image becomes available. Default
                                            value is false. :code:`<br>`:code:`<br>` If this is set to
                                            true for Windows based scale sets, `enableAutomaticUpdates
                                            <https://docs.microsoft.com/dotnet/api/microsoft.azure.management.compute.models.windowsconfiguration.enableautomaticupdates?view=azure-dotnet>`_
                                            is automatically set to false and cannot be set to true.
                                    returned: always
                                    type: bool
                                    sample: null
                                disable_automatic_rollback:
                                    description:
                                        - >-
                                            Whether OS image rollback feature should be disabled.
                                            Default value is false.
                                    returned: always
                                    type: bool
                                    sample: null
                automatic_repairs_policy:
                    description:
                        - Policy for automatic repairs.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        enabled:
                            description:
                                - >-
                                    Specifies whether automatic repairs should be enabled on the
                                    virtual machine scale set. The default value is false.
                            returned: always
                            type: bool
                            sample: null
                        grace_period:
                            description:
                                - >-
                                    The amount of time for which automatic repairs are suspended
                                    due to a state change on VM. The grace time starts after the
                                    state change has completed. This helps avoid premature or
                                    accidental repairs. The time duration should be specified in
                                    ISO 8601 format. The minimum allowed grace period is 30
                                    minutes (PT30M), which is also the default value. The maximum
                                    allowed grace period is 90 minutes (PT90M).
                            returned: always
                            type: str
                            sample: null
                virtual_machine_profile:
                    description:
                        - The virtual machine profile.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        os_profile:
                            description:
                                - >-
                                    Specifies the operating system settings for the virtual
                                    machines in the scale set.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                computer_name_prefix:
                                    description:
                                        - >-
                                            Specifies the computer name prefix for all of the virtual
                                            machines in the scale set. Computer name prefixes must be
                                            1 to 15 characters long.
                                    returned: always
                                    type: str
                                    sample: null
                                admin_username:
                                    description:
                                        - >-
                                            Specifies the name of the administrator account.
                                            :code:`<br>`:code:`<br>` **Windows-only restriction:**
                                            Cannot end in "." :code:`<br>`:code:`<br>` **Disallowed
                                            values:** "administrator", "admin", "user", "user1",
                                            "test", "user2", "test1", "user3", "admin1", "1", "123",
                                            "a", "actuser", "adm", "admin2", "aspnet", "backup",
                                            "console", "david", "guest", "john", "owner", "root",
                                            "server", "sql", "support", "support_388945a0", "sys",
                                            "test2", "test3", "user4", "user5".
                                            :code:`<br>`:code:`<br>` **Minimum-length (Linux):** 1 
                                            character :code:`<br>`:code:`<br>` **Max-length (Linux):**
                                            64 characters :code:`<br>`:code:`<br>` **Max-length
                                            (Windows):** 20 characters 
                                            :code:`<br>`:code:`<br>`:code:`<li>` For root access to
                                            the Linux VM, see `Using root privileges on Linux virtual
                                            machines in Azure
                                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-use-root-privileges?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_\
                                            :code:`<br>`:code:`<li>` For a list of built-in system
                                            users on Linux that should not be used in this field, see
                                            `Selecting User Names for Linux on Azure
                                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-usernames?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                                    returned: always
                                    type: str
                                    sample: null
                                admin_password:
                                    description:
                                        - >-
                                            Specifies the password of the administrator account.
                                            :code:`<br>`:code:`<br>` **Minimum-length (Windows):** 8
                                            characters :code:`<br>`:code:`<br>` **Minimum-length
                                            (Linux):** 6 characters :code:`<br>`:code:`<br>`
                                            **Max-length (Windows):** 123 characters
                                            :code:`<br>`:code:`<br>` **Max-length (Linux):** 72
                                            characters :code:`<br>`:code:`<br>` **Complexity
                                            requirements:** 3 out of 4 conditions below need to be
                                            fulfilled :code:`<br>` Has lower characters
                                            :code:`<br>`Has upper characters :code:`<br>` Has a digit
                                            :code:`<br>` Has a special character (Regex match [\W_])
                                            :code:`<br>`:code:`<br>` **Disallowed values:** "abc@123",
                                            "P@$$w0rd", "P@ssw0rd", "P@ssword123", "Pa$$word",
                                            "pass@word1", "Password!", "Password1", "Password22",
                                            "iloveyou!" :code:`<br>`:code:`<br>` For resetting the
                                            password, see `How to reset the Remote Desktop service or
                                            its login password in a Windows VM
                                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                                            :code:`<br>`:code:`<br>` For resetting root password, see
                                            `Manage users, SSH, and check or repair disks on Azure
                                            Linux VMs using the VMAccess Extension
                                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password>`_
                                    returned: always
                                    type: str
                                    sample: null
                                custom_data:
                                    description:
                                        - >-
                                            Specifies a base-64 encoded string of custom data. The
                                            base-64 encoded string is decoded to a binary array that
                                            is saved as a file on the Virtual Machine. The maximum
                                            length of the binary array is 65535 bytes.
                                            :code:`<br>`:code:`<br>` For using cloud-init for your VM,
                                            see `Using cloud-init to customize a Linux VM during
                                            creation
                                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-cloud-init?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                                    returned: always
                                    type: str
                                    sample: null
                                windows_configuration:
                                    description:
                                        - >-
                                            Specifies Windows operating system settings on the virtual
                                            machine.
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        provision_vm_agent:
                                            description:
                                                - >-
                                                    Indicates whether virtual machine agent should be
                                                    provisioned on the virtual machine.
                                                    :code:`<br>`:code:`<br>` When this property is not
                                                    specified in the request body, default behavior is to
                                                    set it to true.  This will ensure that VM Agent is
                                                    installed on the VM so that extensions can be added to
                                                    the VM later.
                                            returned: always
                                            type: bool
                                            sample: null
                                        enable_automatic_updates:
                                            description:
                                                - >-
                                                    Indicates whether Automatic Updates is enabled for the
                                                    Windows virtual machine. Default value is true.
                                                    :code:`<br>`:code:`<br>` For virtual machine scale
                                                    sets, this property can be updated and updates will
                                                    take effect on OS reprovisioning.
                                            returned: always
                                            type: bool
                                            sample: null
                                        time_zone:
                                            description:
                                                - >-
                                                    Specifies the time zone of the virtual machine. e.g.
                                                    "Pacific Standard Time". :code:`<br>`:code:`<br>`
                                                    Possible values can be `TimeZoneInfo.Id
                                                    <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.id?#System_TimeZoneInfo_Id>`_
                                                    value from time zones returned by
                                                    `TimeZoneInfo.GetSystemTimeZones
                                                    <https://docs.microsoft.com/en-us/dotnet/api/system.timezoneinfo.getsystemtimezones>`_.
                                            returned: always
                                            type: str
                                            sample: null
                                        additional_unattend_content:
                                            description:
                                                - >-
                                                    Specifies additional base-64 encoded XML formatted
                                                    information that can be included in the Unattend.xml
                                                    file, which is used by Windows Setup.
                                            returned: always
                                            type: list
                                            sample: null
                                            contains:
                                                pass_name:
                                                    description:
                                                        - >-
                                                            The pass name. Currently, the only allowable value
                                                            is OobeSystem.
                                                    returned: always
                                                    type: constant
                                                    sample: null
                                                component_name:
                                                    description:
                                                        - >-
                                                            The component name. Currently, the only allowable
                                                            value is Microsoft-Windows-Shell-Setup.
                                                    returned: always
                                                    type: constant
                                                    sample: null
                                                setting_name:
                                                    description:
                                                        - >-
                                                            Specifies the name of the setting to which the
                                                            content applies. Possible values are:
                                                            FirstLogonCommands and AutoLogon.
                                                    returned: always
                                                    type: sealed-choice
                                                    sample: null
                                                content:
                                                    description:
                                                        - >-
                                                            Specifies the XML formatted content that is added
                                                            to the unattend.xml file for the specified path
                                                            and component. The XML must be less than 4KB and
                                                            must include the root element for the setting or
                                                            feature that is being inserted.
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
                                                            Specifies the mode of in-guest patching to IaaS
                                                            virtual machine.:code:`<br />`:code:`<br />`
                                                            Possible values are::code:`<br />`:code:`<br />`
                                                            **Manual** - You  control the application of
                                                            patches to a virtual machine. You do this by
                                                            applying patches manually inside the VM. In this
                                                            mode, automatic updates are disabled; the property
                                                            WindowsConfiguration.enableAutomaticUpdates must
                                                            be false:code:`<br />`:code:`<br />`
                                                            **AutomaticByOS** - The virtual machine will
                                                            automatically be updated by the OS. The property
                                                            WindowsConfiguration.enableAutomaticUpdates must
                                                            be true. :code:`<br />`:code:`<br />` **
                                                            AutomaticByPlatform** - the virtual machine will
                                                            automatically updated by the platform. The
                                                            properties provisionVMAgent and
                                                            WindowsConfiguration.enableAutomaticUpdates must
                                                            be true
                                                    returned: always
                                                    type: str
                                                    sample: null
                                        win_rm:
                                            description:
                                                - >-
                                                    Specifies the Windows Remote Management listeners.
                                                    This enables remote Windows PowerShell.
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
                                                                    :code:`<br>`\ **http**
                                                                    :code:`<br>`:code:`<br>` **https**
                                                            returned: always
                                                            type: sealed-choice
                                                            sample: null
                                                        certificate_url:
                                                            description:
                                                                - >-
                                                                    This is the URL of a certificate that has been
                                                                    uploaded to Key Vault as a secret. For adding
                                                                    a secret to the Key Vault, see `Add a key or
                                                                    secret to the key vault
                                                                    <https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add>`_.
                                                                    In this case, your certificate needs to be It
                                                                    is the Base64 encoding of the following JSON
                                                                    Object which is encoded in UTF-8:
                                                                    :code:`<br>`:code:`<br>` {:code:`<br>` 
                                                                    "data":":code:`<Base64-encoded-certificate>`",:code:`<br>` 
                                                                    "dataType":"pfx",:code:`<br>` 
                                                                    "password":":code:`<pfx-file-password>`":code:`<br>`}
                                                            returned: always
                                                            type: str
                                                            sample: null
                                linux_configuration:
                                    description:
                                        - >-
                                            Specifies the Linux operating system settings on the
                                            virtual machine. :code:`<br>`:code:`<br>`For a list of
                                            supported Linux distributions, see `Linux on
                                            Azure-Endorsed Distributions
                                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-endorsed-distros?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_
                                            :code:`<br>`:code:`<br>` For running non-endorsed
                                            distributions, see `Information for Non-Endorsed
                                            Distributions
                                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-create-upload-generic?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        disable_password_authentication:
                                            description:
                                                - >-
                                                    Specifies whether password authentication should be
                                                    disabled.
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
                                                            The list of SSH public keys used to authenticate
                                                            with linux based VMs.
                                                    returned: always
                                                    type: list
                                                    sample: null
                                                    contains:
                                                        path:
                                                            description:
                                                                - >-
                                                                    Specifies the full path on the created VM
                                                                    where ssh public key is stored. If the file
                                                                    already exists, the specified key is appended
                                                                    to the file. Example:
                                                                    /home/user/.ssh/authorized_keys
                                                            returned: always
                                                            type: str
                                                            sample: null
                                                        key_data:
                                                            description:
                                                                - >-
                                                                    SSH public key certificate used to
                                                                    authenticate with the VM through ssh. The key
                                                                    needs to be at least 2048-bit and in ssh-rsa
                                                                    format. :code:`<br>`:code:`<br>` For creating
                                                                    ssh keys, see `Create SSH keys on Linux and
                                                                    Mac for Linux VMs in Azure
                                                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-mac-create-ssh-keys?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
                                                            returned: always
                                                            type: str
                                                            sample: null
                                        provision_vm_agent:
                                            description:
                                                - >-
                                                    Indicates whether virtual machine agent should be
                                                    provisioned on the virtual machine.
                                                    :code:`<br>`:code:`<br>` When this property is not
                                                    specified in the request body, default behavior is to
                                                    set it to true.  This will ensure that VM Agent is
                                                    installed on the VM so that extensions can be added to
                                                    the VM later.
                                            returned: always
                                            type: bool
                                            sample: null
                                secrets:
                                    description:
                                        - >-
                                            Specifies set of certificates that should be installed
                                            onto the virtual machines in the scale set.
                                    returned: always
                                    type: list
                                    sample: null
                                    contains:
                                        source_vault:
                                            description:
                                                - >-
                                                    The relative URL of the Key Vault containing all of
                                                    the certificates in VaultCertificates.
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
                                                    The list of key vault references in SourceVault which
                                                    contain certificates.
                                            returned: always
                                            type: list
                                            sample: null
                                            contains:
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
                                                    returned: always
                                                    type: str
                                                    sample: null
                                                certificate_store:
                                                    description:
                                                        - >-
                                                            For Windows VMs, specifies the certificate store
                                                            on the Virtual Machine to which the certificate
                                                            should be added. The specified certificate store
                                                            is implicitly in the LocalMachine account.
                                                            :code:`<br>`:code:`<br>`For Linux VMs, the
                                                            certificate file is placed under the
                                                            /var/lib/waagent directory, with the file name
                                                            &lt;UppercaseThumbprint&gt;.crt for the X509
                                                            certificate file and
                                                            &lt;UppercaseThumbprint&gt;.prv for private key.
                                                            Both of these files are .pem formatted.
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
                                            Specifies information about the image to use. You can
                                            specify information about platform images, marketplace
                                            images, or virtual machine images. This element is
                                            required when you want to use a platform image,
                                            marketplace image, or virtual machine image, but is not
                                            used in other creation operations.
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
                                                    Specifies the offer of the platform image or
                                                    marketplace image used to create the virtual machine.
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
                                                    Specifies the version of the platform image or
                                                    marketplace image used to create the virtual machine.
                                                    The allowed formats are Major.Minor.Build or 'latest'.
                                                    Major, Minor, and Build are decimal numbers. Specify
                                                    'latest' to use the latest version of an image
                                                    available at deploy time. Even if you use 'latest',
                                                    the VM image will not automatically update after
                                                    deploy time even if a new version becomes available.
                                            returned: always
                                            type: str
                                            sample: null
                                os_disk:
                                    description:
                                        - >-
                                            Specifies information about the operating system disk used
                                            by the virtual machines in the scale set.
                                            :code:`<br>`:code:`<br>` For more information about disks,
                                            see `About disks and VHDs for Azure virtual machines
                                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        name:
                                            description:
                                                - The disk name.
                                            returned: always
                                            type: str
                                            sample: null
                                        caching:
                                            description:
                                                - >-
                                                    Specifies the caching requirements.
                                                    :code:`<br>`:code:`<br>` Possible values are:
                                                    :code:`<br>`:code:`<br>` **None**
                                                    :code:`<br>`:code:`<br>` **ReadOnly**
                                                    :code:`<br>`:code:`<br>` **ReadWrite**
                                                    :code:`<br>`:code:`<br>` Default: **None for Standard
                                                    storage. ReadOnly for Premium storage**
                                            returned: always
                                            type: sealed-choice
                                            sample: null
                                        write_accelerator_enabled:
                                            description:
                                                - >-
                                                    Specifies whether writeAccelerator should be enabled
                                                    or disabled on the disk.
                                            returned: always
                                            type: bool
                                            sample: null
                                        create_option:
                                            description:
                                                - >-
                                                    Specifies how the virtual machines in the scale set
                                                    should be created.:code:`<br>`:code:`<br>` The only
                                                    allowed value is: **FromImage** \u2013 This value is
                                                    used when you are using an image to create the virtual
                                                    machine. If you are using a platform image, you also
                                                    use the imageReference element described above. If you
                                                    are using a marketplace image, you  also use the plan
                                                    element previously described.
                                            returned: always
                                            type: str
                                            sample: null
                                        diff_disk_settings:
                                            description:
                                                - >-
                                                    Specifies the ephemeral disk Settings for the
                                                    operating system disk used by the virtual machine
                                                    scale set.
                                            returned: always
                                            type: dict
                                            sample: null
                                            contains:
                                                option:
                                                    description:
                                                        - >-
                                                            Specifies the ephemeral disk settings for
                                                            operating system disk.
                                                    returned: always
                                                    type: str
                                                    sample: null
                                                placement:
                                                    description:
                                                        - >-
                                                            Specifies the ephemeral disk placement for
                                                            operating system disk.:code:`<br>`:code:`<br>`
                                                            Possible values are: :code:`<br>`:code:`<br>`
                                                            **CacheDisk** :code:`<br>`:code:`<br>`
                                                            **ResourceDisk** :code:`<br>`:code:`<br>` Default:
                                                            **CacheDisk** if one is configured for the VM size
                                                            otherwise **ResourceDisk** is
                                                            used.:code:`<br>`:code:`<br>` Refer to VM size
                                                            documentation for Windows VM at
                                                            https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
                                                            and Linux VM at
                                                            https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes
                                                            to check which VM sizes exposes a cache disk.
                                                    returned: always
                                                    type: str
                                                    sample: null
                                        disk_size_gb:
                                            description:
                                                - >-
                                                    Specifies the size of the operating system disk in
                                                    gigabytes. This element can be used to overwrite the
                                                    size of the disk in a virtual machine image.
                                                    :code:`<br>`:code:`<br>` This value cannot be larger
                                                    than 1023 GB
                                            returned: always
                                            type: int
                                            sample: null
                                        os_type:
                                            description:
                                                - >-
                                                    This property allows you to specify the type of the OS
                                                    that is included in the disk if creating a VM from
                                                    user-image or a specialized VHD.
                                                    :code:`<br>`:code:`<br>` Possible values are:
                                                    :code:`<br>`:code:`<br>` **Windows**
                                                    :code:`<br>`:code:`<br>` **Linux**
                                            returned: always
                                            type: sealed-choice
                                            sample: null
                                        image:
                                            description:
                                                - >-
                                                    Specifies information about the unmanaged user image
                                                    to base the scale set on.
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
                                        vhd_containers:
                                            description:
                                                - >-
                                                    Specifies the container urls that are used to store
                                                    operating system disks for the scale set.
                                            returned: always
                                            type: list
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
                                                            Specifies the storage account type for the managed
                                                            disk. NOTE: UltraSSD_LRS can only be used with
                                                            data disks, it cannot be used with OS Disk.
                                                    returned: always
                                                    type: str
                                                    sample: null
                                                disk_encryption_set:
                                                    description:
                                                        - >-
                                                            Specifies the customer managed disk encryption set
                                                            resource id for the managed disk.
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
                                            Specifies the parameters that are used to add data disks
                                            to the virtual machines in the scale set.
                                            :code:`<br>`:code:`<br>` For more information about disks,
                                            see `About disks and VHDs for Azure virtual machines
                                            <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
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
                                        lun:
                                            description:
                                                - >-
                                                    Specifies the logical unit number of the data disk.
                                                    This value is used to identify data disks within the
                                                    VM and therefore must be unique for each data disk
                                                    attached to a VM.
                                            returned: always
                                            type: int
                                            sample: null
                                        caching:
                                            description:
                                                - >-
                                                    Specifies the caching requirements.
                                                    :code:`<br>`:code:`<br>` Possible values are:
                                                    :code:`<br>`:code:`<br>` **None**
                                                    :code:`<br>`:code:`<br>` **ReadOnly**
                                                    :code:`<br>`:code:`<br>` **ReadWrite**
                                                    :code:`<br>`:code:`<br>` Default: **None for Standard
                                                    storage. ReadOnly for Premium storage**
                                            returned: always
                                            type: sealed-choice
                                            sample: null
                                        write_accelerator_enabled:
                                            description:
                                                - >-
                                                    Specifies whether writeAccelerator should be enabled
                                                    or disabled on the disk.
                                            returned: always
                                            type: bool
                                            sample: null
                                        create_option:
                                            description:
                                                - The create option.
                                            returned: always
                                            type: str
                                            sample: null
                                        disk_size_gb:
                                            description:
                                                - >-
                                                    Specifies the size of an empty data disk in gigabytes.
                                                    This element can be used to overwrite the size of the
                                                    disk in a virtual machine image.
                                                    :code:`<br>`:code:`<br>` This value cannot be larger
                                                    than 1023 GB
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
                                                            Specifies the storage account type for the managed
                                                            disk. NOTE: UltraSSD_LRS can only be used with
                                                            data disks, it cannot be used with OS Disk.
                                                    returned: always
                                                    type: str
                                                    sample: null
                                                disk_encryption_set:
                                                    description:
                                                        - >-
                                                            Specifies the customer managed disk encryption set
                                                            resource id for the managed disk.
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
                                        disk_iops_read_write:
                                            description:
                                                - >-
                                                    Specifies the Read-Write IOPS for the managed disk.
                                                    Should be used only when StorageAccountType is
                                                    UltraSSD_LRS. If not specified, a default value would
                                                    be assigned based on diskSizeGB.
                                            returned: always
                                            type: int
                                            sample: null
                                        disk_m_bps_read_write:
                                            description:
                                                - >-
                                                    Specifies the bandwidth in MB per second for the
                                                    managed disk. Should be used only when
                                                    StorageAccountType is UltraSSD_LRS. If not specified,
                                                    a default value would be assigned based on diskSizeGB.
                                            returned: always
                                            type: int
                                            sample: null
                        network_profile:
                            description:
                                - >-
                                    Specifies properties of the network interfaces of the virtual
                                    machines in the scale set.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                health_probe:
                                    description:
                                        - >-
                                            A reference to a load balancer probe used to determine the
                                            health of an instance in the virtual machine scale set.
                                            The reference will be in the form:
                                            '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/probes/{probeName}'.
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        id:
                                            description:
                                                - >-
                                                    The ARM resource id in the form of
                                                    /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
                                            returned: always
                                            type: str
                                            sample: null
                                network_interface_configurations:
                                    description:
                                        - The list of network configurations.
                                    returned: always
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
                                            returned: always
                                            type: bool
                                            sample: null
                                        enable_accelerated_networking:
                                            description:
                                                - >-
                                                    Specifies whether the network interface is accelerated
                                                    networking-enabled.
                                            returned: always
                                            type: bool
                                            sample: null
                                        network_security_group:
                                            description:
                                                - The network security group.
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
                                        dns_settings:
                                            description:
                                                - >-
                                                    The dns settings to be applied on the network
                                                    interfaces.
                                            returned: always
                                            type: dict
                                            sample: null
                                            contains:
                                                dns_servers:
                                                    description:
                                                        - List of DNS servers IP addresses
                                                    returned: always
                                                    type: list
                                                    sample: null
                                        ip_configurations:
                                            description:
                                                - >-
                                                    Specifies the IP configurations of the network
                                                    interface.
                                            returned: always
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
                                                    returned: always
                                                    type: dict
                                                    sample: null
                                                    contains:
                                                        id:
                                                            description:
                                                                - >-
                                                                    The ARM resource id in the form of
                                                                    /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
                                                            returned: always
                                                            type: str
                                                            sample: null
                                                primary:
                                                    description:
                                                        - >-
                                                            Specifies the primary network interface in case
                                                            the virtual machine has more than 1 network
                                                            interface.
                                                    returned: always
                                                    type: bool
                                                    sample: null
                                                public_ip_address_configuration:
                                                    description:
                                                        - The publicIPAddressConfiguration.
                                                    returned: always
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
                                                            returned: always
                                                            type: int
                                                            sample: null
                                                        dns_settings:
                                                            description:
                                                                - >-
                                                                    The dns settings to be applied on the publicIP
                                                                    addresses .
                                                            returned: always
                                                            type: dict
                                                            sample: null
                                                            contains:
                                                                domain_name_label:
                                                                    description:
                                                                        - >-
                                                                            The Domain name label.The concatenation of
                                                                            the domain name label and vm index will be
                                                                            the domain name labels of the
                                                                            PublicIPAddress resources that will be
                                                                            created
                                                                    returned: always
                                                                    type: str
                                                                    sample: null
                                                        ip_tags:
                                                            description:
                                                                - >-
                                                                    The list of IP tags associated with the public
                                                                    IP address.
                                                            returned: always
                                                            type: list
                                                            sample: null
                                                            contains:
                                                                ip_tag_type:
                                                                    description:
                                                                        - 'IP tag type. Example: FirstPartyUsage.'
                                                                    returned: always
                                                                    type: str
                                                                    sample: null
                                                                tag:
                                                                    description:
                                                                        - >-
                                                                            IP tag associated with the public IP.
                                                                            Example: SQL, Storage etc.
                                                                    returned: always
                                                                    type: str
                                                                    sample: null
                                                        public_ip_prefix:
                                                            description:
                                                                - >-
                                                                    The PublicIPPrefix from which to allocate
                                                                    publicIP addresses.
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
                                                        public_ip_address_version:
                                                            description:
                                                                - >-
                                                                    Available from Api-Version 2019-07-01 onwards,
                                                                    it represents whether the specific
                                                                    ipconfiguration is IPv4 or IPv6. Default is
                                                                    taken as IPv4. Possible values are: 'IPv4' and
                                                                    'IPv6'.
                                                            returned: always
                                                            type: str
                                                            sample: null
                                                private_ip_address_version:
                                                    description:
                                                        - >-
                                                            Available from Api-Version 2017-03-30 onwards, it
                                                            represents whether the specific ipconfiguration is
                                                            IPv4 or IPv6. Default is taken as IPv4.  Possible
                                                            values are: 'IPv4' and 'IPv6'.
                                                    returned: always
                                                    type: str
                                                    sample: null
                                                application_gateway_backend_address_pools:
                                                    description:
                                                        - >-
                                                            Specifies an array of references to backend
                                                            address pools of application gateways. A scale set
                                                            can reference backend address pools of multiple
                                                            application gateways. Multiple scale sets cannot
                                                            use the same application gateway.
                                                    returned: always
                                                    type: list
                                                    sample: null
                                                    contains:
                                                        id:
                                                            description:
                                                                - Resource Id
                                                            returned: always
                                                            type: str
                                                            sample: null
                                                application_security_groups:
                                                    description:
                                                        - >-
                                                            Specifies an array of references to application
                                                            security group.
                                                    returned: always
                                                    type: list
                                                    sample: null
                                                    contains:
                                                        id:
                                                            description:
                                                                - Resource Id
                                                            returned: always
                                                            type: str
                                                            sample: null
                                                load_balancer_backend_address_pools:
                                                    description:
                                                        - >-
                                                            Specifies an array of references to backend
                                                            address pools of load balancers. A scale set can
                                                            reference backend address pools of one public and
                                                            one internal load balancer. Multiple scale sets
                                                            cannot use the same basic sku load balancer.
                                                    returned: always
                                                    type: list
                                                    sample: null
                                                    contains:
                                                        id:
                                                            description:
                                                                - Resource Id
                                                            returned: always
                                                            type: str
                                                            sample: null
                                                load_balancer_inbound_nat_pools:
                                                    description:
                                                        - >-
                                                            Specifies an array of references to inbound Nat
                                                            pools of the load balancers. A scale set can
                                                            reference inbound nat pools of one public and one
                                                            internal load balancer. Multiple scale sets cannot
                                                            use the same basic sku load balancer.
                                                    returned: always
                                                    type: list
                                                    sample: null
                                                    contains:
                                                        id:
                                                            description:
                                                                - Resource Id
                                                            returned: always
                                                            type: str
                                                            sample: null
                                        enable_ip_forwarding:
                                            description:
                                                - Whether IP forwarding enabled on this NIC.
                                            returned: always
                                            type: bool
                                            sample: null
                        security_profile:
                            description:
                                - >-
                                    Specifies the Security related profile settings for the
                                    virtual machines in the scale set.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                encryption_at_host:
                                    description:
                                        - >-
                                            This property can be used by user in the request to enable
                                            or disable the Host Encryption for the virtual machine or
                                            virtual machine scale set. This will enable the encryption
                                            for all the disks including Resource/Temp disk at host
                                            itself. :code:`<br>`:code:`<br>` Default: The Encryption
                                            at host will be disabled unless this property is set to
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
                                            Boot Diagnostics is a debugging feature which allows you
                                            to view Console Output and Screenshot to diagnose VM
                                            status. :code:`<br>`:code:`<br>` You can easily view the
                                            output of your console log. :code:`<br>`:code:`<br>` Azure
                                            also enables you to see a screenshot of the VM from the
                                            hypervisor.
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        enabled:
                                            description:
                                                - >-
                                                    Whether boot diagnostics should be enabled on the
                                                    Virtual Machine.
                                            returned: always
                                            type: bool
                                            sample: null
                                        storage_uri:
                                            description:
                                                - >-
                                                    Uri of the storage account to use for placing the
                                                    console output and screenshot.
                                                    :code:`<br>`:code:`<br>`If storageUri is not specified
                                                    while enabling boot diagnostics, managed storage will
                                                    be used.
                                            returned: always
                                            type: str
                                            sample: null
                        extension_profile:
                            description:
                                - >-
                                    Specifies a collection of settings for extensions installed on
                                    virtual machines in the scale set.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                extensions:
                                    description:
                                        - The virtual machine scale set child extension resources.
                                    returned: always
                                    type: list
                                    sample: null
                                    contains:
                                        name:
                                            description:
                                                - The name of the extension.
                                            returned: always
                                            type: str
                                            sample: null
                                        force_update_tag:
                                            description:
                                                - >-
                                                    If a value is provided and is different from the
                                                    previous value, the extension handler will be forced
                                                    to update even if the extension configuration has not
                                                    changed.
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
                                                    Indicates whether the extension should use a newer
                                                    minor version if one is available at deployment time.
                                                    Once deployed, however, the extension will not upgrade
                                                    minor versions unless redeployed, even with this
                                                    property set to true.
                                            returned: always
                                            type: bool
                                            sample: null
                                        enable_automatic_upgrade:
                                            description:
                                                - >-
                                                    Indicates whether the extension should be
                                                    automatically upgraded by the platform if there is a
                                                    newer version of the extension available.
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
                                                    protectedSettingsFromKeyVault or no protected settings
                                                    at all.
                                            returned: always
                                            type: any
                                            sample: null
                                        provision_after_extensions:
                                            description:
                                                - >-
                                                    Collection of extension names after which this
                                                    extension needs to be provisioned.
                                            returned: always
                                            type: list
                                            sample: null
                                extensions_time_budget:
                                    description:
                                        - >-
                                            Specifies the time alloted for all extensions to start.
                                            The time duration should be between 15 minutes and 120
                                            minutes (inclusive) and should be specified in ISO 8601
                                            format. The default value is 90 minutes (PT1H30M).
                                            :code:`<br>`:code:`<br>` Minimum api-version: 2020-06-01
                                    returned: always
                                    type: str
                                    sample: null
                        license_type:
                            description:
                                - >-
                                    Specifies that the image or disk that is being used was
                                    licensed on-premises. This element is only used for images
                                    that contain the Windows Server operating system.
                                    :code:`<br>`:code:`<br>` Possible values are:
                                    :code:`<br>`:code:`<br>` Windows_Client
                                    :code:`<br>`:code:`<br>` Windows_Server
                                    :code:`<br>`:code:`<br>` If this element is included in a
                                    request for an update, the value must match the initial value.
                                    This value cannot be updated. :code:`<br>`:code:`<br>` For
                                    more information, see `Azure Hybrid Use Benefit for Windows
                                    Server
                                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                                    :code:`<br>`:code:`<br>` Minimum api-version: 2015-06-15
                            returned: always
                            type: str
                            sample: null
                        priority:
                            description:
                                - >-
                                    Specifies the priority for the virtual machines in the scale
                                    set. :code:`<br>`:code:`<br>`Minimum api-version:
                                    2017-10-30-preview
                            returned: always
                            type: str
                            sample: null
                        eviction_policy:
                            description:
                                - >-
                                    Specifies the eviction policy for the Azure Spot virtual
                                    machine and Azure Spot scale set. :code:`<br>`:code:`<br>`For
                                    Azure Spot virtual machines, both 'Deallocate' and 'Delete'
                                    are supported and the minimum api-version is 2019-03-01.
                                    :code:`<br>`:code:`<br>`For Azure Spot scale sets, both
                                    'Deallocate' and 'Delete' are supported and the minimum
                                    api-version is 2017-10-30-preview.
                            returned: always
                            type: str
                            sample: null
                        billing_profile:
                            description:
                                - >-
                                    Specifies the billing related details of a Azure Spot VMSS.
                                    :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                max_price:
                                    description:
                                        - >-
                                            Specifies the maximum price you are willing to pay for a
                                            Azure Spot VM/VMSS. This price is in US Dollars.
                                            :code:`<br>`:code:`<br>` This price will be compared with
                                            the current Azure Spot price for the VM size. Also, the
                                            prices are compared at the time of create/update of Azure
                                            Spot VM/VMSS and the operation will only succeed if  the
                                            maxPrice is greater than the current Azure Spot price.
                                            :code:`<br>`:code:`<br>` The maxPrice will also be used
                                            for evicting a Azure Spot VM/VMSS if the current Azure
                                            Spot price goes beyond the maxPrice after creation of
                                            VM/VMSS. :code:`<br>`:code:`<br>` Possible values are:
                                            :code:`<br>`:code:`<br>` - Any decimal value greater than
                                            zero. Example: 0.01538 :code:`<br>`:code:`<br>` -1 –
                                            indicates default price to be up-to on-demand.
                                            :code:`<br>`:code:`<br>` You can set the maxPrice to -1 to
                                            indicate that the Azure Spot VM/VMSS should not be evicted
                                            for price reasons. Also, the default max price is -1 if it
                                            is not provided by you. :code:`<br>`:code:`<br>`Minimum
                                            api-version: 2019-03-01.
                                    returned: always
                                    type: number
                                    sample: null
                        scheduled_events_profile:
                            description:
                                - Specifies Scheduled Event related configurations.
                            returned: always
                            type: dict
                            sample: null
                            contains:
                                terminate_notification_profile:
                                    description:
                                        - >-
                                            Specifies Terminate Scheduled Event related
                                            configurations.
                                    returned: always
                                    type: dict
                                    sample: null
                                    contains:
                                        not_before_timeout:
                                            description:
                                                - >-
                                                    Configurable length of time a Virtual Machine being
                                                    deleted will have to potentially approve the Terminate
                                                    Scheduled Event before the event is auto approved
                                                    (timed out). The configuration must be specified in
                                                    ISO 8601 format, the default value is 5 minutes (PT5M)
                                            returned: always
                                            type: str
                                            sample: null
                                        enable:
                                            description:
                                                - >-
                                                    Specifies whether the Terminate Scheduled event is
                                                    enabled or disabled.
                                            returned: always
                                            type: bool
                                            sample: null
                overprovision:
                    description:
                        - >-
                            Specifies whether the Virtual Machine Scale Set should be
                            overprovisioned.
                    returned: always
                    type: bool
                    sample: null
                do_not_run_extensions_on_overprovisioned_v_ms:
                    description:
                        - >-
                            When Overprovision is enabled, extensions are launched only on the
                            requested number of VMs which are finally kept. This property will
                            hence ensure that the extensions do not run on the extra
                            overprovisioned VMs.
                    returned: always
                    type: bool
                    sample: null
                single_placement_group:
                    description:
                        - >-
                            When true this limits the scale set to a single placement group,
                            of max size 100 virtual machines. NOTE: If singlePlacementGroup is
                            true, it may be modified to false. However, if
                            singlePlacementGroup is false, it may not be modified to true.
                    returned: always
                    type: bool
                    sample: null
                zone_balance:
                    description:
                        - >-
                            Whether to force strictly even Virtual Machine distribution cross
                            x-zones in case there is zone outage.
                    returned: always
                    type: bool
                    sample: null
                platform_fault_domain_count:
                    description:
                        - Fault Domain count for each placement group.
                    returned: always
                    type: int
                    sample: null
                proximity_placement_group:
                    description:
                        - >-
                            Specifies information about the proximity placement group that the
                            virtual machine scale set should be assigned to.
                            :code:`<br>`:code:`<br>`Minimum api-version: 2018-04-01.
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
                            Specifies information about the dedicated host group that the
                            virtual machine scale set resides in.
                            :code:`<br>`:code:`<br>`Minimum api-version: 2020-06-01.
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
                additional_capabilities:
                    description:
                        - >-
                            Specifies additional capabilities enabled or disabled on the
                            Virtual Machines in the Virtual Machine Scale Set. For instance:
                            whether the Virtual Machines have the capability to support
                            attaching managed data disks with UltraSSD_LRS storage account
                            type.
                    returned: always
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
                            returned: always
                            type: bool
                            sample: null
                scale_in_policy:
                    description:
                        - >-
                            Specifies the scale-in policy that decides which virtual machines
                            are chosen for removal when a Virtual Machine Scale Set is
                            scaled-in.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        rules:
                            description:
                                - >-
                                    The rules to be followed when scaling-in a virtual machine
                                    scale set. :code:`<br>`:code:`<br>` Possible values are:
                                    :code:`<br>`:code:`<br>` **Default** When a virtual machine
                                    scale set is scaled in, the scale set will first be balanced
                                    across zones if it is a zonal scale set. Then, it will be
                                    balanced across Fault Domains as far as possible. Within each
                                    Fault Domain, the virtual machines chosen for removal will be
                                    the newest ones that are not protected from scale-in.
                                    :code:`<br>`:code:`<br>` **OldestVM** When a virtual machine
                                    scale set is being scaled-in, the oldest virtual machines that
                                    are not protected from scale-in will be chosen for removal.
                                    For zonal virtual machine scale sets, the scale set will first
                                    be balanced across zones. Within each zone, the oldest virtual
                                    machines that are not protected will be chosen for removal.
                                    :code:`<br>`:code:`<br>` **NewestVM** When a virtual machine
                                    scale set is being scaled-in, the newest virtual machines that
                                    are not protected from scale-in will be chosen for removal.
                                    For zonal virtual machine scale sets, the scale set will first
                                    be balanced across zones. Within each zone, the newest virtual
                                    machines that are not protected will be chosen for removal.
                                    :code:`<br>`:code:`<br>`
                            returned: always
                            type: list
                            sample: null
        next_link:
            description:
                - >-
                    The uri to fetch the next page of Virtual Machine Scale Sets. Call
                    ListNext() with this to fetch the next page of VMSS.

                    The uri to fetch the next page of Virtual Machine Scale Sets. Call
                    ListNext() with this to fetch the next page of Virtual Machine Scale
                    Sets.

                    The uri to fetch the next page of Virtual Machine Scale Set Skus. Call
                    ListNext() with this to fetch the next page of VMSS Skus.

                    The uri to fetch the next page of OS Upgrade History. Call ListNext()
                    with this to fetch the next page of history of upgrades.
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


class AzureRMVirtualMachineScaleSetInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            vm_scale_set_name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.vm_scale_set_name = None

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
        super(AzureRMVirtualMachineScaleSetInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.vm_scale_set_name is not None):
            self.results['virtual_machine_scale_sets'] = self.format_item(self.get())
        elif (self.resource_group is not None and
              self.vm_scale_set_name is not None):
            self.results['virtual_machine_scale_sets'] = self.format_item(self.get_instance_view())
        elif (self.resource_group is not None and
              self.vm_scale_set_name is not None):
            self.results['virtual_machine_scale_sets'] = self.format_item(self.list_skus())
        elif (self.resource_group is not None and
              self.vm_scale_set_name is not None):
            self.results['virtual_machine_scale_sets'] = self.format_item(self.get_os_upgrade_history())
        elif (self.resource_group is not None):
            self.results['virtual_machine_scale_sets'] = self.format_item(self.list())
        else:
            self.results['virtual_machine_scale_sets'] = self.format_item(self.list_all())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.get(resource_group=self.resource_group,
                                                                       vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get_instance_view(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.get_instance_view(resource_group=self.resource_group,
                                                                                     vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_skus(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.list_skus(resource_group=self.resource_group,
                                                                             vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def get_os_upgrade_history(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.get_os_upgrade_history(resource_group=self.resource_group,
                                                                                          vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.list(resource_group=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_all(self):
        response = None

        try:
            response = self.mgmt_client.virtual_machine_scale_sets.list_all()
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
    AzureRMVirtualMachineScaleSetInfo()


if __name__ == '__main__':
    main()
