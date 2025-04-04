# -*- coding: utf-8 -*-
from glisco.plone6.extensions.behaviors.market import IMarketAddressableMarker
from glisco.plone6.extensions.testing import (
    GLISCO_PLONE6_EXTENSIONS_INTEGRATION_TESTING,
)
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class PageTypeIntegrationTest(unittest.TestCase):

    layer = GLISCO_PLONE6_EXTENSIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_behavior_page_type(self):
        behavior = getUtility(
            IBehavior, "glisco.plone6.extensions.behaviours.market_addressable"
        )
        self.assertEqual(
            behavior.marker,
            IMarketAddressableMarker,
        )
