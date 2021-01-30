![Zone Tools](/img/zone-tools/zone.png)

The zone tools allow you to create areas on the table that have different impacts on game objects inside them. Hand zones are particularly important because they determine the "seats" a player is able to "sit" in.

## General Zone Modification
Although all zone types work differently, the creation and modification of them is all similar.

### Creation
With your mouse, left-click and hold. Drag your mouse so that the created zone will have the desired width/depth, then release.

### Removal
With the same zone tool selected, left-clicking on a pre-existing zone will remove it.

### Modification
Right-clicking on a pre-existing zone will provide some additional feature/options. What the right-click does depends on the zone type. You can find more information on the right-click feature below.

!!!tip
    When you draw a zone, you aren't stuck with the shape you made it! All zones can be moved/resized/rotated by using the [Gizmo Tool](gizmo-tool.md).


---

## Zone Types
Each zone has different rules when it comes to visibility, right-click functionality and more. This section outlines those differences.

### Hidden Zone
![Hidden Zone Menu](/img/zone-tools/hidden-zone-menu.png)

A hidden zone is an area that is able to hide objects from certain players. It can hide those objects from all other player colors or just one. The GM *(Black seat)* is always able to see what is within any hidden zone.

Hidden zones are visible to all players during gameplay, although their contents are hidden.

#### Right-Click Action
Right-clicking on a hidden zone will bring up a color circle and a gear icon.

<center>![Hidden Zone Right Click](/img/zone-tools/hidden-rc1.png)</center>

Clicking on a color will set the hidden zone will set the zone to match that color player. This determines who it is hiding for.

Clicking on the gear will open the options for this specific hidden zone.

<center>![Hidden Zone Right Click Sub-menu](/img/zone-tools/hidden-rc2.png)</center>

* **Hide Pointers**: If checked, the zone will hide pointers that are within the zone, preventing any clues to what is being done in it.
* **Reverse Hiding**: If checked, it will reveal its contents to all other players. Unchecked, it hides the contents from everyone but the select color.
* **See-through**: If checked, the hidden zone is semi-transparent. If unchecked, it is a solid color. Either way, you cannot see the zone's contents.




---


### Randomize Zone
![Randomize Zone Menu](/img/zone-tools/randomize-zone-menu.png)

A randomize zone will, any time the game is loaded, ask if you want to randomize the objects inside of it. The randomization will shuffle the positions of loose tokens as well as the order of tokens in a stack/cards in a deck.

Randomize zones are invisible to all players unless you select the randomize zone or gizmo tools.

####Right-Click Action
Right-clicking a randomization zone will bring up the confirmation window to randomize the zone's contents.

<center>![Randomize Zone Right Click](/img/zone-tools/randomize-rc1.png)</center>





---


### Hand Zone
![Hand Zone Menu](/img/zone-tools/hand-zone-menu.png)

A hand zone represents a player color. It not only determines where their "seat" is, but also is an area that holds items. Similar to a hidden zone, the contents of a hand zone can be hidden, but with special additional options. The contents of your primary hand zone are also able to be shown on your screen in an easy-access pop-up panel.

Hand zones are invisible to all players unless you select the hand zone or gizmo tools.

####Right-Click Action
Right-clicking on a hand zone will bring up a color circle.

<center>![Hand Zone Right Click](/img/zone-tools/hand-rc1.png)</center>

Clicking on a color will set the hand zone will set the zone to match that color player. This determines who the zone belongs to. If this is the first hand zone of this color on the table, it also determines where that player "sits".

---




### Fog of War Zone
![Fog of War Zone Menu](/img/zone-tools/fog-of-war-zone-menu.png)

Fog of War is an area that is concealed, similar to a [hidden zone](#hidden-zone). The difference is that concealed areas can be revealed by moving a piece set to [Reveal Fog of War](/player-guides/context-menu#toggles) into it.

#### Right-Click Action
Right-click on a Fog of War zone will do two thing. First, it copy the GUID into the clipboard (for scripting). Secondly, it will open a menu.

![Fog of War Zone Right Click](/img/zone-tools/fog-of-war-rc.png)

* **Hide GM Pointer**: If checked, this prevents players from seeing the hand cursor of the player in the Black seat.
* **Hide Objects**: If checked, this causes the fog to hide objects. If you uncheck it, it will just make a black plane which obscures anything under it.
* **ReHide Objects**: If checked, this causes any object that had been revealed in the fog to become hidden again if it is not in direct "line of sight" of a revealer.
* **Fog Height**: How high up the black plane is placed within the zone.
* **Reset Fog**: Causes any revealed fog to obscure again, as if it had been newly drawn.

#### Fog of War Tips
* If you have enabled "Reveal Fog of War" in an item's [toggles menu](/player-guides/context-menu#toggles) you get access to additional settings in the [Context Menu](/player-guides/context-menu).
    * **Reveal Color**: Which color player the fog is revealed for. Default is Black, which is "all players".
    * **Reveal Range**: The radius which the object reveals.
* "Line of sight" is used, which means props can block the revealed area.
* The purpose of Fog of War is to allow game pieces to reveal map/props as they move around.
* The player in the GM seat, the Black seat, is capable of seeing everything hiding within the Fog of War. Hidden objects have a grey border around them.
* You can prevent an object from being hidden by Fog of War in its [toggles menu](/player-guides/context-menu#toggles).
* If you join a player's [team](/player-guides/teams), you can see what they have revealed for them.
    * Example: If you wanted 2 of your 4 players to see what is revealed, you could put them on a team together and reveal for only 1 of the colors.

![Fog of War Zone Example](/img/zone-tools/fog-of-war-demo.png)


---


### Layout Zone

[WIP]

---


### Scripting Zone
![Script Zone Menu](/img/zone-tools/script-zone-menu.png)

A scripting zone has no impact on game objects itself, but it can be utilized by Lua scripting to detect/affect objects in an area. It has no use outside of scripting.

Scripting zones are invisible to all players unless you select the hand zone or gizmo tools.

#### Right-Click Action
Right-clicking on a scripting zone copies it GUID to the clipboard. You can then paste it into your scripts. This is generally how you identify scripting zones in your code.

<center>![Script Zone Right Click](/img/zone-tools/script-rc1.png)</center>

You will see a pop-up message announcing that this has been done, as well as a message in the Game chat log.

---
