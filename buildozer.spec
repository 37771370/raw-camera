[app]
# (str) Title of your application
title = 原图直出相机

# (str) Package name
package.name = rawcamera

# (str) Package domain (needed for android/ios packaging)
package.domain = org.rawcamera

# (str) Source files where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude
#source.exclude_exts = spec

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,numpy,opencv-python-headless,pillow

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of allowed (x, y) screen coordinates
#fullscreen = 0

# 
# Android specific
#

[android]

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (#ffffff or #RRGGBBAA format).
#presplash_color = #ffffff

# (list) Permissions
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
#android.api = 31

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) Whether to bundle the Python runtime in the APK
# android.bundle_python_libs = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = arm64-v8a, armeabi-v7a

# 
# iOS specific
#

[ios]

#
# Mac specific
#

[mac]
