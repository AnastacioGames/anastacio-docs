---
title: Exporting your game
description: How to turn your .range into a game other people can play, on PC, in the browser or on a phone.
---

All export options live in the same tab: **Properties > Export Game** (the box icon in the tab column on the right). It has three panels, one per target.

| Target | Panel | Output | When to use |
|---|---|---|---|
| PC (Windows and Linux) | **Export (RangeArmor)** | `release/` folder with the game executable | To ship on itch.io, Steam or as a zip |
| Browser | **Web** | Folder with `index.html` and the WebGL 2 runtime | To play on a website, no install needed |
| Android phone | **Android (Web)** | `.apk` file (plus `.aab` for Google Play) | To install on a phone or publish on the store |

Android reuses the Web package: the APK is an app that runs the Web version of the game inside it. So **anything that works on Web works on Android**, and Web warnings apply to both.

## Always, before exporting

1. **Save the file** (`Ctrl+S`). All three exports use the `.range` saved on disk, not what is open on screen.
2. **Test with P** in the editor. If the game doesn't run in the editor, it won't run exported.
3. Use **relative paths** for textures, sounds and scripts (`//textures/...`). An absolute path (`C:\Users\...`) only exists on your PC.

## Guides

- [Export to PC with RangeArmor](../rangearmor/)
- [Export to the browser (Web/WebGL)](../web/)
- [Export to Android (APK and .jks key)](../android/)
