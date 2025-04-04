from glisco.plone6.extensions.vocabularies.interfaces import IDesignSettings
from glisco.plone6.extensions.vocabularies.interfaces import IMarketSettings
from glisco.plone6.extensions.vocabularies.interfaces import IPageSettings
from glisco.plone6.extensions.vocabularies.interfaces import IProductSettings
from glisco.plone6.extensions.vocabularies.interfaces import IContentTypeSettings
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from zope.interface import Interface


@adapter(Interface, Interface)
class PageRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IPageSettings
    schema_prefix = "glisco.extensions.settings.pages"
    configlet_id = "glisco.page-controlpanel"
    configlet_category_id = "Products"
    title = "Vocabulary Settings"
    group = "Glisco Configurations"


@adapter(Interface, Interface)
class MarketRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IMarketSettings
    schema_prefix = "glisco.extensions.settings.markets"
    configlet_id = "glisco.market-controlpanel"
    configlet_category_id = "Products"
    title = "Market Settings"
    group = "Glisco Configurations"


@adapter(Interface, Interface)
class ProductRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IProductSettings
    schema_prefix = "glisco.extensions.settings.products"
    configlet_id = "glisco.products-controlpanel"
    configlet_category_id = "Products"
    title = "Products Settings"
    group = "Glisco Configurations"


@adapter(Interface, Interface)
class DesignRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IDesignSettings
    schema_prefix = "glisco.extensions.settings.design"
    configlet_id = "glisco.design-controlpanel"
    configlet_category_id = "Products"
    title = "Design Settings"
    group = "Glisco Configurations"

@adapter(Interface, Interface)
class ContentTypesRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IContentTypeSettings
    schema_prefix = "glisco.extensions.settings.contenttypes"
    configlet_id = "glisco.content-controlpanel"
    configlet_category_id = "Products"
    title = "Content Type Settings"
    group = "Glisco Configurations"

