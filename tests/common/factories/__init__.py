# -*- coding: utf-8 -*-

"""Factory classes for easily generating test objects."""
from .base import set_session

from .activation import Activation
from .annotation import Annotation
from .annotation_moderation import AnnotationModeration
from .auth_client import AuthClient, ConfidentialAuthClient
from .auth_ticket import AuthTicket
from .authz_code import AuthzCode
from .document import Document, DocumentMeta, DocumentURI
from .feature import Feature
from .flag import Flag
from .group import Group, OpenGroup, RestrictedGroup
from .group_scope import GroupScope
from .organization import Organization
from .setting import Setting
from .token import DeveloperToken, OAuth2Token
from .user import User
from .user_identity import UserIdentity

__all__ = (
    "Activation",
    "Annotation",
    "AnnotationModeration",
    "AuthClient",
    "AuthTicket",
    "AuthzCode",
    "ConfidentialAuthClient",
    "DeveloperToken",
    "Document",
    "DocumentMeta",
    "DocumentURI",
    "Feature",
    "Flag",
    "Group",
    "GroupScope",
    "OAuth2Token",
    "OpenGroup",
    "Organization",
    "RestrictedGroup",
    "Setting",
    "User",
    "UserIdentity",
    "set_session",
)
