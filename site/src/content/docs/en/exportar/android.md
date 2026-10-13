---
title: Export to Android
description: Step by step to build the APK, install it on your phone, create the .jks key and publish on Google Play.
---

Android export builds an **APK**: an app that runs the [Web](../web/) version of the game inside it, offline, with no internet needed. So set up and validate Web first: its touch controls and warnings apply here too.

## 1. What to install first

The engine does **not** ship the Android tools. Install them once:

1. **[Android Studio](https://developer.android.com/studio)**. It brings the **JDK** (Java) and the **Android SDK**, the two things the engine needs.
2. Open Android Studio once and let it finish downloading the SDK.
3. In **Tools > SDK Manager > SDK Platforms**, install **Android SDK Platform 37**.

The engine finds Android Studio by itself (it also checks `JAVA_HOME` and `ANDROID_HOME`). If it's somewhere else, point to the folders in **Tools > JDK** and **Android SDK** in the panel.

## 2. Open the panel

**Properties > Export Game > Android (Web)**.

![Panel android](../../../../assets/exportar/android_en.png)

## 3. App

| Field | What it does |
|---|---|
| **App ID** | Unique app identity, like `com.yourname.yourgame` (letters, numbers and `_`, separated by dots; each part starts with a letter). |
| **App name** | Name shown under the icon. Empty uses the file name. |
| **App version** | Version the player sees, for example `1.0`. |
| **Version code** | Whole number. **Increase it with every new version** (1, 2, 3...), or the phone refuses the update. |
| **App icon** | Square PNG, ideally 512×512. Empty uses the Android default icon. |
| **Screen orientation** | **Automatic** (rotates with the phone), **Landscape** or **Portrait**. |

:::caution
**Never change the App ID after publishing.** Android would treat it as a different app: players would get two icons and lose their save.
:::

## 4. Build

- **Build type**:
  - **Debug (testing)**: for testing on **your** phone. No key needed. Use it while developing.
  - **Release (players)**: final version, signed with your key. Use it to ship.
- **Destination**: folder for the APK, report and log (default `//android/`).
- **Touch controls**: the same on-screen controls as the Web panel.

## 5. The signing key (.jks)

Only needed for **Release**. Every Android app must be signed, and **every update must be signed with the same key** as the first release.

**You don't need to get this file from anywhere: the engine creates it for you.**

1. Set **Build type** to **Release (players)**. The **Release Signing** box appears.
2. Fill in:
   - **Key alias**: name of the key inside the file. You can keep `upload`.
   - **Key password**: a password with **at least 6 characters**.
3. Click **Create key**.

The engine uses the JDK's `keytool` to generate the key (RSA 4096, valid for about 27 years) and fills in the **Signing key** field. If you left that field empty, the file goes to:

```
C:\Users\<you>\RangeAndroidKeys\<App ID>.jks
```

To choose another location, fill **Signing key** with the file path **before** clicking **Create key**. The engine never overwrites an existing key.

:::danger[Back up the key and the password]
Copy the `.jks` to a USB drive or cloud storage and write the password down somewhere safe. **If you lose either one, you can no longer update the game**: you'd have to publish it as a new app, and players would lose their save. Don't keep the key inside the project or in Git.
:::

Already have a `.jks` from another game or from Android Studio? You can use it: point **Signing key** to it and fill in its alias and password.

The password is not saved in the `.range`. After reopening the engine, type it again before building.

## 6. Build the APK

Click **Build APK**. The engine saves the file and runs Gradle in the background (the first time takes longer because it downloads dependencies). Progress shows in the panel.

The output goes to **Destination**: the `.apk`, `android-report.json` and `gradle.log` (open this one if something goes wrong).

**Also build AAB (Google Play)**: also builds the `.aab`, the format **Google Play requires**. The APK is still built so you can install it on your phone.

## 7. Install on your phone

1. On the phone, enable **Developer options** (in *About phone*, tap *Build number* 7 times) and, inside them, **USB debugging**.
2. Connect the phone to the PC with a USB cable and accept the *"Allow USB debugging?"* prompt on the phone.
3. Click **Install on phone**. The game installs and opens by itself.

You can also copy the `.apk` to the phone and open it from the file manager (Android asks you to allow "unknown sources").

## 8. Publish on Google Play

1. Build in **Release** with **Also build AAB** on.
2. In the [Google Play Console](https://play.google.com/console), create the app and upload the `.aab`.
3. The first time, accept **Play App Signing**: Google keeps the final key and your `.jks` becomes the *upload key*. Keep your backup anyway.
4. For each update: increase the **Version code**, build again with the **same key** and upload the new `.aab`.

## Common problems

| Message | Fix |
|---|---|
| *JDK and Android SDK not found* (or *JDK not found*) | Install Android Studio or point to the folders in **Tools**. |
| *The Android SDK ... does not have platform 37* | Android Studio > SDK Manager > install **Android SDK Platform 37**. |
| *No phone connected* | USB cable plugged in and **USB debugging** on. Try another cable: some only charge. |
| *The phone did not authorize this computer* | Unlock the phone and accept the USB debugging prompt. |
| *The phone already has ... signed with another key* | The phone has a version signed with another key (for example, the Debug one). Uninstall it and install again. |
| *The phone has a newer version* | Increase the **Version code**. |
| Password or alias error when building | The password or alias doesn't match the `.jks`. |
