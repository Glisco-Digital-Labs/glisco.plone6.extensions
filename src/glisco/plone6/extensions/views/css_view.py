# -*- coding: utf-8 -*-

import pprint
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface
from plone import api
from glisco.plone6.extensions.vocabularies.interfaces import IDesignSettings

class ICssView(Interface):
    """Marker Interface for ICssView"""

@implementer(ICssView)
class CssView(BrowserView):
    
    def bundle(self):
        
        reg_record = api.portal.get_registry_record(interface=IDesignSettings)
        pprint("********************** CSS SETTINGS **********************")
        pprint(reg_record)
        return reg_record
    
    def __call__(self):
        template = """<li class="heading" i18n:translate="">
          Sample View
        </li>"""
        # return template
        return self.bundle()
