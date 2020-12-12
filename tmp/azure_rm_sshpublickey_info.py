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
module: azure_rm_sshpublickey_info
version_added: '2.9'
short_description: Get SshPublicKey info.
description:
    - Get info of SshPublicKey.
options:
    resource_group:
        description:
            - The name of the resource group.
        type: str
    ssh_public_key_name:
        description:
            - The name of the SSH public key.
        type: str
extends_documentation_fragment:
    - azure.azcollection.azure
    - azure.azcollection.azure_tags
author:
    - GuopengLin (@t-glin)

'''

EXAMPLES = '''
    - name: Get an ssh public key.
      azure_rm_sshpublickey_info: 
        resource_group_name: myResourceGroup
        ssh_public_key_name: mySshPublicKeyName
        

'''

RETURN = '''
ssh_public_keys:
    description: >-
        A list of dict results where the key is the name of the SshPublicKey and the
        values are the facts for that SshPublicKey.
    returned: always
    type: complex
    contains:
        value:
            description:
                - The list of SSH public keys
            returned: always
            type: list
            sample: null
            contains:
                public_key:
                    description:
                        - >-
                            SSH public key used to authenticate to a virtual machine through
                            ssh. If this property is not initially provided when the resource
                            is created, the publicKey property will be populated when
                            generateKeyPair is called. If the public key is provided upon
                            resource creation, the provided public key needs to be at least
                            2048-bit and in ssh-rsa format.
                    returned: always
                    type: str
                    sample: null
        next_link:
            description:
                - >-
                    The URI to fetch the next page of SSH public keys. Call ListNext()
                    with this URI to fetch the next page of SSH public keys.
            returned: always
            type: str
            sample: null
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
        public_key:
            description:
                - >-
                    SSH public key used to authenticate to a virtual machine through ssh.
                    If this property is not initially provided when the resource is
                    created, the publicKey property will be populated when generateKeyPair
                    is called. If the public key is provided upon resource creation, the
                    provided public key needs to be at least 2048-bit and in ssh-rsa
                    format.
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


class AzureRMSshPublicKeyInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            ssh_public_key_name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.ssh_public_key_name = None

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
        super(AzureRMSshPublicKeyInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-06-01')

        if (self.resource_group is not None and
            self.ssh_public_key_name is not None):
            self.results['ssh_public_keys'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['ssh_public_keys'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['ssh_public_keys'] = self.format_item(self.list_by_subscription())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.ssh_public_keys.get(resource_group=self.resource_group,
                                                            ssh_public_key_name=self.ssh_public_key_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.ssh_public_keys.list_by_resource_group(resource_group=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_subscription(self):
        response = None

        try:
            response = self.mgmt_client.ssh_public_keys.list_by_subscription()
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
    AzureRMSshPublicKeyInfo()


if __name__ == '__main__':
    main()
