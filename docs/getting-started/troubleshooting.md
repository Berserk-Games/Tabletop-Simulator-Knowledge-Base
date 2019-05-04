Having technical difficulties with Tabletop Simulator? Follow this guide to help resolve them.

!!!tip "Can't find your answer here?"
    Your next stop should be the [Official Forums](http://www.berserk-games.com/forums/forumdisplay.php?12-Technical-Support). You can search for a solution there and, if none is available, post your problem there.

##First Steps
These should always be the first things you try when running into issues with a Steam game.

* [Verify the integrity of the game cache](https://support.steampowered.com/kb_article.php?ref=2037-QEUH-3335)
* Ensure drivers are updated
* Restart Steam and/or your computer

###Port Forwarding
If you want to enable port forwarding:
>UDP (outbound) - 3478, 4379, 4380 (Steam P2P Ports)

###Enable Logging
To enable logging, type /log in chat or add `-log` to your [launch options](launch-options).

Log Locations:

* **Windows** - `C:\Users\username\AppData\LocalLow\Berserk Games\Tabletop Simulator\Player.log`
* **Mac** - `~/Library/Logs/Unity/Player.log`
* **Linux** - `~/.config/unity3d/Berserk Games/Tabletop Simulator/Player.log`

###Debugging
If your game is crashing, using [launch options](launch-options) to disable various elements of the game can help track down the source.

For example, if -nosteam stops the crashing, try reinstalling Steam.

##Crashing on Startup
Does the game fail to load, and either freeze or crash?

###Windows
* Go into programs and features and uninstall both Microsoft Visual C++ 2012 Redistributable Package x86 & x64.
Then RE-install this: https://www.microsoft.com/en-us/download/details.aspx?id=30679 (both the x86 and x64 versions)
* Turn off MSI Afterburner and/or Riva Tuner if installed.
* Ensure all your drivers are up to date.
* Your firewall/anti-virus could be completely blocking Tabletop Simulator causing it not to load. Manually exclude Tabletop Simulator.exe from the detection of modified applications list (this could be worded differently depending on your program).

###Mac
* Try using the second launch option.
* Try disabling Steam's FPS counter if you have it enabled.

###Linux
* Add -force-opengl to your launch options.
* Turn off the Steam Overlay and add -force-gfx-st to your launch options.

###VR
* Delete `C:\Program Files (x86)\Steam\vr\runtime` as this will fix the issue.

###Crash Mentioning Resolution
* Set the launch options of the game to -screen-width 800 -screen-height 600. This can be set in Steam properties for the game.
* Change your monitor's resolution and run TTS. Try changing it back to normal and load up TTS once more.







##Graphical Issues
Visual issues, although the game runs fine otherwise:

###Everything is Blurry
* Open your graphics card properties and make sure your graphical settings are on quality and nothing lower.

###Pink Screen on Startup
* Do a clean reinstall of graphics drivers (uninstall and then reinstall)

###Black Background and Dark
* Try resizing the game window, swapping between fullscreen and windowed mode or vice versa.





##WWW Errors
Online connectivity issues:

###Improper URL or Could Not Resolve Host
* Check to make sure you don't have any firewall or anti-virus blocking the game.

###WWW Error; Could Not Open File
* Disable 'Mod Caching' in settings, for a temporary work around.

###Transfer Closed with ___ Bytes Remaining
Also comes up as <url> Malformed:

* The domain that those images are hosted from are blocked for you.
* URLs could be broken.
* Try [verifying the integrity of the game cache](https://support.steampowered.com/kb_article.php?ref=2037-QEUH-3335).





##Workshop/Mod Issues
Steam Workshop uploading/downloading issues:

###Mod Not Uploading
* Save your mod, then restart the game and try again.

###Black Texture When Loading
* Try playing on a higher video setting in the launcher. Or making sure your images are using power of 2 sizes (128, 256, 512, 1024, 2048, 4096).

###Incorrect Steam Workshop ID Number
* Did you get TTS as a gift and it's the only game you have? In this case, we have found that Steam restricts your account from doing certain things (including uploading to the Workshop) until you have purchased a game.
* If you purchased TTS on another site, you may need to add funds to your wallet so Steam knows your account is legit.
* Try deleting your remotecache.vdf from your userdata for Tabletop Simulator and restart Steam
* Still having issues? Try looking over [this thread](http://www.berserk-games.com/forums/showthread.php?2512-Workshop-Upload-Broken&highlight=workshop) from the forums.




##Controller Issues
Input device issues:

###Spinning Mouse
* Check to make sure your controller/joystick/etc is not plugged into your computer.
* Uncheck the controller box in the configuration/controls menu.
* Try disabling "HID - compliant game controller" in device manager.








##General Issues
Misc issues with know fixes:

###Tablet Doesn't Work
* Make sure you install [basic flash](https://get.adobe.com/flashplayer/otherversions) to your computer.
* The tablet doesn't work on Linux. This is a limitation of the plugin. It is something we hope to fix in the future.

###UI Not Working in Menu
* Go into programs and features and uninstall Microsoft Visual C++ 2010 Redistributable Package (x86)
* Then RE-install this: https://www.microsoft.com/en-us/download/details.aspx?id=5555

###Mic Not Detected
* If you can't be heard in voice chat, manually select your mic audio source in the [Configuration Menu](configuration-menu#sound).

###Host Password Invalid to All Joiners
* Type `/resetallsaved` in chat. This will clear any old player preferences that is causing this issue. (This will also reset ALL your keybinds/controls)

###Missing Mods/Textures
* Go into programs and features and uninstall Microsoft Visual C++ 2012 Redistributable Package (x86)
* Then RE-install this: https://www.microsoft.com/en-us/download/details.aspx?id=30679

!!!important
    If you're getting the asset popups asking for paths to assets, then there is nothing wrong on your end. It just means the site the images are hosted on are down or removed. You need to post on the Workshop page and let the modder know the issue so they can update the mod.




    ---







---
