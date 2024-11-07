import json

TYPE_OF_PAGE_TAXONOMY = "glisco.plone6.extensions.vocabularies.type_of_page"
MARKET_SEGMENTS_TAXONOMY = "glisco.plone6.extensions.vocabularies.market_segments"
PRODUCT_SEGMENTS_TAXONOMY = "glisco.plone6.extensions.vocabularies.product_segments"
PRODUCT_TYPES_TAXONOMY = "glisco.plone6.extensions.vocabularies.product_types"
PRODUCT_MATERIALS_TAXONOMY = "glisco.plone6.extensions.vocabularies.product_materials"
PRODUCTION_TECHNIQUES_TAXONOMY = "glisco.plone6.extensions.vocabularies.production_techniques"

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