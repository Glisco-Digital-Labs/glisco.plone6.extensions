import json

TYPE_OF_PAGE_TAXONOMY = "glisco.extensions.vocabularies.pages.types"
PAGE_BLOCK_LAYOUTS_TAXONOMY = "glisco.extensions.vocabularies.pages.blocks.layouts"
MARKET_SEGMENTS_TAXONOMY = "glisco.extensions.vocabularies.markets.segments"
PRODUCT_SEGMENTS_TAXONOMY = "glisco.extensions.vocabularies.products.segments"
PRODUCT_TYPES_TAXONOMY = "glisco.extensions.vocabularies.products.types"
PRODUCT_MATERIALS_TAXONOMY = "glisco.extensions.vocabularies.products.materials"
PRODUCTION_TECHNIQUES_TAXONOMY = "glisco.extensions.vocabularies.products.techniques"

VOCABULARY_SCHEMA = json.dumps(
    {
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "token": {"type": "string"},
                        "titles": {
                            "type": "object",
                            "properties": {
                                "lang": {"type": "string"},
                                "title": {"type": "string"},
                            },
                        },
                    },
                },
            }
        },
    }
)

CSS_SCHEMA = json.dumps(
    {
        "type": "object",
        "properties": {
            "variables": {
                "type": "string",
            },
            "base": {
                "type": "string",
            },
            "components": {
                "type": "string",
            }, 
            "animations": {
                "type": "string",
            },
            "utilities": {
                "type": "string",
            }
        },
    }
)
