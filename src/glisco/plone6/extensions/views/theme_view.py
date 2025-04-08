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
            "colors": {
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
            },
            "typography": {
                "fontBaseSize": "16px",
                "typeScale": 1.25,
                "fontFamilies": {
                    "heading": {
                        "name": "Poppins",
                        "fallback": "sans-serif",
                        "category": "sans",
                        "weights": [400, 600, 700],
                        "style": "normal"
                    },
                    "body": {
                        "name": "Roboto",
                        "fallback": "sans-serif",
                        'category': "sans",
                        "weights": [400, 500],
                        "style": "normal"
                    }
                },
                "lineHeight": {
                    "body": 1.6,
                    "heading": 1.3
                },
                "letterSpacing": {
                    "body": "normal",
                    "heading": "0.02em"
                },
                "textTransform": {
                    "heading": "none",
                    "nav": "uppercase"
                },
                "textDecoration": {
                    "link": "underline",
                    "hover": "none"
                },
                "verticalRhythmUnit": "8px",
                "fontSizes": {
                    "h1": "2.488rem",
                    "h2": "2.074rem",
                    "h3": "1.728rem",
                    "h4": "1.44rem",
                    "h5": "1.2rem",
                    "body": "1rem",
                    "small": "0.833rem"
                }
            }, 
            
        }

    def site_theme(self):
        
        return json.dumps(self.neutral_theme())

    def __call__(self):
        return self.site_theme()
