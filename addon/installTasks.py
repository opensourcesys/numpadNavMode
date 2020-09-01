# -*- coding: utf-8 -*-
# Numpad Nav Mode installation tasks (installTasks.py)
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

import addonHandler
import gui
import wx
import config

addonHandler.initTranslation()

def onInstall():
	if gui.messageBox(
		# Translators: title of the installation warning dialog
		_("Gesture Save Warning"),
		# Translators: Contents of the installation warning dialog
		_("""This add-on overrides any custom gestures you may have set for keys on the numpad.
		Don't use this add-on if you rely on custom numpad gestures that you or an add-on have setup.
		Additionally, if you save gestures while this add-on is running, the add-on's gestures will be saved.
		You should try to avoid this, as it could lead to unexpected results if you start without add-ons, and try to use the numpad.
		A future version of the add-on will avoid this problem.
		Do you want to continue using this add-on?"""),
		wx.YES | wx.NO | wx.ICON_WARNING
	) is wx.NO:
		# Translators: an exception raised when the user wants to stop installation
		raise AddonError(_("User requested installation abort."))
