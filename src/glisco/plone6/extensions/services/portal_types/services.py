import json
from plone import api
from plone.rest.interfaces import IAPIRequest
from plone.restapi.services import Service
from Products.CMFCore.utils import getToolByName
from zope.interface import providedBy

class PortalTypesServiceGet(Service):

    def __init__(self, context, request):
        self.context = context
        self.request = request       
        
    def reply(self):
        fields = []
        status = 200
        message = "OK"
        try:
            portal_types = getToolByName(self.context, "portal_types")
            cms_types = portal_types.listContentTypes()
            print("**************  cms_types  **************")
            print(cms_types)
            reg_record = api.portal.get_registry_record("glisco.extensions.settings.contenttypes.content_type_settings")
            print("**************  reg_record  **************")
            print(reg_record)
            fields = cms_types if reg_record is None else [ t for t in reg_record if t in cms_types]
            print("**************  EnabledPortalTypes  **************")
            print(reg_record)
            print("**************  ALL PORTAL TYPES  **************")
            print(cms_types)
            print("**************  fields (return)  **************")
            print(fields)
            print("************** /EnabledPortalTypes **************")

        except Exception as e:
            status = 500
            message = "Error retrieving portal types: " + str(e)
            print(e)
        
        return {
            "status": status,
            "message": message,
            "data": fields
        }
