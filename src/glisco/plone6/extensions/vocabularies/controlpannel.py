from zope.component import adapter
from zope.interface import Interface
from plone.restapi.controlpanels import RegistryConfigletPanel

from glisco.plone6.extensions.vocabularies.interfaces import IPageSettings, IMarketSettings

@adapter(Interface, Interface)
class PageRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IPageSettings
    schema_prefix = "glisco.vocabularies"
    configlet_id = "glisco.page-controlpanel"
    configlet_category_id = "Products"
    title = "Vocabulary Settings"
    group = "Products"

@adapter(Interface, Interface)
class MarketRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IMarketSettings
    schema_prefix = "glisco.market"
    configlet_id = "glisco.market-controlpanel"
    configlet_category_id = "Products"
    title = "Market Settings"
    group = "Products"
