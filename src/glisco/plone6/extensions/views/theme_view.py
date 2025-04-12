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

    def get_config_from_file(self, filename):
        """Get configuration from a JSON file."""
        theme_config_path = "/".join(__file__.split("/")[:-2]) + "/themes/data/" + filename
        print("********* >>> ", theme_config_path)

        with open(theme_config_path, "r") as file:
            return json.load(file)
    
    def get_registry_record(self, name):
        """Get a registry record by name."""
        try:
            return api.portal.get_registry_record(name)
        except KeyError:
            return None
    
    def get_theme_name(self):
        """Get a theme by name."""
        prefix = "glisco.extensions.settings.theme"
        field = "theme"
        try:
            # print("****** >>> getting theme name from ", prefix + "." + field)
            config = api.portal.get_registry_record(prefix + "." + field)
            # print("****** >>> theme name is ", config)
            return config
        except KeyError:
            return None
        
        
    def get_custom_theme(self):
        """Get a theme by name."""
        prefix = "glisco.extensions.settings.theme"
        field = "design_configuration"
        try:
            # print("****** >>> getting config from ", prefix + "." + field)
            config = api.portal.get_registry_record(prefix + "." + field)
            return json.dumps(config)
        except KeyError:
            return None
        
    def exception_theme(self):
        return {
            "themeName": "Exception Theme",
            "description": "Error in @@site-theme. Please check the console for more details.",
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
            "spacing" : {
                # Neutral theme uses a balanced and versatile spacing system with default density and standard breakpoints.,
                
                # APPLIES TO:                
                # Containers: for responsive layout and horizontal gutters,
                # Text blocks: outer margins and inner paddings,
                # Images and media: consistent whitespace around visual elements,
                # Cards, buttons, forms: margin, padding, and gap utilities

    
                "baseUnit": 4, # Smallest building block in pixels. Used to derive all spacing values via scale.,

                "density": "default", # Can be 'compact', 'default', or 'minimal'. Controls overall openness of the layout.,

                "scale": [1, 2, 3, 4, 6, 8, 12, 16], # Each scale value is multiplied by baseUnit × density multiplier to yield spacing tokens.,

                "gutters": { #Standard padding applied inside containers (horizontal) and between vertical layout sections (vertical).
                    "horizontal": 24,
                    "vertical": 32
                },

                "sectionSpacing": [40, 80, 120], # Vertical spacing rhythm between sections of the page (e.g., hero → features).,

                "headingSpacing": {
                    "h1": "var(--space-8)",
                    "h2": "var(--space-6)",
                    "h3": "var(--space-4)",
                    "h4": "var(--space-2)",
                    "h5": "var(--space-1)",
                }, # Vertical spacing between headings and their respective content blocks.,

                "textSpacing": {
                    "body": "var(--space-2)",
                    "small": "var(--space-1)"
                }, # Vertical spacing between text elements 

                "containerWidths": { # Max-widths for containers at different screen sizes. XS is fluid by default (null = 100%).
                    "xs": None,
                    "sm": 540,
                    "md": 720,
                    "lg": 960,
                    "xl": 1140
                },

                "breakpoints": { # Defines media query thresholds for layout changes. Matches containerWidths.
                    "xs": 0,
                    "sm": 576,
                    "md": 768,
                    "lg": 992,
                    "xl": 1200
                },
            }
        }

    def __call__(self):
        try:
            theme_name = self.get_theme_name()
            default_theme_file = theme_name.split(".")[-1] + ".json"
            default_theme = self.get_config_from_file(default_theme_file)
            custom_theme = self.get_custom_theme()
            print("****** >>> custom_theme is ", custom_theme)
            # print("****** >>> type of custom_theme is ", type(custom_theme))
            if custom_theme is not None and custom_theme != "null":
                print("****** >>> custom_theme is **", custom_theme, "**", custom_theme != "null")
                return json.dumps(json.loads(custom_theme))
            else:
                # If no custom theme is set, return the default theme
                return json.dumps(json.loads(default_theme))

        except Exception as e:
            print("Error in ThemeView:", e)
            return json.dumps(self.exception_theme())
