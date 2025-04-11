from plone import api
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import (
    SimpleVocabulary,
    SimpleTerm
)

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
    TYPE_OF_PAGE_TAXONOMY,
)

from glisco.plone6.extensions.vocabularies.data.themes import (
    THEMES_DATA,
    SITE_ARCHETYPES_DATA,
    SITE_BUSINESS_SECTORS_DATA
)

def loadVocabularyFromStaticData(data):
    lang = api.portal.get_current_language()
    return SimpleVocabulary.fromItems(
        [
            [
                item["token"],
                item["token"],
                item["titles"][lang],
            ]
            for item in data
        ]
    )

def loadVocabularyFromPloneRegistry(name):
    registry_record_value = api.portal.get_registry_record(name)
    items = registry_record_value.get("items", [])
    lang = api.portal.get_current_language()
    return SimpleVocabulary.fromItems(
        [[item["token"], item["token"], item["titles"][lang]] for item in items]
    )


@provider(IVocabularyFactory)
def PageTypesVocabulary(context):
    return loadVocabularyFromPloneRegistry(TYPE_OF_PAGE_TAXONOMY)


@provider(IVocabularyFactory)
def BlockLayoutTypesVocabulary(context):
    return loadVocabularyFromPloneRegistry(PAGE_BLOCK_LAYOUTS_TAXONOMY)


@provider(IVocabularyFactory)
def MarketSegmentsVocabulary(context):
    return loadVocabularyFromPloneRegistry(MARKET_SEGMENTS_TAXONOMY)


@provider(IVocabularyFactory)
def ProductSegmentsVocabulary(context):
    return loadVocabularyFromPloneRegistry(PRODUCT_SEGMENTS_TAXONOMY)


@provider(IVocabularyFactory)
def ProductTypesVocabulary(context):
    return loadVocabularyFromPloneRegistry(PRODUCT_TYPES_TAXONOMY)


@provider(IVocabularyFactory)
def ProductMaterialsVocabulary(context):
    return loadVocabularyFromPloneRegistry(PRODUCT_MATERIALS_TAXONOMY)


@provider(IVocabularyFactory)
def ProductionTechniquesVocabulary(context):
    return loadVocabularyFromPloneRegistry(PRODUCTION_TECHNIQUES_TAXONOMY)

@provider(IVocabularyFactory)
def PhotographyTonesVocabulary(context):
    return loadVocabularyFromPloneRegistry(PHOTOGRAPHY_TONES_TAXONOMY)

@provider(IVocabularyFactory)
def ImageTreatmentVocabulary(context):
    return loadVocabularyFromPloneRegistry(IMAGE_TREATMENT_TAXONOMY)

@provider(IVocabularyFactory)
def ImageMoodDescriptorsVocabulary(context):
    return loadVocabularyFromPloneRegistry(IMAGE_MOOD_DESCRIPTORS_TAXONOMY)

@provider(IVocabularyFactory)
def IllustrationTypesVocabulary(context):
    return loadVocabularyFromPloneRegistry(ILLUSTRATION_TYPES_TAXONOMY)

@provider(IVocabularyFactory)
def ThemesVocabulary(context):
    return loadVocabularyFromStaticData(THEMES_DATA)

@provider(IVocabularyFactory)
def SiteArchetypesVocabulary(context):
    return loadVocabularyFromStaticData(SITE_ARCHETYPES_DATA)

@provider(IVocabularyFactory)
def SiteBusinessSectorsVocabulary(context):
    return loadVocabularyFromStaticData(SITE_BUSINESS_SECTORS_DATA)
