[app]

title = Tic Tac Toe
package.name = tictactoe
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.kivy_version = 2.2.0
fullscreen = 0

# Android specific
android.api = 33
android.minapi = 21
android.ndk = 28c
android.ndk_api = 21
android.sdk = 33
android.build_tools = 33.0.0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
