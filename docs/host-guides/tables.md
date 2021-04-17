There are 7 default tables and 2 custom table available to play on. Additionally, any model can be imported and used in place of a table by selecting the `None` option.

<center>![Tables Menu](/img/tables/menu.png)</center>

##Player Counts
Each table has a default player count. The player count can be adjusted by adding/removing [hand zones](../game-tools/zone-tools.md#hand-zone).

Table | Player Count
-- | --
* Square | 1-4 players
* Hexagon | 1-6 players
* Octagon | 1-8 players
* Round | 1-8 players
* Poker | 1-8 players
* Rectangle | 1-8 players
* Round Glass | 1-8 players
* Custom Square | 1-8 players
* Custom Rectangle | 1-10 players

##Custom Table
The `Custom Square` and the `Custom Rectangle` are tables that allow for a custom image to be used for the table's surface. The custom image is selected when the table is chosen.

<center>![Tables Menu](/img/tables/custom.png)</center>

##Custom Models As Table
Select `None` for your table, import the model you want as a table, lock it, and then add Hand Zones around it for players to be able to sit at it.

###Grids on Custom Model
Right click on the table model, go to **Toggles > Grid Projection** and enable it. If this is not done, the table will not accept grids if they are enabled.

###Make It Non-Interactable
It is also recommended you make the table non-interactable (so it isn't accidentally unlocked) by following steps:

* Save the game and then load from that save.
* Right click the table and select **Scripting > Scripting Editor**.
* Insert this: `function onload() self.interactable = false end` into the editor.
* Click **Save & Play** in the upper left.

If you ever need to remove the non-interactable status, follow the steps above and remove the code you pasted. Also, you will not be able to right click the table, so instead go to **Scripting** at the top of the screen and select the table in the left column to access the code window.

---
