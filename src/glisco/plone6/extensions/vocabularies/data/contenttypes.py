# ###########################################################################
#
# CONTENT TYPE DEFAULTS
#
# Description: Defines default content types for the site
#
# ###########################################################################

DEFAULT_PLONE_CONTENT_TYPES_DATA = [
    {
        "token": "Document",
        "titles": {
            "en": "Document",
            "pt": "Página",
        },
    },
    {
        "token": "Image",
        "titles": {
            "en": "Image",
            "pt": "Imagem",
        },
    },
    {
        "token": "File",
        "titles": {
            "en": "File",
            "pt": "Ficheiro",
        },
    },
    {
        "token": "Link",
        "titles": {
            "en": "Link",
            "pt": "Link",
        },
    },

    {
        "token": "News Item",
        "titles": {
            "en": "News Item",
            "pt": "Notícia",
        },
    },

    {
        "token": "Event",
        "titles": {
            "en": "Event",
            "pt": "Evento",
        },
    },
]

CONTENT_TYPES_DATA = [] + DEFAULT_PLONE_CONTENT_TYPES_DATA

