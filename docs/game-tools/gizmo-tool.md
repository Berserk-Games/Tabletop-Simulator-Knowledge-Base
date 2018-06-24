The Gizmo Tool is an advanced feature where you can move, rotate and scale objects/zones. You can also set "values" on objects that are based on rotation.

!!!tip "You can even modify "locked" Objects and zones!"

!!!tip "Transform multiple objects at once by CTRL+Clicking each object."
    

##Transform Menu
<center>![Transform Menu](/img/gizmo-tool/transform.png)</center>

With any of the Gizmo Tool options selected, left-clicking an object will open the Transform Menu. It shows numerical values for Position, Rotation and Scale.

###Modifying Transform
Changing any of the values and pressing enter (or clicking outside of the field) will update that property of the Object. So putting 90 in the X field would rotate the Object 90º on its X axis.

###X Y Z
Objects in 3D space are referred to having 3 axes, with the center of each axis being 0. One direction is positive, the other negative. They are labeled **X**, **Y** and **Z**. If you were an Object, here is how those directions would line up with your default facing:

* **X**: Drawing a line from your next to your right shoulder. Negative values would be from your next to the left shoulder.
* **Y**: Drawing a line from your heart to the top of your head. Negative values would be from your heart to your feet.
* **Z**: Drawing a line from your heart to your chest. Negative values would from your heart to your back.

{>>I realize the heart is off-center in the human body. For this example, just pretend it is in the middle.<<}

###Dragging Value Changes
Left-clicking and dragging on an X, Y or Z allows you to increase/decrease the value in its field.

###Copying to Clipboard
The buttons to the right of the Position/Rotation/Scale values is a "copy to clipboard" button. It saves the values in a Lua-formatted table. This is for use with scripting and does not serve any other purpose.

Example of what is copied to clipboard: `#!lua {0.09, 1.06, -0.79}`

---

##Gizmo Modifiers
On the sub-menu that pops out next to the Gizmo Tool button, you can see two circles. These allow the tools to behave slightly differently.

###Transform Space
The round circle on the sub-menu that says Local by default is the Transform Space. It allows you to determine if that UI modifier will be Local or Global.

* **Local**: The tool will move/rotate/scale based on the Object's default axes. No matter how you rotate the Object, it will change based off itself.
* **Global**: The tool will move/rotate/scale based on the World's axes. The Object's position/rotation/scale are ignored and the Object is changed relative to default world coordinates.

!!!tip
    If this sounds confusing, go into the game, rotate a block 45 degrees, and use the Move gizmo on it. Toggling between Local and Global now will illustrate the difference clearly.



###Pivot Point
The round circle on the sub-menu that says Center by default is the Pivot Point. It determines where the UI element is placed.

* **Center**: The pivot point is in the middle of the Object's volume.
* **Pivot**: The pivot point is at the Object's Origin.

!!!tip
    When a person creates a model, they do so on an XYZ grid. The origin point, where the 0 values lie for XYZ, does not have to be in the center of the model they are creating. That is the difference between the center of an Object and its Origin point.


---

##Sub-Menus

###Move (Position)
![Transform Menu, Move](/img/gizmo-tool/gizmo-move.png)

The Move Tool lets you move Objects precisely. It is done by click-and-dragging arrows/squares on the UI.

![Move UI](/img/gizmo-tool/position.png)

####UI Controls
* **Arrows**: Moves the Object on a single axis.
* **Squares**: Moves the Object on 2 axes, with the third axis remaining the same.

####Modifiers
* **Ctrl**: Holding Control will cause Objects to snap to 1 unit increments when moving.
* **Shift**: Holding Shift will cause a white box to appear in the middle of the Transform UI. Clicking and dragging it will move the Object relative to your screen position/direction.

---

###Rotate (Rotation)
![Transform Menu, Rotate](/img/gizmo-tool/gizmo-rotate.png)

The Rotate Tool lets you rotate Objects precisely. It is done by click-and-dragging rings on the UI.

![Rotate UI](/img/gizmo-tool/rotation.png)

####UI Controls
* **Interior Lines**: Rotate the Object on a single axis.
* **Outer Ring**: Rotate the Object relative to the angle of the screen.
* **Space Inside Inner Ring**: Rotate the Object freely on all 3 axes.

####Modifiers
* **Ctrl**: Holding Control will cause Objects to snap to 1 degree increments when rotating.

---


###Scale
![Transform Menu, Scale](/img/gizmo-tool/gizmo-scale.png)

The Scale Tool lets you scale Objects precisely. It is done by click-and-dragging block-lines/triangles on the UI.

![Scale UI](/img/gizmo-tool/scale.png)

####UI Controls
* **Block-Lines**: Scales the Object on a single axis.
* **Triangles**: Scales the Object on 2 axes, with the third axis remaining the same.

####Modifiers
* **Ctrl**: Holding Control will cause Objects to snap to 1 unit increments when scaling.
* **Shift**: Holding Shift will cause the scale changes to be uniform on all axes.

---


###Volume Scale
![Transform Menu, Volume Scale](/img/gizmo-tool/gizmo-volume-scale.png)

The Volume-Scale Tool lets you scale Objects precisely. It is done by click-and-dragging boxes on the UI. Similar to the Scale Tool, this version allows you to change the scale of one side of one axis, rather than making the distance from the center point uniform. A dot is placed on each "side".

![Volume-Scale UI](/img/gizmo-tool/volume.png)

####UI Controls
* **Boxes**: Scales one side of the Object.

####Modifiers
* **Ctrl**: Holding Control will cause Objects to snap to 1 unit increments when scaling.
* **Shift**: Holding Shift will cause the opposite side to scale as well. This makes it act the same as the normal Scale Gizmo.




---


###Rotation Value
![Transform Menu, Rotation Value](/img/gizmo-tool/gizmo-rotation-value.png)

The Rotation Value Gizmo allows for you to set a value that is tied to which way is "up" on an Object. This allows for you to assign values to coins, dice and more.

!!!tip
    Setting Rotation Values, just like setting position or scale, is only recorded if you SAVE YOUR TABLE AFTER MAKING CHANGES!!!

####Rotation Value Menu
The Rotation Value Gizmo is slightly different from the other Gizmo tools. It does give a UI element like the [Rotate Gizmo](#rotate-rotation), but it also opens the Rotations window.

![Rotation Value Menu](/img/gizmo-tool/rotation-value1.png)

In this window you will see any saved Rotation Values an Object has, as well as what that Object looks like face-up.

Mousing over any of these small windows brings up an icon in the upper-right. It allows you to Delete or Edit a value. By default, dice and coins will have these values pre-set, but you can add/remove them to/from any Object.

####Setup Rotation Value
Clicking the red `+` button at the top of the Rotation Menu, or editing an existing value, opens the Rotation Value Setup menu.

![Rotation Value Setup](/img/gizmo-tool/rotation-value2.png)

The window has 2 settings.

#####Value
This is what the Object will display when this face is pointed up. You can use numbers for dice or words.

#####Rotation
This is the rotation the Object when a given face is pointed up. It allows for the same modifications as the [Transform Menu](#transform-menu). 

The red arrow button will copy over the rotation that the Object is currently set to into the fields. These fields always default to 0,0,0. Be sure to update them!


---
