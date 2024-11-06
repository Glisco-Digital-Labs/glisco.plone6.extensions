from zope.component import adapter
from zope.interface import Interface
from plone.restapi.controlpanels import RegistryConfigletPanel

from glisco.plone6.extensions.vocabularies.interfaces import IPageSettings

@adapter(Interface, Interface)
class PageRegistryConfigletPanel(RegistryConfigletPanel):
    """Volto control panel"""

    schema = IPageSettings
    schema_prefix = "glisco.vocabularies"
    configlet_id = "glisco.vocabularies-controlpanel"
    configlet_category_id = "Products"
    title = "Vocabulary Settings"
    group = "Products"
