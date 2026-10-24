# Roman Papyrus (Charta Papyracea Romana)

**Roman Papyrus** is an immersive classical theme for [Obsidian](https://obsidian.md), reconstructing the writing surfaces, atramentum inks, and scribal aesthetics of the Roman Empire as recorded by **Pliny the Elder** (*Naturalis Historia* XIII.74–82) and **Isidore of Seville** (*Etymologiae* VI.10).

Built upon the clean, distraction-free architecture of [Obsidian Typewriter](https://github.com/crashmoney/obsidian-typewriter), Roman Papyrus transforms your vault into a classical Roman tablinum. Write on authentic papyrus sheets (*plagulae*), join them into continuous book scrolls (*volumina*), seal decrees with stamped terracotta bullae, and wield authentic classical typography.

---

## 🏛️ Archaeological Foundation: Pliny's Six Papyrus Grades

Pliny categorized the commercial papyri manufactured in Alexandria and Rome into six distinct quality grades based on pith layer depth, surface levor, candor, and sheet breadth (measured in Roman *digiti*, where 1 digitus &approx; 18.5 mm):

| Grade | Roman Width | Surface & Color | Historical Context |
| :--- | :--- | :--- | :--- |
| **I. Augusta** | 13 Digiti (~240 mm / 9.5 in) | Superfine, polished ivory pith | Named for Emperor Augustus; prime heart of the Cyperus stalk. Smooth, crispest atramentum ink edges. |
| **II. Liviana** | 12 Digiti (~220 mm / 8.7 in) | Warm golden ivory | Named for Empress Livia; identical firmness to Augusta with a rich honeyed warmth. |
| **III. Hieratica / Fanniana** | 9 Digiti (~165 mm / 6.5 in) | Rasped fine, priestly parchment tan | Sacred religious book paper refined in the Roman workshop of grammarian Fannius. |
| **IV. Saitica** | 7–8 Digiti (~140 mm / 5.5 in) | Marsh scraps, knotty amber | Made from outer delta cuttings around the city of Sais; darker grain with slight ink running. |
| **V. Taeneotica** | 6 Digiti (~110 mm / 4.3 in) | Coarse outer bark | Sold strictly by bulk weight (*pondere non bonitate*); rough tooth and heavy feathering. |
| **VI. Emporetica** | <6 Digiti (<100 mm / 3.9 in) | Dark coarse shopkeeper's scrap | Considered "unusable for writing" (*inutilis scribendo*); pasted to wrap merchandise, fish, and spices. |

---

## ✨ Features & Aesthetic System

### 1. Document Architecture
- **Plagula Mode (Default)**: Individual notes are rendered as real Roman papyrus sheets (*plagulae*) with ragged deckle edges, deckle box-shadows, and natural texture floating upon your villa desk.
- **Volumen Mode**: Continuous scroll roll mode with dark wooden rod margins (*umbilici*) and periodic glued seams (*kolleseis*), simulating an unrolled ancient scroll.
- **Modern Full Width**: Clean edge-to-edge layout with full papyrus materiality.

### 2. Atramentum Ink Physics
- **Capillary Reed Bleed**: Natural text-shadow diffusion reproducing ancient carbon and iron gall soot inks (*atramentum librarium*) absorbing into porous plant fibers.
- Adjustable in **Style Settings** between *Historical Calibration*, *Subtle*, *Heavy Porous Bleed*, or *Crisp Modern*.

### 3. Recto & Verso Fiber Weave
- Cross-layered repeating gradients simulate the orthogonal pith strips of the Egyptian reed: horizontal pith strips (*recto*) on the writing surface with vertical backing bundles (*verso*), layered using `mix-blend-mode: multiply`.

### 4. Kollesis Seams
- Overlapping glued joins (*kolleseis*) where papyrus makers pasted individual sheets together with flour paste and Nile water to construct 20-sheet rolls (*scapi*).

### 5. Stamped Terracotta Bulla Seals & Braided Cords
- Authentic clay seals with 3D inset impressions and twisted hemp fastening cords.
- Dedicated custom callouts with historical seal stamps:
  - `> [!decree]` / `> [!edictum]`: Imperial Edict with terracotta `AVG` seal.
  - `> [!senatus]`: Senatus Consultum with golden bronze `SEN` seal.
  - `> [!epistula]`: Roman correspondence letter with `LIV` seal.
  - `> [!legio]`: Military dispatch with iron/terracotta `LEG` seal.
  - `> [!sacrum]`: Sacred temple scroll with `SAC` seal.

### 6. Classical Epigraphy & Scripts
- **Cinzel & Marcellus**: Monumental inscriptional serifs inspired by first-century Roman capital letters (Trajan's Column).
- **IM Fell English**: Weathered antique italic type recreating cursive stylus handwriting (*Old Roman Cursive / Currens*).
- **Interpuncts (`·`)**: Roman word-separator dots with `.interpunct`.
- **Linea Supera**: Classical overline notation for Roman numerals (e.g. `<span class="linea-supera">XIII</span>` or `X̄ĪĪĪ`).
- **Drop Caps**: Elegant monumental initial capitals automatically applied to opening paragraphs.

### 7. Dual Atmospheric Palettes
- **Light Mode — Imperial Atrium**: Warm sunlit travertine stone, polished papyrus desk, and bistre soot ink.
- **Dark Mode — Candlelit Tablinum & Herculaneum Scrolls**: Archaeological ambient desk (`#25201a`), dark basalt, charred cedar, glowing terracotta bullae, and antique aurum gold.

---

## 🎨 Note-Specific Custom Classes (`cssclasses`)

You can set the papyrus grade, layout, script, or seal on any individual note using frontmatter:

```yaml
---
cssclasses:
  - grade-liviana          # Choose: grade-augusta, grade-liviana, grade-hieratica, grade-saitica, grade-taeneotica, grade-emporetica
  - plagula                # Choose: plagula (card sheet) or volumen (continuous roll)
  - roman-cursive          # Choose: roman-cursive (IM Fell English) or roman-monumentalis (Cinzel/Marcellus)
  - bulla-seal             # Displays stamped terracotta bulla seal & fastening cord at bottom margin
---
```

---

## ⚙️ Obsidian Style Settings

Install the **Style Settings** plugin by `@mgmeyers` to unlock in-app configuration:

- **Pliny's Papyrus Grade**: Switch the global default across all 6 historical grades.
- **Document Display Mode**: Toggle between *Plagula Sheet*, *Volumen Scroll*, or *Modern Full Width*.
- **Fiber Weave Striations**: Toggle cross-layered cyperus pith fibers on or off.
- **Kollesis Glue Seams**: Toggle joined plagulae overlap seams.
- **Atramentum Capillary Bleed**: Choose between *Historical Calibration*, *Subtle*, *Heavy*, or *Disabled*.
- **Bulla Seals**: Enable or disable terracotta bulla stamps.
- **Markdown Formatting**: Shrink and fade markdown symbols for focused reading.
- **Active Line Highlight**: Warm amber focus wash.

---

## 📦 Installation

### Recommended (Theme Manager)
1. Open Obsidian **Settings** &rarr; **Appearance** &rarr; **Themes** &rarr; **Manage**.
2. Search for **Roman Papyrus** and click **Install and apply**.

### Manual Installation
1. Download `theme.css` and `manifest.json`.
2. In your Obsidian vault, navigate to `.obsidian/themes/`.
3. Create a folder named `Roman Papyrus/`.
4. Move `theme.css` and `manifest.json` into `.obsidian/themes/Roman Papyrus/`.
5. In Obsidian, go to **Settings** &rarr; **Appearance** &rarr; **Themes** and select **Roman Papyrus**.

---

## 📜 Credits & Attributions

- Built upon the excellent [Obsidian Typewriter](https://github.com/crashmoney/obsidian-typewriter) by **crashmoney**.
- Historical research and calibration based on **Pliny the Elder**, *Naturalis Historia* (Liber XIII, 74–82: *De papyro et chartis*) and **Isidore of Seville**, *Etymologiarum sive Originum* (Liber VI, 10).
- Fonts:
  - [Cinzel](https://fonts.google.com/specimen/Cinzel) by Natanael Gama
  - [Marcellus](https://fonts.google.com/specimen/Marcellus) by Astigmatic
  - [IM Fell English](https://fonts.google.com/specimen/IM+Fell+English) by Igino Marini
  - Embedded iA Writer Mono V, Quattro S, and JetBrains Mono from Typewriter
- Checkbox icons adapted from Minimal by **@kepano**.

---

*C. Plinius Secundus: "Papyri natura dicetur, cum chartae usu maxime humanitas vitae constet, certe memoria."*
