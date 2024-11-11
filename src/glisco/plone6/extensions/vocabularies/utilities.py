from plone import api
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

from glisco.plone6.extensions.vocabularies.constants import \
     MARKET_SEGMENTS_TAXONOMY, PRODUCT_SEGMENTS_TAXONOMY, PRODUCT_TYPES_TAXONOMY, \
     PRODUCT_MATERIALS_TAXONOMY, PRODUCTION_TECHNIQUES_TAXONOMY, TYPE_OF_PAGE_TAXONOMY 

def loadVocabulary(name) :
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    return SimpleVocabulary.fromItems(
        [[item["token"], item["token"], item["titles"][lang]] for item in items]
    )

@provider(IVocabularyFactory)
def PageTypesVocabulary(context):
    return loadVocabulary(TYPE_OF_PAGE_TAXONOMY)
    
@provider(IVocabularyFactory)
def MarketSegmentsVocabulary(context):
    return loadVocabulary(MARKET_SEGMENTS_TAXONOMY)

@provider(IVocabularyFactory)
def ProductSegmentsVocabulary(context):
    return loadVocabulary(PRODUCT_SEGMENTS_TAXONOMY)

@provider(IVocabularyFactory)
def ProductTypesVocabulary(context):
    return loadVocabulary(PRODUCT_TYPES_TAXONOMY)

@provider(IVocabularyFactory)
def ProductMaterialsVocabulary(context):
    return loadVocabulary(PRODUCT_MATERIALS_TAXONOMY)

@provider(IVocabularyFactory)
def ProductionTechniquesVocabulary(context):
    return loadVocabulary(PRODUCTION_TECHNIQUES_TAXONOMY)
