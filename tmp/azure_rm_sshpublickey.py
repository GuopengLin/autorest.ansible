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
    module: azure_rm_sshpublickey
    version_added: '2.9'
    short_description: Manage Azure SshPublicKey instance.
    description:
      - 'Create, update and delete instance of Azure SshPublicKey.'
    options:
      resource_group:
        description:
          - The name of the resource group.
        required: true
        type: str
      ssh_public_key_name:
        description:
          - The name of the SSH public key.
        required: true
        type: str
      public_key:
        description:
          - >-
            SSH public key used to authenticate to a virtual machine through ssh. If
            this property is not initially provided when the resource is created,
            the publicKey property will be populated when generateKeyPair is called.
            If the public key is provided upon resource creation, the provided
            public key needs to be at least 2048-bit and in ssh-rsa format.
        type: str
      state:
        description:
          - Assert the state of the SshPublicKey.
          - >-
            Use C(present) to create or update an SshPublicKey and C(absent) to
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
    - name: Create a new SSH public key resource.
      azure_rm_sshpublickey: 
        resource_group_name: myResourceGroup
        ssh_public_key_name: mySshPublicKeyName
        location: westus
        properties:
          public_key: '{ssh-rsa public key}'
        

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
    public_key:
      description:
        - >-
          SSH public key used to authenticate to a virtual machine through ssh. If
          this property is not initially provided when the resource is created, the
          publicKey property will be populated when generateKeyPair is called. If
          the public key is provided upon resource creation, the provided public key
          needs to be at least 2048-bit and in ssh-rsa format.
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


class AzureRMSshPublicKey(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            ssh_public_key_name=dict(
                type='str',
                required=True
            ),
            public_key=dict(
                type='str',
                disposition='/public_key'
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.resource_group = None
        self.ssh_public_key_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMSshPublicKey, self).__init__(derived_arg_spec=self.module_arg_spec,
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
            if self.to_do == Actions.Create:
                response = self.mgmt_client.ssh_public_keys.create(resource_group=self.resource_group,
                                                                   ssh_public_key_name=self.ssh_public_key_name,
                                                                   parameters=self.body)
            else:
                response = self.mgmt_client.ssh_public_keys.update(resource_group=self.resource_group,
                                                                   ssh_public_key_name=self.ssh_public_key_name,
                                                                   parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the SshPublicKey instance.')
            self.fail('Error creating the SshPublicKey instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.ssh_public_keys.delete(resource_group=self.resource_group,
                                                               ssh_public_key_name=self.ssh_public_key_name)
        except CloudError as e:
            self.log('Error attempting to delete the SshPublicKey instance.')
            self.fail('Error deleting the SshPublicKey instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.ssh_public_keys.get(resource_group=self.resource_group,
                                                            ssh_public_key_name=self.ssh_public_key_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMSshPublicKey()


if __name__ == '__main__':
    main()
