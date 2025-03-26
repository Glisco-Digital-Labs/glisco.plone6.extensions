# -*- coding: utf-8 -*-

from glisco.plone6.extensions import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


class IProductClassifiableMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IProductClassifiable(model.Schema):
    """ """

    product_segments = schema.List(
        title=_("label_product_segments", default="Product Segments"),
        required=False,
        missing_value="",
        value_type=schema.Choice(
            vocabulary="glisco.vocabularies.product_segments",
        ),
    )

    product_types = schema.List(
        title=_("label_product_types", default="Product types"),
        required=False,
        missing_value="",
        value_type=schema.Choice(
            vocabulary="glisco.vocabularies.product_types",
        ),
    )

    product_materials = schema.List(
        title=_("label_product_materials", default="Product materials"),
        required=False,
        missing_value="",
        value_type=schema.Choice(
            vocabulary="glisco.vocabularies.product_materials",
        ),
    )

    production_techniques = schema.List(
        title=_("label_production_techniques", default="Production Techniques"),
        required=False,
        missing_value="",
        value_type=schema.Choice(
            vocabulary="glisco.vocabularies.production_techniques",
        ),
    )


@implementer(IProductClassifiable)
@adapter(IProductClassifiableMarker)
class ProductClassifiable(object):
    def __init__(self, context):
        self.context = context

    ##################################################
    # PRODUCT SEGMENTS
    ##################################################
    @property
    def product_segments(self):
        if safe_hasattr(self.context, "product_segments"):
            return self.context.product_segments
        return None

    @product_segments.setter
    def product_segments(self, value):
        self.context.product_segments = value

    ##################################################
    # PRODUCT TYPES
    ##################################################
    @property
    def product_types(self):
        if safe_hasattr(self.context, "product_types"):
            return self.context.product_types
        return None

    @product_types.setter
    def product_types(self, value):
        self.context.product_types = value

    ##################################################
    # PRODUCT MATERIALS
    ##################################################
    @property
    def product_materials(self):
        if safe_hasattr(self.context, "product_materials"):
            return self.context.product_materials
        return None

    @product_materials.setter
    def product_materials(self, value):
        self.context.product_materials = value

    ##################################################
    # PRODUCTION TECHNIQUES
    ##################################################
    @property
    def production_techniques(self):
        if safe_hasattr(self.context, "production_techniques"):
            return self.context.production_techniques
        return None

    @production_techniques.setter
    def production_techniques(self, value):
        self.context.production_techniques = value
