## Tests we should do to make sure the add-on is acting properly.

### Test 0: before every other test

Each one of these tests has the following implied first steps:

1.  Start a clean portable copy of NVDA, without numpadNavMode installed.
2.  Make sure there are no user gestures set. Either have a blank gestures.ini, or run the following in the Python console, and get no output:
    ```
    import inputCore
    for s in inputCore.manager.userGestureMap.getScriptsForAllGestures(): print(s)
    ```
3.  Install the latest (development) copy of numpadNavMode.
4.  Restart NVDA to activate the add-on.

### User help test:

1.  Enter NVDA keyboard help (NVDA+1).
2.  Press the default shortcut: NVDA+Alt+NumpadPlus.

Expectation:

should here:Toggles the numpad between NVDA navigation and Windows navigation modes.

### Keys work test:

1.  Switch to Windows nav mode.
2.  Test all numpad keys, with control and shift modifiers, and with no modifiers, to make sure they work. May need to do this in a text editor.

Expectation:

All keys work.

### No stray gestures test:

1.  Switch to Windows nav.
2.  Switch back to NVDA nav.
3.  Run the code from test 0 above.

Expectation:

Running step 3 should produce no results as in Test 0.

### No saved gestures test:

1.  In NVDA nav mode, assign a gesture using the gestures window of NVDA.
2.  Switch to Windows nav.
3.  Switch back to NVDA nav.
4.  Run the code from test 0 above.

Expectation:

The gesture set in step 1 should still exist, and only that gesture should be listed.

<!--
* Save gestures (NVDA+n, p, n, shift+tab twice, enter on "OK").
* Make sure gestures.ini is empty.
-->
