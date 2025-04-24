import json
from plone import api
from plone.restapi.services import Service
from Products.CMFCore.utils import getToolByName

class PortalTypesService(Service):

    def __init__(self, context, request):
        self.context = context
        self.request = request
        try:
            # This returns ALL portal types registered in the system
            # including the ones that are not enabled
            # in the registry.
            # We need to filter them out later
            # by checking the registry.
            portal_types = getToolByName(context, "portal_types")
            self.cms_types = portal_types.listContentTypes()
        except Exception as e:
            print("Error getting portal types:", e)
            self.cms_types = []    
        
    def GET(self):
        # List portal types
        fields = []
        status = 200
        message = "OK"
        try:
            reg_record = api.portal.get_registry_record("glisco.extensions.settings.contenttypes.content_type_settings")
            fields = [ t for t in reg_record if t in self.cms_types]
            print("**************  EnabledPortalTypes  **************")
            print(reg_record)
            print("**************  ALL PORTAL TYPES  **************")
            print(self.cms_types)
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

    def __call__(self):
        method = self.request.method.upper()
        handler = getattr(self, method, None)
        if handler is None:
            self.request.response.setStatus(405)
            return {"error": f"Method {method} not allowed"}
        return handler()