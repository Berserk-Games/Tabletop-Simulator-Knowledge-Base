Custom Assets can be made in many sizes and shapes, but there are recommended guidelines to follow to ensure functionality and quality.

##Images

###Image File Type
Either **PNG** or **JPG** are acceptable image formats. The color mode MUST be set to **RGB**.

!!!warning "CMYK color mode will not work in Tabletop Simulator!"

###Image Resolution
There is rarely a "perfect image resolution", however you can use this list as a reference for what makes a good quality-to-file-size ratio.

For Use With | Recommended Resolution
-- | --
Custom Background | 4096x2048
Custom Board | Any, the board is re-scaled based on the image used.
Custom Deck (Square) | 4096×4096 *(see [Templates](#templates))*
Custom Deck (Rectangle) | 4096×(whatever height fits) *(see [Templates](#templates))*
Custom Dice | *(see [Templates](#templates))*
Custom Figurine | *(none)*
Custom Jigsaw | *(none)*
Custom Model | Any, but it is recommended to follow the [power of two](#power-of-two) guideline.
Custom Tile | *(none)*
Custom Token | *(none)*
Custom Table (Square) | A square image (ex. 2048x2048)
Custom Table (Rectangle) | 4400×2600

!!!tip "Max Resolution"
    A good general rule is to keep the dimensions of your images under 4096x4096 unless recommended otherwise.

!!!tip "Power of Two"
    When the game engine renders certain images, textures sometimes are forced into a [power of 2](http://www.tsm-resources.com/alists/pow2.html) rule for their resolution. The game engine will force textures to a resolution tied to the power of 2, but it will not do as good of a job up/down-scaling your image as you could do with image-editing software. It is not required your images adhere to this "rule", but using it as a guideline for image creation can help produce cleaner in-game results.

    This is especially true when creating textures for models.

####Templates
**Decks** and **Dice** both come with templates. They can be found in Steam directory:

> Steam\steamapps\common\Tabletop Simulator\Modding

##Models
There are several hard limits related to model creation.

###Model File Type
Only **OBJ** is an acceptable file format.

###Model Resolution

For Use With | Maximum Limits
-- | --
3d Model (obj) | Less than 25k vertices per model. More vertices will cause failure to import or game crashes.
Collider | Less than 256 tris per model. More tris will cause the collider to fail.

---
