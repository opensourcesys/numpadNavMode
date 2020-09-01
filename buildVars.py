# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x: x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guidelines.txt
	# add-on Name, internal for nvda
	"addon_name": "numpadNavMode",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary": _("Numpad Nav Mode"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description": _("""Allows switching the numpad between NVDA navigation mode, and Windows navigation mode.
This can be especially useful for laptop users who prefer laptop mode, but who have a numpad and want to use it for arrow keys, page up/down, and home/end.
And since the mode can be changed with a keypress (Alt+NVDA+NumpadPlus, by default), the numpad can easily be used for object navigation or review when desired.
I welcome feature requests and other use-case examples."""),
	# version
	"addon_version": "0.3-dev",
	# Author(s)
	"addon_author": u"Luke Davis (Open Source Systems, Ltd.) <newanswertech@gmail.com>",
	# URL for the add-on documentation support
	"addon_url": None,
	# Documentation file name
	"addon_docFileName": "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
	"addon_minimumNVDAVersion": "2019.3",
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion": "2020.3",
	# Add-on update channel (default is None, denoting stable releases, and for development releases, use "dev"; do not change unless you know what you are doing)
	"addon_updateChannel": "dev",
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "*.py"),
os.path.join("addon", "globalPlugins", "*.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
