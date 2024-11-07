# -*- coding: utf-8 -*-

from glisco.plone6.extensions import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IMarketAddressableMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IMarketAddressable(model.Schema):
    """
    """

    market_segments = schema.List(
        title = _(u'label_market_segment', default=u'Market Segment'),
        required = False,
        missing_value = '',
        value_type = schema.Choice(
            vocabulary = 'glisco.vocabularies.market_segments',
        )
    )

    # market_segments = schema.Choice(
    #     title="Market Segment",
    #     vocabulary="glisco.vocabularies.market_segments",
    #     required=True,
    # )


@implementer(IMarketAddressable)
@adapter(IMarketAddressableMarker)
class MarketAddressable(object):
    def __init__(self, context):
        self.context = context

    @property
    def market_segments(self):
        if safe_hasattr(self.context, 'market_segments'):
            return self.context.market_segments
        return None

    @market_segments.setter
    def market_segments(self, value):
        self.context.market_segments = value
