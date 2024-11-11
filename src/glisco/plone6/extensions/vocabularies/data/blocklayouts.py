from glisco.plone6.extensions.vocabularies.constants import PAGE_BLOCK_LAYOUTS_TAXONOMY

# {"id" : "baby", "value" : "baby", "title" : "Baby"},
#         {"id" : "boy", "value" : "boy", "title" : "Boy"},
#         {"id" : "girl", "value" : "girl", "title" : "Girl"},
#         {"id" : "man", "value" : "man", "title" : "Man"},
#         {"id" : "pregnancy", "value" : "pregnancy", "title" : "Pregnancy"},
#         {"id" : "unisex", "value" : "unisex", "title" : "Unisex"},
#         {"id" : "woman", "value" : "woman", "title" : "Woman"},

PAGE_BLOCK_LAYOUTS_DATA = [
    {
        "token": PAGE_BLOCK_LAYOUTS_TAXONOMY + ".hidden",
        "titles": {
            "en": "None",
            "pt": "None",
        },
    },

    {
        "token": PAGE_BLOCK_LAYOUTS_TAXONOMY + ".block",
        "titles": {
            "en": "Block",
            "pt": "Block",
        },
    },

    {
        "token": PAGE_BLOCK_LAYOUTS_TAXONOMY + ".flex",
        "titles": {
            "en": "Flex",
            "pt": "Flex",
        },
    },

    {
        "token": PAGE_BLOCK_LAYOUTS_TAXONOMY + ".grid",
        "titles": {
            "en": "Grid",
            "pt": "Grid",
        },
    },
                
]