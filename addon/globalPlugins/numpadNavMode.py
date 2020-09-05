# -*- coding: utf-8 -*-
# Numpad Nav Mode (numpadNavMode.py), version 0.04-dev
# An NVDA global plugin which allows toggling the numpad between NVDA navigation and Windows navigation modes.
# Written by Luke Davis, based on gesture modifications described by NV Access (specifically @Qchristensen and @feerrenrut) in issue #9549.

#    Copyright (C) 2020 Open Source Systems, Ltd. <newanswertech@gmail.com>
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by    the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# This add-on complies with Semantic Versioning: https://semver.org/

import globalPluginHandler
import addonHandler
import globalVars
import ui
from scriptHandler import script
from inputCore import manager	# Needed for the manager.userGestureMap object
from logHandler import log
from collections import namedtuple

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Constants for accessing the "columns" of the lists and tuples in the dict below
	WIN = 0		# The Windows nav command index of the lists
	NVDA = 1		# The NVDA nav command index of the lists
	MOD_CLS = 0	# Index of the module.Class string of the tuples
	SCR = 1			# Index of the script string of the tuples

	#: Each gesture we store will have these three fields, not including the gesture itself.
	G = namedtuple('G', 'mod cls scr')

	# These are the gestures we care about.
	# The lists are their values in various modes of the add-on.
	# The nested tuples are the module and the script applicable to each mode.
	# gesture: [ WIN, NVDA ]
	# gesture: [ ( module, script ), ( module, script ) ]
	# Note that these are prefix-free gestures. I.E. not including the "kb:", or "kb(laptop):" portions.
	gMap = {
		"numpad1": [ G("globalCommands", "GlobalCommands", "kb:end"), G("globalCommands", "GlobalCommands", "review_previousCharacter") ],
		"nvda+numpad1": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "reviewMode_previous") ],
		"shift+numpad1": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "review_startOfLine") ],
		"control+numpad1": [ G("globalCommands", "GlobalCommands", "kb:control+end"), G("globalCommands", "GlobalCommands", None ) ],
		"numpad2": [ G("globalCommands", "GlobalCommands", "kb:downarrow"), G("globalCommands", "GlobalCommands", "review_currentCharacter") ],
		"nvda+numpad2": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "navigatorObject_firstChild") ],
		"control+numpad2": [ G("globalCommands", "GlobalCommands", "kb:control+downarrow"), G("globalCommands", "GlobalCommands", None ) ],
		"numpad3": [ G("globalCommands", "GlobalCommands", "kb:pagedown"), G("globalCommands", "GlobalCommands", "review_nextCharacter") ],
		"shift+numpad3": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "review_endOfLine") ],
		"control+numpad3": [ G("globalCommands", "GlobalCommands", "kb:control+pagedown"), G("globalCommands", "GlobalCommands", None ) ],
		"numpad4": [ G("globalCommands", "GlobalCommands", "kb:leftarrow"), G("globalCommands", "GlobalCommands", "review_previousWord") ],
		"nvda+numpad4": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "navigatorObject_previous") ],
		"control+numpad4": [ G("globalCommands", "GlobalCommands", "kb:control+leftarrow"), G("globalCommands", "GlobalCommands", None ) ],
		"numpad5": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "review_currentWord") ],
		"nvda+numpad5": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "navigatorObject_current") ],
		"numpad6": [ G("globalCommands", "GlobalCommands", "kb:rightarrow"), G("globalCommands", "GlobalCommands", "review_nextWord") ],
		"nvda+numpad6": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "navigatorObject_next") ],
		"control+numpad6": [ G("globalCommands", "GlobalCommands", "kb:control+rightarrow"), G("globalCommands", "GlobalCommands", None ) ],
		"numpad7": [ G("globalCommands", "GlobalCommands", "kb:home"), G("globalCommands", "GlobalCommands", "review_previousLine") ],
		"nvda+numpad7": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "reviewMode_next") ],
		"shift+numpad7": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "review_top") ],
		"control+numpad7": [ G("globalCommands", "GlobalCommands", "kb:control+home"), G("globalCommands", "GlobalCommands", None ) ],
		"numpad8": [ G("globalCommands", "GlobalCommands", "kb:uparrow"), G("globalCommands", "GlobalCommands", "review_currentLine") ],
		"nvda+numpad8": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "navigatorObject_parent") ],
		"control+numpad8": [ G("globalCommands", "GlobalCommands", "kb:control+uparrow"), G("globalCommands", "GlobalCommands", None ) ],
		"numpad9": [ G("globalCommands", "GlobalCommands", "kb:pageup"), G("globalCommands", "GlobalCommands", "review_nextLine") ],
		"shift+numpad9": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "review_bottom") ],
		"control+numpad9": [ G("globalCommands", "GlobalCommands", "kb:control+pageup"), G("globalCommands", "GlobalCommands", None ) ],
		"nvda+numpadMinus": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "navigatorObject_toFocus") ],
		"nvda+shift+numpadMinus": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "navigatorObject_moveFocus") ],
		"numpadmultiply": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "rightMouseClick") ],
		"nvda+numpadmultiply": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "moveNavigatorObjectToMouse") ],
		"shift+numpadmultiply": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "toggleRightMouseButton") ],
		"numpadDivide": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "leftMouseClick") ],
		"nvda+numpadDivide": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "moveMouseToNavigatorObject") ],
		"shift+numpadDivide": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "toggleLeftMouseButton") ],
		"nvda+numpadEnter": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "review_activate") ],
		"numpadPlus": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "review_sayAll") ],
		"nvda+numpadDelete": [ G("globalCommands", "GlobalCommands", None ), G("globalCommands", "GlobalCommands", "navigatorObject_currentDimensions") ]
	}


	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# FixMe (feature): Determine if gestures are set to anything non-default, and save them/warn the user.
		# Initialize the startup mode, or log it if we're already in one (I.E. a plugin reload)
		try:
			log.debug("Numpad mode already set to {0}.".format(self.getModeText()))
		except AttributeError:	# Raised if this is the first run
			self.setMode(self.NVDA)
			log.debug("numpadNavMode: initialized numpad to {0} mode.".format(self.getModeText()))

	def terminate(self):
		#self.setMode(self.NVDA)
		pass


	def getModeText(self):
		"""Returns a text string representing the current mode of the numpad.
		Warning: Does nothing to make sure that the returned mode is actually the configuration of the numpad!
		Relies on getMode() to throw an exception if the mode is unrecognized
		"""
		if self.getMode() is self.NVDA:
			return "NVDA"
		else:
			return "Windows"


	def getMode(self):
		"""Returns the mode of the numpad as understood by the global variable.
		Throws an exception if the mode is unrecognized.
		Warning: Does nothing to make sure that the returned mode is actually the configuration of the numpad!
		"""
		try:
			if globalVars.numpadNavMode is self.NVDA:
				return self.NVDA
			elif globalVars.numpadNavMode is self.WIN:
				return self.WIN
			else:
				raise AttributeError
		except AttributeError:	# Raised above, or if the global isn't set at all
			raise AttributeError("Unknown numpad state or state was never set")


	@script(
		gesture="kb:alt+NVDA+numpadPlus",
		# Translators: description of the toggle gesture for keyboard help
		description=_("Toggles the numpad between NVDA navigation and Windows navigation modes."),
		category="keyboard"
	)
	def script_numpadNavModeToggle(self, gesture):
		"""Checks the current mode of the numpad, and switches to the opposite one
		"""
		if self.getMode() is self.NVDA:
			self.setMode(self.WIN)
		else:	# Mode is Windows
			self.setMode(self.NVDA)

		ui.message("Numpad mode {0}.".format(self.getModeText()))
		log.debug("Numpad set to {0} nav mode.".format(self.getModeText()))


	def setMode(self, mode):
		"""Iterates the dict of gestures we know about, and sets them to the values for the provided mode.
		It overrides any existing settings for those gestures.
		The values associated with the mode are taken from the hard-coded dict ov gesture mappings included in the add-on.
		The dict will provide None values for some of them, which the manager scripts already know means to unset them completely.
		@param mode: the mode we want the numpad to switch into. This should be provided with the constants self.NVDA or self.WIN.
		@type mode: int
		"""
		# Check the validity of the mode we were given
		if not mode is self.NVDA and not mode is self.WIN:
			raise ValueError("Can not set numpad mode to unknown value '{0}'.".format(mode))

		# Walk the dict of known gestures, and assign each based on the preferred mode
		for gestureFragment, action in self.gMap.items():
			manager.userGestureMap.add(
				"kb:" + gestureFragment,
				action[mode].mod,
				action[mode].cls,
				action[mode].scr,
				True
			)

		# If we made it here, we should be safe to set the mode we just configured as the mode we're in
		globalVars.numpadNavMode = mode
