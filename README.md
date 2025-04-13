# Reconstructed Hexen ACS source code

[Hexen](https://doomwiki.org/wiki/Hexen)'s most notable innovation was to add
scripting to the Doom engine via the
[Action Code Script](https://doomwiki.org/wiki/ACS) (ACS) programming language.
Although Hexen itself
[is open source](https://doomwiki.org/wiki/Raven_source_code_licensing), the
ACS source code to the game's scripts was never released.

This is therefore a project to reconstruct those scripts. The
[DEACC](https://doomwiki.org/wiki/DEACC) decompiler has been able to decompile
them for many years, but the resulting source code lacks any comments or
meaningful variable names. This project is building on the decompiled source
code to add these back. The goal is to produce source code that Doom / Hexen
modders can study when making their own levels.

The source here compiles exactly back to the BEHAVIOR lumps found in the Hexen
IWAD. Credit for this goes to Luc Cluitmans, the author of DEACC. There are
continuous integration checks to ensure any changes do not break this. 

## Status

### Hub 1: Seven Portals

|  Map                       | Bug  | Status |
| ------------------------- | ---- | ------ |
| [MAP01](map01.acs) (Winnowing Hall) | fragglet/hexen-acs-reconstructed#32 | In progress (partially complete) |
| [MAP02](map02.acs) (Seven Portals) | fragglet/hexen-acs-reconstructed#1 | TODO |
| [MAP03](map03.acs) (Guardian of Ice) | fragglet/hexen-acs-reconstructed#2 | TODO |
| [MAP04](map04.acs) (Guardian of Fire) | fragglet/hexen-acs-reconstructed#3 | TODO |
| [MAP05](map05.acs) (Guardian of Steel) | fragglet/hexen-acs-reconstructed#4 | TODO |
| [MAP06](map06.acs) (Bright Crucible) | fragglet/hexen-acs-reconstructed#5 | TODO |

### Hub 2: Shadow Wood

| Map                       | Bug  | Status |
| ------------------------- | ---- | ------ |
| [MAP08](map08.acs) (Darkmere) | fragglet/hexen-acs-reconstructed#7 | TODO |
| [MAP09](map09.acs) (Caves of Circe) | fragglet/hexen-acs-reconstructed#8 | TODO |
| [MAP10](map10.acs) (Wastelands) | fragglet/hexen-acs-reconstructed#9 | TODO |
| [MAP11](map11.acs) (Sacred Grove) | fragglet/hexen-acs-reconstructed#10 | TODO |
| [MAP12](map12.acs) (Hypostyle) | fragglet/hexen-acs-reconstructed#11 | TODO |
| [MAP13](map13.acs) (Shadow Wood) | fragglet/hexen-acs-reconstructed#12 | TODO |

### Hub 3: Heresiarch's Seminary

| Map                       | Bug  | Status |
| ------------------------- | ---- | ------ |
| [MAP27](map27.acs) (Heresiarch's Seminary) | fragglet/hexen-acs-reconstructed#19 | TODO |
| [MAP28](map28.acs) (Dragon Chapel) | fragglet/hexen-acs-reconstructed#20 | TODO |
| [MAP30](map30.acs) (Griffin Chapel) | fragglet/hexen-acs-reconstructed#21 | TODO |
| [MAP31](map31.acs) (Deathwind Chapel) | fragglet/hexen-acs-reconstructed#22 | TODO |
| [MAP32](map32.acs) (Orchard of Lamentations) | fragglet/hexen-acs-reconstructed#23 | TODO |
| [MAP33](map33.acs) (Silent Refectory) | fragglet/hexen-acs-reconstructed#24 | TODO |
| [MAP34](map34.acs) (Wolf Chapel) | fragglet/hexen-acs-reconstructed#25 | TODO |

### Hub 4: Castle of Grief

| Map                       | Bug  | Status |
| ------------------------- | ---- | ------ |
| [MAP21](map21.acs) (Forsaken Outpost) | fragglet/hexen-acs-reconstructed#13 | TODO |
| [MAP22](map22.acs) (Castle of Grief) | fragglet/hexen-acs-reconstructed#14 | TODO |
| [MAP23](map23.acs) (Gibbet) | fragglet/hexen-acs-reconstructed#15 | TODO |
| [MAP24](map24.acs) (Effluvium) | fragglet/hexen-acs-reconstructed#16 | TODO |
| [MAP25](map25.acs) (Dungeons) | fragglet/hexen-acs-reconstructed#17 | TODO |
| [MAP26](map26.acs) (Desolate Garden) | fragglet/hexen-acs-reconstructed#18 | TODO |

### Hub 5: Necropolis

| Map                       | Bug  | Status |
| ------------------------- | ---- | ------ |
| [MAP35](map35.acs) (Necropolis) | fragglet/hexen-acs-reconstructed#26 | TODO |
| [MAP36](map36.acs) (Zedek's Tomb) | fragglet/hexen-acs-reconstructed#27 | TODO |
| [MAP37](map37.acs) (Menelkir's Tomb) | fragglet/hexen-acs-reconstructed#28 | TODO |
| [MAP38](map38.acs) (Traductus' Tomb) | fragglet/hexen-acs-reconstructed#29 | TODO |
| [MAP39](map39.acs) (Vivarium) | fragglet/hexen-acs-reconstructed#30 | TODO |
| [MAP40](map40.acs) (Dark Crucible) | fragglet/hexen-acs-reconstructed#31 | TODO |

## How to help

You don't need to be an expert programmer or reverse engineer to help out.
Pick one of the levels above and start documenting! Before you start, make sure
to comment first on the associated tracking bug for that level to avoid
duplicating others' work.

Before each script, you'll find that header comments have been automatically
added that look like this:
```c
// Started by line 527 at (1576, 2112)
// Started by thing 203 at (1280, 1904)
script 7 (void)
{
```
These comments give helpful context about what the particular script does.
Open up your favorite level editor and locate the named line or thing.
Provided you've played the level before, it usually isn't difficult to find
out what the script is used for within the level. Once you've figured it out,
**replace** the original comments with one that describes what the script
does in plain English. For example:
```c
// Script 7 opens the doors to the four little alcoves surrounding the
// teleporter in the main hall (each contains an Ettin). It is triggered by
// lines surrounding the teleporter if the player gets too close to it.
script 7 (void)
```
Besides commenting, another goal is to give variables more meaningful names --
most importantly, the map variables that are shared between scripts. The
autogenerated names are all of the form `var1` (local variables) or `mapvar1`
(map variables). [Here's an example](https://github.com/fragglet/hexen-acs-reconstructed/commit/769cce64d49dc7c2d)
of a change that added more meaningful names.
