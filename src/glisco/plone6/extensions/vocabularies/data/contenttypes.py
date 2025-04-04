from zope.schema.interfaces import IBaseVocabulary
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

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

content_types = SimpleVocabulary(
    [
        SimpleTerm(value=v["token"], title=v["titles"]["en"]) for v in DEFAULT_PLONE_CONTENT_TYPES_DATA
        # SimpleTerm(value=u'Bill', title=_(u'Bill')),
        # SimpleTerm(value=u'Bob', title=_(u'Bob')),
        # SimpleTerm(value=u'Jim', title=_(u'Jim'))
    ]
)

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
    
