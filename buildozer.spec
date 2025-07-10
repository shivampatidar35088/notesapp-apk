[app]
title = Notes App
package.name = notesapp
package.domain = org.notesapp
source.dir = .
source.include_exts = py,json
version = 1.0
requirements = python3,kivy,kivymd
orientation = portrait
fullscreen = 1
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
