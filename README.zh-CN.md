# 大肥鱼吃 Token（Big Fatty Fish Eats Token）

[English](README.md) | **中文**

一只蓝色大肥鱼在 Token 浪潮中穿梭的 H5 小游戏：点击让大肥鱼上浮，吃 HIT Token 得分，躲开 Bug。单 HTML 文件、零依赖、双击即玩。

![游戏画面预览](prev-play.png)

## 玩法说明

- 点击 / 触摸 / 按键让大肥鱼向上浮；
- 吃掉 **HIT Token** 得分，连续命中可触发热区加成；
- 避开 **Bug**，撞到会损失进度；
- 注意 **峰时 / 谷时**：不同时段 Token 与 Bug 的刷新密度、移动速度和命中率都会变化——峰时更刺激，谷时更从容。

## 操作方式

| 操作 | 输入 |
| ---- | ---- |
| 上浮 | 鼠标点击 · 手机触摸 · `Space` / `↑`（ArrowUp）/ `W` |
| 暂停 | `P` / `Esc` |
| 静音 | `M` |

## 运行方式

直接双击打开 `大肥鱼吃token.html` 即可游玩。游戏为单个自包含 HTML 文件，无外部依赖、无需构建，也适合直接部署到任意静态托管平台。

## 技术栈

- **Canvas 2D**：全部图形程序化绘制（固定时间步长 1/60 + 渲染插值）
- **WebAudio**：音效程序化合成，无需外部音频文件
- **原生 JavaScript**：无框架、无第三方库；图标与角色精灵以 Base64 内嵌

## 项目文件

- `大肥鱼吃token.html` —— 游戏本体（自包含单文件）
- `prev-*.png` —— 各界面预览截图
- `icon-source.png` —— 图标源图
- `build-icon.py` —— 由源图生成各尺寸图标（favicon / iOS 主屏图标）
- `apply-icon.py` —— 把生成的图标内联进游戏 HTML（需先运行 `build-icon.py`）

> 生成出来的各尺寸图标文件不随仓库提交，需要时运行上述两个脚本即可重现。

## 版权说明

“大肥鱼”形象为中文 AI 社区二创角色（源自社区对 DeepSeek 识别乌龙事件的二次创作），与 DeepSeek 官方无任何关联；本作不使用任何官方素材，全部图形由 Canvas 程序化绘制。

## 许可证

本项目以 MIT License 发布——详见 [LICENSE](LICENSE)。

Copyright © 2026 yuxuan-6
