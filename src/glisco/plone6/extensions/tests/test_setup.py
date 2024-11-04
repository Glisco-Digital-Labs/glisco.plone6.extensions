# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from glisco.plone6.extensions.testing import (  # noqa: E501
    GLISCO_PLONE6_EXTENSIONS_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that glisco.plone6.extensions is properly installed."""

    layer = GLISCO_PLONE6_EXTENSIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if glisco.plone6.extensions is installed."""
        self.assertTrue(self.installer.is_product_installed("glisco.plone6.extensions"))

    def test_browserlayer(self):
        """Test that IGliscoPlone6ExtensionsLayer is registered."""
        from glisco.plone6.extensions.interfaces import IGliscoPlone6ExtensionsLayer
        from plone.browserlayer import utils

        self.assertIn(IGliscoPlone6ExtensionsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = GLISCO_PLONE6_EXTENSIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("glisco.plone6.extensions")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if glisco.plone6.extensions is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("glisco.plone6.extensions")
        )

    def test_browserlayer_removed(self):
        """Test that IGliscoPlone6ExtensionsLayer is removed."""
        from glisco.plone6.extensions.interfaces import IGliscoPlone6ExtensionsLayer
        from plone.browserlayer import utils

        self.assertNotIn(IGliscoPlone6ExtensionsLayer, utils.registered_layers())
