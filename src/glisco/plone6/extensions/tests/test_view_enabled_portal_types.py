# -*- coding: utf-8 -*-
from glisco.plone6.extensions.testing import GLISCO_PLONE6_EXTENSIONS_FUNCTIONAL_TESTING
from glisco.plone6.extensions.testing import (
    GLISCO_PLONE6_EXTENSIONS_INTEGRATION_TESTING,
)
from glisco.plone6.extensions.views.enabled_portal_types import IEnabledPortalTypes
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

    def test_enabled_portal_types_is_registered(self):
        view = getMultiAdapter(
            (self.portal["other-folder"], self.portal.REQUEST),
            name="enabled-portal-types",
        )
        self.assertTrue(IEnabledPortalTypes.providedBy(view))

    def test_enabled_portal_types_not_matching_interface(self):
        view_found = True
        try:
            view = getMultiAdapter(
                (self.portal["front-page"], self.portal.REQUEST),
                name="enabled-portal-types",
            )
        except ComponentLookupError:
            view_found = False
        else:
            view_found = IEnabledPortalTypes.providedBy(view)
        self.assertFalse(view_found)


class ViewsFunctionalTest(unittest.TestCase):

    layer = GLISCO_PLONE6_EXTENSIONS_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
