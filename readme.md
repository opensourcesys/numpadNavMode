# Numpad Nav Mode

* Author: Luke Davis (Open Source Systems, Ltd.)
* Download [stable version][1]

Numpad Nav Mode is an [NVDA][2] add-on, which allows you to easily switch your keyboard's numpad between NVDA's navigation controls and the non-screenreader Windows navigation controls. This can be especially useful for users migrating from Jaws to NVDA. This add-on also gives granular control over the numlock key toggle, both when NVDA starts, and optionally in profiles.

### Navigation modes explanation and features

The normal functions of the PC number pad, with numlock off, are: page up, page down, home, end, four-way arrow keys, and a delete key.
But NVDA completely takes over the numpad, to provide review keys, mouse controls, and object navigation controls. This is true even in laptop keyboard mode, which also duplicates those functions on non-numpad keys.

However some users do have a numpad on their laptop, and would prefer to use it for Windows navigation purposes (at least some of the time), especially because some laptops do not provide home, end, or other such keys.  That is where this add-on can help.
Additionally, some desktop users, for example those used to the way the numpad works in JAWS, may sometimes find it convenient to use the numpad for those keyboard functions rather than the normal NVDA keys, which this add-on enables.
This includes the popular JAWS command NumpadInsert+Numpad2, for read to end, which was a specific feature request from some early users of this add-on.

### How it works

With numlock off, no matter what keyboard layout you are using, this add-on will let you press Alt+NVDA+NumpadPlus (which is usually the long key second up on the right), to quickly and easily switch between the normal NVDA navigation controls, and the classic Windows navigation controls. This key can be remapped under Input Gestures, in the Input section.

Note that this add-on doesn't disable the use of numpad insert as an NVDA modifier, if you have it set as such. If you want that feature, please let me know, although you can manually turn off numpad insert as a modifier in NVDA keyboard settings. It also doesn't change the NVDA function of numpad delete (key between zero and enter)--contact me if you desire this.

If you would prefer to have NVDA start with the Windows nav mode active by default, you can configure that in NVDA configuration.  Go to NVDA's preferences, then settings, and find the Numpad Nav Mode settings panel.  There you will be able to select a checkbox to turn Windows Nav Mode on by default when you start NVDA.
To get there quickly, press NVDA+N, P, S, then N one or more times until you hear "Numpad Nav Mode".

### Numlock features

By default, nothing is done with the numlock key.

However, if you share your computer with a sighted user who prefers that numlock always be turned on, but you like having it off so that the numpad works with NVDA, you may want the numlock to automatically turned off when NVDA starts.
Alternatively, you may enter a lot of data, and so prefer the numlock to always be on when you start NVDA.

 Go to NVDA menu, Preferences, Settings, Numpad Nav Mode, and use the "state of numlock when NVDA starts or profile loads" selector. This has three options. The first, "do not change", is the default, and won't touch the numlock. It will be in whatever state it was in before NVDA started.
The second option, is "turn numlock off", which will always turn the numlock off when NVDA starts. The third option, "Turn numlock on", will turn the numlock on if it was off when NVDA started.
If you choose either the second or third option, the numlock will be restored to whatever state it was in before, when you exit NVDA. For example, if you choose "Turn numlock off", and numlock was on when you started NVDA: it will be turned off while you use NVDA, but will be turned back on when you exit NVDA.

#### Advanced use cases

If you use NVDA's powerful configuration profiles, and you would like the numlock to automatically turn on when you enter certain profiles, do the following:
* While in the "normal profile", go to the Numpad Nav Mode settings panel described above. Check the box for "Initial numlock state is configuration profile dependent". This option is unchecked by default.
* Select OK.
* Change to the profile where you want numlock to be always turned off or on.
* Go back to the Numpad Nav Mode settings panel, and select the option to Turn numlock off or on, as you prefer.
* Then select OK. Now, whenever you enter this profile, the numlock will automatically change to the desired state.

Note that this is a new feature, and I don't know if anyone has use for this feature. If you find one, please send an email or open [an issue][3], to let me know how you have found to make use of it.

Or, better yet, leave a [review][4] for the add-on, and comment on it there!
Reviews are very helpful, whether or not you use that feature.

### New features

I encourage you to post an [issue][3], or email with any feature suggestions, or other use cases that I haven't listed here, or just to let me know you find the add-on useful!
But as mentioned above, if you do find it useful, please leave a [review][4].

### History

This add-on was the direct result of requests I've heard from users over the years, and a GitHub discussion in [#9549](https://github.com/nvaccess/nvda/issues/9549). With thanks to @Qchristensen and @feerrenrut.
The basic implementation of the numlock features was borrowed from the legacy NumLock Manager add-on, by Noelia Ruiz (@nvdaes on GitHub), and others. Used with permission.

### Changelog

(This changelog is incomplete. See Git log for full details.)

* 24.1.0: NVDA 2024.X compatibility.
* 23.1.0: Added numlock management features. Better logging. Improved config profile handling (WIP).
* 23.0: NVDA 2023.X compatibility.

[1]: https://github.com/opensourcesys/numpadNavMode/releases/download/v24.1.0/numpadNavMode-24.1.0.nvda-addon
[2]: https://nvaccess.org/
[3]: https://github.com/opensourcesys/numpadNavMode/issues/new
[4]: https://github.com/nvaccess/addon-datastore/discussions/2630
