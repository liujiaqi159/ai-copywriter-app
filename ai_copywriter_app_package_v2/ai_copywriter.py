import random

def offline_generate(fmt, brand, topic, tone):
    templates = {
        "ad": [
            f"{brand}全新升级，让{topic}更高效！立即体验智能AI驱动的创作力量。",
            f"让{topic}更简单——{brand}AI助力，创意无限！",
        ],
        "social": [
            f"🔥 今天的灵感来自{brand}——让{topic}更有趣！#AI创作#",
            f"{brand}帮你轻松搞定{topic}，创作不设限 🚀",
        ],
        "email": [
            f"主题：{brand}新品上线，助你轻松搞定{topic}！",
            f"亲爱的用户，{brand}让{topic}更高效、更智能！",
        ],
        "video_script": [
            f"开场：镜头聚焦{brand}Logo。旁白：在{topic}的时代，AI为你而来。",
            f"画面：创作者灵感爆发。旁白：有了{brand}，{topic}从未如此简单。",
        ],
        "product_description": [
            f"{brand}是一款AI驱动的{topic}工具，帮助你快速生成优质内容。",
            f"通过{brand}，让{topic}的每一步都更智能、更精准。",
        ],
    }
    choices = templates.get(fmt, ["AI文案生成中..."])
    return random.choice(choices)
