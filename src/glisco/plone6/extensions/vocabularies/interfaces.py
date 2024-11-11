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
# FashionProductAddonsVocabularyFactory - Production Techniques (embossing, washing, hand-carved, hand-painted, etc)
#
# ###########################
# Other possible taxonomies are: 
# 
# Product Collection (Birdy, etc)
# Product Theme (Mediterranean Summer, Caotic Nights, etc)
# Product Colour (Red, Indigo, SummeryGreen, etc)
# Product Finish (Hand-decorated, etc) - this can be as techniques
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
from glisco.plone6.extensions.vocabularies.data.productsegments import PRODUCT_SEGMENTS_DATA
from glisco.plone6.extensions.vocabularies.data.productmaterials import PRODUCT_MATERIALS_DATA
from glisco.plone6.extensions.vocabularies.data.productiontechniques import PRODUCTION_TECHNIQUES_DATA
from glisco.plone6.extensions.vocabularies.data.producttypes import PRODUCT_TYPES_DATA
from glisco.plone6.extensions.vocabularies.constants import \
     MARKET_SEGMENTS_TAXONOMY, PRODUCT_SEGMENTS_TAXONOMY, PRODUCT_TYPES_TAXONOMY, \
     PRODUCT_MATERIALS_TAXONOMY, PRODUCTION_TECHNIQUES_TAXONOMY, TYPE_OF_PAGE_TAXONOMY 

class IMarketSettings(Interface)   : 

    enable_market_tagging = schema.Bool(
        title=_(u"Enable Market-based tagging of content"), 
        required=False
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

    

    # product_segments = schema.JSONField(
    #     title="Product Segments",
    #     description="Product Segments",
    #     required=False,
    #     schema=VOCABULARY_SCHEMA,
    #     default={ 
    #         "lid": PRODUCT_SEGMENTS_TAXONOMY,
    #         "items": PRODUCT_SEGMENTS_DATA },
    #     missing_value={"items": []},
    # )
    # directives.widget(
    #     "product_segments",
    #     frontendOptions={
    #         "widget": "vocabularyterms",
    #     },
    # )

    # product_types = schema.JSONField(
    #     title="Product Types",
    #     description="Product Types",
    #     required=False,
    #     schema=VOCABULARY_SCHEMA,
    #     default={ 
    #         "lid": PRODUCT_TYPES_TAXONOMY,
    #         "items": PRODUCT_TYPES_DATA },
    #     missing_value={"items": []},
    # )
    # directives.widget(
    #     "product_types",
    #     frontendOptions={
    #         "widget": "vocabularyterms",
    #     },
    # )


    # product_materials = schema.JSONField(
    #     title="Product Materials",
    #     description="Product Materials",
    #     required=False,
    #     schema=VOCABULARY_SCHEMA,
    #     default={ 
    #         "lid": PRODUCT_MATERIALS_TAXONOMY,
    #         "items": PRODUCT_MATERIALS_DATA },
    #     missing_value={"items": []},
    # )
    # directives.widget(
    #     "product_materials",
    #     frontendOptions={
    #         "widget": "vocabularyterms",
    #     },
    # )

    # production_techniques = schema.JSONField(
    #     title="Production Techniques",
    #     description="Production Techniques",
    #     required=False,
    #     schema=VOCABULARY_SCHEMA,
    #     default={ 
    #         "lid": PRODUCTION_TECHNIQUES_TAXONOMY,
    #         "items": PRODUCTION_TECHNIQUES_DATA },
    #     missing_value={"items": []},
    # )
    # directives.widget(
    #     "production_techniques",
    #     frontendOptions={
    #         "widget": "vocabularyterms",
    #     },
    # )

