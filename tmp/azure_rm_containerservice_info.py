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
    module: azure_rm_containerservice_info
    version_added: '2.9'
    short_description: Get ContainerService info.
    description:
      - Get info of ContainerService.
    options:
      resource_group:
        description:
          - The name of the resource group.
        type: str
      container_service_name:
        description:
          - >-
            The name of the container service in the specified subscription and
            resource group.
        type: str
    extends_documentation_fragment:
      - azure.azcollection.azure
      - azure.azcollection.azure_tags
    author:
      - GuopengLin (@t-glin)
    
'''

EXAMPLES = '''
    - name: List Container Services
      azure_rm_containerservice_info: 

    - name: Get Container Service
      azure_rm_containerservice_info: 
        container_service_name: acs1
        resource_group_name: rg1
        

    - name: List Container Services by Resource Group
      azure_rm_containerservice_info: 
        resource_group_name: rg1
        

'''

RETURN = '''
    container_services:
      description: >-
        A list of dict results where the key is the name of the ContainerService and
        the values are the facts for that ContainerService.
      returned: always
      type: complex
      contains:
        value:
          description:
            - the list of container services.
          returned: always
          type: list
          sample: null
          contains:
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
                      The orchestrator to use to manage container service cluster
                      resources. Valid values are Swarm, DCOS, and Custom.
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
                      Number of masters (VMs) in the container service cluster.
                      Allowed values are 1, 3, and 5. The default value is 1.
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
                      Number of agents (VMs) to host docker containers. Allowed
                      values must be in the range of 1 to 100 (inclusive). The
                      default value is 1.
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
                          the list of SSH public keys used to authenticate with
                          Linux-based VMs.
                      returned: always
                      type: list
                      sample: null
                      contains:
                        key_data:
                          description:
                            - >-
                              Certificate public key used to authenticate with VMs
                              through SSH. The certificate must be in PEM format
                              with or without headers.
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
        next_link:
          description:
            - The URL to get the next set of container service results.
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
        provisioning_state:
          description:
            - >-
              the current deployment or provisioning state, which only appears in
              the response.
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
                  The orchestrator to use to manage container service cluster
                  resources. Valid values are Swarm, DCOS, and Custom.
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
                  Number of agents (VMs) to host docker containers. Allowed values
                  must be in the range of 1 to 100 (inclusive). The default value is
                  1.
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
                      the list of SSH public keys used to authenticate with
                      Linux-based VMs.
                  returned: always
                  type: list
                  sample: null
                  contains:
                    key_data:
                      description:
                        - >-
                          Certificate public key used to authenticate with VMs
                          through SSH. The certificate must be in PEM format with or
                          without headers.
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

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBase
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.compute import ComputeManagementClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureRMContainerServiceInfo(AzureRMModuleBase):
    def __init__(self):
        self.module_arg_spec = dict(
            resource_group=dict(
                type='str'
            ),
            container_service_name=dict(
                type='str'
            )
        )

        self.resource_group = None
        self.container_service_name = None

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.url = None
        self.status_code = [200]

        self.query_parameters = {}
        self.query_parameters['api-version'] = '2017-01-31'
        self.header_parameters = {}
        self.header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        self.mgmt_client = None
        super(AzureRMContainerServiceInfo, self).__init__(self.module_arg_spec, supports_tags=True)

    def exec_module(self, **kwargs):

        for key in self.module_arg_spec:
            setattr(self, key, kwargs[key])

        self.mgmt_client = self.get_mgmt_svc_client(ComputeManagementClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2017-01-31')

        if (self.resource_group is not None and
            self.container_service_name is not None):
            self.results['container_services'] = self.format_item(self.get())
        elif (self.resource_group is not None):
            self.results['container_services'] = self.format_item(self.list_by_resource_group())
        else:
            self.results['container_services'] = self.format_item(self.list())
        return self.results

    def get(self):
        response = None

        try:
            response = self.mgmt_client.container_services.get(resource_group=self.resource_group,
                                                               container_service_name=self.container_service_name)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list_by_resource_group(self):
        response = None

        try:
            response = self.mgmt_client.container_services.list_by_resource_group(resource_group=self.resource_group)
        except CloudError as e:
            self.log('Could not get info for @(Model.ModuleOperationNameUpper).')

        return response

    def list(self):
        response = None

        try:
            response = self.mgmt_client.container_services.list()
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
    AzureRMContainerServiceInfo()


if __name__ == '__main__':
    main()
