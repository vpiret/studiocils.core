# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import studiocils.core


class StudiocilsCoreLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=studiocils.core)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'studiocils.core:default')


STUDIOCILS_CORE_FIXTURE = StudiocilsCoreLayer()


STUDIOCILS_CORE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(STUDIOCILS_CORE_FIXTURE,),
    name='StudiocilsCoreLayer:IntegrationTesting',
)


STUDIOCILS_CORE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(STUDIOCILS_CORE_FIXTURE,),
    name='StudiocilsCoreLayer:FunctionalTesting',
)


STUDIOCILS_CORE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        STUDIOCILS_CORE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='StudiocilsCoreLayer:AcceptanceTesting',
)
