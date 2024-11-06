from plone import schema
from plone.autoform import directives
from zope.interface import Interface

from glisco.plone6.extensions.vocabularies.constants import VOCABULARY_SCHEMA, TYPE_OF_PAGE_TAXONOMY

# This code is based on the Plone 6 training section on 
# Vocabularies, Registry-Settings and Control Panels, whicj is here:
# https://training.plone.org/mastering-plone/registry.html


class IExampleAddonControlPanel(Interface):
   """Define settings for IExampleAddonControlPanel"""

   textline_field = schema.TextLine(
       title='Textline field',
       description='A simple input field',
       required=False,
   )
   
class IPageSettings(Interface):
    talk_submission_open = schema.Bool(
        title="Allow talk submission",
        description="Allow the submission of talks for anonymous user",
        default=False,
        required=False,
    )

    types_of_page = schema.JSONField(
        title="Types of Page",
        description="Available types of a page",
        required=False,
        schema=VOCABULARY_SCHEMA,
        default={
            "items": [
                {
                    "token": TYPE_OF_PAGE_TAXONOMY + ".home",
                    "titles": {
                        "en": "Home Page",
                        "pt": "Home Page",
                    },
                },

                {
                    "token": TYPE_OF_PAGE_TAXONOMY + ".section",
                    "titles": {
                        "en": "Section Page",
                        "pt": "Section Page",
                    },
                },

                {
                    "token": TYPE_OF_PAGE_TAXONOMY + ".product",
                    "titles": {
                        "en": "Product/Service Page",
                        "pt": "Product/Service Page",
                    },
                },

                {
                    "token": TYPE_OF_PAGE_TAXONOMY + ".adlanding",
                    "titles": {
                        "en": "Ad Landing Page",
                        "pt": "Ad Landing Page",
                    },
                },
                
            ]
        },
        missing_value={"items": []},
    )
    directives.widget(
        "types_of_page",
        frontendOptions={
            "widget": "vocabularyterms",
        },
    )

    # audiences = schema.JSONField(
    #     title="Audience",
    #     description="Available audiences of a talk",
    #     required=False,
    #     schema=VOCABULARY_SCHEMA,
    #     default={
    #         "items": [
    #             {
    #                 "token": "beginner",
    #                 "titles": {
    #                     "en": "Beginner",
    #                     "de": "Anfänger",
    #                 },
    #             },
    #             {
    #                 "token": "advanced",
    #                 "titles": {
    #                     "en": "Advanced",
    #                     "de": "Fortgeschrittene",
    #                 },
    #             },
    #             {
    #                 "token": "professional",
    #                 "titles": {
    #                     "en": "Professional",
    #                     "de": "Profi",
    #                 },
    #             },
    #         ]
    #     },
    #     missing_value={"items": []},
    # )
    # directives.widget(
    #     "audiences",
    #     frontendOptions={
    #         "widget": "vocabularyterms",
    #     },
    # )

    # rooms = schema.JSONField(
    #     title="Rooms",
    #     description="Available rooms of the conference",
    #     required=False,
    #     schema=VOCABULARY_SCHEMA,
    #     default={
    #         "items": [
    #             {
    #                 "token": "101",
    #                 "titles": {
    #                     "en": "101",
    #                     "de": "101",
    #                 },
    #             },
    #             {
    #                 "token": "201",
    #                 "titles": {
    #                     "en": "201",
    #                     "de": "201",
    #                 },
    #             },
    #             {
    #                 "token": "auditorium",
    #                 "titles": {
    #                     "en": "Auditorium",
    #                     "de": "Auditorium",
    #                 },
    #             },
    #         ]
    #     },
    #     missing_value={"items": []},
    # )
    # directives.widget(
    #     "rooms",
    #     frontendOptions={
    #         "widget": "vocabularyterms",
    #     },
    # )
