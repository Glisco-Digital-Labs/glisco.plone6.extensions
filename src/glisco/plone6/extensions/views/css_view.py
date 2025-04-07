# -*- coding: utf-8 -*-

from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


class ICssView(Interface):
    """Marker Interface for ICssView"""


@implementer(ICssView)
class CssView(BrowserView):
    def bundle(self):
        prefix = "glisco.extensions.settings.design"
        fields = ["variables", "base", "components", "animations", "utilities"]
        bundle = """
        /* ************************************************************************
          bundle.css
          --------
          Site's bundled css.

          Includes "variables", "base", "components", "animations", "utilities"

        ************************************************************************ */

        """
        for field in fields:
            try:
                reg_record = api.portal.get_registry_record(f"{prefix}.{field}")
                bundle += reg_record
                bundle += "\n\n"
            except:
                bundle += """
              /* ************************************************************************
                {field}.css ERROR
                ---------------
                Could not load {field}.css
              ************************************************************************ */

              """.format(
                    field=field
                )
                bundle += "\n\n"
        return bundle

    def __call__(self):
        return self.bundle()
