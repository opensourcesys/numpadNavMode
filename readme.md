# Numpad Nav Mode

* Author: Luke Davis (Open Source Systems, Ltd.)
* Download [stable version](https://github.com/openSourceSys/numpadNavMode/releases/numpadNavMode-23.0.nvda-addon)

Numpad Nav Mode is an [NVDA](https://nvaccess.org/) add-on, which allows you to easily switch your keyboard's numpad between NVDA's navigation controls and the non-screenreader Windows navigation controls.

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

### New features

I encourage you to post an [issue](https://github.com/openSourceSys/numpadNavMode/issues/new), or email with any feature suggestions, or other use cases that I haven't listed here, or just to let me know you find the add-on useful!

### Inspiration

This add-on was the direct result of requests I've seen from users over the years, and a GitHub discussion in [#9549](https://github.com/nvaccess/nvda/issues/9549). With thanks to @Qchristensen and @feerrenrut.
