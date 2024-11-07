from glisco.plone6.extensions.vocabularies.constants import PRODUCTION_TECHNIQUES_TAXONOMY

        # {'id': 'embroidery', 'value': 'embroidery', 'title': 'Embroidery'},
        # {'id': 'embossing', 'value': 'embossing', 'title': 'Embossing'},
        # {'id': 'printing', 'value': 'printing', 'title': 'Printing'},
        # {'id': 'digitalprinting', 'value': 'digitalprinting', 'title': 'Digital Printing'},
        # {'id': 'sublimated', 'value': 'sublimated', 'title': 'Sublimated'},
        # {'id': 'transfer', 'value': 'transfer', 'title': 'Transfer'},
        # {'id': 'laser', 'value': 'laser', 'title': 'Laser'},
        # {'id': 'pleated', 'value': 'pleated', 'title': 'Pleated'},
        # {'id': 'washed', 'value': 'washed', 'title': 'Washed'},
        # {'id': 'dyeing', 'value': 'dyeing', 'title': 'Dyeing'},
        # {'id': 'allover', 'value': 'allover', 'title': 'All-over'},

PRODUCTION_TECHNIQUES_DATA = [
    {
        "token": PRODUCTION_TECHNIQUES_TAXONOMY + ".embroidery",
        "titles": {
            "en": "Embroidery",
            "pt": "Bordado",
        },
    },

    {
        "token": PRODUCTION_TECHNIQUES_TAXONOMY + ".digitalprinting",
        "titles": {
            "en": "Digital Printing",
            "pt": "Impressão Digital",
        },
    },

    {
        "token": PRODUCTION_TECHNIQUES_TAXONOMY + ".washed",
        "titles": {
            "en": "Washed",
            "pt": "Lavagem",
        },
    },

    {
        "token": PRODUCTION_TECHNIQUES_TAXONOMY + ".other",
        "titles": {
            "en": "Other",
            "pt": "Outros",
        },
    },
                
]