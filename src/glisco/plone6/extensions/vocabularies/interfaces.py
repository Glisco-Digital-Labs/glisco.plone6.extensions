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
from glisco.plone6.extensions import _
from glisco.plone6.extensions.vocabularies.constants import (
    MARKET_SEGMENTS_TAXONOMY,
    PAGE_BLOCK_LAYOUTS_TAXONOMY,
    PHOTOGRAPHY_TONES_TAXONOMY, 
    IMAGE_TREATMENT_TAXONOMY, 
    IMAGE_MOOD_DESCRIPTORS_TAXONOMY,
    ILLUSTRATION_TYPES_TAXONOMY,
    PRODUCT_MATERIALS_TAXONOMY,
    PRODUCT_SEGMENTS_TAXONOMY,
    PRODUCT_TYPES_TAXONOMY,
    PRODUCTION_TECHNIQUES_TAXONOMY,
    TYPE_OF_PAGE_TAXONOMY,
    VOCABULARY_SCHEMA,
    THEMES_TAXONOMY,
    SITE_ARCHETYPES_TAXONOMY,
)

from glisco.plone6.extensions.vocabularies.data.blocklayouts import (
    PAGE_BLOCK_LAYOUTS_DATA,
)
from glisco.plone6.extensions.vocabularies.data.css.defaults import (
    ANIMATIONS_CSS,
    BASE_CSS,
    COMPONENTS_CSS,
    UTILITIES_CSS,
    VARIABLES_CSS
)
from glisco.plone6.extensions.vocabularies.data.marketsegments import (
    MARKET_SEGMENTS_DATA,
)
from glisco.plone6.extensions.vocabularies.data.pagetypes import PAGE_TYPES_DATA
from glisco.plone6.extensions.vocabularies.data.productiontechniques import (
    PRODUCTION_TECHNIQUES_DATA,
)
from glisco.plone6.extensions.vocabularies.data.productmaterials import (
    PRODUCT_MATERIALS_DATA,
)
from glisco.plone6.extensions.vocabularies.data.productsegments import (
    PRODUCT_SEGMENTS_DATA,
)
from glisco.plone6.extensions.vocabularies.data.producttypes import PRODUCT_TYPES_DATA

from glisco.plone6.extensions.vocabularies.data.imagery import (
    PHOTOGRAPHY_TONES_DATA,
    ILLUSTRATION_TYPES_TAXONOMY_DATA,
    IMAGE_TREATMENT_TAXONOMY_DATA,   
    IMAGE_MOOD_DESCRIPTORS_DATA,
)

from plone import schema
from plone.autoform import directives
from zope.interface import Interface


