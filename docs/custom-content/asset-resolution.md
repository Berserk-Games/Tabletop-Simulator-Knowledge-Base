Custom Assets can be made in many sizes and shapes, but there are recommended guidelines to follow to ensure functionality and quality.

##Images

###Image File Type
Either **PNG** or **JPG/JPEG** are acceptable image formats. The color mode MUST be set to **RGB**. CMYK color mode will not work in Tabletop Simulator.

###Image Resolution
You are not required to use an image with these resolutions, but these will provide the best results for the file size used.

For Use With | Recommended Resolution
-- | --
Custom Background | 4000x2000 (Maximum of 8000x4000)
Custom Board | Any, the board is re-scaled based on the image used.
Custom Deck (Square) | 4096×4096
Custom Deck (Rectangle) | 4096×*(whatever height fits)*
Custom Dice | *(none)*
Custom Figurine | *(none)*
Custom Jigsaw | *(none)*
Custom Model | Any, but it is recommended to follow the [power of two](#power-of-two) guideline.
Custom Tile | *(none)*
Custom Token | *(none)*
Custom Table (Square) | A square image (ex. 2048x2048)
Custom Table (Rectangle) | 4400×2600

!!!tip "Max Resolution"
    A good general rule is to keep the dimensions of your images under 4096x4096 unless recommended otherwise.


####Power of Two
When the game engine renders certain images, textures sometimes are forced into a [power of 2](http://www.tsm-resources.com/alists/pow2.html) rule for their resolution. The game engine will force textures to a resolution tied to the power of 2, but it will not do as good of a job up/down-scaling your image as you could do with image-editing software. It is not required your images adhere to this "rule", but using it as a guideline for image creation can help produce cleaner in-game results.

This is especially true when creating textures for models.

##Models

###Model Resolution

For Use With | Recommended Resolution
-- | --
3d Model (obj) | Less than 25k vertices per model. More vertices will cause physic simulation issues, failure to import or game crashes.
