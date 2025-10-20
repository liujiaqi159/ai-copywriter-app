# 📱 AI 文案助手（Android 项目包）

## 一、项目简介
这是一个使用 Python + Kivy 构建的 AI 文案助手 App，支持：
- 离线文案生成
- 一键复制功能
- 安卓打包运行

---

## 二、运行方式（PC端）
```bash
pip install kivy
python main.py
```

---

## 三、安卓打包说明
需要 Linux / WSL 环境：
```bash
sudo apt update
sudo apt install openjdk-11-jdk python3-pip git zip unzip
pip install buildozer
buildozer init
buildozer -v android debug
```

打包完成后生成：
```
bin/ai_copywriter-0.1-debug.apk
```
可直接安装在安卓设备。

---

## 四、项目结构
```
ai_copywriter_app/
├── main.py
├── ai_copywriter.py
├── buildozer.spec
└── README_build_instructions.md
```
