# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from studiocils.core.testing import STUDIOCILS_CORE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that studiocils.core is properly installed."""

    layer = STUDIOCILS_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if studiocils.core is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'studiocils.core'))

    def test_browserlayer(self):
        """Test that IStudiocilsCoreLayer is registered."""
        from studiocils.core.interfaces import (
            IStudiocilsCoreLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IStudiocilsCoreLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = STUDIOCILS_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['studiocils.core'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if studiocils.core is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'studiocils.core'))

    def test_browserlayer_removed(self):
        """Test that IStudiocilsCoreLayer is removed."""
        from studiocils.core.interfaces import \
            IStudiocilsCoreLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IStudiocilsCoreLayer,
            utils.registered_layers())
