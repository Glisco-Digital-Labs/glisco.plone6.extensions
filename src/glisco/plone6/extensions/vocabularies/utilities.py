from plone import api
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

@provider(IVocabularyFactory)
def PageTypesVocabulary(context):
    name = "glisco.vocabularies.pages"
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    return SimpleVocabulary.fromItems(
        [[item["token"], item["token"], item["titles"][lang]] for item in items]
    )

@provider(IVocabularyFactory)
def MarketSegmentsVocabulary(context):
    name = "glisco.vocabularies.market_segments"
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    return SimpleVocabulary.fromItems(
        [[item["token"], item["token"], item["titles"][lang]] for item in items]
    )

@provider(IVocabularyFactory)
def ProductSegmentsVocabulary(context):
    name = "glisco.vocabularies.product_segments"
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    return SimpleVocabulary.fromItems(
        [[item["token"], item["token"], item["titles"][lang]] for item in items]
    )

@provider(IVocabularyFactory)
def ProductTypesVocabulary(context):
    name = "glisco.vocabularies.product_types"
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    return SimpleVocabulary.fromItems(
        [[item["token"], item["token"], item["titles"][lang]] for item in items]
    )

@provider(IVocabularyFactory)
def ProductMaterialsVocabulary(context):
    name = "glisco.vocabularies.product_materials"
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    return SimpleVocabulary.fromItems(
        [[item["token"], item["token"], item["titles"][lang]] for item in items]
    )

@provider(IVocabularyFactory)
def ProductionTechniquesVocabulary(context):
    name = "glisco.vocabularies.production_techniques"
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    return SimpleVocabulary.fromItems(
        [[item["token"], item["token"], item["titles"][lang]] for item in items]
    )