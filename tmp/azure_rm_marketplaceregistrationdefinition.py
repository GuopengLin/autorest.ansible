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
module: azure_rm_marketplaceregistrationdefinition
version_added: '2.9'
short_description: Manage Azure MarketplaceRegistrationDefinition instance.
description:
    - >-
        Create, update and delete instance of Azure
        MarketplaceRegistrationDefinition.
options:
    scope:
        description:
            - Scope of the resource.
        required: true
        type: str
    marketplace_identifier:
        description:
            - >-
                Market place identifer. Expected Formats -
                {publisher}.{product[-preview]}.{planName}.{version} or
                {publisher}.{product[-preview]}.{planName} or
                {publisher}.{product[-preview]} or {publisher}).
        required: true
        type: str
    state:
        description:
            - Assert the state of the MarketplaceRegistrationDefinition.
            - >-
                Use C(present) to create or update an MarketplaceRegistrationDefinition
                and C(absent) to delete it.
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
'''

RETURN = '''
properties:
    description:
        - Properties of a marketplace registration definition.
    returned: always
    type: dict
    sample: null
    contains:
        managed_by_tenant_id:
            description:
                - Id of the managedBy tenant.
            returned: always
            type: str
            sample: null
        authorizations:
            description:
                - >-
                    Authorization tuple containing principal id of the user/security group
                    or service principal and id of the build-in role.
            returned: always
            type: list
            sample: null
            contains:
                principal_id:
                    description:
                        - >-
                            Principal Id of the security group/service principal/user that
                            would be assigned permissions to the projected subscription
                    returned: always
                    type: str
                    sample: null
                principal_id_display_name:
                    description:
                        - Display name of the principal Id.
                    returned: always
                    type: str
                    sample: null
                role_definition_id:
                    description:
                        - >-
                            The role definition identifier. This role will define all the
                            permissions that the security group/service principal/user must
                            have on the projected subscription. This role cannot be an owner
                            role.
                    returned: always
                    type: str
                    sample: null
                delegated_role_definition_ids:
                    description:
                        - >-
                            The delegatedRoleDefinitionIds field is required when the
                            roleDefinitionId refers to the User Access Administrator Role. It
                            is the list of role definition ids which define all the
                            permissions that the user in the authorization can assign to other
                            security groups/service principals/users.
                    returned: always
                    type: list
                    sample: null
        eligible_authorizations:
            description:
                - >-
                    Eligible PIM authorization tuple containing principal id of the
                    user/security group or service principal, id of the built-in role, and
                    just-in-time access policy setting
            returned: always
            type: list
            sample: null
            contains:
                principal_id:
                    description:
                        - >-
                            Principal Id of the security group/service principal/user that
                            would be delegated permissions to the projected subscription
                    returned: always
                    type: str
                    sample: null
                principal_id_display_name:
                    description:
                        - Display name of the principal Id.
                    returned: always
                    type: str
                    sample: null
                role_definition_id:
                    description:
                        - >-
                            The role definition identifier. This role will delegate all the
                            permissions that the security group/service principal/user must
                            have on the projected subscription. This role cannot be an owner
                            role.
                    returned: always
                    type: str
                    sample: null
                just_in_time_access_policy:
                    description:
                        - Just-in-time access policy setting.
                    returned: always
                    type: dict
                    sample: null
                    contains:
                        multi_factor_auth_provider:
                            description:
                                - MFA provider.
                            returned: always
                            type: str
                            sample: null
                        maximum_activation_duration:
                            description:
                                - >-
                                    Maximum access duration in ISO 8601 format.  The default value
                                    is "PT8H".
                            returned: always
                            type: str
                            sample: null
        offer_display_name:
            description:
                - The marketplace offer display name.
            returned: always
            type: str
            sample: null
        publisher_display_name:
            description:
                - The marketplace publisher display name.
            returned: always
            type: str
            sample: null
        plan_display_name:
            description:
                - The marketplace plan display name.
            returned: always
            type: str
            sample: null
plan:
    description:
        - Plan details for the managed services.
    returned: always
    type: dict
    sample: null
    contains:
        name:
            description:
                - The plan name.
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
                - The product code.
            returned: always
            type: str
            sample: null
        version:
            description:
                - The plan's version.
            returned: always
            type: str
            sample: null
id:
    description:
        - Fully qualified path of the marketplace registration definition.
    returned: always
    type: str
    sample: null
type:
    description:
        - Type of the resource.
    returned: always
    type: str
    sample: null
name:
    description:
        - Name of the marketplace registration definition.
    returned: always
    type: str
    sample: null

'''

from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common_ext import AzureRMModuleBaseExt
try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.managed import ManagedServicesClient
    from msrestazure.azure_operation import AzureOperationPoller
    from msrest.polling import LROPoller
except ImportError:
    # This is handled in azure_rm_common
    pass


class Actions:
    NoAction, Create, Update, Delete = range(4)


class AzureRMMarketplaceRegistrationDefinition(AzureRMModuleBaseExt):
    def __init__(self):
        self.module_arg_spec = dict(
            scope=dict(
                type='str',
                required=True
            ),
            marketplace_identifier=dict(
                type='str',
                required=True
            ),
            state=dict(
                type='str',
                default='present',
                choices=['present', 'absent']
            )
        )

        self.scope = None
        self.marketplace_identifier = None
        self.body = {}

        self.results = dict(changed=False)
        self.mgmt_client = None
        self.state = None
        self.to_do = Actions.NoAction

        super(AzureRMMarketplaceRegistrationDefinition, self).__init__(derived_arg_spec=self.module_arg_spec,
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

        self.mgmt_client = self.get_mgmt_svc_client(ManagedServicesClient,
                                                    base_url=self._cloud_environment.endpoints.resource_manager,
                                                    api_version='2020-02-01-preview')

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

    def get_resource(self):
        try:
            response = self.mgmt_client.marketplace_registration_definitions.get(scope=self.scope,
                                                                                 marketplace_identifier=self.marketplace_identifier)
        except CloudError as e:
            return False
        return response.as_dict()


def main():
    AzureRMMarketplaceRegistrationDefinition()


if __name__ == '__main__':
    main()
