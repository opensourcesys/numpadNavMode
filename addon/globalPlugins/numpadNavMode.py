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

# For compatibility with NVDA 2017.3 and other pre-Python 3 versions
# (Backporting is a work in progress)
#from __future__ import unicode_literals
#from globalCommands import SCRCAT_TOOLS

import globalPluginHandler
import addonHandler
import globalVars
import ui
from scriptHandler import script
from inputCore import manager	# Needed for the manager.userGestureMap object
from logHandler import log

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Constants for accessing the "columns" of the lists and tuples in the dict below
	WIN = 0		# The Windows nav command index of the lists
	NVDA = 1		# The NVDA nav command index of the lists
	MOD_AND_CLS = 0	# Index of the module.Class string of the tuples
	SCR = 1			# Index of the script string of the tuples

	# These are the gestures we care about.
	# The lists are their values in various modes of the add-on.
	# The nested tuples are the module and the script applicable to each mode.
	# gesture: [ WIN, NVDA ]
	# gesture: [ ( module, script ), ( module, script ) ]
	# Note that these are prefix-free gestures. I.E. not including the "kb:", or "kb(laptop):" portions.
	numpadGestures = {
		"numpad0": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", None ) ],
		"numpad1": [ ("globalCommands.GlobalCommands", "kb:end" ), ( "globalCommands.GlobalCommands", "review_previousCharacter" ) ],
		"nvda+numpad1": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "reviewMode_previous" ) ],
		"shift+numpad1": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "review_startOfLine" ) ],
		"control+numpad1": [ ("globalCommands.GlobalCommands", "kb:control+end" ), ( "globalCommands.GlobalCommands", None ) ],
		"numpad2": [ ("globalCommands.GlobalCommands", "kb:downarrow" ), ( "globalCommands.GlobalCommands", "review_currentCharacter" ) ],
		"nvda+numpad2": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "navigatorObject_firstChild" ) ],
		"control+numpad2": [ ("globalCommands.GlobalCommands", "kb:control+downarrow" ), ( "globalCommands.GlobalCommands", None ) ],
		"numpad3": [ ("globalCommands.GlobalCommands", "kb:pagedown" ), ( "globalCommands.GlobalCommands", "review_nextCharacter" ) ],
		"shift+numpad3": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "review_endOfLine" ) ],
		"control+numpad3": [ ("globalCommands.GlobalCommands", "kb:control+pagedown" ), ( "globalCommands.GlobalCommands", None ) ],
		"numpad4": [ ("globalCommands.GlobalCommands", "kb:leftarrow" ), ( "globalCommands.GlobalCommands", "review_previousWord" ) ],
		"nvda+numpad4": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "navigatorObject_previous" ) ],
		"control+numpad4": [ ("globalCommands.GlobalCommands", "kb:control+leftarrow" ), ( "globalCommands.GlobalCommands", None ) ],
		"numpad5": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "review_currentWord" ) ],
		"nvda+numpad5": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "navigatorObject_current" ) ],
		"numpad6": [ ("globalCommands.GlobalCommands", "kb:rightarrow" ), ( "globalCommands.GlobalCommands", "review_nextWord" ) ],
		"nvda+numpad6": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "navigatorObject_next" ) ],
		"control+numpad6": [ ("globalCommands.GlobalCommands", "kb:control+rightarrow" ), ( "globalCommands.GlobalCommands", None ) ],
		"numpad7": [ ("globalCommands.GlobalCommands", "kb:home" ), ( "globalCommands.GlobalCommands", "review_previousLine" ) ],
		"nvda+numpad7": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "reviewMode_next" ) ],
		"shift+numpad7": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "review_top" ) ],
		"control+numpad7": [ ("globalCommands.GlobalCommands", "kb:control+home" ), ( "globalCommands.GlobalCommands", None ) ],
		"numpad8": [ ("globalCommands.GlobalCommands", "kb:uparrow" ), ( "globalCommands.GlobalCommands", "review_currentLine" ) ],
		"nvda+numpad8": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "navigatorObject_parent" ) ],
		"control+numpad8": [ ("globalCommands.GlobalCommands", "kb:control+uparrow" ), ( "globalCommands.GlobalCommands", None ) ],
		"numpad9": [ ("globalCommands.GlobalCommands", "kb:pageup" ), ( "globalCommands.GlobalCommands", "review_nextLine" ) ],
		"shift+numpad9": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "review_bottom" ) ],
		"control+numpad9": [ ("globalCommands.GlobalCommands", "kb:control+pageup" ), ( "globalCommands.GlobalCommands", None ) ],
		"nvda+numpadMinus": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "navigatorObject_toFocus" ) ],
		"nvda+shift+numpadMinus": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "navigatorObject_moveFocus" ) ],
		"numpadmultiply": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "rightMouseClick" ) ],
		"nvda+numpadmultiply": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "moveNavigatorObjectToMouse" ) ],
		"shift+numpadmultiply": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "toggleRightMouseButton" ) ],
		"numpadDivide": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "leftMouseClick" ) ],
		"nvda+numpadDivide": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "moveMouseToNavigatorObject" ) ],
		"shift+numpadDivide": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "toggleLeftMouseButton" ) ],
		"nvda+numpadEnter": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "review_activate" ) ],
		"numpadPlus": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "review_sayAll" ) ],
		"nvda+numpadDelete": [ ("globalCommands.GlobalCommands", None ), ( "globalCommands.GlobalCommands", "navigatorObject_currentDimensions" ) ]
	}


	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# FixMe (feature): Warn the user that custom gestures effecting the numpad will be lost.
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
		category="keyboard",
		bypassInputHelp=True
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
		for gestureFragment in self.numpadGestures:
			manager.userGestureMap.add(
				"kb:" + gestureFragment,
				*self.numpadGestures[gestureFragment][mode][self.MOD_AND_CLS].split(sep='.'),
				self.numpadGestures[gestureFragment][mode][self.SCR],
				True
			)

		# If we made it here, we should be safe to set the mode we just configured as the mode we're in
		globalVars.numpadNavMode = mode

# FixMe: Backporting
	#script_numpadNavModeToggle.category=SCRCAT_TOOLS
	# Translators: input help message for the numpad mode toggle command
	#script_numpadNavModeToggle_doc__ = _("Toggles the numpad mode between NVDA navigation and Windows navigation")
	#__gestures = { "kb:alt+NVDA+numpadPlus" : "numpadNavModeToggle" }
