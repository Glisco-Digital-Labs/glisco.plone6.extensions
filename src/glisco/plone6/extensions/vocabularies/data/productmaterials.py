from glisco.plone6.extensions.vocabularies.constants import PRODUCT_MATERIALS_TAXONOMY

        # {'id': 'acetate', 'value': 'acetate', 'title': 'Acetate'}, 
        # {'id': 'acrylic', 'value': 'acrylic', 'title': 'Acrylic'},
        # {'id': 'cashmere', 'value': 'cashmere', 'title': 'Cashmere'},
        # {'id': 'chlorofibre', 'value': 'chlorofibre', 'title': 'Chlorofibre'},
        # {'id': 'cotton', 'value': 'cotton', 'title': 'Cotton'},
        # {'id': 'elastane', 'value': 'elastane', 'title': 'Elastane'},
        # {'id': 'linen', 'value': 'linen', 'title': 'Linen'},
        # {'id': 'polyamide', 'value': 'polyamide', 'title': 'Polyamide'},
        # {'id': 'polyester', 'value': 'polyester', 'title': 'Polyester'},
        # {'id': 'polyethylene', 'value': 'polyethylene', 'title': 'Polyethylene'},

PRODUCT_MATERIALS_DATA = [
    {
        "token": PRODUCT_MATERIALS_TAXONOMY + ".acetate",
        "titles": {
            "en": "Acetate",
            "pt": "Acetato",
        },
    },

    {
        "token": PRODUCT_MATERIALS_TAXONOMY + ".cashmere",
        "titles": {
            "en": "Cashmere",
            "pt": "Cachemira",
        },
    },

    {
        "token": PRODUCT_MATERIALS_TAXONOMY + ".linen",
        "titles": {
            "en": "Linen",
            "pt": "Linho",
        },
    },

    {
        "token": PRODUCT_MATERIALS_TAXONOMY + ".other",
        "titles": {
            "en": "Other",
            "pt": "Outros",
        },
    },
                
]