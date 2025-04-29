# This view is giving me a bit of an issue:
# It is declared as belowL
# <plone:service
#         name="portal-types"
#         method="GET"
#         for="*"
#         factory=".portal_types.services.PortalTypesServiceGet"
#         permission="zope2.View" 
#         /> 
# But when it returns the data, it is not in JSON format.
# It is returning the data in a non-json format, with ' instead of " in the data field of the result

import json
from plone import api
from plone.restapi.services import Service
from Products.CMFCore.utils import getToolByName
from zope.interface import providedBy

class PortalTypesServiceGet(Service):

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
            # This comes out as 
            # ['Collection', 'Discussion Item', 'Document', 'Event', 'File', 'Folder', 'Image', 'LIF', 'LRF', 'Link', 'News Item', 'Plone Site', 'TempFolder']
            print("************** /EnabledPortalTypes **************")

        except Exception as e:
            status = 500
            message = "Error retrieving portal types: " + str(e)
            print(e)
        
        return {
            "status": status,
            "message": message,
            "data": fields 
            # "data" is the list of enabled portal types
            # But is being rendered in non-json format, with ' instead of ". 
        }
