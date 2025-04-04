# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IEnabledPortalTypes(Interface):
    """Marker Interface for IEnabledPortalTypes"""


@implementer(IEnabledPortalTypes)
class EnabledPortalTypes(BrowserView):
    def enabledPortalTypes(self):
        reg_record = api.portal.get_registry_record("glisco.extensions.settings.contenttypes")
        print("**************  EnabledPortalTypes  **************")
        print(reg_record)
        print("************** /EnabledPortalTypes **************")
        fields = ["content_type_settings"]
        return """{dummy: "dummy"}"""

    def __call__(self):
        return self.enabledPortalTypes()
