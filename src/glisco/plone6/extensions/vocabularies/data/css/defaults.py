# ###########################################################################
#
# CSS DEFAULTS
#
# Description: Default CSS files for the CSS Vocabulary
#
# The CSS Data is a set of CSS files that are used to style the site.
# To start with we just provide a basic documentation header for each file
# leaving the actual content to be filled in by the site admin.
#
# ###########################################################################

VARIABLES_CSS = """
/* 
  variables.css
  --------------
  Design token definitions for your color system, spacing, typography, and themes.

  Includes:
  - OKLCH color variables (e.g. --blue-50, --gray-900)
  - Light/Dark mode overrides via :root and [data-theme]
  - Global tokens for sizing, font stacks, etc.

  Used throughout Tailwind config and custom CSS.
*/

"""

BASE_CSS = """
/* 
  base.css
  --------
  Global base styles and reset layer.

  Includes:
  - Normalize styles, scroll behavior
  - Global typography and background defaults

  Import this early to establish baseline styling.
*/

"""

COMPONENTS_CSS = """
/* 
  components.css
  ---------------
  Reusable, design-tokenized UI components.

  Includes:
  - Buttons, cards, alerts, modals
  - Layout-ready class patterns
  - Styles tied to CSS variables for easy theming

  Extend this file with custom design system elements.
*/

"""


ANIMATIONS_CSS = """
/* 
  animations.css
  ---------------
  Keyframes and animation-related utility classes.

  Includes:
  - Reusable @keyframes blocks
  - Animation/transition classes (e.g. .fade-in, .slide-up)
  - Timing/easing helpers for motion design

  Keeps animation logic clean and separate from layout/components.
*/

"""

UTILITIES_CSS = """
/* 
  utilities.css
  ---------------
  Project-specific utility classes that complement Tailwind.

  Includes:
  - Accessibility helpers (e.g. .visually-hidden)
  - Custom spacing/grid/flex tweaks
  - Overflow, z-index, and shadow helpers

  Add here what doesn't make sense as a component or Tailwind plugin.
*/

"""

CSS_DATA = {
    "variables": VARIABLES_CSS,
    "base": BASE_CSS,
    "components": COMPONENTS_CSS,
    "animations": ANIMATIONS_CSS,
    "utilities": UTILITIES_CSS
}
