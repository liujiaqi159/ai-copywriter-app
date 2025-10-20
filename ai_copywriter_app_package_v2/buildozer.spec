[app]
# 应用信息
title = AI Copywriter
package.name = ai_copywriter
package.domain = org.example

# 入口文件（main.py）
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
main = main.py

# 使用的依赖
requirements = python3,kivy

# 权限与方向
orientation = portrait
android.permissions = INTERNET

# 图标（可选，如果没有图标文件，可以留空）
# icon.filename = %(source.dir)s/data/icon.png

# 是否全屏
fullscreen = 0

# 版本号
version = 0.1

# Android 打包选项
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.debug = True  # 使用默认 debug 签名

# 允许 Buildozer 自动下载 Android SDK / NDK
android.sdk_path = ~/.buildozer/android/platform/android-sdk
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b

# log 等级
log_level = 2

# 保留的文件
include_exts = py,png,jpg,kv,atlas

# 禁用 logcat 自动打开（GitHub Actions 无交互）
logcat_filter = *

[buildozer]
log_level = 2
warn_on_root = 1
