# Changelog

## Modula 3.2 (Modula Fullscreen 1.1), 2026-10-21

- **30 global presets**, thirty different designs (light and dark, flat and glass, editorial, terminal, arcade, store, console...): every part of the look changes together (colours, fonts, material, density, corners, accent, the generated backdrop, the hero, where the sections sit, which information shows) and each is coherent on its own. Pick one on the first page of the editor.
- **11 new colour profiles, 7 of them light** (dark text on a light window: Paper, Mist, Sand, Mint, Blush, Lilac, Monochrome; and DeepTeal, Wine, Terminal, Dusk), and **11 font personalities** (Windows fonts only). The Play and context button colours now really change, and light profiles draw their lines, titles and chips in ink.
- **Grid view fixed**: it was blank (an option bound straight to Visibility made every cover throw). Grid + details no longer clips its column titles, the placeholder of a game without cover reads on light and dark profiles, tiles follow the corner rounding, and there are options for the title over the cover and the zoom slider.
- **Modula Fullscreen 1.1**: shares the colour profiles of the desktop theme, safe margins and aligned screens, new home layouts and typography presets, a toast for achievements at TV scale, and optional add-on integrations (logo and trailer, Now Playing, Back To Game, status chips, Aniki Helper cards), all guarded so nothing is required.
- **705 settings** in total (646 desktop, 59 Fullscreen) and 245 preset choices.
- **Add-ons round** (11 new settings, all off or harmless until the add-on is installed; nothing is required):
  - **ImageRotater**: the banner background and the banner cover host the add-on's rotating, animated and video artwork (`UseImageRotater`, on by default; each host shows only when the add-on says it renders that artwork). The Grid view banner background hosts it too.
  - **Now Playing** (or **Back To Game**): a chip in the top bar while a game runs: icon, name, session time, a click returns to the game (`TopPanelShowNowPlaying`; a close button with `NowPlayingShowCloseButton`, off by default). With Back To Game alone, a plain "Back to game" button.
  - **AnikiHelper** (its public library data only, nothing of its Fullscreen theme): a top bar button opens a **library overview**: games, installed, favourites, play time, average, this month, the game of the month, a suggested game, most played, completion states, sources, never played, latest Steam updates (`TopPanelShowLibraryOverview`).
  - **PlayerActivities**: a new Details section "Player activity" (friends' play, achievements and finished games) with the usual show, open, column, order, header and tab options. Details view only.
  - **Extra Metadata Loader**: nothing new is hosted. Looked at and left out on purpose: the silent / with-sound trailer players (`VideoLoaderControl_NoControls_*`), because every player of the add-on writes the same play-state flags as the Video section's player and would flip its play / pause button for everybody; a logo on the Grid cards, because the add-on's logo control keeps one global flag, and reading `Logo.png` straight from its folder did not draw on the test bench. `ExtraMetadataLoader_LogoLoaderControlGrid`, the name other themes use, is not an element the add-on registers.
  - **Audio Switcher** and **Controller Manager** add their own button to the top bar; Modula ships `AudioSwitcher/theme-bridge.json` and `ControllerManager/theme-bridge.json` so their notifications follow the theme's colours when their "follow the active Playnite theme" switch is on.
  - Recommended add-ons: ImageRotater and Now Playing join the list (still never required).
  - **What was seen on the test bench** (add-ons installed from their GitHub releases): the theme loads with ImageRotater, Now Playing, PlayerActivities and AnikiHelper installed and the banner looks the same; ImageRotater's cover control is created and runs in the banner; the AnikiHelper overview button, its popup and its bindings resolve in Desktop mode, and the button stays hidden while the plugin reports 0 games (on the bench its statistics were not computed, so the lists were never seen filled); the Player activity section stays hidden without data.
  - **Not seen working** (read from the add-ons' documentation and source only): the Now Playing chip and the Back To Game button while a game runs, a rotating or video ImageRotater artwork, PlayerActivities with friends data, the Audio Switcher and Controller Manager colour mapping.
- **Generated backdrop**: behind the whole window, a colour, a linear or radial gradient (two or three colours) or soft circles instead of the game artwork, the same for every game (option `BackdropMode`, **off by default**: the artwork stays as it is). It sits where the artwork sits, under the glass layers, so every panel, glass and darkness setting keeps working. It can be used only for games that have no artwork (`BackdropFallbackOnly`). Everything is drawn with gradient brushes (no blur, nothing animated), cached at half size: on the test machine idle, game list scrolling and page scrolling cost the same as with the artwork. Options: three colours, gradient angle and midpoint, radial centre and size, up to eight circles (position, size, colour, opacity), their size, spread, opacity and edge hardness, a pattern (dots, grid or diagonal lines) and a darkness veil. A new preset group, Backdrop, ships thirteen ready-made looks (Mist, Sunset, Ocean, Paper, Mint, Dusk, Studio black, Candy, Aurora, Ember, Lavender, Blueprint, Bokeh night). The two window gradient colours of the colour profiles are part of the same system.
- **Global presets**: the whole look at once (colours, material, fonts, density, corners, accent, backdrop, hero, placement of the sections), chosen from the first page of the editor, each with a real preview. A new profile starts from the default one, and "Reset all" goes back to it.
- **Every row of the information panel can be hidden** (recent activity, date added, release date, library, source, platform, developer, publisher, install size, install directory, series, region, version, your score, community score, critic score, age rating): one option each, all on by default. A hidden row leaves no gap and the whole panel disappears when every row is off.
- **Section headers are optional**: a global option "Section headers: show" and one option per section. Without its header a section keeps its place and spacing and stays open (there is nothing to click to fold it).
- **Every section of the game page can move to the other column** (Layout Studio, Sections page). Add-on sections included: the extension moves the live block, so the add-on keeps working. The default layout is unchanged.
- The UniPlaySong ready-made player can show in the game banner while a game's music plays (option "HeroShowMusicPlayer", **off by default**: UniPlaySong already puts play, pause and next in the top bar).
- **Readable text**: the game description uses the main text color (it used the label grey), the muted label and secondary text colors of every color profile are lighter, link text, list header text and inactive filter labels are stronger.

- **Links are a section**: the chips of the game's links sit at the top of the left column by default and can be moved to the right column, ordered or hidden like any other section (the chips look and the link text brightness option are unchanged).
- **Chips in any order**: one order setting per chip of the artwork header (it replaces the six group orders; old profiles are migrated); the chip row is written once in the theme, which makes the theme file about 5,300 lines shorter.
- **Completion status card**: a selector fed by Layout Studio (Playnite's own statuses, the choice is written to the game); read-only value without the extension. A card is a template of its own: Playnite and the add-ons cannot find named elements inside it, so none is used there any more.
- **Left icon bar readable over any artwork**: near-white icons with a thin dark halo and a light pad, the selected icon in orange on a darker pad; options for the icon colour, the active colour, the pad opacities and the halo.
- **Play, dropdown, edit and favourite buttons** are exactly as tall as the cards in the header row.
- **Players online** is centred on the cover and always labelled "Players".
- Demoted sections (shown as chips elsewhere) get a row of their own: HowLongToBeat and Achievements no longer overprint Genres and Categories. The quick filters panel no longer has a lighter frost box (the frost option defaults to 0).
- Option to show your own play time in the game list (off by default).
- Playnite Sounds Mod is no longer in the recommended add-ons (its music engine overlaps UniPlaySong).
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
