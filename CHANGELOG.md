# Changelog

## Unreleased

- **Every section of the game page can move to the other column** (Layout Studio, Sections page). Add-on sections included: the extension moves the live block, so the add-on keeps working. The default layout is unchanged.
- The UniPlaySong ready-made player can show in the game banner while a game's music plays (option "HeroShowMusicPlayer", **off by default**: UniPlaySong already puts play, pause and next in the top bar).
- **Readable text**: the game description uses the main text color (it used the label grey), the muted label and secondary text colors of every color profile are lighter, link text, list header text and inactive filter labels are stronger.

- **Cover**: new option to show the whole cover instead of cropping it (`HeroCoverShowWhole`), cover position and outline color, shape presets (poster, tall, square, wide).
- **Players online** (Steam News and Players Viewer): shown large above the cover, option `HeroShowPlayersCount` and its size.
- **Banner and header bands**: three edge modes (fade at the sides, hard edge, fade everywhere) so the bands no longer show ugly borders.
- **Glass**: a glass outline on the standard controls (check boxes, text boxes, lists, round header buttons, section gears) and pill tabs, with a preset to go back to the old look; a glass veil on the filter and explorer panels (`SidePanelFrostOpacity`).
- **Scroll bars**: a preset to thin or hide them; mouse wheel scrolling keeps working.
- **Information panel**: Release date, Platforms, Developers, Install size and Source rows can each be hidden (groundwork for "information shown once").
- More options: section title margin, header label and text opacity, achievements bar colors, tab spacing, Play button and top-left positions; a warning in the theme when "show background image on the window" is off in Playnite; the gap between the banner and the info cards is 16 px; the schema generator refuses two sections with the same order number in a column.
- **Performance**: the window glass blur is computed once and cached (GPU use while scrolling the game list about 13 % to 2 %, page scroll 41 % to 24 % on the test machine; the screenshot is pixel-identical).
- **Fullscreen**: shared Look with the desktop theme, generated radii and glass, details page with a big Play button, genre chips, screenshot row, add-on info cards and a slow background zoom, glass filter panel, card arrival animation, Motion / Performance / Sound presets.
## Modula 3.1 (Modula Fullscreen 1.0)

- No more background slab behind the rounded panels of the game page.
- The gears next to the sections and the chips now open Layout Studio on the right page.
- One spacing scale for the gaps between blocks and between tiles (Compact, Comfortable and Airy follow it).
- The "Light" material preset is now called **Lite** (saves GPU: no glow, no shadows).
- The Layout Studio editor opens on a new Graphics and performance page (see Layout Studio 0.2.0).
- Settings reorganised into clearer pages (see Layout Studio 0.2.0).

## Modula 3.0 / Modula Fullscreen 1.0

First public release: liquid-glass desktop theme, PS5-style Fullscreen theme, Layout Studio integration.
