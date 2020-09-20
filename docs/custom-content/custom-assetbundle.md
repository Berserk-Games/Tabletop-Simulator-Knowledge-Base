> View the [AssetBundles Tutorial Video](/getting-started/video-tutorials#custom-asset-bundles)

An AssetBundle is the most advanced, fully featured asset type for Tabletop Simulator. An asset is created in Unity, and then exported in a special format to be imported into your game.

<center>![Example Asset Bundle in Unity](/img/custom-assetbundle/example.gif)</center>


##AssetBundle Features
AssetBundles can do many things other custom Objects cannot.

* Customizable physics sounds
* Access to the full array of Unity materials
* Play custom sounds
* Triggerable animations and looping animations
* Particles
* Lights
* *And more*

Basically, if you can make the object in Unity using all of the default resources available, you can import it into your game.

---


##Instructions
In order to create an AssetBundle, you will need to:

* [Download/Install Unity](#install-unity)
* [Download GitHub Project file](#download-project)
* [Open project file in Unity](#open-project)
* [Create Asset using Unity](#create-asset)
* [Export to AssetBundle](#export-assetbundle)
* [Import in Tabletop Simulator](#import-assetbundle)

Follow the instructions for each step closely.

###Install Unity
The first thing you need is Unity. But not just any version of Unity, it needs to be **[Unity 2019.1.14f1](https://unity3d.com/get-unity/download/archive)**.

You want the **installer**.

!!!warning "Wrong Unity Version"
    Using the wrong version of Unity will result in possible issues in your exported AssetBundles, if it works at all.

Run the installer and you will be asked which components to include. Be sure **Windows, Linux and Mac** are all checked.

<center>![Unity Installer](/img/custom-assetbundle/unity-install.png)</center>

###Download Project
Download the project file from **[GitHub](https://github.com/Berserk-Games/Tabletop-Simulator-Modding)**.

<center>![Github Download](/img/custom-assetbundle/github-download.png)</center>

If needed, unzip the files, and then place them into the directory of your choice.

###Open Project
Run Unity. A window opens, asking if you want to create a new project or open one.

Select **Open** and choose the folder obtained from GitHub.

<center>![Opening the Project](/img/custom-assetbundle/unity-run.png)</center>

###Create Asset
Any number of methods can be used to create an Asset, so the steps you take here are based on the end-result of what you are trying to make.

####Asset Examples
The project file contains some examples of assets as well as an example scene that matches the Museum background's lighting.

<center>![Project Examples](/img/custom-assetbundle/unity-examples.png)</center>

You are not required to use any of these when creating your asset.

####Example Asset Creation
You can create any asset, but here is an example of basic asset creation.

<center>![Creation: Step 1](/img/custom-assetbundle/create1.png)</center>

<center>![Creation: Step 2](/img/custom-assetbundle/create2.png)</center>

<center>
    <video controls
        loop
        autoPlay
        muted
        src="/img/custom-assetbundle/create3.webm">
        Sorry, your browser doesn't support embedded videos.
    </video>
</center>

####Optional Scripts
There are 2 scripts included which you can add to Assets you create.

* **TTSAssetBundleEffects**: In Tabletop Simulator, this will add an option in the Object's context menu. There are two types:
    * *Trigger*: Used to activate animations, sounds, lights, etc that run once and stop.
    * *Looping*: Used to activate animations, sounds, lights, etc that continue running until another Loop is activated.
* **TTSAssetBundleSounds**: In Tabletop Simulator, this lets you replace the sound that this Object would make with custom sounds.

In Tabletop Simulator, Lua scripting is able to interact with these triggers. However you are not able to create/add your own Unity scripts to Objects.

###Export AssetBundle
Once you are finished creating your asset, you must turn it into a pre-fab.

<center>
    <video controls
        loop
        autoPlay
        muted
        src="/img/custom-assetbundle/prefab.webm">
        Sorry, your browser doesn't support embedded videos.
    </video>
</center>

Give it a unique name.

<center>
    <video controls
        loop
        autoPlay
        muted
        src="/img/custom-assetbundle/name.webm">
        Sorry, your browser doesn't support embedded videos.
    </video>
</center>

Then Build the AssetBundle by right-clicking anywhere in the project view and selecting **Build AssetBundles**.

<center>![Build AssetBundle](/img/custom-assetbundle/build.png)</center>

The resulting file that is created will be found in the Project folder under *AssetBundles*.

> The file format for an AssetBundle is `.unity3d`

<center>![AssetBundle location](/img/custom-assetbundle/bundle-location.png)</center>

###Import AssetBundle
Open Tabletop Simulator and upload your AssetBundle to a webhost or the in-game [Steam Cloud](cloud-manager).

!!!warning "Importing Assets"
    How you choose to import files impacts if other players can see them when you're finished.<br>For help with importing, visit [Asset Hosting](asset-importing).

<center>
    <video controls
        loop
        autoPlay
        muted
        src="/img/custom-assetbundle/import-assetbundle.webm">
        Sorry, your browser doesn't support embedded videos.
    </video>
</center>

---


##Secondary AssetBundles
Secondary AssetBundles are an additional AssetBundle which are great for shared effects like sound or particle effects that you want to use on multiple objects without duplicating them in each individual asset bundle. Great for reducing memory and bandwidth usage.

<center>![Secondary AssetBundle](/img/custom-assetbundle/secondary.png)</center>

In the example below, the main AssetBundle is the blue capsule and the secondary AssetBundle is the explosion and light effect. This allows you to reuse the explosion and light effect on any one of your AssestBundles for greater modularity and reduced memory and bandwidth usage.

<center>
    <video controls
        loop
        autoPlay
        muted
        src="/img/custom-assetbundle/secondary-example.webm">
        Sorry, your browser doesn't support embedded videos.
    </video>
</center>

---


##Best Practices
* Avoid duplicating large assets like textures and sounds on multiple AssetBundles by using Secondary AssetBundles.
* Don’t use legacy, mobile, or custom shaders because they will most likely show up as pink on other platforms.

###Texture Import Settings
* If your textures don’t need transparency, use RGB Compressed DXT1.
* If your textures need alphas retained, highlight just those textures and change the format to RGBA Compressed DXT5.
* NEVER use uncompressed textures.
* Make sure the texture is the size that makes sense for it, but watch out for the size of the texture as that will eat up a lot of space.
* Save 4k textures for large boards and other similar items.

###Tutorials
* [Unity Manual](https://docs.unity3d.com/Manual/UnityManual.html)
* [Unity Tutorials](https://unity3d.com/learn/tutorials)
* [Lighting and Rendering](https://unity3d.com/learn/tutorials/s/graphics)
* [Animation](https://unity3d.com/learn/tutorials/s/animation)


---
