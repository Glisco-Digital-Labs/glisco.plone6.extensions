from glisco.plone6.extensions.vocabularies.constants import PRODUCT_SEGMENTS_TAXONOMY


# {"id" : "body", "value" : "body", "title" : "Body"},
# {"id" : "dress", "value" : "dress", "title" : "Dress"},
# {"id" : "loungewear", "value" : "loungewear", "title" : "Loungewear"},
# {"id" : "overalls", "value" : "overalls", "title" : "Overalls"},
# {"id" : "shirt", "value" : "shirt", "title" : "Shirt"},
# {"id" : "skirt", "value" : "skirt", "title" : "Skirt"},
# {"id" : "sweatshirts", "value" : "sweatshirts", "title" : "Sweatshirts"},
# {"id" : "top", "value" : "top", "title" : "Top"},
# {"id" : "trousers", "value" : "trousers", "title" : "Trousers"},
# {"id" : "vest", "value" : "vest", "title" : "Vest"},

PRODUCT_SEGMENTS_DATA = [
    {
        "token": PRODUCT_SEGMENTS_TAXONOMY + ".body",
        "titles": {
            "en": "Body",
            "pt": "Body",
        },
    },
    {
        "token": PRODUCT_SEGMENTS_TAXONOMY + ".dress",
        "titles": {
            "en": "Dress",
            "pt": "Vestido",
        },
    },
    {
        "token": PRODUCT_SEGMENTS_TAXONOMY + ".shirt",
        "titles": {
            "en": "Shirt",
            "pt": "Camisa",
        },
    },
    {
        "token": PRODUCT_SEGMENTS_TAXONOMY + ".trousers",
        "titles": {
            "en": "Trousers",
            "pt": "Calças",
        },
    },
]
