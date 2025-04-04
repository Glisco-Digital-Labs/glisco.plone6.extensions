# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface

from Products.CMFCore.utils import getToolByName

class IEnabledPortalTypes(Interface):
    """Marker Interface for IEnabledPortalTypes"""


@implementer(IEnabledPortalTypes)
class EnabledPortalTypes(BrowserView):
    def __init__(self, context, request):
          self.context = context
          self.request = request
          portal_types = getToolByName(context, "portal_types")
          self.types = portal_types.listContentTypes()


    def enabledPortalTypes(self):
        try:
            
          reg_record = api.portal.get_registry_record("glisco.extensions.settings.contenttypes.content_type_settings")
          print("**************  EnabledPortalTypes  **************")
          print(reg_record)
          print("**************  PORTAL TYPES  **************")
          print(self.types)
          print("************** /EnabledPortalTypes **************")
          fields = ["content_type_settings"]
        except Exception as e:
          print(e)
           
        return """{dummy: "dummy"}"""

    def __call__(self):
        return self.enabledPortalTypes()
