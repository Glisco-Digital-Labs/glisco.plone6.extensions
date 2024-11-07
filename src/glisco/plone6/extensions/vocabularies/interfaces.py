from plone import schema
from plone.autoform import directives
from zope.interface import Interface

#######################################################################
# This code is based on the Plone 6 training section on 
# Vocabularies, Registry-Settings and Control Panels, whicj is here:
# https://training.plone.org/mastering-plone/registry.html
#######################################################################
# 
# Regarding Taxonomies, we need them to be flexible enough to support 
# multiple business needs, for different clients in different industries.
#
# ###########################
# Segments from IR map to broader segments, which we will use
#
# FashionProductSegmentVocabularyFactory - Market Segment (boy, woman, etc)
# FashionProductGenreVocabularyFactory - Product Segment (body, dress, shirt, egg cups, dishes, guitar, etc)
# FashionProductStructureVocabularyFactory - Product Type (quilt, jacquard, acoustic guitar, digital guitar)
# FashionProductCompositionVocabularyFactory - Composition/Materials (elastane, cotton, Stoneware, maple, mahogany, etc)
# FashionProductAddonsVocabularyFactory - Product Techniques (embossing, washing, hand-carved, hand-painted, etc)
#
# ###########################
# Other possible taxonomies are: 
# 
# Product Collection (Birdy, etc)
# Product Theme (Mediterranean Summer, Caotic Nights, etc)
# Product Colour (Red, Indigo, SummeryGreen, etc)
# Product Finish (Hand-decorated, etc)
# Product Safety (dishwasher safe, microwave safe, food-approved, etc)
#
# ###########################
# Outside the taxonomy space, more in terms of additional behaviours consider:
#
# Product Dimensions
# Product Weight
# Product Pricing

from glisco.plone6.extensions.vocabularies.constants import VOCABULARY_SCHEMA
from glisco.plone6.extensions.vocabularies.data.pagetypes import PAGE_TYPES_DATA
from glisco.plone6.extensions.vocabularies.data.marketsegments import MARKET_SEGMENTS_DATA
from glisco.plone6.extensions.vocabularies.constants import MARKET_SEGMENTS_TAXONOMY, TYPE_OF_PAGE_TAXONOMY
   
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

