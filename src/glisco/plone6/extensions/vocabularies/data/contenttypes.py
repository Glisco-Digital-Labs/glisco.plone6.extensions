from zope.schema.interfaces import IBaseVocabulary
# ###########################################################################
#
# CONTENT TYPE DEFAULTS
#
# Description: Defines default content types for the site
#
# ###########################################################################

DEFAULT_PLONE_CONTENT_TYPES_DATA = [
    {
        "token": "Document",
        "titles": {
            "en": "Document",
            "pt": "Página",
        },
    },
    {
        "token": "Image",
        "titles": {
            "en": "Image",
            "pt": "Imagem",
        },
    },
    {
        "token": "File",
        "titles": {
            "en": "File",
            "pt": "Ficheiro",
        },
    },
    {
        "token": "Link",
        "titles": {
            "en": "Link",
            "pt": "Link",
        },
    },

    {
        "token": "News Item",
        "titles": {
            "en": "News Item",
            "pt": "Notícia",
        },
    },

    {
        "token": "Event",
        "titles": {
            "en": "Event",
            "pt": "Evento",
        },
    },
]

CONTENT_TYPES_DATA = [] + DEFAULT_PLONE_CONTENT_TYPES_DATA

class IContentTypesVocabulary(IBaseVocabulary):

    def __contains__(self, token):
        """Check if the vocabulary contains a specific token."""
        return len([v for v in CONTENT_TYPES_DATA if v["token"] == token]) >= 1

    def getTerm(value):
        """Return the ITerm object for the term 'value'.

        If 'value' is not a valid term, this method raises LookupError.
        """
        for term in CONTENT_TYPES_DATA:
            if term["token"] == value:
                return term["titles"]["en"]
        raise LookupError(f"Term '{value}' not found in vocabulary.")
    
    def __iter__(self):
        """Return an iterator over the vocabulary terms."""
        for term in self.CONTENT_TYPES_DATA:
            yield term["titles"]["en"]

    def __len__(self):
        """Return the number of terms in the vocabulary."""
        return len(self.CONTENT_TYPES_DATA)
    
    def __getitem__(self, token):
        """Return the term with the given token."""
        for term in self.CONTENT_TYPES_DATA:
            if term["token"] == token:
                return term["titles"]["en"]
            
        raise LookupError(f"Term '{token}' not found in vocabulary.")
    
