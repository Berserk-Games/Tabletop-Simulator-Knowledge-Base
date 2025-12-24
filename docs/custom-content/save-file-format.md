Saving uses [JSON serialization](https://en.wikipedia.org/wiki/JSON) for easy to use, human readable format. More specifically, **JSON .NET for Unity**. This page is a technical document which can be used to better understand how an in-game table is recorded into a save file. Bson is used for saving to the workshop, but is converted back to JSON when saved to disk.

If you make any mistakes when editing a save, the chat will spit out a debugging error for troubleshooting.

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

```cs
public class SaveState //Holds a state of the game
{ 
	public string SaveName = "";
	public string GameMode = "";
    public float Gravity = 0.5f;
    public float PlayArea = 0.5f;
	public string Date = "";
	public string Table = "";
    [Tag(TagType.URL)]
    public string TableURL = null; //For custom tables
	public string Sky = "";
    [Tag(TagType.URL)]
    public string SkyURL = null; //For custom sky
	public string Note = "";
	public string Rules = "";
    public string XmlUI = ""; //Custom Xml UI
    public List<CustomAssetState> CustomUIAssets;
    public string LuaScript = "";
    public string LuaScriptState = ""; // Serialized running Lua code    
	public GridState Grid; //Grid menu settings    
    public LightingState Lighting; //Lighting menu settings
    public HandsState Hands; //Hand menu settings and hand positions
    public TurnsState Turns; //Turn menu settings    
    public List<VectorLineState> VectorLines; // Vector lines on canvas 0 (table + beyond)   
	public List<ObjectState> ObjectStates; //Objects on the table
    public List<SnapPointState> SnapPoints; //Snap points not attached to objects
    public List<CustomDecalState> DecalPallet; //Decals that can be placed in the world
    public List<DecalState> Decals; //Decals not attached to objects
    public Dictionary<int, TabState> TabStates = new Dictionary<int, TabState>(); //Notepad tabs
    public CameraState[] CameraStates; //Saved camera positions
    public string VersionNumber = "";
}

public class ObjectState //Moveable objects
{ 
	public string Name = ""; //Internal object name
	public TransformState Transform; //Position, Rotation, Scale
	public string Nickname = ""; //Name supplied in game
	public string Description = "";
	public ColourState ColorDiffuse; //Material color tint
    /*Toggles*/
    public bool Locked = false; //Freeze object in place
	public bool Grid = true; //Object will snap to grid
    public bool Snap = true; //Object will snap to snap points	
    public bool Autoraise = true; //Object will raise above others and avoid collision
    public bool Sticky = true; //When picked up objects above this one will be attached to it
    public bool Tooltip = true; //When hovering object will display tooltips
    public bool GridProjection = false; //Grid will project on this object
    /*Nullable to hide object specific properties and save space*/
    public bool? HideWhenFaceDown; //When face down object is question mark hidden
    public bool? Hands; //Object will enter player hands
    public bool? AltSound; //Some objects have 2 materials, with two sound sets
	public int? MaterialIndex; //Some objects can have multiple materials
	public int? MeshIndex; //Some objects can have multiple meshes
	public int? Layer; //Sound Layer
	public int? Number;
	public int? CardID;
	public bool? SidewaysCard;
	public bool? RPGmode;
	public bool? RPGdead;
	public string FogColor = null;
	public bool? FogHidePointers;
    public bool? FogReverseHiding;
    public bool? FogSeethrough;
	public List<int> DeckIDs;
	public Dictionary<int, CustomDeckState> CustomDeck; //Key matches the hundreth place of the id (ex. id = 354, index = 3)
	public CustomMeshState CustomMesh;
	public CustomImageState CustomImage;
    public CustomAssetbundleState CustomAssetbundle;
    public FogOfWarSaveState FogOfWar;
    public FogOfWarRevealerSaveState FogOfWarRevealer;
    public ClockSaveState Clock;
    public CounterState Counter;
	public TabletState Tablet;
    public Mp3PlayerState Mp3Player;
    public CalculatorState Calculator;
    public TextState Text;
    public string XmlUI = ""; //Custom Xml UI
    public List<CustomAssetState> CustomUIAssets;
    public string LuaScript = "";
    public string LuaScriptState = ""; // Serialized running Lua code
    public List<ObjectState> ContainedObjects; //Objects inside this one
	public PhysicsMaterialState PhysicsMaterial; //Use to modify the physics material (friction, bounce, etc.) http://docs.unity3d.com/Manual/class-PhysicMaterial.html
	public RigidbodyState Rigidbody; //Use to modify the physical properties (mass, drag, etc) http://docs.unity3d.com/Manual/class-Rigidbody.html
	public JointFixedState JointFixed; //Joints can be used to attached/link objects together check the classes below
	public JointHingeState JointHinge;
	public JointSpringState JointSpring;
	public string GUID = ""; //Used so objects can reference other objects, ex. joints or scripting
    public List<SnapPointState> AttachedSnapPoints; //Snap points that are stuck to this object, happens when placing a snap point on a locked object
    public List<VectorLineState> AttachedVectorLines; // Vector lines that are stuck to this object, happens when drawing a vector line on a locked object
    public List<DecalState> AttachedDecals; //Decals that are attached to this objects
    public Dictionary<int, ObjectState> States; //Objects can have multiple states which can be swapped between    
    public List<RotationValueState> RotationValues; //Rotation values are tooltip values tied to rotations

	public bool EqualsObject(object obj)
	{
		if (obj == null)
		{
			return false;
		}		

		ObjectState os = obj as ObjectState;
		if (os == null)
		{
			return false;
		}

        TransformState ThisTransform = this.Transform;
        TransformState OtherTransform = os.Transform;        

        ColourState ThisColor = this.ColorDiffuse;
        ColourState OtherColor = os.ColorDiffuse;
        if (ThisColor != null && OtherColor != null && ThisColor.ToColour() != OtherColor.ToColour())
        {
            return false;
        }               

        string ThisGUID = this.GUID;
        string OtherGUID = os.GUID;

        bool ThisLocked = this.Locked;
        bool ThisGrid = this.Grid;
        bool ThisSnap = this.Snap;
        bool ThisAutoraise = this.Autoraise;
        bool ThisSticky = this.Sticky;
        bool ThisTooltip = this.Tooltip;
        bool ThisGridProjection = this.GridProjection;
        bool? ThisHideWhenFaceDown = this.HideWhenFaceDown;
        bool? ThisHands = this.Hands;

        bool OtherLocked = os.Locked;
        bool OtherGrid = os.Grid;
        bool OtherSnap = os.Snap;
        bool OtherAutoraise = os.Autoraise;
        bool OtherSticky = os.Sticky;
        bool OtherTooltip = os.Tooltip;
        bool OtherGridProjection = os.GridProjection;
        bool? OtherHideWhenFaceDown = os.HideWhenFaceDown;
        bool? OtherHands = os.Hands;

        this.Transform = null;
        os.Transform = null;
        this.ColorDiffuse = null;
        os.ColorDiffuse = null;
        this.GUID = null;
        os.GUID = null;

        this.Locked = false;
        this.Grid = false;
        this.Snap = false;
        this.Autoraise = false;
        this.Sticky = false;
        this.Tooltip = false;
        this.GridProjection = false;
        this.HideWhenFaceDown = false;
        this.Hands = null;

        os.Locked = false;
        os.Grid = false;
        os.Snap = false;
        os.Autoraise = false;
        os.Sticky = false;
        os.Tooltip = false;
        os.GridProjection = false;
        os.HideWhenFaceDown = false;
        os.Hands = null;

        string ThisJson = Json.GetJson(this, false);
		string NewJson = Json.GetJson(os, false);        

        this.Transform = ThisTransform;
        os.Transform = OtherTransform;
        this.ColorDiffuse = ThisColor;
        os.ColorDiffuse = OtherColor;
        this.GUID = ThisGUID;
        os.GUID = OtherGUID;

        this.Locked = ThisLocked;
        this.Grid = ThisGrid;
        this.Snap = ThisSnap;
        this.Autoraise = ThisAutoraise;
        this.Sticky = ThisSticky;
        this.Tooltip = ThisTooltip;
        this.GridProjection = ThisGridProjection;
        this.HideWhenFaceDown = ThisHideWhenFaceDown;
        this.Hands = ThisHands;

        os.Locked = OtherLocked;
        os.Grid = OtherGrid;
        os.Snap = OtherSnap;
        os.Autoraise = OtherAutoraise;
        os.Sticky = OtherSticky;
        os.Tooltip = OtherTooltip;
        os.GridProjection = OtherGridProjection;
        os.HideWhenFaceDown = OtherHideWhenFaceDown;
        os.Hands = OtherHands;

        return ThisJson == NewJson;
	}

	public ObjectState Clone()
	{		
		return Json.Clone(this);
	}

	public string ToJson()
	{
		return Json.GetJson(this);
	}

    public static List<ObjectState> RemoveDuplicates(List<ObjectState> objectStates)
    {
        List<ObjectState> newObjectStates = new List<ObjectState>();

        for (int i = 0; i < objectStates.Count; i++)
        {
            ObjectState objectState = objectStates[i];

            if (objectState == null) continue;

            bool isDuplicate = false;

            for (int j = 0; j < newObjectStates.Count; j++)
            {
                ObjectState os = newObjectStates[j];

                if (objectState.EqualsObject(os))
                {
                    isDuplicate = true;
                    break;
                }
            }

            if (isDuplicate) continue;

            newObjectStates.Add(objectState);
        }

        return newObjectStates;
    }
}

public class GridState
{	
	public GridType Type = GridType.Box;
	public bool Lines = false;
    public ColourState Color = new ColourState(0,0,0);
    public float Opacity = 0.75f; //0-1 Alpha opacity
    public bool ThickLines = false;
	public bool Snapping = false; //Line snapping
	public bool Offset = false; //Center snapping
    public bool BothSnapping = false; //Both snapping
	public float xSize = 2f;
	public float ySize = 2f;
    public VectorState PosOffset = new VectorState(0,1,0);
}

public enum GridType
{
    Box, HexHorizontal, HexVertical
};

public class LightingState
{    
    public float LightIntensity = 0.54f; //0-8
    public ColourState LightColor = new ColourState(1f, 0.9804f, 0.8902f);    
    public float AmbientIntensity = 1.3f; //0-8
    public AmbientType AmbientType = AmbientType.Background;
    public ColourState AmbientSkyColor = new ColourState(0.5f, 0.5f, 0.5f);
    public ColourState AmbientEquatorColor = new ColourState(0.5f, 0.5f, 0.5f);
    public ColourState AmbientGroundColor = new ColourState(0.5f, 0.5f, 0.5f);
    public float ReflectionIntensity = 1f; //0-1
    public int LutIndex = 0;
    public float LutContribution = 1f; //0-1
    [Tag(TagType.URL)]
    public string LutURL; //LUT 256x16
}

public enum AmbientType
{
    Background, Gradient //Background = ambient light comes from the background, Gradient = ambient light comes from the three ambient colors
}

public class HandsState
{
    public bool Enable = true;
    public bool DisableUnused = false;
    public HidingType Hiding = HidingType.Default;
    public List<HandTransformState> HandTransforms;
}

public enum HidingType
{
    Default, Reverse, Disable //Default = only owner can see, Reverse = opposite of default, Disable = hiding is disabled
};

public class HandTransformState
{
    public string Color;
    public TransformState Transform;
}

public class TurnsState
{
    public bool Enable;
    public TurnType Type = TurnType.Auto;
    public List<string> TurnOrder = new List<string>();
    public bool Reverse;
    public bool SkipEmpty;
    public bool DisableInteractions;
    public bool PassTurns = true;
    public string TurnColor;
}

public enum TurnType
{
    Auto, Custom //Auto = turn order is based on positioning of hands on around table, Custom = turn order is based on an user color list
}

public class TextState
{
    public string Text;
    public ColourState colorstate;
    public int fontSize = 64;
}

public class TabState
{
    public string title;
    public string body;
    public string color;
    public ColourState visibleColor;
    public int id = -1;

    [JsonConstructor]
    public TabState() { }
    
    public TabState(UITab to)
    {
        title = to.title;
        body = to.body;
        visibleColor = new ColourState(to.VisibleColor);
        color = Colour.LabelFromColour(to.VisibleColor);
        id = to.id;
    }
}

public class SnapPointState
{
    public VectorState Position; //World position when not attached and local position when attached to an object
    public VectorState Rotation; //Rotate is only set for rotation snap points
}

public class DecalState
{
    public TransformState Transform;
    public CustomDecalState CustomDecal;
}

public class CustomDecalState
{
    public string Name;
    [Tag(TagType.URL)]
    public string ImageURL;
    public float Size; //Size in inches
}

public class RotationValueState
{
    public object Value;
    public VectorState Rotation;
}

public class CustomAssetState
{
    public string Name;
    [Tag(TagType.URL)]
    public string URL;
}

public class OrientationState
{
    public Vector3 position;
    public Quaternion rotation;
    public OrientationState(Vector3 position, Quaternion rotation)
    {
        this.position = position;
        this.rotation = rotation;
    }
    public OrientationState()
    {
        this.position = Vector3.zero;
        this.rotation = Quaternion.identity;
    }
}

public class TransformState
{	
	public float posX;
	public float posY;
	public float posZ;
	
	public float rotX;
	public float rotY;
	public float rotZ;
	
	public float scaleX;
	public float scaleY;
	public float scaleZ;

    [JsonConstructor]
    public TransformState() {}
    
    public TransformState(Transform T)
    {
        Vector3 pos = T.position;
        posX = pos.x;
        posY = pos.y;
        posZ = pos.z;

        Vector3 rot = T.eulerAngles;
        rotX = rot.x;
        rotY = rot.y;
        rotZ = rot.z;

        Vector3 scale = T.localScale;
        scaleX = scale.x;
        scaleY = scale.y;
        scaleZ = scale.z;
    }

    public TransformState(Vector3 pos, Vector3 rot, Vector3 scale)
    {        
        posX = pos.x;
        posY = pos.y;
        posZ = pos.z;
       
        rotX = rot.x;
        rotY = rot.y;
        rotZ = rot.z;
        
        scaleX = scale.x;
        scaleY = scale.y;
        scaleZ = scale.z;
    }

    public Vector3 ToPosition()
    {
        return new Vector3(posX, posY, posZ);
    }

    public Vector3 ToRotation()
    {
        return new Vector3(rotX, rotY, rotZ);
    }

    public Vector3 ToScale()
    {
        return new Vector3(scaleX, scaleY, scaleZ);
    }
}

public class ColourState
{
	public float r, g, b;

    public ColourState() { }

    [JsonConstructor]
	public ColourState(float r, float g, float b)
	{
		this.r = r;
		this.g = g;
		this.b = b;
	}

    public ColourState(Colour c)
    {
        this.r = c.r;
        this.g = c.g;
        this.b = c.b;
    }

    public Colour ToColour()
    {
        return new Colour(r, g, b);
    }
}

public class VectorState
{
    public float x, y, z;

    public VectorState() { }

    [JsonConstructor]
    public VectorState(float x, float y, float z)
    {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public VectorState(Vector3 vector)
    {
        this.x = vector.x;
        this.y = vector.y;
        this.z = vector.z;
    }

    public Vector3 ToVector()
    {
        return new Vector3(x, y, z);
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
	public float StaticFriction = 0.4f; //The friction used when an object is laying still on a surface. Usually a value from 0 to 1. A value of zero feels like ice, a value of 1 will make it very hard to get the object moving.
	public float DynamicFriction = 0.4f; //The friction used when already moving. Usually a value from 0 to 1. A value of zero feels like ice, a value of 1 will make it come to rest very quickly unless a lot of force or gravity pushes the object.
	public float Bounciness = 0f; //How bouncy is the surface? A value of 0 will not bounce. A value of 1 will bounce without any loss of energy.
	public PhysicMaterialCombine FrictionCombine = PhysicMaterialCombine.Average; //How the friction of two colliding objects is combined. 0 = Average, 1 = Minimum, 2 = Maximum, 3 = Multiply.
	public PhysicMaterialCombine BounceCombine = PhysicMaterialCombine.Average; //How the bounciness of two colliding objects is combined. 0 = Average, 1 = Minimum, 2 = Maximum, 3 = Multiply.
}

public class CustomDeckState
{
    [Tag(TagType.URL)]
    public string FaceURL = "";
    [Tag(TagType.URL)]
    public string BackURL = "";
    public int? NumWidth;
    public int? NumHeight;
    public bool BackIsHidden = false; //Back of cards becames the hidden card when in a hand
    public bool UniqueBack = false; //Each back is a unique card just like the front
}

public class CustomImageState
{
    [Tag(TagType.URL)]
    public string ImageURL = "";
    [Tag(TagType.URL)]
    public string ImageSecondaryURL = "";
	public float WidthScale; //Holds the scaled size of the object based on the image dimensions
    public CustomDiceState CustomDice;
    public CustomTokenState CustomToken;
    public CustomJigsawPuzzleState CustomJigsawPuzzle;
    public CustomTileState CustomTile;
}

public class CustomAssetbundleState
{
    [Tag(TagType.URL)]
    public string AssetbundleURL = "";
    [Tag(TagType.URL)]
    public string AssetbundleSecondaryURL = "";
    public int MaterialIndex = 0; //0 = Plastic, 1 = Wood, 2 = Metal, 3 = Cardboard   
    public int TypeIndex = 0; //0 = Generic, 1 = Figurine, 2 = Dice, 3 = Coin, 4 = Board, 5 = Chip, 6 = Bag, 7 = Infinite   
    public int LoopingEffectIndex = 0;     
}

public class CustomDiceState
{
    public DiceType Type;
}

public class CustomTokenState
{
    public float Thickness;
    public float MergeDistancePixels;
    public bool Stackable = false;
}

public class CustomTileState
{
    public TileType Type; //0 = Box, 1 = Hex, 2 = Circle, 3 = Rounded
    public float Thickness;    
    public bool Stackable = false;
    public bool Stretch = false;
}

public class CustomJigsawPuzzleState
{
    public int NumPuzzlePieces = 80;
    public bool ImageOnBoard = true;
}

public class CustomMeshState
{
    [Tag(TagType.URL)]
    public string MeshURL = "";
    [Tag(TagType.URL)]
    public string DiffuseURL = "";
    [Tag(TagType.URL)]
    public string NormalURL = "";
    [Tag(TagType.URL)]
    public string ColliderURL = "";
	public bool Convex = true;
	public int MaterialIndex = 0; //0 = Plastic, 1 = Wood, 2 = Metal, 3 = Cardboard
    public int TypeIndex = 0; //0 = Generic, 1 = Figurine, 2 = Dice, 3 = Coin, 4 = Board, 5 = Chip, 6 = Bag, 7 = Infinite
	public CustomShaderState CustomShader; //Used to override the shader
    public bool CastShadows = true;
}

public class CustomShaderState
{
	public ColourState SpecularColor = new ColourState(0.9f, 0.9f, 0.9f);
	public float SpecularIntensity = 0.1f; 
	public float SpecularSharpness = 3f; //Range: 2 - 8
	public float FresnelStrength = 0.1f; //Range: 0 - 1
}

public class FogOfWarSaveState
{
    public bool HideGmPointer;
    public bool HideObjects;
    public float Height;
    public Dictionary<string, HashSet<int>> RevealedLocations;
}

public class FogOfWarRevealerSaveState
{
    public bool Active;
    public float Range;
    public string Color;
}

public class TabletState
{
    [Tag(TagType.URL)]
    public string PageURL = "";
}

public class ClockSaveState
{
	public ClockScript.ClockState ClockState;
	public int SecondsPassed = 0;
	public bool Paused = false;
}

public class CounterState
{
    public int value = 0;
}

public class Mp3PlayerState
{
    public string songTitle = "";
    public string genre = "";
    public float volume = 0.5f;
    public bool isPlaying = false;
    public bool loopOne = false;
    public string menuTitle = "GENRES";
    public Menus menu = Menus.GENRES;
}

public class CalculatorState
{
    public string value = "";
    public float memory = 0;
}

public class VectorLineState
{    
    public List<VectorState> points3;
    public ColourState color;    
    public float thickness = 0.1f;
    public VectorState rotation;
    public bool? loop;
    public bool? square;
}

public class CameraState
{
    public VectorState Position;
    public VectorState Rotation;
    public float Distance;
    public bool Zoomed = false;
}

public class JointState //http://docs.unity3d.com/ScriptReference/Joint.html
{ 	
	public string ConnectedBodyGUID = ""; //A reference to another rigidbody this joint connects to.
	public bool EnableCollision; //Enable collision between bodies connected with the joint.
	public VectorState Axis = new VectorState(); //The Direction of the axis around which the body is constrained.
	public VectorState Anchor = new VectorState(); //The Position of the anchor around which the joints motion is constrained.
	public VectorState ConnectedAnchor = new VectorState(); //Position of the anchor relative to the connected Rigidbody.
	public float BreakForce; //The force that needs to be applied for this joint to break.
	public float BreakTorgue; //The torque that needs to be applied for this joint to break.

	public void Assign(JointState jointState)
	{
		this.ConnectedBodyGUID = jointState.ConnectedBodyGUID;
		this.EnableCollision = jointState.EnableCollision;
		this.Anchor = jointState.Anchor;
		this.Axis = jointState.Axis;
		this.ConnectedAnchor = jointState.ConnectedAnchor;
		this.BreakForce = jointState.BreakForce;
		this.BreakTorgue = jointState.BreakTorgue;
	}
}

public class JointFixedState : JointState //http://docs.unity3d.com/ScriptReference/FixedJoint.html
{ 
}

public class JointHingeState : JointState //http://docs.unity3d.com/ScriptReference/HingeJoint.html
{ 
	public bool UseLimits;
	public JointLimits Limits; //Limit of angular rotation on the hinge joint. http://docs.unity3d.com/ScriptReference/JointLimits.html
	public bool UseMotor;
	public JointMotor Motor; //The motor will apply a force up to a maximum force to achieve the target velocity in degrees per second. http://docs.unity3d.com/ScriptReference/JointMotor.html
	public bool UseSpring;
	public JointSpring Spring; //The spring attempts to reach a target angle by adding spring and damping forces. http://docs.unity3d.com/ScriptReference/JointSpring.html
}

public class JointSpringState : JointState //http://docs.unity3d.com/ScriptReference/SpringJoint.html
{ 
	public float Damper; //The damper force used to dampen the spring force.
	public float MaxDistance; //The maximum distance between the bodies relative to their initial distance.
	public float MinDistance; //The minimum distance between the bodies relative to their initial distance.
	public float Spring; //The spring force used to keep the two objects together.
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
