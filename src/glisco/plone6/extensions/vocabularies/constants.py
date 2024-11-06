import json

TYPE_OF_PAGE_TAXONOMY = "glisco.plone6.extensions.vocabularies.type_of_page"

VOCABULARY_SCHEMA = json.dumps(
    {
        "type": "object",
        "properties": {
            # "lid": {"type": "string"},
            # "title": {
            #     "type": "object",
            #     "properties": {
            #         "lang": {"type": "string"},
            #         "title": {"type": "string"},
            #     },
            # },
            # "description": {
            #     "type": "object",
            #     "properties": {
            #         "lang": {"type": "string"},
            #         "title": {"type": "string"},
            #     },
            # },
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