from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from ai_copywriter import offline_generate

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 10

    Label:
        text: "AI 文案助手"
        font_size: 26
        size_hint_y: None
        height: 50

    TextInput:
        id: brand
        hint_text: "输入品牌名"
        multiline: False

    TextInput:
        id: topic
        hint_text: "输入主题（如新品发布、活动宣传）"
        multiline: False

    Spinner:
        id: tone
        text: "选择语气"
        values: ["formal", "humorous", "youthful", "professional", "friendly"]

    Spinner:
        id: fmt
        text: "选择文案类型"
        values: ["ad", "social", "email", "video_script", "product_description"]

    Button:
        text: "生成文案"
        size_hint_y: None
        height: 50
        on_press: app.generate_copy()

    TextInput:
        id: output
        hint_text: "生成结果将在此显示"
        readonly: True
        size_hint_y: 3

    Button:
        text: "复制文案"
        size_hint_y: None
        height: 50
        on_press: app.copy_text()
'''

class CopyApp(App):
    def build(self):
        return Builder.load_string(KV)

    def generate_copy(self):
        brand = self.root.ids.brand.text.strip()
        topic = self.root.ids.topic.text.strip()
        tone = self.root.ids.tone.text
        fmt = self.root.ids.fmt.text
        if not brand or not topic or "选择" in tone or "选择" in fmt:
            self.root.ids.output.text = "⚠️ 请填写完整信息"
            return
        result = offline_generate(fmt, brand, topic, tone)
        self.root.ids.output.text = result

    def copy_text(self):
        text = self.root.ids.output.text
        if text:
            Clipboard.copy(text)
            self.root.ids.output.text = text + "\n\n✅ 已复制到剪贴板！"

if __name__ == "__main__":
    CopyApp().run()
