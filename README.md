<div align="center">

**🤖 Made with [Claude Code](https://claude.com/claude-code), Anthropic's coding agent**

# Modula

### The Playnite theme that is stunning out of the box, and yours to bend into any shape.

Liquid-glass desktop theme + a PS5-style Fullscreen theme, one look, one set of rules.<br>
Rearrange, resize and recolour everything live with the **[Layout Studio](https://github.com/YannD-Delta/Layout-Studio)** editor.

[![Playnite 10](https://img.shields.io/badge/Playnite-10.x-1f6feb?style=flat-square)](https://playnite.link)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Made with Claude Code](https://img.shields.io/badge/made%20with-Claude%20Code-d97757?style=flat-square)](https://claude.com/claude-code)

<img src="docs/images/desktop-details-echoes.png" alt="Modula desktop, game details page" width="100%">

</div>

---

## Why Modula

Most Playnite themes make you choose: pretty or configurable. Modula is built to be both.

- **Sublime by default.** Install it, pick a game: frosted liquid glass, soft glows, the game's own art washing over the page. No setup.
- **Ultra customisable.** Every section, size, corner, colour and information card is a setting. With Layout Studio you drag sections between columns and watch the real window change while you edit.
- **One look on desktop and on the TV.** Modula Desktop and Modula Fullscreen share the same rules: the same accent colours, rounded corners, glow, and the same information cards.
- **Never an inner scrollbar.** Sections adapt to their content instead of hiding it behind nested scroll areas.
- **Your add-ons, integrated.** It uses the Playnite add-ons you already have (achievements, HowLongToBeat, activity, music...) and hides what is not installed.

## Desktop

<table>
<tr>
<td width="50%"><img src="docs/images/desktop-details-neon.png" alt="Neon Drifter details"></td>
<td width="50%"><img src="docs/images/desktop-details-hollow.png" alt="Hollow Lantern details"></td>
</tr>
<tr>
<td align="center"><sub>The page takes its colours from the game's art</sub></td>
<td align="center"><sub>Glass tiles, chips and link buttons share one recipe</sub></td>
</tr>
</table>

- **Liquid Glass material**: translucent panels with a soft rim, gloss and bloom. Tiles, chips, link buttons and the Play button are the same family, so nothing looks bolted on.
- **Header cards**: choose which facts show above the description (time played, last played, scores, install size, HowLongToBeat, activity...). Scores are colour-coded by value.
- **Sections you control**: reorder, hide, collapse or move them to the other column. Every section can switch column, add-on sections included.
- **Four looks, one switch**: Liquid Glass, Frosted Mono, Neon Night, Flat. Plus spacing (Compact, Comfortable, Airy), corner rounding (Square to Very round), and a **Lite** mode (saves GPU: no glow, no shadows) for when a game is running.
- **14 colour profiles and 9 accents**, or any `#RRGGBB` of your own.

<table>
<tr>
<td width="25%"><img src="docs/images/desktop-look-default.png" alt="Liquid Glass"></td>
<td width="25%"><img src="docs/images/desktop-look-frostedmono.png" alt="Frosted Mono"></td>
<td width="25%"><img src="docs/images/desktop-look-neonnight.png" alt="Neon Night"></td>
<td width="25%"><img src="docs/images/desktop-look-flat.png" alt="Flat"></td>
</tr>
<tr>
<td align="center"><sub>Liquid Glass</sub></td>
<td align="center"><sub>Frosted Mono</sub></td>
<td align="center"><sub>Neon Night</sub></td>
<td align="center"><sub>Flat</sub></td>
</tr>
</table>

<img src="docs/images/desktop-details-sections.png" alt="Sections below the header, scrolled" width="100%">

## Fullscreen

A home that feels like a console: big cards, a hero title, the game's art behind everything, a focus ring that glows, entrance animations, and interface sounds. Built for a controller and a TV.

<img src="docs/images/fullscreen-home.png" alt="Modula Fullscreen, home" width="100%">

<table>
<tr>
<td width="50%"><img src="docs/images/fullscreen-details.png" alt="Fullscreen game details"></td>
<td width="50%"><img src="docs/images/fullscreen-main-menu.png" alt="Fullscreen main menu"></td>
</tr>
<tr>
<td align="center"><sub>Details: glass info cards, a white Play pill, the cover</sub></td>
<td align="center"><sub>Main menu, restyled to match</sub></td>
</tr>
</table>

Accent colour, corner roundness, glow and which information cards to show are presets you can change from the Fullscreen main menu (Extensions > Layout Studio), with the controller, without leaving the couch:

<table>
<tr>
<td width="25%"><img src="docs/images/fullscreen-accent-violet.png" alt="Violet accent"></td>
<td width="25%"><img src="docs/images/fullscreen-accent-mint.png" alt="Mint accent"></td>
<td width="25%"><img src="docs/images/fullscreen-accent-amber.png" alt="Amber accent"></td>
<td width="25%"><img src="docs/images/fullscreen-corners-round.png" alt="Very round corners"></td>
</tr>
<tr>
<td align="center"><sub>Violet</sub></td>
<td align="center"><sub>Mint</sub></td>
<td align="center"><sub>Amber</sub></td>
<td align="center"><sub>Very round corners</sub></td>
</tr>
</table>

## Layout Studio, the editor behind it

Modula ships its settings through **[Layout Studio](https://github.com/YannD-Delta/Layout-Studio)**, a Playnite extension that replaces the usual options page with a live editor: a search box over every setting, drag-and-drop sections, visual size handles, **presets shown as picture tiles** so you see what a choice changes, segmented switches, number boxes with no hard limit (the slider is a guide, type any value), undo and redo, and profiles you can export as a short text code and share. The first page, **Graphics and performance**, detects Playnite settings that break the look or cost performance, says which of the two each one touches with measured numbers, and fixes them in one click. The small gear next to each section in the theme opens the editor on the right page.

<table>
<tr>
<td width="33%"><img src="docs/images/editor-sections.png" alt="Sections editor"></td>
<td width="33%"><img src="docs/images/editor-colors.png" alt="Colours"></td>
<td width="33%"><img src="docs/images/editor-appearance.png" alt="Appearance"></td>
</tr>
<tr>
<td align="center"><sub>Drag sections between columns</sub></td>
<td align="center"><sub>Colour profiles and accents</sub></td>
<td align="center"><sub>Looks, spacing, corners</sub></td>
</tr>
</table>

Modula also runs without Layout Studio with its default look (the `options.yaml` presets are readable by the Theme Options extension), but you then lose the live editor, the Fullscreen quick menu and the colour rules of the information cards.

## Install

1. Install [Playnite](https://playnite.link) 10.x.
2. Download the latest `.pthm` files from the [Releases](https://github.com/YannD-Delta/Modula/releases) page and double-click them: **Modula** (desktop) and **Modula Fullscreen**. Or copy the `Modula` and `Modula-Fullscreen` folders into `<Playnite>\Themes\Desktop` and `<Playnite>\Themes\Fullscreen`.
3. Install **Layout Studio** (`.pext` from its [releases](https://github.com/YannD-Delta/Layout-Studio/releases)).
4. Select the theme in *Settings > Appearance* and restart Playnite. Open the editor from *Main menu > Extensions > Layout Studio*.

If you use **Theme Options** or a similar extension for another theme, disable it while Modula is active: Layout Studio stays idle while ThemeOptions is enabled so a setting is never applied twice.

## Recommended add-ons

Nothing is required. Each integration shows up only when its add-on is installed. At start, Layout Studio shows one Playnite notification naming the optional add-ons you do not have yet (and only again if that list changes).

| Add-on | What Modula does with it |
| --- | --- |
| [Layout Studio](https://github.com/YannD-Delta/Layout-Studio) | The editor, presets, Fullscreen quick menu, colour rules |
| [Extra Metadata Loader](https://github.com/darklinkpower/PlayniteExtensionsCollection) | Logos and videos on the details page |
| [Playnite Achievements](https://github.com/justin-delano/PlayniteAchievements) | Achievements section and card |
| [HowLongToBeat](https://github.com/Lacro59/playnite-howlongtobeat-plugin) | Time-to-beat card and section |
| [GameActivity](https://github.com/Lacro59/playnite-gameactivity-plugin) | Activity card and chart |
| [ThemeExtras](https://github.com/felixkmh/ThemeExtras-for-Playnite) | Extra UI elements for themes |
| [ScreenshotsVisualizer](https://github.com/Lacro59/playnite-screenshotsvisualizer-plugin), [CheckDlc](https://github.com/Lacro59/playnite-checkdlc-plugin), [Game Relations, Play Notes, Steam Trailers](https://github.com/darklinkpower/PlayniteExtensionsCollection) | Sections on the details page |
| [UniPlaySong](https://github.com/aHuddini/UniPlaySong) | Per-game music while you browse, with a quick toggle in Fullscreen |
| [Playnite Sounds Mod](https://codeberg.org/ashpynov/PlayniteSoundMod) | Interface and event sounds |
| [Custom Fade Animations](https://github.com/saVantCZ/CustomFadeAnim) | Smooth background transitions when the game changes |
| [Display Manager](https://github.com/Naerian/playnite-nx-display-session) | Resolution, refresh rate and HDR when a game starts (handy on a TV) |
| [Playtime Insights](https://github.com/SHINKU1506/PlaytimeInsights) | Playtime trends and rankings |



## Made with Claude Code

Modula and Layout Studio were designed and built together with [**Claude Code**](https://claude.com/claude-code), Anthropic's coding agent: the XAML, the C# extension, the tests, the generators, the screenshots and these docs. The direction, the taste and every decision come from the human behind it; the typing came from the agent. Everything is verified the boring way: a lint for the themes, an automated test suite for the extension, and a sandbox Playnite with fake games for the screenshots you see here (no real library, no personal data).

## Credits and licence

Modula started from three excellent MIT-licensed Playnite themes and keeps their notices:
**Neon** (Xenor), **Helium** (darklinkpower) and **Dune Rev** (hugsyf). See [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).

Modula is released under the [MIT licence](LICENSE). What is inside the themes:

- **Code and styles**: XAML written for Modula, or inherited from the three MIT themes above and from Playnite's own default themes (Playnite is MIT too).
- **Sounds and music** of Modula Fullscreen: synthesised by `make-audio.py` in the author's tooling, no samples, no third-party audio.
- **Fonts**: none are shipped. The themes use Segoe UI Variable and Segoe Fluent Icons from Windows, and the Titillium font that Playnite itself provides.
- **Platform, store and social logos** in `Images/Banners` and `Images/*.png` (Steam, Discord, Reddit...) come from the upstream themes. They are trademarks of their owners and are only used to label the matching platform or link.
- **Screenshots** use generated placeholder art and fictional games.

Modula is an independent theme and is not affiliated with Playnite or any platform shown.

## Playnite's add-on browser

Playnite lists themes in its built-in add-on browser through [a community database](https://github.com/JosefNemec/PlayniteAddonDatabase). Theme submissions are open; submissions of extensions are currently on hold (the maintainer plans a new database with a verification system for Playnite 11). Until Modula is listed, install it from the [Releases](https://github.com/YannD-Delta/Modula/releases) page as described above.

## Feedback

I would love to hear what you think, what breaks, and what you would change.

- Open an [issue](https://github.com/YannD-Delta/Modula/issues) on GitHub for bugs and ideas.
- Talk to me on Discord: **@yannd_delta** (or open an issue, either is welcome).
## Contributing

Issues and pull requests are welcome. Before sending a change to a theme, run the lint:

```bash
python tools/check-theme.py Modula
python tools/check-theme.py Modula-Fullscreen
```
