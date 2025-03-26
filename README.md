# Glisco Plone 6 Extensions 

Platform extensions to standard Plone 6, so that we can build the types of CMS-based sites 
we want. 

This contains extended functionality such as:

- New Content Types, for example: Adaptive Image
- Vocabularies, used for multi-vector navigation 
- Behaviours 


## How this package was setup 

I ran the following to create this package

```sh
plonecli create addon glisco.plone6.extensions
```

and got this output:

```pre
RUN: bobtemplates.plone:addon -O glisco.plone6.extensions

Welcome to mr.bob interactive mode. Before we generate directory structure, some questions need to be answered.

Answer with a question mark to display help.
Values in square brackets at the end of the questions show the default value if there is no answer.


--> Author's name [Joe Medicis]: 

--> Author's email [joe.medicis@gmail.com]: joe@glisco.io

--> Author's GitHub username: joemedicis

--> Package description [An add-on for Plone]: Glisco Plone 6 Extensions

--> Do you want me to initialize a GIT repository in your new package? (y/n) [y]: n

--> Plone version [6.0.0]: 

--> Python version for virtualenv [python3]: 

--> Do you want me to activate VS Code support? (y/n) [y]: 



isort-apply: successful:
isort-apply: install_deps> python -I -m pip install isort -c constraints.txt
isort-apply: commands[0]> isort /Users/joemedicis/Development/glisco/platform/plone6/glisco.plone6.extensions/glisco.plone6.extensions/src /Users/joemedicis/Development/glisco/platform/plone6/glisco.plone6.extensions/glisco.plone6.extensions/setup.py
Fixing /Users/joemedicis/Development/glisco/platform/plone6/glisco.plone6.extensions/glisco.plone6.extensions/src/glisco/plone6/extensions/testing.py
Fixing /Users/joemedicis/Development/glisco/platform/plone6/glisco.plone6.extensions/glisco.plone6.extensions/src/glisco/plone6/extensions/tests/test_setup.py
Fixing /Users/joemedicis/Development/glisco/platform/plone6/glisco.plone6.extensions/glisco.plone6.extensions/src/glisco/plone6/extensions/tests/test_robot.py
  isort-apply: OK (3.54=setup[2.87]+cmd[0.67] seconds)
  congratulations :) (3.70 seconds)



Identified `/` as project root containing a file system root.
Sources to be formatted: "Users/joemedicis/Development/glisco/platform/plone6/glisco.plone6.extensions/glisco.plone6.extensions/src", "Users/joemedicis/Development/glisco/platform/plone6/glisco.plone6.extensions/glisco.plone6.extensions/setup.py"
src/glisco/__init__.py already well formatted, good job.
src/glisco/plone6/__init__.py already well formatted, good job.
src/glisco/plone6/extensions/browser/__init__.py already well formatted, good job.
src/glisco/plone6/extensions/interfaces.py already well formatted, good job.
src/glisco/plone6/extensions/locales/__init__.py already well formatted, good job.
reformatted src/glisco/plone6/extensions/__init__.py
reformatted src/glisco/plone6/extensions/setuphandlers.py
src/glisco/plone6/extensions/tests/__init__.py already well formatted, good job.
reformatted src/glisco/plone6/extensions/tests/test_robot.py
reformatted setup.py
reformatted src/glisco/plone6/extensions/testing.py
reformatted src/glisco/plone6/extensions/locales/update.py
reformatted src/glisco/plone6/extensions/tests/test_setup.py

All done! ✨ 🍰 ✨
7 files reformatted, 6 files left unchanged.

black-enforce: successful:
black-enforce: install_deps> python -I -m pip install black -c constraints.txt
black-enforce: commands[0]> black -v src setup.py
  black-enforce: OK (12.91=setup[2.86]+cmd[10.04] seconds)
  congratulations :) (12.99 seconds)


git init is disabled!
Generated file structure at /Users/joemedicis/Development/glisco/platform/plone6/glisco.plone6.extensions/glisco.plone6.extensions
```

## Adding a vocabulary

Using the same [plonecli docs][plonecli] as guide, we went on to do:

```sh
plonecli add vocabulary
```

We just followed the prompts to create a PageLayoutTypes taxonomy, 
and the necessary ZCML and Python config was added, with placeholder code.

[plonecli]: https://pypi.org/project/plonecli/