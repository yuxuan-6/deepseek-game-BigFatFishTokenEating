"""从 prev-fish.png 生成 H5 游戏图标（favicon / 主屏图标）。
产出：icon-512.png, icon-192.png, icon-180.png, icon-128.png, favicon-32.png, favicon-16.png, icon-preview.png
"""
from PIL import Image, ImageDraw, ImageFilter
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "icon-source.png")

# 1) 裁剪：以角色面部为中心取正方形（左上留出头发，右侧留出尾巴弧线）
CROP_BOX = (12, 56, 232, 276)          # 220 x 220
SIZE = 512                             # 母版边长
RADIUS_RATIO = 0.22                    # 圆角半径

src = Image.open(SRC).convert("RGBA")
crop = src.crop(CROP_BOX).resize((SIZE, SIZE), Image.LANCZOS)

# 2) 圆形/圆角蒙版
mask = Image.new("L", (SIZE, SIZE), 0)
ImageDraw.Draw(mask).rounded_rectangle(
    (0, 0, SIZE - 1, SIZE - 1), radius=int(SIZE * RADIUS_RATIO), fill=255
)

base = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
base.paste(crop, (0, 0), mask)

# 3) 内描边：浅蓝细环，贴近游戏 UI 的高光色 #a9c6ff
ring = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
d = ImageDraw.Draw(ring)
w = max(2, SIZE // 128)
d.rounded_rectangle(
    (w, w, SIZE - 1 - w, SIZE - 1 - w),
    radius=int(SIZE * RADIUS_RATIO) - w,
    outline=(169, 198, 255, 110),
    width=w,
)
base = Image.alpha_composite(base, ring)

# 4) 导出多尺寸
outputs = {
    "icon-512.png": 512,
    "icon-192.png": 192,
    "icon-180.png": 180,
    "icon-128.png": 128,
    "favicon-32.png": 32,
    "favicon-16.png": 16,
}
for name, px in outputs.items():
    base.resize((px, px), Image.LANCZOS).save(os.path.join(HERE, name))
print("wrote:", ", ".join(outputs))

# 5) 预览图：棋盘底 + 实际尺寸并排
strip = Image.new("RGBA", (760, 340), (10, 14, 26, 255))
sd = ImageDraw.Draw(strip)
for i in range(0, 760, 20):
    for j in range(0, 340, 20):
        if (i // 20 + j // 20) % 2 == 0:
            sd.rectangle((i, j, i + 19, j + 19), fill=(18, 24, 40, 255))
x = 24
for px in (256, 128, 64, 32, 16):
    icon = base.resize((px, px), Image.LANCZOS)
    strip.alpha_composite(icon, (x, 42 + (256 - px) // 2))
    sd.text((x, 20), f"{px}px", fill=(169, 198, 255, 255))
    x += px + 28
strip.save(os.path.join(HERE, "icon-preview.png"))
print("wrote: icon-preview.png")
