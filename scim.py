# Module scim

import json

class SCIMObject:
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

class User(SCIMObject):
    CORE_USER_SCHEMA = "urn:ietf:params:scim:schemas:core:2.0:User"
    ENTERPRISE_USER_SCHEMA = "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
    IDCS_USER_SCHEMA = "urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User"
    PASSWORDSTATE_USER_SCHEMA = "urn:ietf:params:scim:schemas:oracle:idcs:extension:passwordState:User"
    USERSTATE_USER_SCHEMA = "urn:ietf:params:scim:schemas:oracle:idcs:extension:userState:User"

    SCIM_ATTRS = ['schemas', 'id', 'externalId', 'meta', 'idaasCreatedBy',
    'idaasLastModifiedBy']
    CORE_ATTRS = ['userName', 'name', 'displayName', 'nickName', 'profileUrl',
    'title', 'userType', 'locale', 'preferredLanguage', 'timezone', 'active',
    'password', 'emails', 'phoneNumbers', 'ims', 'photos', 'addresses',
    'groups', 'entitlements', 'roles', 'x509certificates']
    ENTERPRISE_ATTRS = ['employeeNumber', 'costCenter', 'organization',
    'division', 'department', 'manager']
    IDCS_ATTRS = ['isFederatedUser', 'status', 'internalName', 'provider',
    'creationMechanism', 'appRoles', 'doNotShowGettingStarted']
    PASSWORDSTATE_ATTRS = ['lastSuccessfulSetDate', 'cantChange', 'cantExpire',
            'mustChange', 'expired', 'passwordHistory']
    USERSTATE_ATTRS = ['lastSuccessfulLoginDate', 'lastFailedLoginDate',
    'loginAttempts', 'locked']

    def __init__(self, *initial_data, **kwargs):
        self.schemas = [User.CORE_USER_SCHEMA]

        super(SCIMObject, self).__init__()

        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __setattr__(self, name, value):
        if name in User.ENTERPRISE_ATTRS:
            self.schemas += [User.ENTERPRISE_USER_SCHEMA]
        elif name in User.IDCS_ATTRS:
            self.schemas += [User.IDCS_USER_SCHEMA]
        elif name in User.PASSWORDSTATE_ATTRS:
            self.schemas += [User.PASSWORDSTATE_USER_SCHEMA]
        elif name in User.USERSTATE_ATTRS:
            self.schemas += [User.USERSTATE_USER_SCHEMA]

        self.__dict__[name] = value
