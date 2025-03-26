from zope.component import adapter
from zope.interface import Interface
from plone.restapi.controlpanels import RegistryConfigletPanel

from glisco.plone6.extensions.vocabularies.interfaces import IPageSettings, IMarketSettings, IProductSettings, IDesignSettings

@adapter(Interface, Interface)
class PageRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IPageSettings
    schema_prefix = "glisco.extensions.settings.pages"
    configlet_id = "glisco.page-controlpanel"
    configlet_category_id = "Products"
    title = "Vocabulary Settings"
    group = "Products"

@adapter(Interface, Interface)
class MarketRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IMarketSettings
    schema_prefix = "glisco.extensions.settings.markets"
    configlet_id = "glisco.market-controlpanel"
    configlet_category_id = "Products"
    title = "Market Settings"
    group = "Products"

@adapter(Interface, Interface)
class ProductRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IProductSettings
    schema_prefix = "glisco.extensions.settings.products"
    configlet_id = "glisco.products-controlpanel"
    configlet_category_id = "Products"
    title = "Products Settings"
    group = "Products"

@adapter(Interface, Interface)
class DesignRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IDesignSettings
    schema_prefix = "glisco.extensions.settings.design"
    configlet_id = "glisco.design-controlpanel"
    configlet_category_id = "Design"
    title = "Design Settings"
    group = "Products"
