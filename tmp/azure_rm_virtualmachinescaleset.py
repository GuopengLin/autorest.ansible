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
    module: azure_rm_virtualmachinescaleset
    version_added: '2.9'
    short_description: Manage Azure VirtualMachineScaleSet instance.
    description:
      - 'Create, update and delete instance of Azure VirtualMachineScaleSet.'
    options:
      resource_group:
        description:
          - The name of the resource group.
        required: true
        type: str
      vm_scale_set_name:
        description:
          - The name of the VM scale set to create or update.
          - The name of the VM scale set.
        required: true
        type: str
      sku:
        description:
          - The virtual machine scale set sku.
        type: dict
        suboptions:
          name:
            description:
              - The sku name.
            type: str
          tier:
            description:
              - >-
                Specifies the tier of virtual machines in a scale set.:code:`<br
                />`:code:`<br />` Possible Values::code:`<br />`:code:`<br />`
                **Standard**\ :code:`<br />`:code:`<br />` **Basic**
            type: str
          capacity:
            description:
              - Specifies the number of virtual machines in the scale set.
            type: int
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
          - >-
            The purchase plan when deploying a virtual machine scale set from VM
            Marketplace images.
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
      identity:
        description:
          - 'The identity of the virtual machine scale set, if configured.'
        type: dict
        suboptions:
          type:
            description:
              - >-
                The type of identity used for the virtual machine scale set. The
                type 'SystemAssigned, UserAssigned' includes both an implicitly
                created identity and a set of user assigned identities. The type
                'None' will remove any identities from the virtual machine scale
                set.
            type: sealed-choice
          user_assigned_identities:
            description:
              - >-
                The list of user identities associated with the virtual machine
                scale set. The user identity dictionary key references will be ARM
                resource ids in the form:
                '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
            type: dict
      zones:
        description:
          - >-
            The virtual machine scale set zones. NOTE: Availability zones can only
            be set when you create the scale set
        type: list
      upgrade_policy:
        description:
          - The upgrade policy.
        type: dict
        suboptions:
          mode:
            description:
              - >-
                Specifies the mode of an upgrade to virtual machines in the scale
                set.:code:`<br />`:code:`<br />` Possible values are::code:`<br
                />`:code:`<br />` **Manual** - You  control the application of
                updates to virtual machines in the scale set. You do this by using
                the manualUpgrade action.:code:`<br />`:code:`<br />` **Automatic**
                - All virtual machines in the scale set are  automatically updated
                at the same time.
            type: sealed-choice
          rolling_upgrade_policy:
            description:
              - >-
                The configuration parameters used while performing a rolling
                upgrade.
            type: dict
            suboptions:
              max_batch_instance_percent:
                description:
                  - >-
                    The maximum percent of total virtual machine instances that will
                    be upgraded simultaneously by the rolling upgrade in one batch.
                    As this is a maximum, unhealthy instances in previous or future
                    batches can cause the percentage of instances in a batch to
                    decrease to ensure higher reliability. The default value for
                    this parameter is 20%.
                type: int
              max_unhealthy_instance_percent:
                description:
                  - >-
                    The maximum percentage of the total virtual machine instances in
                    the scale set that can be simultaneously unhealthy, either as a
                    result of being upgraded, or by being found in an unhealthy
                    state by the virtual machine health checks before the rolling
                    upgrade aborts. This constraint will be checked prior to
                    starting any batch. The default value for this parameter is 20%.
                type: int
              max_unhealthy_upgraded_instance_percent:
                description:
                  - >-
                    The maximum percentage of upgraded virtual machine instances
                    that can be found to be in an unhealthy state. This check will
                    happen after each batch is upgraded. If this percentage is ever
                    exceeded, the rolling update aborts. The default value for this
                    parameter is 20%.
                type: int
              pause_time_between_batches:
                description:
                  - >-
                    The wait time between completing the update for all virtual
                    machines in one batch and starting the next batch. The time
                    duration should be specified in ISO 8601 format. The default
                    value is 0 seconds (PT0S).
                type: str
          automatic_os_upgrade_policy:
            description:
              - Configuration parameters used for performing automatic OS Upgrade.
            type: dict
            suboptions:
              enable_automatic_os_upgrade:
                description:
                  - >-
                    Indicates whether OS upgrades should automatically be applied to
                    scale set instances in a rolling fashion when a newer version of
                    the OS image becomes available. Default value is false.
                    :code:`<br>`:code:`<br>` If this is set to true for Windows
                    based scale sets, `enableAutomaticUpdates
                    <https://docs.microsoft.com/dotnet/api/microsoft.azure.management.compute.models.windowsconfiguration.enableautomaticupdates?view=azure-dotnet>`_
                    is automatically set to false and cannot be set to true.
                type: bool
              disable_automatic_rollback:
                description:
                  - >-
                    Whether OS image rollback feature should be disabled. Default
                    value is false.
                type: bool
      automatic_repairs_policy:
        description:
          - Policy for automatic repairs.
        type: dict
        suboptions:
          enabled:
            description:
              - >-
                Specifies whether automatic repairs should be enabled on the virtual
                machine scale set. The default value is false.
            type: bool
          grace_period:
            description:
              - >-
                The amount of time for which automatic repairs are suspended due to
                a state change on VM. The grace time starts after the state change
                has completed. This helps avoid premature or accidental repairs. The
                time duration should be specified in ISO 8601 format. The minimum
                allowed grace period is 30 minutes (PT30M), which is also the
                default value. The maximum allowed grace period is 90 minutes
                (PT90M).
            type: str
      virtual_machine_profile:
        description:
          - The virtual machine profile.
        type: dict
        suboptions:
          os_profile:
            description:
              - >-
                Specifies the operating system settings for the virtual machines in
                the scale set.
            type: dict
            suboptions:
              computer_name_prefix:
                description:
                  - >-
                    Specifies the computer name prefix for all of the virtual
                    machines in the scale set. Computer name prefixes must be 1 to
                    15 characters long.
                type: str
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
              admin_password:
                description:
                  - >-
                    Specifies the password of the administrator account.
                    :code:`<br>`:code:`<br>` **Minimum-length (Windows):** 8
                    characters :code:`<br>`:code:`<br>` **Minimum-length (Linux):**
                    6 characters :code:`<br>`:code:`<br>` **Max-length (Windows):**
                    123 characters :code:`<br>`:code:`<br>` **Max-length (Linux):**
                    72 characters :code:`<br>`:code:`<br>` **Complexity
                    requirements:** 3 out of 4 conditions below need to be fulfilled
                    :code:`<br>` Has lower characters :code:`<br>`Has upper
                    characters :code:`<br>` Has a digit :code:`<br>` Has a special
                    character (Regex match [\W_]) :code:`<br>`:code:`<br>`
                    **Disallowed values:** "abc@123", "P@$$w0rd", "P@ssw0rd",
                    "P@ssword123", "Pa$$word", "pass@word1", "Password!",
                    "Password1", "Password22", "iloveyou!" :code:`<br>`:code:`<br>`
                    For resetting the password, see `How to reset the Remote Desktop
                    service or its login password in a Windows VM
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-reset-rdp?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_
                    :code:`<br>`:code:`<br>` For resetting root password, see
                    `Manage users, SSH, and check or repair disks on Azure Linux VMs
                    using the VMAccess Extension
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-using-vmaccess-extension?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#reset-root-password>`_
                type: str
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
                type: str
              windows_configuration:
                description:
                  - >-
                    Specifies Windows operating system settings on the virtual
                    machine.
                type: dict
                suboptions:
                  provision_vm_agent:
                    description:
                      - >-
                        Indicates whether virtual machine agent should be
                        provisioned on the virtual machine. :code:`<br>`:code:`<br>`
                        When this property is not specified in the request body,
                        default behavior is to set it to true.  This will ensure
                        that VM Agent is installed on the VM so that extensions can
                        be added to the VM later.
                    type: bool
                  enable_automatic_updates:
                    description:
                      - >-
                        Indicates whether Automatic Updates is enabled for the
                        Windows virtual machine. Default value is true.
                        :code:`<br>`:code:`<br>` For virtual machine scale sets,
                        this property can be updated and updates will take effect on
                        OS reprovisioning.
                    type: bool
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
                  additional_unattend_content:
                    description:
                      - >-
                        Specifies additional base-64 encoded XML formatted
                        information that can be included in the Unattend.xml file,
                        which is used by Windows Setup.
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
                            The component name. Currently, the only allowable value
                            is Microsoft-Windows-Shell-Setup.
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
                            unattend.xml file for the specified path and component.
                            The XML must be less than 4KB and must include the root
                            element for the setting or feature that is being
                            inserted.
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
                            are::code:`<br />`:code:`<br />` **Manual** - You 
                            control the application of patches to a virtual machine.
                            You do this by applying patches manually inside the VM.
                            In this mode, automatic updates are disabled; the
                            property WindowsConfiguration.enableAutomaticUpdates
                            must be false:code:`<br />`:code:`<br />`
                            **AutomaticByOS** - The virtual machine will
                            automatically be updated by the OS. The property
                            WindowsConfiguration.enableAutomaticUpdates must be
                            true. :code:`<br />`:code:`<br />` **
                            AutomaticByPlatform** - the virtual machine will
                            automatically updated by the platform. The properties
                            provisionVMAgent and
                            WindowsConfiguration.enableAutomaticUpdates must be true
                        type: str
                        choices:
                          - Manual
                          - AutomaticByOS
                          - AutomaticByPlatform
                  win_rm:
                    description:
                      - >-
                        Specifies the Windows Remote Management listeners. This
                        enables remote Windows PowerShell.
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
                                This is the URL of a certificate that has been
                                uploaded to Key Vault as a secret. For adding a
                                secret to the Key Vault, see `Add a key or secret to
                                the key vault
                                <https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add>`_.
                                In this case, your certificate needs to be It is the
                                Base64 encoding of the following JSON Object which
                                is encoded in UTF-8: :code:`<br>`:code:`<br>`
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
                    :code:`<br>`:code:`<br>` For running non-endorsed distributions,
                    see `Information for Non-Endorsed Distributions
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-create-upload-generic?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json>`_.
                type: dict
                suboptions:
                  disable_password_authentication:
                    description:
                      - >-
                        Specifies whether password authentication should be
                        disabled.
                    type: bool
                  ssh:
                    description:
                      - Specifies the ssh key configuration for a Linux OS.
                    type: dict
                    suboptions:
                      public_keys:
                        description:
                          - >-
                            The list of SSH public keys used to authenticate with
                            linux based VMs.
                        type: list
                        suboptions:
                          path:
                            description:
                              - >-
                                Specifies the full path on the created VM where ssh
                                public key is stored. If the file already exists,
                                the specified key is appended to the file. Example:
                                /home/user/.ssh/authorized_keys
                            type: str
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
                  provision_vm_agent:
                    description:
                      - >-
                        Indicates whether virtual machine agent should be
                        provisioned on the virtual machine. :code:`<br>`:code:`<br>`
                        When this property is not specified in the request body,
                        default behavior is to set it to true.  This will ensure
                        that VM Agent is installed on the VM so that extensions can
                        be added to the VM later.
                    type: bool
              secrets:
                description:
                  - >-
                    Specifies set of certificates that should be installed onto the
                    virtual machines in the scale set.
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
                        The list of key vault references in SourceVault which
                        contain certificates.
                    type: list
                    suboptions:
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
                      certificate_store:
                        description:
                          - >-
                            For Windows VMs, specifies the certificate store on the
                            Virtual Machine to which the certificate should be
                            added. The specified certificate store is implicitly in
                            the LocalMachine account. :code:`<br>`:code:`<br>`For
                            Linux VMs, the certificate file is placed under the
                            /var/lib/waagent directory, with the file name
                            &lt;UppercaseThumbprint&gt;.crt for the X509 certificate
                            file and &lt;UppercaseThumbprint&gt;.prv for private
                            key. Both of these files are .pem formatted.
                        type: str
          storage_profile:
            description:
              - Specifies the storage settings for the virtual machine disks.
            type: dict
            suboptions:
              image_reference:
                description:
                  - >-
                    Specifies information about the image to use. You can specify
                    information about platform images, marketplace images, or
                    virtual machine images. This element is required when you want
                    to use a platform image, marketplace image, or virtual machine
                    image, but is not used in other creation operations.
                type: dict
                suboptions:
                  publisher:
                    description:
                      - The image publisher.
                    type: str
                  offer:
                    description:
                      - >-
                        Specifies the offer of the platform image or marketplace
                        image used to create the virtual machine.
                    type: str
                  sku:
                    description:
                      - The image SKU.
                    type: str
                  version:
                    description:
                      - >-
                        Specifies the version of the platform image or marketplace
                        image used to create the virtual machine. The allowed
                        formats are Major.Minor.Build or 'latest'. Major, Minor, and
                        Build are decimal numbers. Specify 'latest' to use the
                        latest version of an image available at deploy time. Even if
                        you use 'latest', the VM image will not automatically update
                        after deploy time even if a new version becomes available.
                    type: str
              os_disk:
                description:
                  - >-
                    Specifies information about the operating system disk used by
                    the virtual machines in the scale set. :code:`<br>`:code:`<br>`
                    For more information about disks, see `About disks and VHDs for
                    Azure virtual machines
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                type: dict
                suboptions:
                  name:
                    description:
                      - The disk name.
                    type: str
                  caching:
                    description:
                      - >-
                        Specifies the caching requirements. :code:`<br>`:code:`<br>`
                        Possible values are: :code:`<br>`:code:`<br>` **None**
                        :code:`<br>`:code:`<br>` **ReadOnly**
                        :code:`<br>`:code:`<br>` **ReadWrite**
                        :code:`<br>`:code:`<br>` Default: **None for Standard
                        storage. ReadOnly for Premium storage**
                    type: sealed-choice
                  write_accelerator_enabled:
                    description:
                      - >-
                        Specifies whether writeAccelerator should be enabled or
                        disabled on the disk.
                    type: bool
                  create_option:
                    description:
                      - >-
                        Specifies how the virtual machines in the scale set should
                        be created.:code:`<br>`:code:`<br>` The only allowed value
                        is: **FromImage** \u2013 This value is used when you are
                        using an image to create the virtual machine. If you are
                        using a platform image, you also use the imageReference
                        element described above. If you are using a marketplace
                        image, you  also use the plan element previously described.
                    required: true
                    type: str
                    choices:
                      - FromImage
                      - Empty
                      - Attach
                  diff_disk_settings:
                    description:
                      - >-
                        Specifies the ephemeral disk Settings for the operating
                        system disk used by the virtual machine scale set.
                    type: dict
                    suboptions:
                      option:
                        description:
                          - >-
                            Specifies the ephemeral disk settings for operating
                            system disk.
                        type: str
                        choices:
                          - Local
                      placement:
                        description:
                          - >-
                            Specifies the ephemeral disk placement for operating
                            system disk.:code:`<br>`:code:`<br>` Possible values
                            are: :code:`<br>`:code:`<br>` **CacheDisk**
                            :code:`<br>`:code:`<br>` **ResourceDisk**
                            :code:`<br>`:code:`<br>` Default: **CacheDisk** if one
                            is configured for the VM size otherwise **ResourceDisk**
                            is used.:code:`<br>`:code:`<br>` Refer to VM size
                            documentation for Windows VM at
                            https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes
                            and Linux VM at
                            https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes
                            to check which VM sizes exposes a cache disk.
                        type: str
                        choices:
                          - CacheDisk
                          - ResourceDisk
                  disk_size_gb:
                    description:
                      - >-
                        Specifies the size of the operating system disk in
                        gigabytes. This element can be used to overwrite the size of
                        the disk in a virtual machine image.
                        :code:`<br>`:code:`<br>` This value cannot be larger than
                        1023 GB
                    type: int
                  os_type:
                    description:
                      - >-
                        This property allows you to specify the type of the OS that
                        is included in the disk if creating a VM from user-image or
                        a specialized VHD. :code:`<br>`:code:`<br>` Possible values
                        are: :code:`<br>`:code:`<br>` **Windows**
                        :code:`<br>`:code:`<br>` **Linux**
                    type: sealed-choice
                  image:
                    description:
                      - >-
                        Specifies information about the unmanaged user image to base
                        the scale set on.
                    type: dict
                    suboptions:
                      uri:
                        description:
                          - Specifies the virtual hard disk's uri.
                        type: str
                  vhd_containers:
                    description:
                      - >-
                        Specifies the container urls that are used to store
                        operating system disks for the scale set.
                    type: list
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
                            Specifies the customer managed disk encryption set
                            resource id for the managed disk.
                        type: dict
                        suboptions:
                          id:
                            description:
                              - Resource Id
                            type: str
              data_disks:
                description:
                  - >-
                    Specifies the parameters that are used to add data disks to the
                    virtual machines in the scale set. :code:`<br>`:code:`<br>` For
                    more information about disks, see `About disks and VHDs for
                    Azure virtual machines
                    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
                type: list
                suboptions:
                  name:
                    description:
                      - The disk name.
                    type: str
                  lun:
                    description:
                      - >-
                        Specifies the logical unit number of the data disk. This
                        value is used to identify data disks within the VM and
                        therefore must be unique for each data disk attached to a
                        VM.
                    required: true
                    type: int
                  caching:
                    description:
                      - >-
                        Specifies the caching requirements. :code:`<br>`:code:`<br>`
                        Possible values are: :code:`<br>`:code:`<br>` **None**
                        :code:`<br>`:code:`<br>` **ReadOnly**
                        :code:`<br>`:code:`<br>` **ReadWrite**
                        :code:`<br>`:code:`<br>` Default: **None for Standard
                        storage. ReadOnly for Premium storage**
                    type: sealed-choice
                  write_accelerator_enabled:
                    description:
                      - >-
                        Specifies whether writeAccelerator should be enabled or
                        disabled on the disk.
                    type: bool
                  create_option:
                    description:
                      - The create option.
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
                            Specifies the customer managed disk encryption set
                            resource id for the managed disk.
                        type: dict
                        suboptions:
                          id:
                            description:
                              - Resource Id
                            type: str
                  disk_iops_read_write:
                    description:
                      - >-
                        Specifies the Read-Write IOPS for the managed disk. Should
                        be used only when StorageAccountType is UltraSSD_LRS. If not
                        specified, a default value would be assigned based on
                        diskSizeGB.
                    type: int
                  disk_m_bps_read_write:
                    description:
                      - >-
                        Specifies the bandwidth in MB per second for the managed
                        disk. Should be used only when StorageAccountType is
                        UltraSSD_LRS. If not specified, a default value would be
                        assigned based on diskSizeGB.
                    type: int
          network_profile:
            description:
              - >-
                Specifies properties of the network interfaces of the virtual
                machines in the scale set.
            type: dict
            suboptions:
              health_probe:
                description:
                  - >-
                    A reference to a load balancer probe used to determine the
                    health of an instance in the virtual machine scale set. The
                    reference will be in the form:
                    '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/loadBalancers/{loadBalancerName}/probes/{probeName}'.
                type: dict
                suboptions:
                  id:
                    description:
                      - >-
                        The ARM resource id in the form of
                        /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
                    type: str
              network_interface_configurations:
                description:
                  - The list of network configurations.
                type: list
                suboptions:
                  name:
                    description:
                      - The network configuration name.
                    required: true
                    type: str
                  primary:
                    description:
                      - >-
                        Specifies the primary network interface in case the virtual
                        machine has more than 1 network interface.
                    type: bool
                  enable_accelerated_networking:
                    description:
                      - >-
                        Specifies whether the network interface is accelerated
                        networking-enabled.
                    type: bool
                  network_security_group:
                    description:
                      - The network security group.
                    type: dict
                    suboptions:
                      id:
                        description:
                          - Resource Id
                        type: str
                  dns_settings:
                    description:
                      - The dns settings to be applied on the network interfaces.
                    type: dict
                    suboptions:
                      dns_servers:
                        description:
                          - List of DNS servers IP addresses
                        type: list
                  ip_configurations:
                    description:
                      - Specifies the IP configurations of the network interface.
                    type: list
                    suboptions:
                      name:
                        description:
                          - The IP configuration name.
                        required: true
                        type: str
                      subnet:
                        description:
                          - Specifies the identifier of the subnet.
                        type: dict
                        suboptions:
                          id:
                            description:
                              - >-
                                The ARM resource id in the form of
                                /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
                            type: str
                      primary:
                        description:
                          - >-
                            Specifies the primary network interface in case the
                            virtual machine has more than 1 network interface.
                        type: bool
                      public_ip_address_configuration:
                        description:
                          - The publicIPAddressConfiguration.
                        type: dict
                        suboptions:
                          name:
                            description:
                              - The publicIP address configuration name.
                            required: true
                            type: str
                          idle_timeout_in_minutes:
                            description:
                              - The idle timeout of the public IP address.
                            type: int
                          dns_settings:
                            description:
                              - >-
                                The dns settings to be applied on the publicIP
                                addresses .
                            type: dict
                            suboptions:
                              domain_name_label:
                                description:
                                  - >-
                                    The Domain name label.The concatenation of the
                                    domain name label and vm index will be the
                                    domain name labels of the PublicIPAddress
                                    resources that will be created
                                required: true
                                type: str
                          ip_tags:
                            description:
                              - >-
                                The list of IP tags associated with the public IP
                                address.
                            type: list
                            suboptions:
                              ip_tag_type:
                                description:
                                  - 'IP tag type. Example: FirstPartyUsage.'
                                type: str
                              tag:
                                description:
                                  - >-
                                    IP tag associated with the public IP. Example:
                                    SQL, Storage etc.
                                type: str
                          public_ip_prefix:
                            description:
                              - >-
                                The PublicIPPrefix from which to allocate publicIP
                                addresses.
                            type: dict
                            suboptions:
                              id:
                                description:
                                  - Resource Id
                                type: str
                          public_ip_address_version:
                            description:
                              - >-
                                Available from Api-Version 2019-07-01 onwards, it
                                represents whether the specific ipconfiguration is
                                IPv4 or IPv6. Default is taken as IPv4. Possible
                                values are: 'IPv4' and 'IPv6'.
                            type: str
                            choices:
                              - IPv4
                              - IPv6
                      private_ip_address_version:
                        description:
                          - >-
                            Available from Api-Version 2017-03-30 onwards, it
                            represents whether the specific ipconfiguration is IPv4
                            or IPv6. Default is taken as IPv4.  Possible values are:
                            'IPv4' and 'IPv6'.
                        type: str
                        choices:
                          - IPv4
                          - IPv6
                      application_gateway_backend_address_pools:
                        description:
                          - >-
                            Specifies an array of references to backend address
                            pools of application gateways. A scale set can reference
                            backend address pools of multiple application gateways.
                            Multiple scale sets cannot use the same application
                            gateway.
                        type: list
                        suboptions:
                          id:
                            description:
                              - Resource Id
                            type: str
                      application_security_groups:
                        description:
                          - >-
                            Specifies an array of references to application security
                            group.
                        type: list
                        suboptions:
                          id:
                            description:
                              - Resource Id
                            type: str
                      load_balancer_backend_address_pools:
                        description:
                          - >-
                            Specifies an array of references to backend address
                            pools of load balancers. A scale set can reference
                            backend address pools of one public and one internal
                            load balancer. Multiple scale sets cannot use the same
                            basic sku load balancer.
                        type: list
                        suboptions:
                          id:
                            description:
                              - Resource Id
                            type: str
                      load_balancer_inbound_nat_pools:
                        description:
                          - >-
                            Specifies an array of references to inbound Nat pools of
                            the load balancers. A scale set can reference inbound
                            nat pools of one public and one internal load balancer.
                            Multiple scale sets cannot use the same basic sku load
                            balancer.
                        type: list
                        suboptions:
                          id:
                            description:
                              - Resource Id
                            type: str
                  enable_ip_forwarding:
                    description:
                      - Whether IP forwarding enabled on this NIC.
                    type: bool
          security_profile:
            description:
              - >-
                Specifies the Security related profile settings for the virtual
                machines in the scale set.
            type: dict
            suboptions:
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
                    console log. :code:`<br>`:code:`<br>` Azure also enables you to
                    see a screenshot of the VM from the hypervisor.
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
                        Uri of the storage account to use for placing the console
                        output and screenshot. :code:`<br>`:code:`<br>`If storageUri
                        is not specified while enabling boot diagnostics, managed
                        storage will be used.
                    type: str
          extension_profile:
            description:
              - >-
                Specifies a collection of settings for extensions installed on
                virtual machines in the scale set.
            type: dict
            suboptions:
              extensions:
                description:
                  - The virtual machine scale set child extension resources.
                type: list
                suboptions:
                  name:
                    description:
                      - The name of the extension.
                    type: str
                  force_update_tag:
                    description:
                      - >-
                        If a value is provided and is different from the previous
                        value, the extension handler will be forced to update even
                        if the extension configuration has not changed.
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
                        Indicates whether the extension should use a newer minor
                        version if one is available at deployment time. Once
                        deployed, however, the extension will not upgrade minor
                        versions unless redeployed, even with this property set to
                        true.
                    type: bool
                  enable_automatic_upgrade:
                    description:
                      - >-
                        Indicates whether the extension should be automatically
                        upgraded by the platform if there is a newer version of the
                        extension available.
                    type: bool
                  settings:
                    description:
                      - Json formatted public settings for the extension.
                    type: any
                  protected_settings:
                    description:
                      - >-
                        The extension can contain either protectedSettings or
                        protectedSettingsFromKeyVault or no protected settings at
                        all.
                    type: any
                  provision_after_extensions:
                    description:
                      - >-
                        Collection of extension names after which this extension
                        needs to be provisioned.
                    type: list
              extensions_time_budget:
                description:
                  - >-
                    Specifies the time alloted for all extensions to start. The time
                    duration should be between 15 minutes and 120 minutes
                    (inclusive) and should be specified in ISO 8601 format. The
                    default value is 90 minutes (PT1H30M). :code:`<br>`:code:`<br>`
                    Minimum api-version: 2020-06-01
                type: str
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
          priority:
            description:
              - >-
                Specifies the priority for the virtual machines in the scale set.
                :code:`<br>`:code:`<br>`Minimum api-version: 2017-10-30-preview
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
                machines, both 'Deallocate' and 'Delete' are supported and the
                minimum api-version is 2019-03-01. :code:`<br>`:code:`<br>`For Azure
                Spot scale sets, both 'Deallocate' and 'Delete' are supported and
                the minimum api-version is 2017-10-30-preview.
            type: str
            choices:
              - Deallocate
              - Delete
          billing_profile:
            description:
              - >-
                Specifies the billing related details of a Azure Spot VMSS.
                :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
            type: dict
            suboptions:
              max_price:
                description:
                  - >-
                    Specifies the maximum price you are willing to pay for a Azure
                    Spot VM/VMSS. This price is in US Dollars.
                    :code:`<br>`:code:`<br>` This price will be compared with the
                    current Azure Spot price for the VM size. Also, the prices are
                    compared at the time of create/update of Azure Spot VM/VMSS and
                    the operation will only succeed if  the maxPrice is greater than
                    the current Azure Spot price. :code:`<br>`:code:`<br>` The
                    maxPrice will also be used for evicting a Azure Spot VM/VMSS if
                    the current Azure Spot price goes beyond the maxPrice after
                    creation of VM/VMSS. :code:`<br>`:code:`<br>` Possible values
                    are: :code:`<br>`:code:`<br>` - Any decimal value greater than
                    zero. Example: 0.01538 :code:`<br>`:code:`<br>` -1 – indicates
                    default price to be up-to on-demand. :code:`<br>`:code:`<br>`
                    You can set the maxPrice to -1 to indicate that the Azure Spot
                    VM/VMSS should not be evicted for price reasons. Also, the
                    default max price is -1 if it is not provided by you.
                    :code:`<br>`:code:`<br>`Minimum api-version: 2019-03-01.
                type: number
          scheduled_events_profile:
            description:
              - Specifies Scheduled Event related configurations.
            type: dict
            suboptions:
              terminate_notification_profile:
                description:
                  - Specifies Terminate Scheduled Event related configurations.
                type: dict
                suboptions:
                  not_before_timeout:
                    description:
                      - >-
                        Configurable length of time a Virtual Machine being deleted
                        will have to potentially approve the Terminate Scheduled
                        Event before the event is auto approved (timed out). The
                        configuration must be specified in ISO 8601 format, the
                        default value is 5 minutes (PT5M)
                    type: str
                  enable:
                    description:
                      - >-
                        Specifies whether the Terminate Scheduled event is enabled
                        or disabled.
                    type: bool
      overprovision:
        description:
          - >-
            Specifies whether the Virtual Machine Scale Set should be
            overprovisioned.
        type: bool
      do_not_run_extensions_on_overprovisioned_v_ms:
        description:
          - >-
            When Overprovision is enabled, extensions are launched only on the
            requested number of VMs which are finally kept. This property will hence
            ensure that the extensions do not run on the extra overprovisioned VMs.
        type: bool
      single_placement_group:
        description:
          - >-
            When true this limits the scale set to a single placement group, of max
            size 100 virtual machines. NOTE: If singlePlacementGroup is true, it may
            be modified to false. However, if singlePlacementGroup is false, it may
            not be modified to true.
        type: bool
      zone_balance:
        description:
          - >-
            Whether to force strictly even Virtual Machine distribution cross
            x-zones in case there is zone outage.
        type: bool
      platform_fault_domain_count:
        description:
          - Fault Domain count for each placement group.
        type: int
      proximity_placement_group:
        description:
          - >-
            Specifies information about the proximity placement group that the
            virtual machine scale set should be assigned to.
            :code:`<br>`:code:`<br>`Minimum api-version: 2018-04-01.
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
            machine scale set resides in. :code:`<br>`:code:`<br>`Minimum
            api-version: 2020-06-01.
        type: dict
        suboptions:
          id:
            description:
              - Resource Id
            type: str
      additional_capabilities:
        description:
          - >-
            Specifies additional capabilities enabled or disabled on the Virtual
            Machines in the Virtual Machine Scale Set. For instance: whether the
            Virtual Machines have the capability to support attaching managed data
            disks with UltraSSD_LRS storage account type.
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
      scale_in_policy:
        description:
          - >-
            Specifies the scale-in policy that decides which virtual machines are
            chosen for removal when a Virtual Machine Scale Set is scaled-in.
        type: dict
        suboptions:
          rules:
            description:
              - >-
                The rules to be followed when scaling-in a virtual machine scale
                set. :code:`<br>`:code:`<br>` Possible values are:
                :code:`<br>`:code:`<br>` **Default** When a virtual machine scale
                set is scaled in, the scale set will first be balanced across zones
                if it is a zonal scale set. Then, it will be balanced across Fault
                Domains as far as possible. Within each Fault Domain, the virtual
                machines chosen for removal will be the newest ones that are not
                protected from scale-in. :code:`<br>`:code:`<br>` **OldestVM** When
                a virtual machine scale set is being scaled-in, the oldest virtual
                machines that are not protected from scale-in will be chosen for
                removal. For zonal virtual machine scale sets, the scale set will
                first be balanced across zones. Within each zone, the oldest virtual
                machines that are not protected will be chosen for removal.
                :code:`<br>`:code:`<br>` **NewestVM** When a virtual machine scale
                set is being scaled-in, the newest virtual machines that are not
                protected from scale-in will be chosen for removal. For zonal
                virtual machine scale sets, the scale set will first be balanced
                across zones. Within each zone, the newest virtual machines that are
                not protected will be chosen for removal. :code:`<br>`:code:`<br>`
            type: list
      state:
        description:
          - Assert the state of the VirtualMachineScaleSet.
          - >-
            Use C(present) to create or update an VirtualMachineScaleSet and
            C(absent) to delete it.
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
    - name: Create a custom-image scale set from an unmanaged generalized os image.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
            storage_profile:
              os_disk:
                caching: ReadWrite
                create_option: FromImage
                image:
                  uri: >-
                    http://{existing-storage-account-name}.blob.core.windows.net/{existing-container-name}/{existing-generalized-os-image-blob-name}.vhd
                name: osDisk
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a platform-image scale set with unmanaged os disks.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
            storage_profile:
              image_reference:
                offer: WindowsServer
                publisher: MicrosoftWindowsServer
                sku: 2016-Datacenter
                version: latest
              os_disk:
                caching: ReadWrite
                create_option: FromImage
                name: osDisk
                vhd_containers:
                  - >-
                    http://{existing-storage-account-name-0}.blob.core.windows.net/vhdContainer
                  - >-
                    http://{existing-storage-account-name-1}.blob.core.windows.net/vhdContainer
                  - >-
                    http://{existing-storage-account-name-2}.blob.core.windows.net/vhdContainer
                  - >-
                    http://{existing-storage-account-name-3}.blob.core.windows.net/vhdContainer
                  - >-
                    http://{existing-storage-account-name-4}.blob.core.windows.net/vhdContainer
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set from a custom image.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
            storage_profile:
              image_reference:
                id: >-
                  /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Compute/images/{existing-custom-image-name}
              os_disk:
                caching: ReadWrite
                create_option: FromImage
                managed_disk:
                  storage_account_type: Standard_LRS
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with DiskEncryptionSet resource in os disk and data disk.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_DS1_v2
          tier: Standard
        

    - name: Create a scale set with Host Encryption using encryptionAtHost property.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        plan:
          name: windows2016
          product: windows-data-science-vm
          publisher: microsoft-ads
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_DS1_v2
          tier: Standard
        

    - name: Create a scale set with a marketplace image plan.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        plan:
          name: windows2016
          product: windows-data-science-vm
          publisher: microsoft-ads
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with an azure application gateway.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          application_gateway_backend_address_pools:
                            - id: >-
                                /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/applicationGateways/{existing-application-gateway-name}/backendAddressPools/{existing-backend-address-pool-name}
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with an azure load balancer.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          load_balancer_backend_address_pools:
                            - id: >-
                                /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/loadBalancers/{existing-load-balancer-name}/backendAddressPools/{existing-backend-address-pool-name}
                          load_balancer_inbound_nat_pools:
                            - id: >-
                                /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/loadBalancers/{existing-load-balancer-name}/inboundNatPools/{existing-nat-pool-name}
                          public_ipaddress_configuration:
                            name: '{vmss-name}'
                            properties:
                              public_ipaddress_version: IPv4
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with automatic repairs enabled
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          automatic_repairs_policy:
            enabled: true
            grace_period: PT30M
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with boot diagnostics.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            diagnostics_profile:
              boot_diagnostics:
                enabled: true
                storage_uri: 'http://{existing-storage-account-name}.blob.core.windows.net'
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with empty data disks on each vm.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
                disk_size_gb: 512
                managed_disk:
                  storage_account_type: Standard_LRS
        sku:
          capacity: 3
          name: Standard_D2_v2
          tier: Standard
        

    - name: Create a scale set with ephemeral os disks using placement property.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        plan:
          name: windows2016
          product: windows-data-science-vm
          publisher: microsoft-ads
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_DS1_v2
          tier: Standard
        

    - name: Create a scale set with ephemeral os disks.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        plan:
          name: windows2016
          product: windows-data-science-vm
          publisher: microsoft-ads
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_DS1_v2
          tier: Standard
        

    - name: Create a scale set with extension time budget.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            diagnostics_profile:
              boot_diagnostics:
                enabled: true
                storage_uri: 'http://{existing-storage-account-name}.blob.core.windows.net'
            extension_profile:
              extensions:
                - name: '{extension-name}'
                  properties:
                    auto_upgrade_minor_version: false
                    publisher: '{extension-Publisher}'
                    settings: {}
                    type: '{extension-Type}'
                    type_handler_version: '{handler-version}'
              extensions_time_budget: PT1H20M
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with managed boot diagnostics.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            diagnostics_profile:
              boot_diagnostics:
                enabled: true
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with password authentication.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with premium storage.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with ssh authentication.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
                offer: WindowsServer
                publisher: MicrosoftWindowsServer
                sku: 2016-Datacenter
                version: latest
              os_disk:
                caching: ReadWrite
                create_option: FromImage
                managed_disk:
                  storage_account_type: Standard_LRS
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with terminate scheduled events enabled.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: westus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Manual
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
            scheduled_events_profile:
              terminate_notification_profile:
                enable: true
                not_before_timeout: PT5M
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
        sku:
          capacity: 3
          name: Standard_D1_v2
          tier: Standard
        

    - name: Create a scale set with virtual machines in different zones.
      azure_rm_virtualmachinescaleset: 
        resource_group_name: myResourceGroup
        vm_scale_set_name: '{vmss-name}'
        location: centralus
        properties:
          overprovision: true
          upgrade_policy:
            mode: Automatic
          virtual_machine_profile:
            network_profile:
              network_interface_configurations:
                - name: '{vmss-name}'
                  properties:
                    enable_ipforwarding: true
                    ip_configurations:
                      - name: '{vmss-name}'
                        properties:
                          subnet:
                            id: >-
                              /subscriptions/{subscription-id}/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/{existing-virtual-network-name}/subnets/{existing-subnet-name}
                    primary: true
            os_profile:
              admin_password: '{your-password}'
              admin_username: '{your-username}'
              computer_name_prefix: '{vmss-name}'
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
                disk_size_gb: 512
                managed_disk:
                  storage_account_type: Standard_LRS
        sku:
          capacity: 2
          name: Standard_A1_v2
          tier: Standard
        zones:
          - '1'
          - '3'
        

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
              The type of identity used for the virtual machine scale set. The type
              'SystemAssigned, UserAssigned' includes both an implicitly created
              identity and a set of user assigned identities. The type 'None' will
              remove any identities from the virtual machine scale set.
          returned: always
          type: sealed-choice
          sample: null
        user_assigned_identities:
          description:
            - >-
              The list of user identities associated with the virtual machine scale
              set. The user identity dictionary key references will be ARM resource
              ids in the form:
              '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
          returned: always
          type: dict
          sample: null
    zones:
      description:
        - >-
          The virtual machine scale set zones. NOTE: Availability zones can only be
          set when you create the scale set
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
              />`:code:`<br />` **Manual** - You  control the application of updates
              to virtual machines in the scale set. You do this by using the
              manualUpgrade action.:code:`<br />`:code:`<br />` **Automatic** - All
              virtual machines in the scale set are  automatically updated at the
              same time.
          returned: always
          type: sealed-choice
          sample: null
        rolling_upgrade_policy:
          description:
            - The configuration parameters used while performing a rolling upgrade.
          returned: always
          type: dict
          sample: null
          contains:
            max_batch_instance_percent:
              description:
                - >-
                  The maximum percent of total virtual machine instances that will
                  be upgraded simultaneously by the rolling upgrade in one batch. As
                  this is a maximum, unhealthy instances in previous or future
                  batches can cause the percentage of instances in a batch to
                  decrease to ensure higher reliability. The default value for this
                  parameter is 20%.
              returned: always
              type: int
              sample: null
            max_unhealthy_instance_percent:
              description:
                - >-
                  The maximum percentage of the total virtual machine instances in
                  the scale set that can be simultaneously unhealthy, either as a
                  result of being upgraded, or by being found in an unhealthy state
                  by the virtual machine health checks before the rolling upgrade
                  aborts. This constraint will be checked prior to starting any
                  batch. The default value for this parameter is 20%.
              returned: always
              type: int
              sample: null
            max_unhealthy_upgraded_instance_percent:
              description:
                - >-
                  The maximum percentage of upgraded virtual machine instances that
                  can be found to be in an unhealthy state. This check will happen
                  after each batch is upgraded. If this percentage is ever exceeded,
                  the rolling update aborts. The default value for this parameter is
                  20%.
              returned: always
              type: int
              sample: null
            pause_time_between_batches:
              description:
                - >-
                  The wait time between completing the update for all virtual
                  machines in one batch and starting the next batch. The time
                  duration should be specified in ISO 8601 format. The default value
                  is 0 seconds (PT0S).
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
                  Indicates whether OS upgrades should automatically be applied to
                  scale set instances in a rolling fashion when a newer version of
                  the OS image becomes available. Default value is false.
                  :code:`<br>`:code:`<br>` If this is set to true for Windows based
                  scale sets, `enableAutomaticUpdates
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
              Specifies whether automatic repairs should be enabled on the virtual
              machine scale set. The default value is false.
          returned: always
          type: bool
          sample: null
        grace_period:
          description:
            - >-
              The amount of time for which automatic repairs are suspended due to a
              state change on VM. The grace time starts after the state change has
              completed. This helps avoid premature or accidental repairs. The time
              duration should be specified in ISO 8601 format. The minimum allowed
              grace period is 30 minutes (PT30M), which is also the default value.
              The maximum allowed grace period is 90 minutes (PT90M).
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
              Specifies the operating system settings for the virtual machines in
              the scale set.
          returned: always
          type: dict
          sample: null
          contains:
            computer_name_prefix:
              description:
                - >-
                  Specifies the computer name prefix for all of the virtual machines
                  in the scale set. Computer name prefixes must be 1 to 15
                  characters long.
              returned: always
              type: str
              sample: null
            admin_username:
              description:
                - >-
                  Specifies the name of the administrator account.
                  :code:`<br>`:code:`<br>` **Windows-only restriction:** Cannot end
                  in "." :code:`<br>`:code:`<br>` **Disallowed values:**
                  "administrator", "admin", "user", "user1", "test", "user2",
                  "test1", "user3", "admin1", "1", "123", "a", "actuser", "adm",
                  "admin2", "aspnet", "backup", "console", "david", "guest", "john",
                  "owner", "root", "server", "sql", "support", "support_388945a0",
                  "sys", "test2", "test3", "user4", "user5".
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
              returned: always
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
                  cloud-init for your VM, see `Using cloud-init to customize a Linux
                  VM during creation
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
                      Indicates whether virtual machine agent should be provisioned
                      on the virtual machine. :code:`<br>`:code:`<br>` When this
                      property is not specified in the request body, default
                      behavior is to set it to true.  This will ensure that VM Agent
                      is installed on the VM so that extensions can be added to the
                      VM later.
                  returned: always
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
                  returned: always
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
                  returned: always
                  type: str
                  sample: null
                additional_unattend_content:
                  description:
                    - >-
                      Specifies additional base-64 encoded XML formatted information
                      that can be included in the Unattend.xml file, which is used
                      by Windows Setup.
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
                          unattend.xml file for the specified path and component.
                          The XML must be less than 4KB and must include the root
                          element for the setting or feature that is being inserted.
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
                          The list of SSH public keys used to authenticate with
                          linux based VMs.
                      returned: always
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
                          returned: always
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
                          returned: always
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
                  returned: always
                  type: bool
                  sample: null
            secrets:
              description:
                - >-
                  Specifies set of certificates that should be installed onto the
                  virtual machines in the scale set.
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
                  platform image, marketplace image, or virtual machine image, but
                  is not used in other creation operations.
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
                      Specifies the version of the platform image or marketplace
                      image used to create the virtual machine. The allowed formats
                      are Major.Minor.Build or 'latest'. Major, Minor, and Build are
                      decimal numbers. Specify 'latest' to use the latest version of
                      an image available at deploy time. Even if you use 'latest',
                      the VM image will not automatically update after deploy time
                      even if a new version becomes available.
                  returned: always
                  type: str
                  sample: null
            os_disk:
              description:
                - >-
                  Specifies information about the operating system disk used by the
                  virtual machines in the scale set. :code:`<br>`:code:`<br>` For
                  more information about disks, see `About disks and VHDs for Azure
                  virtual machines
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
                      Specifies whether writeAccelerator should be enabled or
                      disabled on the disk.
                  returned: always
                  type: bool
                  sample: null
                create_option:
                  description:
                    - >-
                      Specifies how the virtual machines in the scale set should be
                      created.:code:`<br>`:code:`<br>` The only allowed value is:
                      **FromImage** \u2013 This value is used when you are using an
                      image to create the virtual machine. If you are using a
                      platform image, you also use the imageReference element
                      described above. If you are using a marketplace image, you 
                      also use the plan element previously described.
                  returned: always
                  type: str
                  sample: null
                diff_disk_settings:
                  description:
                    - >-
                      Specifies the ephemeral disk Settings for the operating system
                      disk used by the virtual machine scale set.
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
                      returned: always
                      type: str
                      sample: null
                disk_size_gb:
                  description:
                    - >-
                      Specifies the size of the operating system disk in gigabytes.
                      This element can be used to overwrite the size of the disk in
                      a virtual machine image. :code:`<br>`:code:`<br>` This value
                      cannot be larger than 1023 GB
                  returned: always
                  type: int
                  sample: null
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
                image:
                  description:
                    - >-
                      Specifies information about the unmanaged user image to base
                      the scale set on.
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
                      Specifies the container urls that are used to store operating
                      system disks for the scale set.
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
                          Specifies the storage account type for the managed disk.
                          NOTE: UltraSSD_LRS can only be used with data disks, it
                          cannot be used with OS Disk.
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
                  Specifies the parameters that are used to add data disks to the
                  virtual machines in the scale set. :code:`<br>`:code:`<br>` For
                  more information about disks, see `About disks and VHDs for Azure
                  virtual machines
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
                      Specifies the logical unit number of the data disk. This value
                      is used to identify data disks within the VM and therefore
                      must be unique for each data disk attached to a VM.
                  returned: always
                  type: int
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
                      Specifies the size of an empty data disk in gigabytes. This
                      element can be used to overwrite the size of the disk in a
                      virtual machine image. :code:`<br>`:code:`<br>` This value
                      cannot be larger than 1023 GB
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
                          Specifies the storage account type for the managed disk.
                          NOTE: UltraSSD_LRS can only be used with data disks, it
                          cannot be used with OS Disk.
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
                      Specifies the Read-Write IOPS for the managed disk. Should be
                      used only when StorageAccountType is UltraSSD_LRS. If not
                      specified, a default value would be assigned based on
                      diskSizeGB.
                  returned: always
                  type: int
                  sample: null
                disk_m_bps_read_write:
                  description:
                    - >-
                      Specifies the bandwidth in MB per second for the managed disk.
                      Should be used only when StorageAccountType is UltraSSD_LRS.
                      If not specified, a default value would be assigned based on
                      diskSizeGB.
                  returned: always
                  type: int
                  sample: null
        network_profile:
          description:
            - >-
              Specifies properties of the network interfaces of the virtual machines
              in the scale set.
          returned: always
          type: dict
          sample: null
          contains:
            health_probe:
              description:
                - >-
                  A reference to a load balancer probe used to determine the health
                  of an instance in the virtual machine scale set. The reference
                  will be in the form:
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
                      Specifies the primary network interface in case the virtual
                      machine has more than 1 network interface.
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
                          represents whether the specific ipconfiguration is IPv4 or
                          IPv6. Default is taken as IPv4.  Possible values are:
                          'IPv4' and 'IPv6'.
                      returned: always
                      type: str
                      sample: null
                    application_gateway_backend_address_pools:
                      description:
                        - >-
                          Specifies an array of references to backend address pools
                          of application gateways. A scale set can reference backend
                          address pools of multiple application gateways. Multiple
                          scale sets cannot use the same application gateway.
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
                          Specifies an array of references to application security
                          group.
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
                          Specifies an array of references to backend address pools
                          of load balancers. A scale set can reference backend
                          address pools of one public and one internal load
                          balancer. Multiple scale sets cannot use the same basic
                          sku load balancer.
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
                          Specifies an array of references to inbound Nat pools of
                          the load balancers. A scale set can reference inbound nat
                          pools of one public and one internal load balancer.
                          Multiple scale sets cannot use the same basic sku load
                          balancer.
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
                  :code:`<br>`:code:`<br>` Default: The Encryption at host will be
                  disabled unless this property is set to true for the resource.
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
                  console log. :code:`<br>`:code:`<br>` Azure also enables you to
                  see a screenshot of the VM from the hypervisor.
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
                      output and screenshot. :code:`<br>`:code:`<br>`If storageUri
                      is not specified while enabling boot diagnostics, managed
                      storage will be used.
                  returned: always
                  type: str
                  sample: null
        extension_profile:
          description:
            - >-
              Specifies a collection of settings for extensions installed on virtual
              machines in the scale set.
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
                      value, the extension handler will be forced to update even if
                      the extension configuration has not changed.
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
                      version if one is available at deployment time. Once deployed,
                      however, the extension will not upgrade minor versions unless
                      redeployed, even with this property set to true.
                  returned: always
                  type: bool
                  sample: null
                enable_automatic_upgrade:
                  description:
                    - >-
                      Indicates whether the extension should be automatically
                      upgraded by the platform if there is a newer version of the
                      extension available.
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
                provision_after_extensions:
                  description:
                    - >-
                      Collection of extension names after which this extension needs
                      to be provisioned.
                  returned: always
                  type: list
                  sample: null
            extensions_time_budget:
              description:
                - >-
                  Specifies the time alloted for all extensions to start. The time
                  duration should be between 15 minutes and 120 minutes (inclusive)
                  and should be specified in ISO 8601 format. The default value is
                  90 minutes (PT1H30M). :code:`<br>`:code:`<br>` Minimum
                  api-version: 2020-06-01
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
              :code:`<br>`:code:`<br>` Windows_Server :code:`<br>`:code:`<br>` If
              this element is included in a request for an update, the value must
              match the initial value. This value cannot be updated.
              :code:`<br>`:code:`<br>` For more information, see `Azure Hybrid Use
              Benefit for Windows Server
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
              Specifies the eviction policy for the Azure Spot virtual machine and
              Azure Spot scale set. :code:`<br>`:code:`<br>`For Azure Spot virtual
              machines, both 'Deallocate' and 'Delete' are supported and the minimum
              api-version is 2019-03-01. :code:`<br>`:code:`<br>`For Azure Spot
              scale sets, both 'Deallocate' and 'Delete' are supported and the
              minimum api-version is 2017-10-30-preview.
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
                  compared at the time of create/update of Azure Spot VM/VMSS and
                  the operation will only succeed if  the maxPrice is greater than
                  the current Azure Spot price. :code:`<br>`:code:`<br>` The
                  maxPrice will also be used for evicting a Azure Spot VM/VMSS if
                  the current Azure Spot price goes beyond the maxPrice after
                  creation of VM/VMSS. :code:`<br>`:code:`<br>` Possible values are:
                  :code:`<br>`:code:`<br>` - Any decimal value greater than zero.
                  Example: 0.01538 :code:`<br>`:code:`<br>` -1 – indicates default
                  price to be up-to on-demand. :code:`<br>`:code:`<br>` You can set
                  the maxPrice to -1 to indicate that the Azure Spot VM/VMSS should
                  not be evicted for price reasons. Also, the default max price is
                  -1 if it is not provided by you. :code:`<br>`:code:`<br>`Minimum
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
                - Specifies Terminate Scheduled Event related configurations.
              returned: always
              type: dict
              sample: null
              contains:
                not_before_timeout:
                  description:
                    - >-
                      Configurable length of time a Virtual Machine being deleted
                      will have to potentially approve the Terminate Scheduled Event
                      before the event is auto approved (timed out). The
                      configuration must be specified in ISO 8601 format, the
                      default value is 5 minutes (PT5M)
                  returned: always
                  type: str
                  sample: null
                enable:
                  description:
                    - >-
                      Specifies whether the Terminate Scheduled event is enabled or
                      disabled.
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
        - Specifies whether the Virtual Machine Scale Set should be overprovisioned.
      returned: always
      type: bool
      sample: null
    do_not_run_extensions_on_overprovisioned_v_ms:
      description:
        - >-
          When Overprovision is enabled, extensions are launched only on the
          requested number of VMs which are finally kept. This property will hence
          ensure that the extensions do not run on the extra overprovisioned VMs.
      returned: always
      type: bool
      sample: null
    unique_id:
      description:
        - Specifies the ID which uniquely identifies a Virtual Machine Scale Set.
      returned: always
      type: str
      sample: null
    single_placement_group:
      description:
        - >-
          When true this limits the scale set to a single placement group, of max
          size 100 virtual machines. NOTE: If singlePlacementGroup is true, it may
          be modified to false. However, if singlePlacementGroup is false, it may
          not be modified to true.
      returned: always
      type: bool
      sample: null
    zone_balance:
      description:
        - >-
          Whether to force strictly even Virtual Machine distribution cross x-zones
          in case there is zone outage.
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
          Specifies information about the proximity placement group that the virtual
          machine scale set should be assigned to. :code:`<br>`:code:`<br>`Minimum
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
    host_group:
      description:
        - >-
          Specifies information about the dedicated host group that the virtual
          machine scale set resides in. :code:`<br>`:code:`<br>`Minimum api-version:
          2020-06-01.
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
              managed data disks with UltraSSD_LRS storage account type on the VM or
              VMSS. Managed disks with storage account type UltraSSD_LRS can be
              added to a virtual machine or virtual machine scale set only if this
              property is enabled.
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
              The rules to be followed when scaling-in a virtual machine scale set.
              :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`:code:`<br>`
              **Default** When a virtual machine scale set is scaled in, the scale
              set will first be balanced across zones if it is a zonal scale set.
              Then, it will be balanced across Fault Domains as far as possible.
              Within each Fault Domain, the virtual machines chosen for removal will
              be the newest ones that are not protected from scale-in.
              :code:`<br>`:code:`<br>` **OldestVM** When a virtual machine scale set
              is being scaled-in, the oldest virtual machines that are not protected
              from scale-in will be chosen for removal. For zonal virtual machine
              scale sets, the scale set will first be balanced across zones. Within
              each zone, the oldest virtual machines that are not protected will be
              chosen for removal. :code:`<br>`:code:`<br>` **NewestVM** When a
              virtual machine scale set is being scaled-in, the newest virtual
              machines that are not protected from scale-in will be chosen for
              removal. For zonal virtual machine scale sets, the scale set will
              first be balanced across zones. Within each zone, the newest virtual
              machines that are not protected will be chosen for removal.
              :code:`<br>`:code:`<br>`
          returned: always
          type: list
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


class AzureRMVirtualMachineScaleSet(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            vm_scale_set_name=dict(
                type='str',
                required=True
            ),
            sku=dict(
                type='dict',
                disposition='/sku',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name'
                    ),
                    tier=dict(
                        type='str',
                        disposition='tier'
                    ),
                    capacity=dict(
                        type='int',
                        disposition='capacity'
                    )
                )
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
            upgrade_policy=dict(
                type='dict',
                disposition='/upgrade_policy',
                options=dict(
                    mode=dict(
                        type='sealed-choice',
                        disposition='mode'
                    ),
                    rolling_upgrade_policy=dict(
                        type='dict',
                        disposition='rolling_upgrade_policy',
                        options=dict(
                            max_batch_instance_percent=dict(
                                type='int',
                                disposition='max_batch_instance_percent'
                            ),
                            max_unhealthy_instance_percent=dict(
                                type='int',
                                disposition='max_unhealthy_instance_percent'
                            ),
                            max_unhealthy_upgraded_instance_percent=dict(
                                type='int',
                                disposition='max_unhealthy_upgraded_instance_percent'
                            ),
                            pause_time_between_batches=dict(
                                type='str',
                                disposition='pause_time_between_batches'
                            )
                        )
                    ),
                    automatic_os_upgrade_policy=dict(
                        type='dict',
                        disposition='automatic_os_upgrade_policy',
                        options=dict(
                            enable_automatic_os_upgrade=dict(
                                type='bool',
                                disposition='enable_automatic_os_upgrade'
                            ),
                            disable_automatic_rollback=dict(
                                type='bool',
                                disposition='disable_automatic_rollback'
                            )
                        )
                    )
                )
            ),
            automatic_repairs_policy=dict(
                type='dict',
                disposition='/automatic_repairs_policy',
                options=dict(
                    enabled=dict(
                        type='bool',
                        disposition='enabled'
                    ),
                    grace_period=dict(
                        type='str',
                        disposition='grace_period'
                    )
                )
            ),
            virtual_machine_profile=dict(
                type='dict',
                disposition='/virtual_machine_profile',
                options=dict(
                    os_profile=dict(
                        type='dict',
                        disposition='os_profile',
                        options=dict(
                            computer_name_prefix=dict(
                                type='str',
                                disposition='computer_name_prefix'
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
                            )
                        )
                    ),
                    storage_profile=dict(
                        type='dict',
                        disposition='storage_profile',
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
                                    name=dict(
                                        type='str',
                                        disposition='name'
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
                                    disk_size_gb=dict(
                                        type='int',
                                        disposition='disk_size_gb'
                                    ),
                                    os_type=dict(
                                        type='sealed-choice',
                                        disposition='os_type'
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
                                    vhd_containers=dict(
                                        type='list',
                                        disposition='vhd_containers',
                                        elements='str'
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
                                    name=dict(
                                        type='str',
                                        disposition='name'
                                    ),
                                    lun=dict(
                                        type='int',
                                        disposition='lun',
                                        required=True
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
                                    disk_iops_read_write=dict(
                                        type='int',
                                        disposition='disk_iops_read_write'
                                    ),
                                    disk_m_bps_read_write=dict(
                                        type='int',
                                        disposition='disk_m_bps_read_write'
                                    )
                                )
                            )
                        )
                    ),
                    network_profile=dict(
                        type='dict',
                        disposition='network_profile',
                        options=dict(
                            health_probe=dict(
                                type='dict',
                                disposition='health_probe',
                                options=dict(
                                    id=dict(
                                        type='str',
                                        disposition='id'
                                    )
                                )
                            ),
                            network_interface_configurations=dict(
                                type='list',
                                disposition='network_interface_configurations',
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name',
                                        required=True
                                    ),
                                    primary=dict(
                                        type='bool',
                                        disposition='primary'
                                    ),
                                    enable_accelerated_networking=dict(
                                        type='bool',
                                        disposition='enable_accelerated_networking'
                                    ),
                                    network_security_group=dict(
                                        type='dict',
                                        disposition='network_security_group',
                                        options=dict(
                                            id=dict(
                                                type='str',
                                                disposition='id'
                                            )
                                        )
                                    ),
                                    dns_settings=dict(
                                        type='dict',
                                        disposition='dns_settings',
                                        options=dict(
                                            dns_servers=dict(
                                                type='list',
                                                disposition='dns_servers',
                                                elements='str'
                                            )
                                        )
                                    ),
                                    ip_configurations=dict(
                                        type='list',
                                        disposition='ip_configurations',
                                        elements='dict',
                                        options=dict(
                                            name=dict(
                                                type='str',
                                                disposition='name',
                                                required=True
                                            ),
                                            subnet=dict(
                                                type='dict',
                                                disposition='subnet',
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            ),
                                            primary=dict(
                                                type='bool',
                                                disposition='primary'
                                            ),
                                            public_ip_address_configuration=dict(
                                                type='dict',
                                                disposition='public_ip_address_configuration',
                                                options=dict(
                                                    name=dict(
                                                        type='str',
                                                        disposition='name',
                                                        required=True
                                                    ),
                                                    idle_timeout_in_minutes=dict(
                                                        type='int',
                                                        disposition='idle_timeout_in_minutes'
                                                    ),
                                                    dns_settings=dict(
                                                        type='dict',
                                                        disposition='dns_settings',
                                                        options=dict(
                                                            domain_name_label=dict(
                                                                type='str',
                                                                disposition='domain_name_label',
                                                                required=True
                                                            )
                                                        )
                                                    ),
                                                    ip_tags=dict(
                                                        type='list',
                                                        disposition='ip_tags',
                                                        elements='dict',
                                                        options=dict(
                                                            ip_tag_type=dict(
                                                                type='str',
                                                                disposition='ip_tag_type'
                                                            ),
                                                            tag=dict(
                                                                type='str',
                                                                disposition='tag'
                                                            )
                                                        )
                                                    ),
                                                    public_ip_prefix=dict(
                                                        type='dict',
                                                        disposition='public_ip_prefix',
                                                        options=dict(
                                                            id=dict(
                                                                type='str',
                                                                disposition='id'
                                                            )
                                                        )
                                                    ),
                                                    public_ip_address_version=dict(
                                                        type='str',
                                                        disposition='public_ip_address_version',
                                                        choices=['IPv4',
                                                                 'IPv6']
                                                    )
                                                )
                                            ),
                                            private_ip_address_version=dict(
                                                type='str',
                                                disposition='private_ip_address_version',
                                                choices=['IPv4',
                                                         'IPv6']
                                            ),
                                            application_gateway_backend_address_pools=dict(
                                                type='list',
                                                disposition='application_gateway_backend_address_pools',
                                                elements='dict',
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            ),
                                            application_security_groups=dict(
                                                type='list',
                                                disposition='application_security_groups',
                                                elements='dict',
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            ),
                                            load_balancer_backend_address_pools=dict(
                                                type='list',
                                                disposition='load_balancer_backend_address_pools',
                                                elements='dict',
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            ),
                                            load_balancer_inbound_nat_pools=dict(
                                                type='list',
                                                disposition='load_balancer_inbound_nat_pools',
                                                elements='dict',
                                                options=dict(
                                                    id=dict(
                                                        type='str',
                                                        disposition='id'
                                                    )
                                                )
                                            )
                                        )
                                    ),
                                    enable_ip_forwarding=dict(
                                        type='bool',
                                        disposition='enable_ip_forwarding'
                                    )
                                )
                            )
                        )
                    ),
                    security_profile=dict(
                        type='dict',
                        disposition='security_profile',
                        options=dict(
                            encryption_at_host=dict(
                                type='bool',
                                disposition='encryption_at_host'
                            )
                        )
                    ),
                    diagnostics_profile=dict(
                        type='dict',
                        disposition='diagnostics_profile',
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
                    extension_profile=dict(
                        type='dict',
                        disposition='extension_profile',
                        options=dict(
                            extensions=dict(
                                type='list',
                                disposition='extensions',
                                elements='dict',
                                options=dict(
                                    name=dict(
                                        type='str',
                                        disposition='name'
                                    ),
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
                                    provision_after_extensions=dict(
                                        type='list',
                                        disposition='provision_after_extensions',
                                        elements='str'
                                    )
                                )
                            ),
                            extensions_time_budget=dict(
                                type='str',
                                disposition='extensions_time_budget'
                            )
                        )
                    ),
                    license_type=dict(
                        type='str',
                        disposition='license_type'
                    ),
                    priority=dict(
                        type='str',
                        disposition='priority',
                        choices=['Regular',
                                 'Low',
                                 'Spot']
                    ),
                    eviction_policy=dict(
                        type='str',
                        disposition='eviction_policy',
                        choices=['Deallocate',
                                 'Delete']
                    ),
                    billing_profile=dict(
                        type='dict',
                        disposition='billing_profile',
                        options=dict(
                            max_price=dict(
                                type='number',
                                disposition='max_price'
                            )
                        )
                    ),
                    scheduled_events_profile=dict(
                        type='dict',
                        disposition='scheduled_events_profile',
                        options=dict(
                            terminate_notification_profile=dict(
                                type='dict',
                                disposition='terminate_notification_profile',
                                options=dict(
                                    not_before_timeout=dict(
                                        type='str',
                                        disposition='not_before_timeout'
                                    ),
                                    enable=dict(
                                        type='bool',
                                        disposition='enable'
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            overprovision=dict(
                type='bool',
                disposition='/overprovision'
            ),
            do_not_run_extensions_on_overprovisioned_v_ms=dict(
                type='bool',
                disposition='/do_not_run_extensions_on_overprovisioned_v_ms'
            ),
            single_placement_group=dict(
                type='bool',
                disposition='/single_placement_group'
            ),
            zone_balance=dict(
                type='bool',
                disposition='/zone_balance'
            ),
            platform_fault_domain_count=dict(
                type='int',
                disposition='/platform_fault_domain_count'
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
            scale_in_policy=dict(
                type='dict',
                disposition='/scale_in_policy',
                options=dict(
                    rules=dict(
                        type='list',
                        disposition='rules',
                        elements='str'
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
        self.vm_scale_set_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMVirtualMachineScaleSet, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            response = self.mgmt_client.virtual_machine_scale_sets.create_or_update(resource_group=self.resource_group,
                                                                                    vm_scale_set_name=self.vm_scale_set_name,
                                                                                    parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the VirtualMachineScaleSet instance.')
            self.fail('Error creating the VirtualMachineScaleSet instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_scale_sets.delete(resource_group=self.resource_group,
                                                                          vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            self.log('Error attempting to delete the VirtualMachineScaleSet instance.')
            self.fail('Error deleting the VirtualMachineScaleSet instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.virtual_machine_scale_sets.get(resource_group=self.resource_group,
                                                                       vm_scale_set_name=self.vm_scale_set_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMVirtualMachineScaleSet()


if __name__ == '__main__':
    main()
