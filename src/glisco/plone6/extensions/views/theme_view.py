# -*- coding: utf-8 -*-
import json
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class IThemeView(Interface):
    """Marker Interface for IThemeView"""


@implementer(IThemeView)
class ThemeView(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request


    def site_theme(self):
        
        dummy_theme = {
            "colors": {
                "primary": "#ff0000",
                "secondary": "#00ff00",
                "tertiary": "#0000ff",
            },
            "fonts": {
                "heading": "Arial",
                "body": "Helvetica",
            },
        }
        
        return json.dumps(dummy_theme)

    def __call__(self):
        return self.site_theme()
