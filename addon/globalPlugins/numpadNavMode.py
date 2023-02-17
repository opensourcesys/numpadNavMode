# Numpad Nav Mode (numpadNavMode.py), version 2.0
# An NVDA global plugin which allows toggling the numpad between NVDA navigation and Windows navigation modes.
# Written by Luke Davis, based on gesture modifications described by NV Access (specifically @Qchristensen and @feerrenrut) in issue #9549.
#    Copyright (C) 2020-2023 Luke Davis and Open Source Systems, Ltd. <XLTechie@newanswertech.com>
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by    the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import types
from collections import namedtuple
import wx

import gui
import globalVars
import config
import addonHandler
import globalPluginHandler
import ui
from inputCore import manager, normalizeGestureIdentifier
from logHandler import log
from scriptHandler import script

addonHandler.initTranslation()

#: numpadNavMode Add-on config database
config.conf.spec["numpadNavMode"] = {
	"startInWindowsMode": "boolean(default=False)",
}

class NumpadNavModeSettings (gui.settingsDialogs.SettingsPanel):
	"""NVDA configuration panel based configurator  for numpadNavMode."""

	# Translators: This is the label for the Numpad Nav Mode settings category in NVDA Settings panel.
	title = _("Numpad Nav Mode")

	def makeSettings(self, settingsSizer):
		"""Creates a settings panel."""
		helper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self.startInWindowsModeCB = helper.addItem(
			wx.CheckBox(
				self,
				# Translators: The label for a checkbox in Numpad Nav Mode settings panel
				label=_("Start NVDA with the numpad set to Windows nav mode")
			)
		)
		self.startInWindowsModeCB.SetValue(config.conf["numpadNavMode"]["startInWindowsMode"])

	def onSave(self):
		config.conf["numpadNavMode"]["startInWindowsMode"] = self.startInWindowsModeCB.Value


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	"""Class providing the Numpad Nav Mode add-on global plugin."""

	#: Used to indicate a value of the mode property, and therefore to track state in various places.
	WIN = 0
	#: Used to indicate a value of the mode property, and therefore to track state in various places.
	NVDA = 1

	#: Each gesture we manipulate will have these three fields, not including the gesture itself.
	G = namedtuple('G', 'mod cls scr')

	#: These are the gestures we override to make the numpad perform Windows nav.
	#: The G objects are namedtuples holding the module, class, and the script applicable to each gesture.
	#: Note that these are prefix-free gestures. E.G. not including the "kb:", or "kb(laptop):" portions.
	numpadGestures = {
		"numpad1": G("globalCommands", "GlobalCommands", "kb:end"),
		"nvda+numpad1": G("globalCommands", "GlobalCommands", "kb:nvda+end" ),
		"shift+numpad1": G("globalCommands", "GlobalCommands", "kb:shift+end" ),
		"control+numpad1": G("globalCommands", "GlobalCommands", "kb:control+end"),
		"shift+control+numpad1": G("globalCommands", "GlobalCommands", "kb:shift+control+end"),
		"numpad2": G("globalCommands", "GlobalCommands", "kb:downarrow"),
		"shift+numpad2": G("globalCommands", "GlobalCommands", "kb:shift+downarrow"),
		"nvda+numpad2": G("globalCommands", "GlobalCommands", "kb:nvda+downarrow" ),
		"control+numpad2": G("globalCommands", "GlobalCommands", "kb:control+downarrow"),
		"shift+control+numpad2": G("globalCommands", "GlobalCommands", "kb:shift+control+downarrow"),
		"numpad3": G("globalCommands", "GlobalCommands", "kb:pagedown"),
		"nvda+numpad3": G("globalCommands", "GlobalCommands", "kb:nvda+pagedown"),
		"shift+numpad3": G("globalCommands", "GlobalCommands", "kb:shift+pagedown" ),
		"control+numpad3": G("globalCommands", "GlobalCommands", "kb:control+pagedown"),
		"shift+control+numpad3": G("globalCommands", "GlobalCommands", "kb:shift+control+pagedown"),
		"numpad4": G("globalCommands", "GlobalCommands", "kb:leftarrow"),
		"shift+numpad4": G("globalCommands", "GlobalCommands", "kb:shift+leftarrow"),
		"nvda+numpad4": G("globalCommands", "GlobalCommands", "kb:nvda+leftarrow" ),
		"control+numpad4": G("globalCommands", "GlobalCommands", "kb:control+leftarrow"),
		"shift+control+numpad4": G("globalCommands", "GlobalCommands", "kb:shift+control+leftarrow"),
		"numpad5": G("globalCommands", "GlobalCommands", None ),
		"nvda+numpad5": G("globalCommands", "GlobalCommands", None ),
		"numpad6": G("globalCommands", "GlobalCommands", "kb:rightarrow"),
		"shift+numpad6": G("globalCommands", "GlobalCommands", "kb:shift+rightarrow"),
		"nvda+numpad6": G("globalCommands", "GlobalCommands", "kb:nvda+rightarrow" ),
		"control+numpad6": G("globalCommands", "GlobalCommands", "kb:control+rightarrow"),
		"shift+control+numpad6": G("globalCommands", "GlobalCommands", "kb:shift+control+rightarrow"),
		"numpad7": G("globalCommands", "GlobalCommands", "kb:home"),
		"nvda+numpad7": G("globalCommands", "GlobalCommands", "kb:nvda+home" ),
		"shift+numpad7": G("globalCommands", "GlobalCommands", "kb:shift+home" ),
		"control+numpad7": G("globalCommands", "GlobalCommands", "kb:control+home"),
		"shift+control+numpad7": G("globalCommands", "GlobalCommands", "kb:shift+control+home"),
		"numpad8": G("globalCommands", "GlobalCommands", "kb:uparrow"),
		"shift+numpad8": G("globalCommands", "GlobalCommands", "kb:shift+uparrow"),
		"nvda+numpad8": G("globalCommands", "GlobalCommands", "kb:nvda+uparrow" ),
		"control+numpad8": G("globalCommands", "GlobalCommands", "kb:control+uparrow"),
		"shift+control+numpad8": G("globalCommands", "GlobalCommands", "kb:shift+control+uparrow"),
		"numpad9": G("globalCommands", "GlobalCommands", "kb:pageup"),
		"nvda+numpad9": G("globalCommands", "GlobalCommands", "kb:nvda+pageup"),
		"shift+numpad9": G("globalCommands", "GlobalCommands", "kb:shift+pageup" ),
		"control+numpad9": G("globalCommands", "GlobalCommands", "kb:control+pageup"),
		"shift+control+numpad9": G("globalCommands", "GlobalCommands", "kb:shift+control+pageup"),
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

	#: A dict of user assigned gestures, containing their values in G form
	userGestures = {}

	def __init__(self):
		"""Initializes the add-on by performing the following tasks:
		- If the NVDA config is set to enter Windows nav mode on startup, we enter it here.
		- Otherwise, checks whether there is an existing numpad nav mode set, and if not, sets to NVDA mode.
		The mode may be already set because plugins have been reloaded, in which case the user would not
		expect a reload to change it.
		- Wraps (monkey patches) the manager.userGestureMap.save method, to prevent saving of Windows nav
		mode gestures.
		- Sets up the NVDA config mechanism that we use.
		"""
		super().__init__()
		# Establish the add-on's NVDA config
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(NumpadNavModeSettings)
		# Initialize the startup mode, or log it if we're already in one (I.E. a plugin reload)
		try:
			initialMode = self.modeTextEN
			log.debug(f"Numpad mode already set to {initialMode}.")
		except AttributeError:  # Raised if this is the first run
			# There is no mode set.  The config will tell us which mode to start in.
			if config.conf["numpadNavMode"]["startInWindowsMode"]:
				self.setMode(self.WIN)
			else:  # Start in NVDA mode
				# We're effectively already in it, so we just establish the global flag.
				globalVars.numpadNavMode = self.NVDA
			# In either case, we log it
			log.info(f"numpadNavMode: initialized numpad to {self.modeTextEN} mode.")

		# Monkey patch manager.userGestureMap.save()
		originalManagerSave = manager.userGestureMap.save
		def numpadNavModePatchedSave(self):
			if self.mode == self.WIN:
				# Reset our idea of user gestures, since the user may have just added/removed some
				self.userGestures = {}
				log.debug("Disabling Windows nav mode before saving user gestures.")
				self.setMode(self.NVDA)
				originalManagerSave()
				self.setMode(self.WIN)
				log.debug("Restored Windows nav mode after saving user gestures.")
			else:
				originalManagerSave()
		manager.userGestureMap.save = types.MethodType(numpadNavModePatchedSave, self)

	def terminate(self):
		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(NumpadNavModeSettings)
		super().terminate()

	@property
	def modeText(self) -> str:
		"""Returns a translated text string representing the current mode of the numpad.
		Warning: Does nothing to make sure that the returned mode is actually the configuration of the numpad!
		Relies on the mode accessor to throw an exception if the mode is unrecognized
		"""
		if self.mode == self.NVDA:
			# Translators: returned as part of some user messages
			return _("NVDA")
		else:
			# Translators: returned as part of some user messages
			return _("Windows")

	@property
	def modeTextEN(self) -> str:
		"""Returns an untranslated text string representing the current mode of the numpad.
		Warning: Does nothing to make sure that the returned mode is actually the configuration of the numpad!
		Relies on the mode accessor to throw an exception if the mode is unrecognized
		"""
		if self.mode == self.NVDA:
			return "NVDA"
		else:
			return "Windows"

	@property
	def mode(self) -> int:
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
				raise AttributeError("Unknown numpad nav mode or mode was never set")
		except AttributeError:	# Raised above, or if the global isn't set at all
			raise

	@script(
		gesture="kb:alt+NVDA+numpadPlus",
		# Translators: description of the Numpad Nav Mode toggle gesture for keyboard help
		description=_("Toggles the numpad between NVDA navigation and Windows navigation modes."),
		category="keyboard"
	)
	def script_toggleNumpadNavMode(self, gesture):
		"""Checks the current nav mode of the numpad, and switches to the opposite one."""
		if self.mode == self.NVDA:
			self.setMode(self.WIN)
		else:  # Mode is Windows
			self.setMode(self.NVDA)
		# Translators: message given to the user when the numpad's mode changes between NVDA and Windows nav
		# Note: the variable given to format() is already translated.
		ui.message(_("Numpad mode {}.").format(self.modeText))
		log.info(f"Numpad set to {self.modeTextEN} nav mode.")

	@classmethod
	def _getAllGesturesAsGDict(cls) -> dict:
		"""Returns a dict of all currently configured user gestures, using G objects."""
		gDict = {
			gest: cls.G(mc.__module__, mc.__name__, scr)
			for mc, gest, scr in manager.userGestureMap.getScriptsForAllGestures()
		}
		return gDict

	def setMode(self, mode: int):
		"""Checks the validity of the given mode.  If it's one of the two valid modes, calls a
		helper method to configure the numpad as desired.
		Raises a ValueError if an invalid mode is provided.
		@param mode: the mode we want the numpad to enter. Provide with the constants self.NVDA or self.WIN.
		@type mode: int
		"""
		if mode == self.WIN:
			self._setWindowsNavMode()
		elif mode == self.NVDA:
			self._setNVDANavMode()
		else:	# An invalid mode was provided
			raise ValueError(f"Can not set numpad mode to unknown value '{mode}'.")
		# If we made it here, we should be safe to set the mode we just configured as the mode we're in
		globalVars.numpadNavMode = mode

	def _setWindowsNavMode(self):
		"""A setMode() helper method, to put the numpad in Windows mode."""
		# Obtain all configured userGestures for use later
		self.userGestures = self._getAllGesturesAsGDict()
		# Assign the Windows emulations
		for gFrag, action in self.numpadGestures.items():
			# We ignore the main gesture, and assign laptop and desktop to the same thing
			manager.userGestureMap.add("kb(desktop):" + gFrag, *action, True)
			manager.userGestureMap.add("kb(laptop):" + gFrag, *action, True)
			manager.userGestureMap.add("kb:" + gFrag, action.mod, action.cls, None, True)

	def _setNVDANavMode(self):
		"""A setMode() helper method, to put the numpad back in NVDA mode.
		Overview: for each numpad gesture, check whether:
		- There is a script for it; and
		- Whether it is our script, which will be an emulated gesture or None.
		If so, remove it.
		If not (meaning it has been reassigned by the user or an add-on), leave it alone.
		"""
		checkThese = {}	#: Mungible dict of gestures we use
		# Build the checkables
		for gFrag, action in self.numpadGestures.items():
			checkThese[normalizeGestureIdentifier("kb(desktop):" + gFrag)] = action
			checkThese[normalizeGestureIdentifier("kb(laptop):" + gFrag)] = action
			# For these, the script should be None
			checkThese[normalizeGestureIdentifier("kb:" + gFrag)] = self.G(action.mod, action.cls, None)

		# For each user gesture, check:
		# - Whether it is the laptop or desktop or main version of one of ours; and
		# - if so, whether it is set as we set it (meaning it hasn't been remapped).
		# in which case we can delete it.
		for gest, action in self._getAllGesturesAsGDict().items():
			try:
				# If it matches, we delete the gesture.
				# We skip it if it doesn't match, or if there's a KeyError.
				if checkThese[gest] == action:
					manager.userGestureMap.remove(gest, *action)
					del checkThese[gest]
			except KeyError:
				pass
		# FixMe: integrate the below code into the above, so we only have to loop the list once.

		# For our next trick, we need to check whether all former user gestures got reset.
		# We do that by checking each one against currently set gestures, and setting any that are missing.
		# We don't overwrite any gesture that has been set in the meantime.
		#: A map of the currently set user gestures, after Windows nav commands have been removed
		currentGestures = self._getAllGesturesAsGDict()
		for gest, action in self.userGestures.items():
			# If the gesture isn't set, we need to put it back.
			if not gest in currentGestures:
				manager.userGestureMap.add(gest, *action, True)
