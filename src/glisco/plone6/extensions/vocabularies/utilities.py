from glisco.plone6.extensions.vocabularies.constants import (
    MARKET_SEGMENTS_TAXONOMY,
    PAGE_BLOCK_LAYOUTS_TAXONOMY,
    PRODUCT_MATERIALS_TAXONOMY,
    PRODUCT_SEGMENTS_TAXONOMY,
    PRODUCT_TYPES_TAXONOMY,
    PHOTOGRAPHY_TONES_TAXONOMY,
    IMAGE_TREATMENT_TAXONOMY,
    IMAGE_MOOD_DESCRIPTORS_TAXONOMY,
    ILLUSTRATION_TYPES_TAXONOMY,
    PRODUCTION_TECHNIQUES_TAXONOMY,
    THEMES_TAXONOMY,
    SITE_ARCHETYPES_TAXONOMY,
)
from glisco.plone6.extensions.vocabularies.constants import TYPE_OF_PAGE_TAXONOMY
from plone import api
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


def loadVocabulary(name):
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
def BlockLayoutTypesVocabulary(context):
    return loadVocabulary(PAGE_BLOCK_LAYOUTS_TAXONOMY)


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

@provider(IVocabularyFactory)
def PhotographyTonesVocabulary(context):
    return loadVocabulary(PHOTOGRAPHY_TONES_TAXONOMY)

@provider(IVocabularyFactory)
def ImageTreatmentVocabulary(context):
    return loadVocabulary(IMAGE_TREATMENT_TAXONOMY)

@provider(IVocabularyFactory)
def ImageMoodDescriptorsVocabulary(context):
    return loadVocabulary(IMAGE_MOOD_DESCRIPTORS_TAXONOMY)

@provider(IVocabularyFactory)
def IllustrationTypesVocabulary(context):
    return loadVocabulary(ILLUSTRATION_TYPES_TAXONOMY)

@provider(IVocabularyFactory)
def ThemesVocabulary(context):
    return loadVocabulary(ILLUSTRATION_TYPES_TAXONOMY)

@provider(IVocabularyFactory)
def SiteArchetypesVocabulary(context):
    return loadVocabulary(SITE_ARCHETYPES_TAXONOMY)
