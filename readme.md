# Numpad Nav Mode

* Author: Luke Davis (Open Source Systems, Ltd.)
* Download [stable version](https://github.com/opensourcesys/numpadNavMode/releases)

Numpad Nav Mode is an [NVDA](https://nvaccess.org/) add-on, which allows you to easily switch your keyboard's numpad between NVDA's navigation controls and the classic Windows navigation controls.

The normal functions of the PC number pad, with numlock off, are: page up, page down, home, end, four-way arrow keys, and a delete key.
But NVDA completely takes over the numpad, to provide review keys, mouse controls, and object navigation controls. This is true even in laptop keyboard mode, which also provides those functions on non-numpad keys for those who do not have a numpad.

However some users do have a numpad on their laptop, and would prefer to use it for Windows navigation purposes, especially because some laptops do not provide home, end, or other such keys.

Some desktop users may even find it convenient to use the numpad for those keyboard functions rather than the normal keys, at least some of the time.

This add-on makes that possible.

With this add-on enabled: no matter what keyboard layout you are using, you can press Alt+NVDA+NumpadPlus (which is usually the long key second up on the right), and quickly and easily switch between the normal NVDA navigation controls, and the classical Windows navigation controls.
Note that this key can be remapped under Input Gestures, in the Input section.

Note also that this add-on does not disable the use of numpad insert as the NVDA modifier, if you have it set as such. If you want that feature, please let me know.

## WARNING!

There is one point of caution of which you should be aware before installing this add-on.

Because of the way this add-on works, any custom key assignments you have made to keys on the numpad (with numlock off) in Input Gestures, will not be active with this add-on enabled.
Additionally, if you save your gestures while this add-on is running, the add-on's gestures will be saved along with your normal gestures, and you will need to use the add-on to restore normal NVDA numpad functioning.

## New features

Some further features are planned for this add-on, such as a configuration dialog which will enable using Windows numpad navigation automatically, whenever you are in laptop keyboard mode.

I encourage you to email with any feature suggestions, or other use cases that I haven't listed here.

## Release history:

* V1.0: September, 2020. Initial release. Based on various user requests, and ultimately a discussion in [#9549](https://github.com/nvaccess/nvda/issues/9549). With thanks to @Qchristensen and @feerrenrut.
