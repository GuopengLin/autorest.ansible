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
    module: azure_rm_containerservice
    version_added: '2.9'
    short_description: Manage Azure ContainerService instance.
    description:
      - 'Create, update and delete instance of Azure ContainerService.'
    options:
      resource_group:
        description:
          - The name of the resource group.
        required: true
        type: str
      container_service_name:
        description:
          - >-
            The name of the container service in the specified subscription and
            resource group.
        required: true
        type: str
      orchestrator_profile:
        description:
          - Properties of the orchestrator.
        type: dict
        suboptions:
          orchestrator_type:
            description:
              - >-
                The orchestrator to use to manage container service cluster
                resources. Valid values are Swarm, DCOS, and Custom.
            required: true
            type: sealed-choice
      custom_profile:
        description:
          - Properties for custom clusters.
        type: dict
        suboptions:
          orchestrator:
            description:
              - The name of the custom orchestrator to use.
            required: true
            type: str
      service_principal_profile:
        description:
          - Properties for cluster service principals.
        type: dict
        suboptions:
          client_id:
            description:
              - The ID for the service principal.
            required: true
            type: str
          secret:
            description:
              - The secret password associated with the service principal.
            required: true
            type: str
      master_profile:
        description:
          - Properties of master agents.
        type: dict
        suboptions:
          count:
            description:
              - >-
                Number of masters (VMs) in the container service cluster. Allowed
                values are 1, 3, and 5. The default value is 1.
            type: str
            choices:
              - 1
              - 3
              - 5
          dns_prefix:
            description:
              - DNS prefix to be used to create the FQDN for master.
            required: true
            type: str
      agent_pool_profiles:
        description:
          - Properties of the agent pool.
        type: list
        suboptions:
          name:
            description:
              - >-
                Unique name of the agent pool profile in the context of the
                subscription and resource group.
            required: true
            type: str
          count:
            description:
              - >-
                Number of agents (VMs) to host docker containers. Allowed values
                must be in the range of 1 to 100 (inclusive). The default value is
                1.
            required: true
            type: int
          vm_size:
            description:
              - Size of agent VMs.
            required: true
            type: str
            choices:
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
              - Standard_D11_v2
              - Standard_D12_v2
              - Standard_D13_v2
              - Standard_D14_v2
              - Standard_G1
              - Standard_G2
              - Standard_G3
              - Standard_G4
              - Standard_G5
              - Standard_DS1
              - Standard_DS2
              - Standard_DS3
              - Standard_DS4
              - Standard_DS11
              - Standard_DS12
              - Standard_DS13
              - Standard_DS14
              - Standard_GS1
              - Standard_GS2
              - Standard_GS3
              - Standard_GS4
              - Standard_GS5
          dns_prefix:
            description:
              - DNS prefix to be used to create the FQDN for the agent pool.
            required: true
            type: str
      windows_profile:
        description:
          - Properties of Windows VMs.
        type: dict
        suboptions:
          admin_username:
            description:
              - The administrator username to use for Windows VMs.
            required: true
            type: str
          admin_password:
            description:
              - The administrator password to use for Windows VMs.
            required: true
            type: str
      linux_profile:
        description:
          - Properties of Linux VMs.
        type: dict
        suboptions:
          admin_username:
            description:
              - The administrator username to use for Linux VMs.
            required: true
            type: str
          ssh:
            description:
              - The ssh key configuration for Linux VMs.
            required: true
            type: dict
            suboptions:
              public_keys:
                description:
                  - >-
                    the list of SSH public keys used to authenticate with
                    Linux-based VMs.
                required: true
                type: list
                suboptions:
                  key_data:
                    description:
                      - >-
                        Certificate public key used to authenticate with VMs through
                        SSH. The certificate must be in PEM format with or without
                        headers.
                    required: true
                    type: str
      diagnostics_profile:
        description:
          - Properties of the diagnostic agent.
        type: dict
        suboptions:
          vm_diagnostics:
            description:
              - Profile for the container service VM diagnostic agent.
            required: true
            type: dict
            suboptions:
              enabled:
                description:
                  - Whether the VM diagnostic agent is provisioned on the VM.
                required: true
                type: bool
      state:
        description:
          - Assert the state of the ContainerService.
          - >-
            Use C(present) to create or update an ContainerService and C(absent) to
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
    - name: Create/Update Container Service
      azure_rm_containerservice: 
        container_service_name: acs1
        resource_group_name: rg1
        location: location1
        

    - name: Delete Container Service
      azure_rm_containerservice: 
        container_service_name: acs1
        resource_group_name: rg1
        

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
    provisioning_state:
      description:
        - >-
          the current deployment or provisioning state, which only appears in the
          response.
      returned: always
      type: str
      sample: null
    orchestrator_profile:
      description:
        - Properties of the orchestrator.
      returned: always
      type: dict
      sample: null
      contains:
        orchestrator_type:
          description:
            - >-
              The orchestrator to use to manage container service cluster resources.
              Valid values are Swarm, DCOS, and Custom.
          returned: always
          type: sealed-choice
          sample: null
    custom_profile:
      description:
        - Properties for custom clusters.
      returned: always
      type: dict
      sample: null
      contains:
        orchestrator:
          description:
            - The name of the custom orchestrator to use.
          returned: always
          type: str
          sample: null
    service_principal_profile:
      description:
        - Properties for cluster service principals.
      returned: always
      type: dict
      sample: null
      contains:
        client_id:
          description:
            - The ID for the service principal.
          returned: always
          type: str
          sample: null
        secret:
          description:
            - The secret password associated with the service principal.
          returned: always
          type: str
          sample: null
    master_profile:
      description:
        - Properties of master agents.
      returned: always
      type: dict
      sample: null
      contains:
        count:
          description:
            - >-
              Number of masters (VMs) in the container service cluster. Allowed
              values are 1, 3, and 5. The default value is 1.
          returned: always
          type: str
          sample: null
        dns_prefix:
          description:
            - DNS prefix to be used to create the FQDN for master.
          returned: always
          type: str
          sample: null
    agent_pool_profiles:
      description:
        - Properties of the agent pool.
      returned: always
      type: list
      sample: null
      contains:
        name:
          description:
            - >-
              Unique name of the agent pool profile in the context of the
              subscription and resource group.
          returned: always
          type: str
          sample: null
        count:
          description:
            - >-
              Number of agents (VMs) to host docker containers. Allowed values must
              be in the range of 1 to 100 (inclusive). The default value is 1.
          returned: always
          type: int
          sample: null
        vm_size:
          description:
            - Size of agent VMs.
          returned: always
          type: str
          sample: null
        dns_prefix:
          description:
            - DNS prefix to be used to create the FQDN for the agent pool.
          returned: always
          type: str
          sample: null
    windows_profile:
      description:
        - Properties of Windows VMs.
      returned: always
      type: dict
      sample: null
      contains:
        admin_username:
          description:
            - The administrator username to use for Windows VMs.
          returned: always
          type: str
          sample: null
        admin_password:
          description:
            - The administrator password to use for Windows VMs.
          returned: always
          type: str
          sample: null
    linux_profile:
      description:
        - Properties of Linux VMs.
      returned: always
      type: dict
      sample: null
      contains:
        admin_username:
          description:
            - The administrator username to use for Linux VMs.
          returned: always
          type: str
          sample: null
        ssh:
          description:
            - The ssh key configuration for Linux VMs.
          returned: always
          type: dict
          sample: null
          contains:
            public_keys:
              description:
                - >-
                  the list of SSH public keys used to authenticate with Linux-based
                  VMs.
              returned: always
              type: list
              sample: null
              contains:
                key_data:
                  description:
                    - >-
                      Certificate public key used to authenticate with VMs through
                      SSH. The certificate must be in PEM format with or without
                      headers.
                  returned: always
                  type: str
                  sample: null
    diagnostics_profile:
      description:
        - Properties of the diagnostic agent.
      returned: always
      type: dict
      sample: null
      contains:
        vm_diagnostics:
          description:
            - Profile for the container service VM diagnostic agent.
          returned: always
          type: dict
          sample: null
          contains:
            enabled:
              description:
                - Whether the VM diagnostic agent is provisioned on the VM.
              returned: always
              type: bool
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


