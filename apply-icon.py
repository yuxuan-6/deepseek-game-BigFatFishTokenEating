"""把生成好的图标内联进 大肥鱼吃token.html 的 <head>。
- favicon 用 128px PNG 的 data URI（单文件游戏，保持零外部依赖）
- apple-touch-icon 同时输出 180px data URI，供 iOS 添加到主屏时使用
可重复执行：每节内容由注释标记包裹，重跑只替换标记内部，不会重复追加。
"""
import base64
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, "大肥鱼吃token.html")
BEGIN = "<!-- ICON:BEGIN (由 build-icon.py 生成，请勿手改) -->"
END = "<!-- ICON:END -->"


def data_uri(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")


def wrap(raw, indent="  ", width=76):
    """把长 data URI 折行，便于在编辑器里阅读（URI 中不含空白，换行不影响解析）。"""
    head = "data:image/png;base64,"
    b64 = raw[len(head):]
    lines = [head + b64[i:i + width] for i in range(0, len(b64), width)]
    # 折行只为可读：正文行不再重复 data: 前缀，浏览器把整段 href 当一条 URI
    lines[1:] = [ln[len(head):] for ln in lines[1:]]
    return ("\n" + indent).join(lines)


block = "\n".join([
    BEGIN,
    '  <link rel="icon" type="image/png" sizes="128x128" href="' + wrap(data_uri(os.path.join(HERE, "icon-128.png"))) + '">',
    '  <link rel="apple-touch-icon" sizes="180x180" href="' + wrap(data_uri(os.path.join(HERE, "icon-180.png"))) + '">',
    END,
])

with open(HTML, encoding="utf-8") as f:
    html = f.read()

# 先移除旧块（含上一次运行写入的内容），再插入到 <title> 之后
html = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?", "", html, flags=re.S)

anchor = "<title>大肥鱼吃 Token</title>\n"
assert anchor in html, "找不到标题锚点"
html = html.replace(anchor, anchor + block + "\n", 1)

with open(HTML, "w", encoding="utf-8", newline="\n") as f:
    f.write(html)

print("injected icon block, html size =", os.path.getsize(HTML), "bytes")
