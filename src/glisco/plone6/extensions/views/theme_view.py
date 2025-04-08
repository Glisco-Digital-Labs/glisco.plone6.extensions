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

    def neutral_theme(self):
        return {
            "themeName": "Neutral Theme",
            "description": "Minimal theme config with HSL base colors and derived harmony",
            "mode": "light",
            "baseColors": {
                "accent": "hsl(208, 100%, 43%)",
                "grey": "hsl(0, 0%, 40%)"
            },
            "colorRoles": {
                "analogous": "hsl(178, 100%, 43%)",
                "triadic1": "hsl(328, 100%, 43%)",
                "triadic2": "hsl(88, 100%, 43%)"
            },
            "lightnessStops": [
                0.07,
                0.1,
                0.15,
                0.25,
                0.35,
                0.45,
                0.55,
                0.65,
                0.75,
                0.85,
                0.92,
                0.97
            ]
        }

    def site_theme(self):
        
        return json.dumps(self.neutral_theme())

    def __call__(self):
        return self.site_theme()