class IMarketSettings(Interface):

    enable_market_tagging = schema.Bool(
        title=_("Enable Market-based tagging of content"), required=False
    )

    market_segments = schema.JSONField(
        title="Market Segments",
        description="Market Segments",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={"lid": MARKET_SEGMENTS_TAXONOMY, "items": MARKET_SEGMENTS_DATA},
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
        default={"lid": TYPE_OF_PAGE_TAXONOMY, "items": PAGE_TYPES_DATA},
        missing_value={"items": []},
    )
    directives.widget(
        "types_of_page",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

    block_layouts = schema.JSONField(
        title="Block Layouts",
        description="Available layouts for page blocks",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={"lid": PAGE_BLOCK_LAYOUTS_TAXONOMY, "items": PAGE_BLOCK_LAYOUTS_DATA},
        missing_value={"items": []},
    )

    directives.widget(
        "block_layouts",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )


class IProductSettings(Interface):

    product_segments = schema.JSONField(
        title="Product Segments",
        description="Product Segments",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={"lid": PRODUCT_SEGMENTS_TAXONOMY, "items": PRODUCT_SEGMENTS_DATA},
        missing_value={"items": []},
    )
    directives.widget(
        "product_segments",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

    product_types = schema.JSONField(
        title="Product Types",
        description="Product Types",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={"lid": PRODUCT_TYPES_TAXONOMY, "items": PRODUCT_TYPES_DATA},
        missing_value={"items": []},
    )
    directives.widget(
        "product_types",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

    product_materials = schema.JSONField(
        title="Product Materials",
        description="Product Materials",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={"lid": PRODUCT_MATERIALS_TAXONOMY, "items": PRODUCT_MATERIALS_DATA},
        missing_value={"items": []},
    )
    directives.widget(
        "product_materials",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

    production_techniques = schema.JSONField(
        title="Production Techniques",
        description="Production Techniques",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={
            "lid": PRODUCTION_TECHNIQUES_TAXONOMY,
            "items": PRODUCTION_TECHNIQUES_DATA,
        },
        missing_value={"items": []},
    )
    directives.widget(
        "production_techniques",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )


class IDesignSettings(Interface):

    enable_css_customization = schema.Bool(
        title=_("Enable CSS customization"),
        description=_("Enable CSS customization for the site"),
        default=True,
        required=False,
    )

    variables = schema.SourceText(
        title=_("CSS variables"),
        description="Design token definitions for your color system, spacing, typography, and themes",
        default=VARIABLES_CSS,
        required=False,
    )

    base = schema.SourceText(
        title=_("Base CSS"),
        description="Global base styles and reset layer",
        default=BASE_CSS,
        required=False,
    )

    components = schema.SourceText(
        title=_("Components CSS"),
        description="Reusable, design-tokenized UI components",
        default=COMPONENTS_CSS,
        required=False,
    )

    animations = schema.SourceText(
        title=_("Animations CSS"),
        description="Keyframes and animation-related utility classes",
        default=ANIMATIONS_CSS,
        required=False,
    )

    utilities = schema.SourceText(
        title=_("Utilities CSS"),
        description="Utility classes for layout, spacing, and more",
        default=UTILITIES_CSS,
        required=False,
    )


class IContentTypeSettings(Interface):

    # https://5.docs.plone.org/external/plone.app.dexterity/docs/advanced/vocabularies.html

    enable_content_types_customization = schema.Bool(
        title=_("Enable Content Types customization"),
        description=_("Restricts content types to be used in the site"),
        default=True,
        required=False,
    )

    content_type_settings = schema.List(
        title=_("Content Types Settings"),
        description="What content types are available on the site",
        value_type=schema.Choice(
            title=_("Organiser"),
            vocabulary="plone.app.vocabularies.PortalTypes",
            required=False,
        ),
        required=False,
    )


class IImagerySettings(Interface):

    photography_tones = schema.JSONField(
        title="Fotography Tones",
        description="Fotography Tones",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={"lid": PHOTOGRAPHY_TONES_TAXONOMY, "items": PHOTOGRAPHY_TONES_DATA},
        missing_value={"items": []},
    )
    directives.widget(
        "photography_tones",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

    illustration_types = schema.JSONField(
        title="Illustration Types",
        description="Illustration Types",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={"lid": ILLUSTRATION_TYPES_TAXONOMY, "items": ILLUSTRATION_TYPES_TAXONOMY_DATA},
        missing_value={"items": []},
    )
    directives.widget(
        "illustration_types",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

    image_treatment = schema.JSONField(
        title="Image Treatment",
        description="Image Treatment",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={"lid": IMAGE_TREATMENT_TAXONOMY, "items": IMAGE_TREATMENT_TAXONOMY_DATA},
        missing_value={"items": []},
    )
    directives.widget(
        "image_treatment",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

    image_mood = schema.JSONField(
        title="Image Moods",
        description="Image Moods",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={"lid": IMAGE_MOOD_DESCRIPTORS_TAXONOMY, "items": IMAGE_MOOD_DESCRIPTORS_DATA},
        missing_value={"items": []},
    )
    directives.widget(
        "image_mood",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

class IThemeSettings(Interface):

    # https://5.docs.plone.org/external/plone.app.dexterity/docs/advanced/vocabularies.html

    enable_theme_customization = schema.Bool(
        title=_("Enable Theme Customization"),
        description=_("Defines the theme for the site"),
        default=True,
        required=False,
    )

    theme = schema.List(
        title=_("Site Theme"),
        description="Visual Theme for the site",
        value_type=schema.Choice(
            title=_("Theme"),
            vocabulary="glisco.extensions.vocabularies.themes",
            required=False,
        ),
        required=False,
    )

    # site_archetypes = schema.List(
    #     title=_("Site Archetypes"),
    #     description="Site Archetype",
    #     value_type=schema.Choice(
    #         title=_("Site Archetypes"),
    #         vocabulary=SITE_ARCHETYPES_TAXONOMY,
    #         required=False,
    #     ),
    #     required=False,
    # )