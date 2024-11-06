from plone import schema
from plone.autoform import directives
from zope.interface import Interface

from glisco.plone6.extensions.vocabularies.constants import VOCABULARY_SCHEMA
from glisco.plone6.extensions.vocabularies.data.pagetypes import PAGE_TYPES_DATA
from glisco.plone6.extensions.vocabularies.data.marketsegments import MARKET_SEGMENTS_DATA
from glisco.plone6.extensions.vocabularies.constants import MARKET_SEGMENTS_TAXONOMY, TYPE_OF_PAGE_TAXONOMY


# This code is based on the Plone 6 training section on 
# Vocabularies, Registry-Settings and Control Panels, whicj is here:
# https://training.plone.org/mastering-plone/registry.html

   
class IPageSettings(Interface):

    types_of_page = schema.JSONField(
        title="Types of Page",
        description="Available types of a page",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={ 
            "lid": TYPE_OF_PAGE_TAXONOMY,
            "items": PAGE_TYPES_DATA },
        missing_value={"items": []},
    )
    directives.widget(
        "types_of_page",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

    market_segments = schema.JSONField(
        title="Market Segments",
        description="Market Segments",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={ 
            "lid": MARKET_SEGMENTS_TAXONOMY,
            "items": MARKET_SEGMENTS_DATA },
        missing_value={"items": []},
    )
    directives.widget(
        "market_segments",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

