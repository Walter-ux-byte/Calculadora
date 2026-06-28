[app]

title = Calculadora
package.name = calculadora
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 0.1

requirements = python3,hostpython3,kivy,pillow

presplash.filename = %(source.dir)s/calcu.jpeg
icon.filename = %(source.dir)s/calcu.jpeg

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 24

# SOLUCIÓN CLAVE: Cambiado de '25b' a la versión textual completa requerida por el compilador
android.ndk = 25.2.9519653
android.ndk_api = 24

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false

[buildozer]
log_level = 2
warn_on_root = 1
