The Physics Menu is an advanced feature, which gives you control on the physics and materials of individual objects. To access it, right click on an object and choose the **Physics** option.

<center>![Physics Menu](/img/physics/menu.png)</center>

##Rigidbody
Determines how the Object behaves when moving through space.

Setting Name | What It Does
-- | --
**Use&nbsp;Gravity** | Enable being affected by gravity.
**Mass** | Mass of the object. {>>Uses arbitrary mass units<<}
**Drag** | How much air resistance affects the object when moving from forces. 0 means no air resistance, and infinity makes the object stop moving immediately. A low Drag value makes an object seem heavy. A high one makes it seem light. Typical values for Drag are between .001 (solid block of metal) and 10 (feather).
**Angular&nbsp;Drag** | How much air resistance affects the object when rotating from torque. 0 means no air resistance. {>>ou cannot make the object stop rotating just by setting its Angular Drag to infinity<<}

!!!tip "Setting Gravity"
    Gravity is for the whole table and can be changed at the top of the screen under **Options > Game**.

##Material
Determines how the Object behaves when impacting/touching other Objects.

!!!note "Dynamic Friction vs Static Friction"
    Friction comes in two forms, dynamic and static. Static friction is used when the object is lying still. It will prevent the object from starting to move. If a large enough force is applied to the object it will start moving. At this point Dynamic Friction will come into play. Dynamic Friction will now attempt to slow down the object while in contact with another.

Setting Name | What It Does
-- | --
**Static&nbsp;Friction** | The friction used when an object is laying still on a surface. Usually a value from 0 to 1. A value of zero feels like ice, a value of 1 will make it very hard to get the object moving.
**Dynamic&nbsp;Friction** | The friction used when already moving. Usually a value from 0 to 1. A value of zero feels like ice, a value of 1 will make it come to rest very quickly unless a lot of force or gravity pushes the object.
**Bounciness** | How bouncy is the surface? A value of 0 will not bounce. A value of 1 will bounce without any loss of energy.


---
