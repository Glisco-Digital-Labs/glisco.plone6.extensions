from Products.CMFCore.utils import getToolByName
from zope.interface import provider
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from plone.dexterity import utils
from plone import api

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

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


def registeredContentTypes():
    portal = api.portal.get()
    typeList = getToolByName(portal, 'portal_types').listTypeInfo()

    terms = []
    for type in typeList:
        dottedName = getattr(type, 'klass', None)

        print("dottedName is ", dottedName, ".")
        if dottedName is None:
            continue

        terms.append(
            SimpleVocabulary.createTerm(
                type.id,
                type.title,
                type.description
            )
        )

    print("registeredContentTypes terms is ", terms)

    return SimpleVocabulary(terms)

registeredContentTypesVocabulary = registeredContentTypes()

content_types = SimpleVocabulary(
    [
        SimpleTerm(value=v["token"], title=v["titles"]["en"]) for v in DEFAULT_PLONE_CONTENT_TYPES_DATA
    ]
)

CONTENT_TYPES_DATA = [] + DEFAULT_PLONE_CONTENT_TYPES_DATA

