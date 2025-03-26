# -*- coding: utf-8 -*-
from glisco.plone6.extensions.testing import GLISCO_PLONE6_EXTENSIONS_FUNCTIONAL_TESTING
from glisco.plone6.extensions.testing import (
    GLISCO_PLONE6_EXTENSIONS_INTEGRATION_TESTING,
)
from glisco.plone6.extensions.views.css_view import ICssView
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from zope.component import getMultiAdapter
from zope.interface.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = GLISCO_PLONE6_EXTENSIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        api.content.create(self.portal, "Folder", "other-folder")
        api.content.create(self.portal, "Document", "front-page")

    def test_site_css_bundle_is_registered(self):
        view = getMultiAdapter(
            (self.portal["other-folder"], self.portal.REQUEST), name="site-css-bundle"
        )
        self.assertTrue(ICssView.providedBy(view))

    def test_site_css_bundle_not_matching_interface(self):
        view_found = True
        try:
            view = getMultiAdapter(
                (self.portal["front-page"], self.portal.REQUEST), name="site-css-bundle"
            )
        except ComponentLookupError:
            view_found = False
        else:
            view_found = ICssView.providedBy(view)
        self.assertFalse(view_found)


class ViewsFunctionalTest(unittest.TestCase):

    layer = GLISCO_PLONE6_EXTENSIONS_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