class AzureRMContainerService(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str',
                required=True
            ),
            container_service_name=dict(
                type='str',
                required=True
            ),
            orchestrator_profile=dict(
                type='dict',
                disposition='/orchestrator_profile',
                options=dict(
                    orchestrator_type=dict(
                        type='sealed-choice',
                        disposition='orchestrator_type',
                        required=True
                    )
                )
            ),
            custom_profile=dict(
                type='dict',
                disposition='/custom_profile',
                options=dict(
                    orchestrator=dict(
                        type='str',
                        disposition='orchestrator',
                        required=True
                    )
                )
            ),
            service_principal_profile=dict(
                type='dict',
                disposition='/service_principal_profile',
                options=dict(
                    client_id=dict(
                        type='str',
                        disposition='client_id',
                        required=True
                    ),
                    secret=dict(
                        type='str',
                        disposition='secret',
                        required=True
                    )
                )
            ),
            master_profile=dict(
                type='dict',
                disposition='/master_profile',
                options=dict(
                    count=dict(
                        type='str',
                        disposition='count',
                        choices=['1',
                                 '3',
                                 '5']
                    ),
                    dns_prefix=dict(
                        type='str',
                        disposition='dns_prefix',
                        required=True
                    )
                )
            ),
            agent_pool_profiles=dict(
                type='list',
                disposition='/agent_pool_profiles',
                elements='dict',
                options=dict(
                    name=dict(
                        type='str',
                        disposition='name',
                        required=True
                    ),
                    count=dict(
                        type='int',
                        disposition='count',
                        required=True
                    ),
                    vm_size=dict(
                        type='str',
                        disposition='vm_size',
                        choices=['Standard_A0',
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
                                 'Standard_D11_v2',
                                 'Standard_D12_v2',
                                 'Standard_D13_v2',
                                 'Standard_D14_v2',
                                 'Standard_G1',
                                 'Standard_G2',
                                 'Standard_G3',
                                 'Standard_G4',
                                 'Standard_G5',
                                 'Standard_DS1',
                                 'Standard_DS2',
                                 'Standard_DS3',
                                 'Standard_DS4',
                                 'Standard_DS11',
                                 'Standard_DS12',
                                 'Standard_DS13',
                                 'Standard_DS14',
                                 'Standard_GS1',
                                 'Standard_GS2',
                                 'Standard_GS3',
                                 'Standard_GS4',
                                 'Standard_GS5'],
                        required=True
                    ),
                    dns_prefix=dict(
                        type='str',
                        disposition='dns_prefix',
                        required=True
                    )
                )
            ),
            windows_profile=dict(
                type='dict',
                disposition='/windows_profile',
                options=dict(
                    admin_username=dict(
                        type='str',
                        disposition='admin_username',
                        required=True
                    ),
                    admin_password=dict(
                        type='str',
                        disposition='admin_password',
                        required=True
                    )
                )
            ),
            linux_profile=dict(
                type='dict',
                disposition='/linux_profile',
                options=dict(
                    admin_username=dict(
                        type='str',
                        disposition='admin_username',
                        required=True
                    ),
                    ssh=dict(
                        type='dict',
                        disposition='ssh',
                        required=True,
                        options=dict(
                            public_keys=dict(
                                type='list',
                                disposition='public_keys',
                                required=True,
                                elements='dict',
                                options=dict(
                                    key_data=dict(
                                        type='str',
                                        disposition='key_data',
                                        required=True
                                    )
                                )
                            )
                        )
                    )
                )
            ),
            diagnostics_profile=dict(
                type='dict',
                disposition='/diagnostics_profile',
                options=dict(
                    vm_diagnostics=dict(
                        type='dict',
                        disposition='vm_diagnostics',
                        required=True,
                        options=dict(
                            enabled=dict(
                                type='bool',
                                disposition='enabled',
                                required=True
                            )
                        )
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
        self.container_service_name = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMContainerService, self).__init__(derived_arg_spec=self.module_arg_spec,
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
                                                    api_version='2017-01-31')

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
            response = self.mgmt_client.container_services.create_or_update(resource_group=self.resource_group,
                                                                            container_service_name=self.container_service_name,
                                                                            parameters=self.body)
            if isinstance(response, AzureOperationPoller) or isinstance(response, LROPoller):
                response = self.get_poller_result(response)
        except CloudError as exc:
            self.log('Error attempting to create the ContainerService instance.')
            self.fail('Error creating the ContainerService instance: {0}'.format(str(exc)))
        return response.as_dict()

    def delete_resource(self):
        try:
            response = self.mgmt_client.container_services.delete(resource_group=self.resource_group,
                                                                  container_service_name=self.container_service_name)
        except CloudError as e:
            self.log('Error attempting to delete the ContainerService instance.')
            self.fail('Error deleting the ContainerService instance: {0}'.format(str(e)))

        return True

    def get_resource(self):
        try:
            response = self.mgmt_client.container_services.get(resource_group=self.resource_group,
                                                               container_service_name=self.container_service_name)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMContainerService()


if __name__ == '__main__':
    main()
