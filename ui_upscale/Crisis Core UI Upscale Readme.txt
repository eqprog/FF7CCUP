---
Introduction:
---
I wanted to play Crisis Core: Final Fantasy 7 using PPSSPP, with higher resolution. Upon loading the game, I noticed the UI was, of course, not scaling well for the increased resolution of a PC, causing intense pixelization. While this is to be expected, I decided to maybe try to clean up the game's text a little, maybe make things a little clearer.

This turned into a months long project, trying to redraw or replace every portion of the UI with higher resolution equivalents. As I'm not an artist, most of the actual icons were taken from other places, or redrawn to at least resemble their original counterparts. The lack of discernible detail in many items forced me to try to rebuild them from scratch, recreating what I assumed they were supposed to look like. Particularly, the background for the Materia Fusion screen was incredibly difficult, to the point I simply redesigned it entirely.

This is not by any means perfect, or even entirely finished. Unfortunately, while taking a break from the project after essentially completing its current incarnation, the laptop I was using failed. I have since been able to move to another laptop, and retrieved everything, but that fact made me wish to release what I had now, just in case. So, I hope this is of some use to someone, even in its less-than-perfect state.

---
Installation
---

1. Load your Crisis Core ISO in PPSSPP. This will create the necessary folder structure.

2. Extract the ZIP into %UserProfile%\Documents\PPSSPP\PSP\TEXTURES\ULUS10336. If this folder doesn't exist, create it. PPSSPP should have at least created the PPSSPP\PSP folder.

3. In PPSSPP's settings, go to Tools on the left, followed by Developer Tools, and then ensure the bottom option, "Replace Textures", is checked.

4. Run the game. The first noticeable change should be on the main title screen, if you notice the game has clearer text for menu options there, you should be good to go.

---
Extras
---

Recreating the Materia Fusion background, I was unsure if the circuitry pattern still fit or not. By default, the background without circuitry is installed. Versions both with and without are included in separate, labelled folders. If you wish to swap one for the other, simply copy the files inside the labelled folder, and overwrite the ones in the TEXTURES\ULUS10336 folder with them.

---
Known Issues
---

This pack is not fully tested, and not 100% polished. There are minor alignment issues with some portions of the UI, things I am still trying to adjust. I have minimized as much as I can, but work is ongoing. In addition, the pack was designed on and for a resolution of 1920x1080. Higher or lower resolutions may have oddities, or look less clear. I may have missed one or two files; the game loads textures on demand, and thus until I reach a portion of the game that uses a piece of the UI, its file won't load.

The text for dialog gave me many problems; my first attempt at replacing it involved pasting in another font entirely, changing each character in the font image file separately. The resulting letters, while clearer, had a myriad of issues.

My next attempt involved trying to fix those issues one letter at a time, leading to text that was technically better, but looked incredibly awkward. So far as I can tell, the game doesn't simply print a letter 1:1 from the font map. It tries to adjust for width and position. This means that if the text is shaped differently, it can lead to odd results.

My current attempt threw external fonts out the window, and I simply attempted to recreate the letters in place, with clearer lines. This seems to be the best solution for the moment, and while the letters look a little awkward, they behave much better.

Due to my lack of artistic skill, I can't recreate icons that aren't mostly geometric shapes. Envelope and folder icons and the like, I feel I was able to make something passable. For things like bracers, shop icons, potions, I wasn't able to do as well. So, icons were pulled from other sources, and adjusted to try to fit. I think I have an alright selection here, but there are clear differences in design that I can't really resolve due to being unable to replicate the originals.

A lack of high quality and matching art for DMW profiles leads to most of them being sourced from the highest resolution in-game cut-ins they have. Thus, while smaller portraits look better, larger ones are simply scaled a bit.

Not every effect is present, or rescaled. The Pause icon, for instance, was never finished. Thus, as a place holder, I used an original scale Pause icon with the rest of the image file expanded to fill space. The result is a relatively tiny Pause icon at the original resolution, which looks surprisingly clear in higher resolutions. Meanwhile, some of the fog in the Materia Fusion screens refused to function correctly, and was entirely removed.

---
Credits
---

Shin-Ra logos, Save Point logos, and the SOLDIER logo were taken and modified from work done by Phil Strahl, gas01line on deviantArt.

https://gas01ine.deviantart.com/

Most item and equipment icons were taken and modified from Breath of Fire 6 on mobile, by Capcom.

A few others were taken and modified from other mobile games, though I don't have the list with me right now.

Various other icons were taken and modified from free images on the internet, particularly the Materia orbs and the Genji equipment helm.

The pointing finger icon was sourced from Final Fantasy XIII.

Art for Zack was taken from Square Enix promotional materials for Crisis Core.

Portions of the UI were taken and modified from Crisis Core itself, because obviously.

All other art, so far as I know, was created by me, Kaosu Reido, for this project.

All rights reserved by the content's original creators, don't pay for this work anywhere, all usage is unofficial, etc etc etc. Feel free to modify anything you find here, though please provide credit where it is due. Thank you.