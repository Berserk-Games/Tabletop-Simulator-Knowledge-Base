Saving now uses [JSON serialization](https://en.wikipedia.org/wiki/JSON) for easy to use, human readable format. More specifically, **JSON .NET for Unity**. This page is a technical document which can be used to better understand how an in-game table is recorded into a save file.

You can modify the physics properties of an object in the save file. By adding and modifying the [PhysicsMaterial](https://docs.unity3d.com/Manual/class-PhysicMaterial.html) and [Rigidbody](https://docs.unity3d.com/Manual/class-Rigidbody.html). You can see an example of that in the JSON below.

You can also change an objects scaling separately in each axis, unlike the uniform only scaling in-game.

If you make any mistakes when editing a save, the chat will spit out a debugging error for troubleshooting.
If you have any questions on this topic feel free to post about it on our forums.

##Example JSON

```json
{
    “SaveName”: “JSON Example Save”,
    “GameMode”: “None”,
    “Date”: “2/22/2015 2:44:18 PM”,
    “Table”: “Table_Octagon”,
    “Sky”: “Sky_Forest”,
    “Note”: “This is an example save demonstrating how to use the custom shader and edit physics properties.”,
    “Rules”: “”,
    “PlayerTurn”: “”,
    “Grid”:
    {
        “Type”: 0,
        “Lines”: false,
        “Snapping”: false,
        “Offset”: false,
        “xSize”: 2.0,
        “ySize”: 2.0
    },
    “DrawImage”: “”,
    “ObjectStates”: [
    {
        “Name”: “Custom_Model”,
        “Transform”:
        {
            “posX”: -6.14662361,
            “posY”: 1.02520883,
            “posZ”: 0.435920656,
            “rotX”: 8.387837E-06,
            “rotY”: 179.991959,
            “rotZ”: 1.49730022E-05,
            “scaleX”: 1.0,
            “scaleY”: 1.0,
            “scaleZ”: 1.0
        },
        “Nickname”: “Example Chip”,
        “Description”: “You can see how to tweak the custom shader with this example.”,
        “ColorDiffuse”:
        {
            “r”: 0.9999999,
            “g”: 0.9999999,
            “b”: 0.9999999
        },
        “Grid”: true,
        “Locked”: false,
        “CustomMesh”:
        {
            “MeshURL”: “http://pastebin.com/raw.php?i=00YWZ28Y”,
            “DiffuseURL”: “http://www.berserk-games.com/images/TTS-Coin-Template.png”,
            “NormalURL”: “”,
            “ColliderURL”: “”,
            “Convex”: true,
            “MaterialIndex”: 1,
            “TypeIndex”: 5,
            “CustomShader”:
            {
                “SpecularColor”:
                {
                    “r”: 0.9,
                    “g”: 0.9,
                    “b”: 0.9
                },
                “SpecularIntensity”: 0.1,
                “SpecularSharpness”: 3.0,
                “FresnelStrength”: 0.1
            }
        }
    },
    {
        “Name”: “Die_20”,
        “Transform”:
        {
            “posX”: 5.3177824,
            “posY”: 1.38374138,
            “posZ”: 0.03327445,
            “rotX”: 10.8123074,
            “rotY”: 0.00238325051,
            “rotZ”: 198.000031,
            “scaleX”: 1.0,
            “scaleY”: 1.0,
            “scaleZ”: 1.0
        },
        “Nickname”: “Example D20”,
        “Description”: “You can see how to tweak the physics properties of an object with this example.”,
        “ColorDiffuse”:
        {
            “r”: 0.7960843,
            “g”: 0.0,
            “b”: 0.0
        },
        “Grid”: false,
        “Locked”: false,
        “MaterialIndex”: 0,
        “PhysicsMaterial”:
        {
            “DynamicFriction”: 0.4,
            “StaticFriction”: 0.4,
            “Bounciness”: 0.0,
            “FrictionCombine”: 0,
            “BounceCombine”: 0
        },
        “Rigidbody”:
        {
            “Mass”: 1.0,
            “Drag”: 0.1,
            “AngularDrag”: 0.1,
            “UseGravity”: true
        }
    }
    ]
}
```

##Serialized Classes
Here are the classes that are serialized:

```json
public class SaveState { //Holds a state of the game
public string SaveName = “”;
public string GameMode = “”;
public string Date = “”;
public string Table = “”;
public string TableURL = null; //For custom large table
public string Sky = “”;
public string SkyURL = null; //For custom sky
public string Note = “”;
public string Rules = “”;
public string PlayerTurn = “”;
public GridState Grid;
public byte[] DrawImage; //PNG converted to bytes
public List<ObjectState> ObjectStates; //Object on the table
}

public class ObjectState { //Moveable objects

public string Name = “”; //Internal object name
public TransformState Transform;
public string Nickname = “”; //Name supplied in game
public string Description = “”;
public ColorState ColorDiffuse;
public bool Grid = true;
public bool Locked = false;
/*Nullable to hide object specific properties and save space*/
public Nullable<bool> AltSound; //Some objects have 2 materials, with two sound sets
public Nullable<int> MaterialIndex;
public Nullable<int> MeshIndex;
public Nullable<int> Layer; //Sound Layer
public Nullable<int> Number;
public Nullable<int> CardID;
public Nullable<bool> SidewaysCard;
public Nullable<bool> RPGmode;
public Nullable<bool> RPGdead;
public string FogColor = null;
public Nullable<bool> FogHidePointers;
public List<int> DeckIDs;
public Dictionary<int, CustomDeckState> CustomDeck; //Key matches the hundreth place of the id (ex. id = 354, index = 3)
public CustomMeshState CustomMesh;
public CustomImageState CustomImage;
public ClockSaveState Clock;
public TabletState Tablet;
public List<ObjectState> ContainedObjects; //Objects in bag
public PhysicsMaterialState PhysicsMaterial; //Use to modify the physics material (friction, bounce, etc.)
http://docs.unity3d.com/Manual/class-PhysicMaterial.html
public RigidbodyState Rigidbody; //Use to modify the physical properties (mass, drag, etc) http://docs.unity3d.com/Manual/class-Rigidbody.html

public bool EqualsJSON(System.Object obj)
{
if (obj == null)
{
return false;
}

ObjectState p = obj as ObjectState;
if ((System.Object)p == null)
{
return false;
}

string ThisJSON = SaveScript.GetJSONString(this);
string NewJSON = SaveScript.GetJSONString(p);
return ThisJSON == NewJSON;
}

public ObjectState Clone()
{
string JSONString = SaveScript.GetJSONString(this);
return SaveScript.GetObjectState(JSONString);
}

public string ToJSON()
{
return SaveScript.GetJSONString(this);
}

}

public class GridState {

public GridType Type;
public bool Lines;
public bool Snapping;
public bool Offset;
public float xSize;
public float ySize;
}

public enum GridType
{
Box, Hex
};

public class TransformState {

public float posX;
public float posY;
public float posZ;

public float rotX;
public float rotY;
public float rotZ;

public float scaleX;
public float scaleY;
public float scaleZ;
}

public class ColorState
{
public float r, g, b;
public ColorState(float r, float g, float b)
{
    this.r = r;
    this.g = g;
    this.b = b;
}
}

public class RigidbodyState
{
    public float Mass = 1f; //The mass of the object (arbitrary units). You should not make masses more or less than 100 times that of other Rigidbodies.
    public float Drag = 0.1f; //How much air resistance affects the object when moving from forces. 0 means no air resistance, and infinity makes the object stop moving immediately.
    public float AngularDrag = 0.1f; //How much air resistance affects the object when rotating from torque. 0 means no air resistance. Note that you cannot make the object stop rotating just by setting its Angular Drag to infinity.
    public bool UseGravity = true; //If enabled, the object is affected by gravity.
}

public class PhysicsMaterialState
{
    public float DynamicFriction = 0.4f; //The friction used when already moving. Usually a value from 0 to 1. A value of zero feels like ice, a value of 1 will make it come to rest very quickly unless a lot of force or gravity pushes the object.
    public float StaticFriction = 0.4f; //The friction used when an object is laying still on a surface. Usually a value from 0 to 1. A value of zero feels like ice, a value of 1 will make it very hard to get the object moving.
    public float Bounciness = 0f; //How bouncy is the surface? A value of 0 will not bounce. A value of 1 will bounce without any loss of energy.
    public PhysicMaterialCombine FrictionCombine = PhysicMaterialCombine.Average; //How the friction of two colliding objects is combined. 0 = Average, 1 = Minimum, 2 = Maximum, 3 = Multiply.
    public PhysicMaterialCombine BounceCombine = PhysicMaterialCombine.Average; //How the bounciness of two colliding objects is combined. 0 = Average, 1 = Minimum, 2 = Maximum, 3 = Multiply.
}

public class CustomDeckState
{
    public string FaceURL = “”;
    public string BackURL = “”;
}

public class CustomImageState
{
    public string ImageURL = “”;
    public float WidthScale;
}

public class CustomMeshState
{
    public string MeshURL = “”;
    public string DiffuseURL = “”;
    public string NormalURL = “”;
    public string ColliderURL = “”;
    public bool Convex = true;
    public int MaterialIndex = 0; //0 = Plastic, 1 = Wood, 2 = Metal.
    public int TypeIndex = 0; //0 = Generic, 1 = Figurine, 2 = Dice, 3 = Coin, 4 = Board, 5 = Chip
    public CustomShaderState CustomShader; //Used to override the shader
}

public class CustomShaderState
{
    public ColorState SpecularColor = new ColorState(0.9f, 0.9f, 0.9f);
    public float SpecularIntensity = 0.1f;
    public float SpecularSharpness = 3f; //Range: 2 – 8
    public float FresnelStrength = 0.1f; //Range: 0 – 1
}

public class TabletState
{
    public string PageURL = “”;
}

public class ClockSaveState
{
    public ClockScript.ClockState ClockState;
    public int SecondsPassed = 0;
    public bool Paused = false;
}
```


##Object Name List

```
backgammon_board
backgammon_piece_brown
backgammon_piece_white
Bag
BlockRectangle
BlockSquare
BlockTriangle
Card Facade
Card
CardBot_Board
CheckerFacade
CheckerStack
Checker_black
Checker_Board
Checker_red
Checker_white
Chess_Bishop
Chess_Board
Chess_King
Chess_Knight
Chess_Pawn
Chess_Queen
Chess_Rook
Chinese_Checkers_Board
Chinese_Checkers_Piece
ChipFacade
ChipStack
Chip_10
Chip_100
Chip_1000
Chip_50
Chip_500
Cup
Custom_Board
Custom_Model
Deck
DeckCustom
Deck_CardBot_Head
Deck_CardBot_Main
Die_10
Die_12
Die_20
Die_4
Die_6
Die_6_Rounded
Die_8
Die_Piecepack
Digital_Clock
Domino
Figurine_Card_Bot
Figurine_Custom
Figurine_Kimi_Kat
Figurine_Knil
Figurine_Mara
Figurine_Sir_Loin
Figurine_Zeke
Figurine_Zomblor
FogOfWarTrigger
Go_Board
go_game_bowl_black
go_game_bowl_white
go_game_piece_black
go_game_piece_white
LineObject
Mahjong_Coin
Mahjong_Stick
Mahjong_Tile
MarqueeTrigger
Metal Ball
Pachisi_board
PiecePack_Arms
PiecePack_Crowns
PiecePack_Moons
PiecePack_Suns
PlayerPawn
Quarter
reversi_board
reversi_chip
rpg_BEAR
rpg_CHIMERA
rpg_CYCLOP
rpg_DRAGONIDE
rpg_EVIL_WATCHER
rpg_GHOUL
rpg_GIANT_VIPER
rpg_GOBLIN
rpg_GOLEM
rpg_GRIFFON
rpg_HYDRA
rpg_KOBOLD
rpg_LIZARD_WARRIOR
rpg_MANTICORA
rpg_MUMMY
rpg_OGRE
rpg_ORC
rpg_RAT
rpg_SKELETON_KNIGHT
rpg_TREE_ENT
rpg_TROLL
rpg_VAMPIRE
rpg_WEREWOLF
rpg_WOLF
rpg_WYVERN
SearchSpaceHolder
SearchTriggerObject
Sky_Field
Sky_Forest
Sky_Museum
Sky_Tunnel
Table_Circular
Table_Custom
Table_Glass
Table_Hexagon
Table_Octagon
Table_Poker
Table_RPG
Table_Square
Tileset_Barrel
Tileset_Chair
Tileset_Chest
Tileset_Corner
Tileset_Floor
Tileset_Rock
Tileset_Table
Tileset_Tree
Tileset_Wall
```

---
