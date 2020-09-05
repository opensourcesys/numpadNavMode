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

	#: Used to indicate a return status of getMode(), and therefore to track state in various places.
	WIN = 0
	#: Used to indicate a return status of getMode(), and therefore to track state in various places.
	NVDA = 1

	#: Each gesture we store will have these three fields, not including the gesture itself.
	G = namedtuple('G', 'mod cls scr')

	#: A dict of user assigned gestures, containing their values in G form
	userGestures = {}

	#: These are the gestures we override to make the numpad perform Windows nav.
	#: The G objects are namedtuples holding the module, class, and the script applicable to each gesture.
	#: Note that these are prefix-free gestures. I.E. not including the "kb:", or "kb(laptop):" portions.
	numpadGestures = {
		"numpad1": G("globalCommands", "GlobalCommands", "kb:end"),
		"nvda+numpad1": G("globalCommands", "GlobalCommands", None ),
		"shift+numpad1": G("globalCommands", "GlobalCommands", None ),
		"control+numpad1": G("globalCommands", "GlobalCommands", "kb:control+end"),
		"numpad2": G("globalCommands", "GlobalCommands", "kb:downarrow"),
		"nvda+numpad2": G("globalCommands", "GlobalCommands", None ),
		"control+numpad2": G("globalCommands", "GlobalCommands", "kb:control+downarrow"),
		"numpad3": G("globalCommands", "GlobalCommands", "kb:pagedown"),
		"shift+numpad3": G("globalCommands", "GlobalCommands", None ),
		"control+numpad3": G("globalCommands", "GlobalCommands", "kb:control+pagedown"),
		"numpad4": G("globalCommands", "GlobalCommands", "kb:leftarrow"),
		"nvda+numpad4": G("globalCommands", "GlobalCommands", None ),
		"control+numpad4": G("globalCommands", "GlobalCommands", "kb:control+leftarrow"),
		"numpad5": G("globalCommands", "GlobalCommands", None ),
		"nvda+numpad5": G("globalCommands", "GlobalCommands", None ),
		"numpad6": G("globalCommands", "GlobalCommands", "kb:rightarrow"),
		"nvda+numpad6": G("globalCommands", "GlobalCommands", None ),
		"control+numpad6": G("globalCommands", "GlobalCommands", "kb:control+rightarrow"),
		"numpad7": G("globalCommands", "GlobalCommands", "kb:home"),
		"nvda+numpad7": G("globalCommands", "GlobalCommands", None ),
		"shift+numpad7": G("globalCommands", "GlobalCommands", None ),
		"control+numpad7": G("globalCommands", "GlobalCommands", "kb:control+home"),
		"numpad8": G("globalCommands", "GlobalCommands", "kb:uparrow"),
		"nvda+numpad8": G("globalCommands", "GlobalCommands", None ),
		"control+numpad8": G("globalCommands", "GlobalCommands", "kb:control+uparrow"),
		"numpad9": G("globalCommands", "GlobalCommands", "kb:pageup"),
		"shift+numpad9": G("globalCommands", "GlobalCommands", None ),
		"control+numpad9": G("globalCommands", "GlobalCommands", "kb:control+pageup"),
		"nvda+numpadMinus": G("globalCommands", "GlobalCommands", None ),
		"nvda+shift+numpadMinus": G("globalCommands", "GlobalCommands", None ),
		"numpadmultiply": G("globalCommands", "GlobalCommands", None ),
		"nvda+numpadmultiply": G("globalCommands", "GlobalCommands", None ),
		"shift+numpadmultiply": G("globalCommands", "GlobalCommands", None ),
		"numpadDivide": G("globalCommands", "GlobalCommands", None ),
		"nvda+numpadDivide": G("globalCommands", "GlobalCommands", None ),
		"shift+numpadDivide": G("globalCommands", "GlobalCommands", None ),
		"nvda+numpadEnter": G("globalCommands", "GlobalCommands", None ),
		"numpadPlus": G("globalCommands", "GlobalCommands", None ),
		"nvda+numpadDelete": G("globalCommands", "GlobalCommands", None )
	}


	def __init__(self):
		super(GlobalPlugin, self).__init__()
		# Initialize the startup mode, or log it if we're already in one (I.E. a plugin reload)
		try:
			log.debug("Numpad mode already set to {0}.".format(self.getModeText()))
		except AttributeError:	# Raised if this is the first run
			self.setMode(self.NVDA)
			log.debug("numpadNavMode: initialized numpad to {0} mode.".format(self.getModeText()))


	def terminate(self):
		#self.setMode(self.NVDA)
		pass


	def getModeText(self) -> str:
		"""Returns a text string representing the current mode of the numpad.
		Warning: Does nothing to make sure that the returned mode is actually the configuration of the numpad!
		Relies on getMode() to throw an exception if the mode is unrecognized
		"""
		if self.getMode() == self.NVDA:
			return "NVDA"
		else:
			return "Windows"


	def getMode(self) -> int:
		"""Returns the mode of the numpad as understood by the global variable.
		Throws an exception if the mode is unrecognized.
		Warning: Does nothing to make sure that the returned mode is actually the configuration of the numpad!
		"""
		try:
			if globalVars.numpadNavMode == self.NVDA:
				return self.NVDA
			elif globalVars.numpadNavMode == self.WIN:
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
	def script_toggleNumpadNavMode(self, gesture):
		"""Checks the current mode of the numpad, and switches to the opposite one
		"""
		if self.getMode() == self.NVDA:
			self.setMode(self.WIN)
		else:	# Mode is Windows
			self.setMode(self.NVDA)

		ui.message("Numpad mode {0}.".format(self.getModeText()))
		log.debug("Numpad set to {0} nav mode.".format(self.getModeText()))


	@classmethod
	def _getAllGesturesAsGDict(cls) -> dict:
		"""Returns a dict of all currently configured user gestures, using G objects.
		"""
		return {
			gest : cls.G(mc.__module__, mc.__name__, scr)
			for mc, gest, scr in manager.userGestureMap.getScriptsForAllGestures()
		}


	def setMode(self, mode : int):
		"""Iterates the dict of gestures we know about, and sets them to the values for the provided mode.
		It overrides any existing settings for those gestures.
		The values associated with the mode are taken from the hard-coded dict ov gesture mappings included in the add-on.
		The dict will provide None values for some of them, which the manager scripts already know means to unset them completely.
		@param mode: the mode we want the numpad to switch into. This should be provided with the constants self.NVDA or self.WIN.
		@type mode: int
		"""
		# if we're switching to Windows mode
		if mode == self.WIN:
			# Acquire all configured userGestures
			self.userGestures = self._getAllGesturesAsDict()
			# Assign the Windows emmulations
			for gFrag, action in self.numpadGestures.items():
				# We only want to use the main gesture, not desktop or laptop
				manager.userGestureMap.add("kb(desktop):" + str(gFrag), action.mod, action.cls, None, True)
				manager.userGestureMap.add("kb(laptop):" + str(gFrag), action.mod, action.cls, None, True)
				manager.userGestureMap.add("kb:" + str(gFrag), action.mod, action.cls, action.scr, True)

		# if we're switching to NVDA mode
		elif mode == self.NVDA:
			# Overview: for each numpad gesture, check whether:
			# - There is a script for it; and
			# - Whether it is our script, which will be an emmulated gesture or None.
			# If so, remove it. If not (meaning it has been reassigned) leave it alone.
			# Do the same for laptop and desktop versions of the gestures, which should all be None.
			checkThese = {}	#: Mungible dict of gestures we use
			# Build the checkables
			for gFrag, action in self.numpadGestures.items():
				checkThese.append("kb:" + str(gFrag), action)
				# For these, we know that the script should be None
				checkThese.append("kb(desktop):" + str(gFrag), self.G(action.mod, action.cls, None))
				checkThese.append("kb(laptop):" + str(gFrag), self.G(action.mod, action.cls, None))
			# For each user gesture, check:
			# - Whether it is one of ours, or a layout-varient version of one of ours, and
			# - if so, whether it is set as we set it (meaning it hasn't been remapped):
			# then we can delete it.
			for gest, action in self._getAllGesturesAsGDict():
				try:
					# If it matches, we delete the gesture.
					# We skip it if it doesn't match, or if there's a KeyError.
					if checkThese[gest] == action:
						manager.userGestureMap.remove(gest, *action)
						del checkThese[gest]
				except KeyError:
					pass
			# For our next trick: we need to check whether all former user gestures got reset

		else:	# An invalid mode was provided
			raise ValueError("Can not set numpad mode to unknown value '{0}'.".format(mode))

		# If we made it here, we should be safe to set the mode we just configured as the mode we're in
		globalVars.numpadNavMode = mode
