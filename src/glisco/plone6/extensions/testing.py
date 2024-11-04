# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import glisco.plone6.extensions


class GliscoPlone6ExtensionsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=glisco.plone6.extensions)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "glisco.plone6.extensions:default")


GLISCO_PLONE6_EXTENSIONS_FIXTURE = GliscoPlone6ExtensionsLayer()


GLISCO_PLONE6_EXTENSIONS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GLISCO_PLONE6_EXTENSIONS_FIXTURE,),
    name="GliscoPlone6ExtensionsLayer:IntegrationTesting",
)


GLISCO_PLONE6_EXTENSIONS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GLISCO_PLONE6_EXTENSIONS_FIXTURE,),
    name="GliscoPlone6ExtensionsLayer:FunctionalTesting",
)


GLISCO_PLONE6_EXTENSIONS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        GLISCO_PLONE6_EXTENSIONS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="GliscoPlone6ExtensionsLayer:AcceptanceTesting",
)
