# Big Fatty Fish Eats Token (大肥鱼吃 Token)

**English** | [中文](README.zh-CN.md)

A single-file H5 game: a chubby blue fish darts through a stream of Tokens — tap to make it swim upward, eat **HIT Tokens** to score, and dodge the **Bugs**. One HTML file, zero dependencies, double-click to play.

![Gameplay preview](prev-play.png)

## Gameplay

- Click / tap / press a key to make the fish swim upward;
- Eat **HIT Tokens** to score — consecutive hits trigger a hot-streak bonus;
- Dodge the **Bugs**; hitting one costs you progress;
- Watch the **peak / off-peak hours**: Token and Bug spawn density, movement speed and hit rate all shift over time — peak is intense, off-peak is relaxed.

## Controls

| Action | Input |
| ------ | ----- |
| Swim up | Mouse click · Touch · `Space` / `↑` (ArrowUp) / `W` |
| Pause | `P` / `Esc` |
| Mute | `M` |

## How to run

Just double-click `大肥鱼吃token.html`. The game is a single self-contained HTML file with no external dependencies and no build step — it also drops straight onto any static host.

## Tech stack

- **Canvas 2D** — every graphic is drawn procedurally (fixed 1/60 timestep + render interpolation)
- **WebAudio** — all sound effects are synthesized at runtime, with no audio files
- **Vanilla JavaScript** — no frameworks, no third-party libraries; icons and the character sprite are embedded as Base64

## Project files

- `大肥鱼吃token.html` — the game itself (self-contained single file)
- `prev-*.png` — preview screenshots of each screen
- `icon-source.png` — source image for the app icon
- `build-icon.py` — generates every icon size (favicon / iOS home-screen icon) from `icon-source.png`
- `apply-icon.py` — inlines the generated icons into the game HTML (run `build-icon.py` first)

> The generated icon files are not committed to the repository; run the two scripts above to recreate them.

## Credits & disclaimer

The "Big Fatty Fish" character is a fan creation from the Chinese AI community (it grew out of a community joke about DeepSeek's image recognition misreading its own logo), and is **not affiliated with DeepSeek in any way**. This project uses no official assets — every graphic is drawn procedurally with Canvas.

## License

Released under the MIT License — see [LICENSE](LICENSE).

Copyright © 2026 yuxuan-6
