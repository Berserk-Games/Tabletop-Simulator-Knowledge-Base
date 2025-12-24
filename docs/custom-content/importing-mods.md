Generally, you will use the [Steam Workshop](steam-workshop.md) to find games to play within Tabletop Simulator. However, you can also import saved tables another way.

##Importing Saves
A game save contains all of the information for the setup and placement of game assets that were created in that game. They do not contain asset files (images/models/etc).

If you received a save file from someone, then you place it in the location where your Save folder is. That is usually at **Documents/My Games/Tabletop Simulator/Saves** (see [Save Game Data Location](../getting-started/technical-info.md#save-game-data-location)).

Place the save file in this folder, keeping in mind whether you already have a save of the same number or not (they can be renamed). Save files are complete as is, with everything already included. Login to Tabletop Simulator and start up a game. Then click **GAMES -> SAVE & LOAD** and choose the save you’d like to load. You will be prompted whether you wish to load this save or not. You can read about saving and loading games here.
Only numbered files can be placed in the Saves folder.

![Loading Saved Games](/img/importing-mods/loading.png){: style="display:block; margin:0 auto;"}

##Importing Files
Game files contain all of the images/models/etc that can then be used by a game save. However these files do nothing on their own without a save. Often times, if assets are hosted online somewhere, then you can automatically load them when you boot up the save. But if the files are not available online, you can import them manually.

If you download a mod from another site like Nexus Mods or someone gives you a named .json and all the images and models, then you need to place them in your Mods folder at **Documents/My Games/Tabletop Simulator/Mods** (see [Save Game Data Location](../getting-started/technical-info.md#save-game-data-location)).

![Importing Saved Files](/img/importing-mods/files.png){: style="display:block; margin:0 auto;"}

In the Mods folder, you have three other folders – **Images**, **Models**, and **Workshop**. In the Models folder, this is where you place all the .OBJ files. The Images folder will contain all .JPGs and .PNGs (Deck template images, dice templates, all your images!). The Workshop folder is where you place your .JSON file. This is usually a series of numbers or it can be named. Keep in mind that named .JSONs cannot be deleted from in-game. This JSON file is also where you want to name your “GameMode”. By default it’s set to None. Name this so it’s easy to locate your game.

Once you have everything imported, you can now click on **GAMES -> WORKSHOP** and locate your game in the list.
