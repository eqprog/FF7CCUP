<img src="https://github.com/eqprog/FF7CCUP/blob/master/logo.png?raw=true" align=center>

All are welcome to participate so long as any submitted artwork is your own. *Do not source images from outside sources without license.*

View current progress or leave feedback here: <a href="http://forums.qhimm.com/index.php?topic=20208.0">http://forums.qhimm.com/index.php?topic=20208.0</a>
Or, participate in our <a href="https://discord.gg/HHMC2UBq4s">Discord Server.</a>

## New! Download the latest release from the official site! <a href="http://eqprog.com/">Visit eqprog.com</a>

# Setting up FF7CCUP

## Part One: Getting the Emulator set up & Finding texture path

1) Download PPSSPP - https://www.ppsspp.org
2) Add FF7CC to PPSSPP's Game Library using the "Games" tab.
3) Run FF7CC.
4) While the game is running, press ESC to open the PPSPP menu.
5) Open Settings>Tools>Developer Tools
6) Check "Replace Textures"
7) Select "Create/Open textures.ini file for current game". This should open up in your default text editor.
8) The textures.ini file will open in your default text editor. Find the directory of this file by using File>Save As and copying the path that shows up.
9) The directory should be something like `C:\Users\<user>\Documents\PPSSPP\PSP\TEXTURES\ULUS10336` If the directory does not end with `ULUS10336`, your version of Crisis Core is incompatible! (Try the US version instead)

## Part Two - Option 1 - Setting up with Github Desktop
*Note: If you prefer using commandline then I'm assuming you know how to do this on your own.*

1) Download and install Github desktop - https://desktop.github.com
2) Log in to your github account.
3) Clone the FF7CCUP Repository (File> Clone Repository)
4) Paste in "https://github.com/eqprog/FF7CCUP" for the source URL
5) Use your "Game Directory" for the 'Local Path'. It should be similar to 'C:\Users\[local user]\Documents\PPSSPP\PSP\TEXTURES\ULUS10336\' If you can't find this folder, please make sure you follow the steps in part one as it will generate these directories for you.
6) Press the blue "Clone" button and let Github Desktop do its thing.
7) Restart the game in PPSSPP, if it is currently open

You should now be able to enjoy the FF7CC Upscale Project mod!

#### Updating FF7CCUP with Github Desktop:
Easy. Just open up Github Deskop. Make sure you're on the FF7CCUP Repo if you have others installed, then click "Fetch Origin". This will download any changes that have been uploaded recently.


## Part Two - Option 2 - Manual Download

1) Download this repository as a zip (Code -> Download ZIP)
2) Extract the contents of the zip into the folder from part one (should be a folder called `ULUS10336`)
3) Restart the game in PPSSPP, if it is currently open

You should now be able to enjoy the FF7CC Upscale Project mod!

**To update using this method, you will need to re-download the entire repository. For this reason, it is not recommended to use this method on slow or metered internet connections.**

# Extras
## (Optional) Mods
A few additional texture mods are available.
- Remove accessible zone gems
- Remove slash effects
- Transparent UI
- Xbox Button Propts
These mods are stored in the `mods` folder. 
To install a mod, simply copy the files within the mod's folder to the proper directory in your textures folder *(from installation part one)*

## (Optional) Linear Texture Filtering
**If you are confused, just leave this on Auto and ignore this section!**

PPSSPP features an option to override texture filtering so that all textures are filtered linearly. This has a few benefits.
- Prerendered cutscenes look much better (they are not upscaled, but will no longer be pixelated)
- UI scales much better, especially to resolutions above 1080p
- Some in-game effects (like fire) look better

However, the game was not intended to be run in this mode, so there are also some issues.
- Slivers of incorrect textures will render on the edges of some UI elements
- Some parts of the UI will not connect properly (mostly fixed)
- Colored boxes appear behind numbers on the ui (fixed)
This texture pack fixes most issues with linear filtering, however some still remain. 

To change the texture filtering mode, go to the PPSSPP settings for Crisis Core and select the Texture filtering option. Use 'Linear' for linear filtering, or 'Auto' for normal filtering. Try both options and see which you prefer.
  
## Low Performance / Troubleshooting
The textures in this pack are much higher resolution that the orginals, and may cause performance issues with some configurations.

If you have issues with performance, try the following _(in recommended order)_:
1. In the PPSSPP settings for Crisis Core, go to Graphics and set the following settings:
  - Software rendering (slow) -> OFF
  - Postprocessing shader -> OFF
  - Upscale level -> OFF _This is not the same as the mod, and will absolutely kill performance!_
  - Render duplicate frames to 60 Hz -> ON _This should make performance much smoother on 30fps games like Crisis Core_
  - Lazy texture cache -> ON
  - VSync -> OFF
  
2. In the PPSSPP settings for Crisis Core, go to System and set "I/O timing method" to "Host (bugs, less lag)" Make sure "I/O on thread" and "Fast memory" are also enabled.

3. Ensure that PPSSPP, the game, and the texture folder are all stored on your fastest drive. In most cases, this will be your C: drive on windows and your internal storage on other systems.

4. In the PPSSPP settings, go to Graphics and try each option for backend (Vulkan is most likely to be the fastest, but it depends on device)
