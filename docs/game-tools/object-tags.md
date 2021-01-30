Tags can be used to govern how objects interact with some of the tools described in this section.


## Standard Interaction Rules
Tags govern interaction between `features` (Zones, Snap-Points, etc.) and `objects` (Cards, Dice, etc.).

* If the feature has _no_ tags, then it will interact with every object, regardless of what tags the object has.
* If the feature has _one or more_ tags, then it will interact only with objects which share at least one of those tags.

### Features which utilize tags

* Hidden Zones
* Randomize Zones
* Hand Zones
* Fog of War Zones
* Layout Zones
* Scripting Zones
* Snap Points

---

## Tagging
To add a tag to an object or feature, right-click and select the `Tags` menu item.  This will open the Tags window:

<center>![Tags Window](/img/tags/object-tag-ui.png)</center>

Clicking on a tag will toggle it being enabled for that object.  The host may add further tags by typing the tag name into the input at the bottom.


!!!note
    Only the host may create new tags, but any promoted player may toggle already existing tags.


### Snap Point Creation Tags

Editting tags on a lot of snap points would quickly get tedious; instead it is better to set the default snap-point tags:

<center>![Snap-Point Creation Tags](/img/tags/snap-point-tags.png)</center>

Whatever tags you select for these will be applied to every snap point created from then on.


## Object-Object Interactions

By default tags do not affect how objects interact with each other; however you may add such functionality with scripting.  For example, the following script will add tag checking to objects entering containers, using the standard interaction rules described above.  It will also add all the container tags to an object when the object is removed from the container.

```lua
function tryObjectEnterContainer(container, object)

    allow_interaction = not container.hasAnyTag() or container.hasMatchingTag(object)
    -- The above is the standard tag interaction rule:
    -- If the 'feature' does not have any tags, or if the
    -- feature and object share a tag.

    return allow_interaction
end

function onObjectLeaveContainer(container, object)
    for i, tag in pairs(container.getTags()) do
        object.addTag(tag)
    end
end

```

---

## Edit Tags Window

The host has access to the `Edit Tags` window (via `Modding->Tags` in the top toolbar).

<center>![Edit Tags](/img/tags/edit-tags.png)</center>

Hovering over a tag in this window will highlight all objects on the table which have that tag, *or*, if you already have objects selected, which of those selected objects have that tag.

Clicking on a tag will set the object selection to the highlighted objects.

You may delete the tag, removing it from *all* objects, by clicking the Delete button.
