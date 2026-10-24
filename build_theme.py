import re

def build_theme():
    with open('theme.css', 'r', encoding='utf-8') as f:
        existing_content = f.read()

    # Extract the font-face block
    font_start = existing_content.find('/* +++ FONT FACES {{{ */')
    font_end = existing_content.find('/* +++ ROMAN PAPYRUS CORE VARIABLES')
    if font_start == -1 or font_end == -1:
        # Fall back to original marker if not yet replaced
        font_end = existing_content.find('/* +++ COLOR VARIABLES {{{ */')
    
    if font_start == -1 or font_end == -1:
        raise Exception("Could not find font markers in theme.css")

    fonts_block = existing_content[font_start:font_end].strip()

    front_matter = """/* -------- FRONT MATTER ---------
** Theme: Roman Papyrus (Charta Papyracea Romana)
** Version number: 1.0.0
** GitHub Repo: https://github.com/gavmor/obsidian-roman-papyrus-theme
** Original template by: crashmoney (Obsidian Typewriter)
** Roman Papyrus enhancements by: gavmor
** Based on: Pliny the Elder (Naturalis Historia XIII.74–82) & Isidore (Etymologiae VI.10)
----------------------------------- */

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=IM+Fell+English:ital@0;1&family=Marcellus&display=swap');

/* +++ TOC
|_ FONT FACES & CLASSICAL TYPOGRAPHY
|_ ROMAN PAPYRUS CORE VARIABLES & PLINY'S SIX GRADES
|_ LIGHT THEME (IMPERIAL ATRIUM & PAPYRUS DESK)
|_ DARK THEME (CANDLELIT TABLINUM & HERCULANEUM SCROLLS)
|_ PLINY'S SIX HISTORICAL GRADES (CSS CLASSES & TOKENS)
|_ DOCUMENT LAYOUT ARCHITECTURE (PLAGULA SHEETS & VOLUMEN ROLLS)
|_ FIBER WEAVE LAYERING (RECTO & VERSO PITH STRIPS)
|_ KOLLESIS (GLUED SEAMS BETWEEN PLAGULA SHEETS)
|_ ATRAMENTUM INK BLEED & CAPILLARY FEATHERING
|_ BULLA SEALS & BRAIDED FASTENING CORDS
|_ CLASSICAL SCRIPTS (CURSIVE, MONUMENTALIS, SCRIPTIO CONTINUA)
|_ ROMAN INTERPUNCTS & LINEA SUPERA
|_ CALLOUTS & IMPERIAL DECREES
|_ WAX TABLET CHECKBOXES
|_ UI COMPONENTS (TABS, SIDEBARS, MODALS, SCROLLBARS)
|_ STYLE SETTINGS CONFIGURATION
|_ OBSIDIAN HUB
*/
"""

    css_body = """
/* +++ ROMAN PAPYRUS CORE VARIABLES & PLINY'S SIX GRADES {{{ */
:root {
  /* Classical Roman Ink Pigments (Atramentum) */
  --ink-augusta: rgba(26, 20, 16, 0.94);
  --ink-liviana: rgba(28, 22, 17, 0.94);
  --ink-hieratica: rgba(30, 24, 18, 0.93);
  --ink-saitica: rgba(35, 26, 18, 0.92);
  --ink-taeneotica: rgba(40, 28, 16, 0.92);
  --ink-emporetica: rgba(45, 30, 16, 0.95);

  /* Roman Seal, Metal & Mineral Pigments */
  --bulla-terracotta: #8c3b24;
  --bulla-terracotta-bright: #b25333;
  --bulla-shadow: #3b140b;
  --roman-gold: #c59b27;
  --roman-gold-bright: #dfb743;
  --roman-gold-dim: #7a591a;
  --roman-purple: #631a31;
  --roman-purple-bright: #842342;
  --roman-cinnabar: #a83222;
  --roman-cinnabar-bright: #c8402c;
  --roman-malachite: #2e6347;
  --roman-lapis: #264e70;
  --roman-bistre: #2d2015;

  /* Standard Ink Bleed blur radius */
  --ink-shadow-blur: 0.35px;
  --ink-shadow: 0 0 var(--ink-shadow-blur) rgba(20, 14, 8, 0.6);

  /* SVG displacement filters data URIs for ragged edge and reed fiber capillary distortion */
  --filter-papyrus-tear: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='papyrus-tear-filter' x='-10%25' y='-10%25' width='120%25' height='120%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.045 0.08' numOctaves='4' result='noise'/%3E%3CfeDisplacementMap in='SourceGraphic' in2='noise' scale='6' xChannelSelector='R' yChannelSelector='G'/%3E%3C/filter%3E%3C/svg%3E#papyrus-tear-filter");
  --filter-ink-capillary: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='ink-capillary-filter' x='-10%25' y='-10%25' width='120%25' height='120%25'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.05 0.15' numOctaves='3' result='fiberNoise'/%3E%3CfeDisplacementMap in='SourceGraphic' in2='fiberNoise' scale='1.2' xChannelSelector='R' yChannelSelector='G'/%3E%3C/filter%3E%3C/svg%3E#ink-capillary-filter");

  /* 1. AUGUSTA: 13 Digiti (~240mm), Fine, White, Polished Ivory Pith */
  --bg-grade-augusta: 
    radial-gradient(ellipse at 80% 20%, rgba(255, 250, 240, 0.5) 0%, transparent 60%),
    repeating-linear-gradient(90deg, 
      rgba(224, 212, 188, 0.42) 0px, 
      rgba(215, 201, 175, 0.35) 1px, 
      rgba(238, 228, 208, 0.3) 2px, 
      rgba(230, 218, 195, 0.45) 4px
    ),
    repeating-linear-gradient(0deg, 
      rgba(247, 240, 228, 0.6) 0px, 
      rgba(229, 217, 197, 0.5) 1.5px, 
      rgba(242, 233, 219, 0.75) 4px
    ),
    #f5ede0;

  /* 2. LIVIANA: 12 Digiti (~220mm), Golden Ivory, Imperial Quality */
  --bg-grade-liviana: 
    radial-gradient(ellipse at 20% 70%, rgba(200, 165, 110, 0.12) 0%, transparent 55%),
    repeating-linear-gradient(90deg, 
      rgba(215, 196, 162, 0.5) 0px, 
      rgba(198, 178, 140, 0.4) 1px, 
      transparent 3px
    ),
    repeating-linear-gradient(0deg, 
      rgba(235, 215, 182, 0.6) 0px, 
      rgba(218, 198, 160, 0.55) 2px, 
      transparent 4px
    ),
    #ebd8b8;

  /* 3. HIERATICA / FANNIANA: 9 Digiti (~165mm), Thin, Religious & Book Grade */
  --bg-grade-hieratica: 
    radial-gradient(circle at 60% 40%, rgba(140, 95, 45, 0.1) 0%, transparent 60%),
    repeating-linear-gradient(90deg, 
      rgba(195, 170, 130, 0.4) 0px, 
      transparent 2px, 
      rgba(178, 152, 112, 0.4) 4px
    ),
    repeating-linear-gradient(0deg, 
      rgba(225, 200, 160, 0.75) 0px, 
      rgba(195, 165, 125, 0.6) 1.5px, 
      transparent 3px
    ),
    #dfcaa4;

  /* 4. SAITICA: 7-8 Digiti (~140mm), Nile Marsh Scraps, Knotty & Darker */
  --bg-grade-saitica: 
    radial-gradient(ellipse at 40% 60%, rgba(130, 85, 40, 0.18) 0%, transparent 60%),
    repeating-linear-gradient(90deg, 
      rgba(175, 140, 100, 0.6) 0px, 
      rgba(150, 115, 75, 0.45) 2px, 
      transparent 5px
    ),
    repeating-linear-gradient(0deg, 
      rgba(205, 175, 130, 0.75) 0px, 
      rgba(165, 130, 88, 0.65) 2px, 
      transparent 4px
    ),
    #cfb186;

  /* 5. TAENEOTICA: 6 Digiti (~110mm), Sold by Weight, Coarse Outer Bark */
  --bg-grade-taeneotica: 
    radial-gradient(circle at 75% 20%, rgba(95, 55, 15, 0.22) 0%, transparent 50%),
    radial-gradient(circle at 20% 80%, rgba(85, 45, 10, 0.2) 0%, transparent 45%),
    repeating-linear-gradient(90deg, 
      rgba(145, 108, 68, 0.7) 0px, 
      rgba(115, 78, 40, 0.55) 2px, 
      transparent 4px
    ),
    repeating-linear-gradient(0deg, 
      rgba(180, 142, 98, 0.75) 0px, 
      rgba(135, 92, 52, 0.65) 3px, 
      transparent 6px
    ),
    #bfa072;

  /* 6. EMPORETICA: <6 Digiti (<100mm), Merchant Wrapping Scrap */
  --bg-grade-emporetica: 
    radial-gradient(circle at 50% 50%, rgba(70, 40, 12, 0.3) 0%, transparent 60%),
    repeating-linear-gradient(90deg, 
      rgba(110, 75, 42, 0.8) 0px, 
      rgba(80, 50, 24, 0.75) 2px, 
      transparent 3px
    ),
    repeating-linear-gradient(0deg, 
      rgba(150, 110, 68, 0.85) 0px, 
      rgba(100, 68, 36, 0.8) 3px, 
      transparent 5px
    ),
    #9e7b4e;

  /* Active Papyrus Texture (Default: Augusta) */
  --papyrus-bg-active: var(--bg-grade-augusta);
  --papyrus-ink-active: var(--ink-augusta);
  --papyrus-sheet-width: 240mm;

  /* Kollesis (glued seam) overlay */
  --kollesis-gradient: linear-gradient(to right,
    transparent 0%,
    rgba(70, 45, 18, 0.16) 35%,
    rgba(45, 25, 8, 0.28) 50%,
    transparent 100%
  );

  /* Fastening cord */
  --cord-gradient: repeating-linear-gradient(45deg,
    #a89070,
    #a89070 3px,
    #6d5538 3px,
    #6d5538 6px
  );
}

/* Base Theme Hue / Saturation overrides */
body {
  --base-h: 38;
  --base-s: 25%;
  --base-d: 12%;
  --base-l: 92%;

  --theme-accent-h: 13;
  --theme-accent-s: 59%;
  --theme-accent-l: 35%;

  --color-accent: var(--bulla-terracotta);
  --color-accent-2: var(--bulla-terracotta-bright);
}
/* }}} */

/* +++ LIGHT THEME (IMPERIAL ATRIUM & PAPYRUS DESK) {{{ */
.theme-light {
  --background-primary: var(--papyrus-bg-active);
  --background-primary-alt: #f0e6d6;
  --background-secondary: #e6dcce;
  --background-secondary-alt: #dfd4c3;
  --background-transparent: rgba(245, 237, 224, 0);
  --background-translucent: rgba(245, 237, 224, 0.85);

  --background-modifier-border: #d2c3ae;
  --background-modifier-border-hover: #bda890;
  --background-modifier-border-focus: var(--bulla-terracotta);
  --background-modifier-form-field: #fdf9f2;
  --background-modifier-form-field-highlighted: #ffffff;

  --color-accent: var(--bulla-terracotta);
  --background-modifier-accent: rgba(140, 59, 36, 0.12);
  --vim-cursor: rgba(140, 59, 36, 0.75);
  --text-accent: var(--bulla-terracotta);
  --text-accent-hover: var(--bulla-terracotta-bright);

  --text-normal: var(--papyrus-ink-active);
  --text-muted: #5e4c3a;
  --text-faint: #8a7662;

  --text-highlight-bg: rgba(223, 183, 67, 0.4);
  --text-highlight-bg-active: rgba(178, 83, 51, 0.35);
  --text-selection: rgba(212, 175, 55, 0.28);
  --text-on-accent: #fdfaf4;

  --interactive-normal: #ede3d5;
  --interactive-hover: #e3d6c5;
  --interactive-accent: var(--bulla-terracotta);
  --interactive-accent-hover: var(--bulla-terracotta-bright);
  --interactive-success: #2e6347;

  --scrollbar-active-thumb-bg: #5c4735;
  --scrollbar-bg: rgba(70, 45, 20, 0.08);
  --scrollbar-thumb-bg: #826c58;
  --highlight-mix-blend-mode: multiply;

  --icon-color: var(--text-muted);
  --icon-hex: 3b2a1a;
  --graph-line-color: #baa994;
  --code-background: #e8dcce;
  --code-normal: #7a2b16;

  --divider-color: #cbb9a3;
  --tab-outline-color: #d8cabd;
}
/* }}} */

/* +++ DARK THEME (CANDLELIT TABLINUM & HERCULANEUM SCROLLS) {{{ */
.theme-dark {
  --background-primary: radial-gradient(circle at 50% 25%, #25201a 0%, #171410 100%);
  --background-primary-alt: #1f1b16;
  --background-secondary: #181511;
  --background-secondary-alt: #110e0a;
  --background-transparent: rgba(23, 20, 16, 0);
  --background-translucent: rgba(26, 22, 17, 0.88);

  --background-modifier-border: #3b3228;
  --background-modifier-border-hover: #574a3b;
  --background-modifier-border-focus: var(--roman-gold-bright);
  --background-modifier-form-field: #221d17;
  --background-modifier-form-field-highlighted: #2c251e;

  --color-accent: var(--bulla-terracotta-bright);
  --background-modifier-accent: rgba(178, 83, 51, 0.22);
  --vim-cursor: rgba(223, 183, 67, 0.8);
  --text-accent: var(--roman-gold-bright);
  --text-accent-hover: #f0cb67;

  --text-normal: #e6dfd5;
  --text-muted: #b8aba0;
  --text-faint: #7d7266;

  --text-highlight-bg: rgba(223, 183, 67, 0.28);
  --text-highlight-bg-active: rgba(178, 83, 51, 0.45);
  --text-selection: rgba(197, 155, 39, 0.35);
  --text-on-accent: #ffffff;

  --interactive-normal: #2a241d;
  --interactive-hover: #383027;
  --interactive-accent: var(--bulla-terracotta-bright);
  --interactive-accent-hover: #c45f3e;
  --interactive-success: #438863;

  --scrollbar-active-thumb-bg: #8c735a;
  --scrollbar-bg: #1d1a16;
  --scrollbar-thumb-bg: #544434;
  --highlight-mix-blend-mode: screen;

  --icon-color: var(--text-muted);
  --icon-hex: dcd2c3;
  --graph-line-color: #4a4034;
  --code-background: #1e1913;
  --code-normal: #e28468;

  --divider-color: #3f362a;
  --tab-outline-color: #352d23;
}
/* }}} */

/* +++ PLINY'S SIX HISTORICAL GRADES (CSS CLASSES & TOKENS) {{{ */
/* 1. Augusta */
body.grade-augusta, .grade-augusta {
  --papyrus-bg-active: var(--bg-grade-augusta) !important;
  --papyrus-ink-active: var(--ink-augusta) !important;
  --ink-shadow: 0 0 0.25px rgba(20, 14, 8, 0.55) !important;
  --papyrus-sheet-width: 240mm !important;
}

/* 2. Liviana */
body.grade-liviana, .grade-liviana {
  --papyrus-bg-active: var(--bg-grade-liviana) !important;
  --papyrus-ink-active: var(--ink-liviana) !important;
  --ink-shadow: 0 0 0.4px rgba(22, 16, 9, 0.6) !important;
  --papyrus-sheet-width: 220mm !important;
}

/* 3. Hieratica */
body.grade-hieratica, .grade-hieratica {
  --papyrus-bg-active: var(--bg-grade-hieratica) !important;
  --papyrus-ink-active: var(--ink-hieratica) !important;
  --ink-shadow: 0 0 0.65px rgba(25, 18, 10, 0.65) !important;
  --papyrus-sheet-width: 165mm !important;
}

/* 4. Saitica */
body.grade-saitica, .grade-saitica {
  --papyrus-bg-active: var(--bg-grade-saitica) !important;
  --papyrus-ink-active: var(--ink-saitica) !important;
  --ink-shadow: 0 0 1.05px rgba(28, 20, 11, 0.72) !important;
  --papyrus-sheet-width: 140mm !important;
}

/* 5. Taeneotica */
body.grade-taeneotica, .grade-taeneotica {
  --papyrus-bg-active: var(--bg-grade-taeneotica) !important;
  --papyrus-ink-active: var(--ink-taeneotica) !important;
  --ink-shadow: 0 0 1.55px rgba(32, 22, 12, 0.8) !important;
  --papyrus-sheet-width: 110mm !important;
}

/* 6. Emporetica */
body.grade-emporetica, .grade-emporetica {
  --papyrus-bg-active: var(--bg-grade-emporetica) !important;
  --papyrus-ink-active: var(--ink-emporetica) !important;
  --ink-shadow: 0 0 2.2px rgba(35, 24, 12, 0.95) !important;
  --papyrus-sheet-width: 100mm !important;
}
/* }}} */

/* +++ DOCUMENT LAYOUT ARCHITECTURE (PLAGULA SHEETS & VOLUMEN ROLLS) {{{ */

/* 1. PLAGULA MODE (Bounded Papyrus Sheet on Roman Desk) */
body.papyrus-mode-plagula .markdown-source-view.mod-cm6 .cm-scroller,
body.papyrus-mode-plagula .markdown-preview-view,
.plagula .markdown-source-view.mod-cm6 .cm-scroller,
.plagula .markdown-preview-view {
  background: transparent !important;
}

body.papyrus-mode-plagula .workspace-leaf-content[data-type="markdown"] .view-content,
.plagula .workspace-leaf-content[data-type="markdown"] .view-content {
  background: var(--background-secondary) !important;
}

body.papyrus-mode-plagula .markdown-source-view.mod-cm6 .cm-sizer,
body.papyrus-mode-plagula .markdown-preview-view .markdown-rendered,
.plagula .markdown-source-view.mod-cm6 .cm-sizer,
.plagula .markdown-preview-view .markdown-rendered {
  background: var(--papyrus-bg-active) !important;
  max-width: var(--papyrus-sheet-width, 240mm) !important;
  margin: 28px auto !important;
  padding: 38px 52px !important;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.45), 0 2px 6px rgba(0, 0, 0, 0.25) !important;
  border-radius: 2px 4px 3px 5px / 4px 2px 5px 3px !important;
  position: relative !important;
  border: 1px solid rgba(80, 50, 20, 0.14) !important;
  transition: max-width 0.3s ease, background 0.3s ease;
}

/* Ragged Deckle Edge Effect via drop-shadow and border-radius */
.papyrus-wrapper,
body.papyrus-deckle-edges .markdown-source-view.mod-cm6 .cm-sizer,
body.papyrus-deckle-edges .markdown-preview-view .markdown-rendered {
  filter: drop-shadow(0 14px 28px rgba(0, 0, 0, 0.55));
  border-radius: 4px 2px 5px 3px / 2px 5px 3px 4px;
}

/* 2. VOLUMEN MODE (Continuous Scroll Roll with Wooden Umbilicus Rod Margins) */
body.papyrus-mode-volumen .markdown-source-view.mod-cm6 .cm-sizer,
body.papyrus-mode-volumen .markdown-preview-view .markdown-rendered,
.volumen .markdown-source-view.mod-cm6 .cm-sizer,
.volumen .markdown-preview-view .markdown-rendered {
  background: var(--papyrus-bg-active) !important;
  border-left: 14px solid #4a3622 !important;
  border-right: 14px solid #4a3622 !important;
  box-shadow: inset 12px 0 24px rgba(0, 0, 0, 0.4), inset -12px 0 24px rgba(0, 0, 0, 0.4) !important;
  padding-left: 48px !important;
  padding-right: 48px !important;
  position: relative !important;
}

/* Kollesis (glued seam) overlay on note sheets */
.kollesis-seam::after,
body.papyrus-kollesis-seams .markdown-preview-view .markdown-rendered::after,
body.papyrus-kollesis-seams .markdown-source-view.mod-cm6 .cm-sizer::after {
  content: "";
  position: absolute;
  top: 0; bottom: 0; right: 28px;
  width: 18px;
  background: var(--kollesis-gradient);
  pointer-events: none;
  z-index: 5;
}
/* }}} */

/* +++ FIBER WEAVE LAYERING (RECTO & VERSO PITH STRIPS) {{{ */
body.papyrus-fibers-on .markdown-source-view.mod-cm6 .cm-sizer::before,
body.papyrus-fibers-on .markdown-preview-view .markdown-rendered::before,
.papyrus-fibers::before {
  content: "";
  position: absolute;
  inset: 0;
  background: 
    repeating-linear-gradient(0deg, 
      rgba(255, 255, 255, 0.04) 0px, 
      transparent 1.5px, 
      rgba(60, 30, 10, 0.05) 3px
    ),
    repeating-linear-gradient(90deg, 
      transparent 0px, 
      rgba(40, 20, 5, 0.03) 2px, 
      transparent 4px
    );
  pointer-events: none;
  z-index: 1;
  mix-blend-mode: multiply;
}
/* }}} */

/* +++ ATRAMENTUM INK BLEED & CAPILLARY FEATHERING {{{ */
/* Ink Capillary bleed presets */
body.ink-bleed-none, .ink-bleed-none {
  --ink-shadow: none !important;
}

body.ink-bleed-subtle, .ink-bleed-subtle {
  --ink-shadow: 0 0 0.25px rgba(20, 14, 8, 0.5) !important;
}

body.ink-bleed-historical, .ink-bleed-historical {
  --ink-shadow: 0 0 0.65px rgba(25, 18, 10, 0.65) !important;
}

body.ink-bleed-heavy, .ink-bleed-heavy {
  --ink-shadow: 0 0 1.6px rgba(32, 22, 12, 0.85) !important;
}

/* Applying Ink Bleed */
.ink-bleed,
.markdown-source-view.mod-cm6 .cm-line,
.markdown-rendered p,
.markdown-rendered li,
.markdown-rendered blockquote {
  text-shadow: var(--ink-shadow);
}
/* }}} */

/* +++ BULLA SEALS & BRAIDED FASTENING CORDS {{{ */
.fastening-cord {
  position: absolute;
  bottom: 0;
  left: 36px;
  width: 5px;
  height: 95px;
  background: var(--cord-gradient);
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.45);
  z-index: 15;
}

.bulla-seal {
  position: absolute;
  bottom: 14px;
  left: 18px;
  width: 48px;
  height: 48px;
  background: radial-gradient(circle at 35% 35%, var(--bulla-terracotta-bright), var(--bulla-terracotta) 60%, var(--bulla-shadow) 100%);
  border-radius: 46% 54% 52% 48% / 48% 46% 54% 52%;
  box-shadow: 
    2px 3px 8px rgba(0, 0, 0, 0.65),
    inset 1.5px 1.5px 3px rgba(255, 255, 255, 0.25),
    inset -2.5px -3px 5px rgba(0, 0, 0, 0.75);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 16;
  transform: rotate(-10deg);
}

.bulla-impression {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  border: 1px dashed rgba(60, 20, 10, 0.45);
  box-shadow: 
    inset 1.5px 1.5px 3px rgba(0, 0, 0, 0.8),
    inset -1px -1px 2px rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Marcellus', 'Cinzel', serif;
  font-size: 0.62rem;
  font-weight: 700;
  color: rgba(50, 15, 8, 0.85);
  text-shadow: 1px 1px 1px rgba(255, 255, 255, 0.2);
  letter-spacing: 0.06em;
}

/* Note Frontmatter Seal Injection (cssclasses: bulla-seal) */
.bulla-seal-active .markdown-preview-view .markdown-rendered::before,
.bulla-seal .markdown-preview-view .markdown-rendered::before {
  content: "";
  position: absolute;
  bottom: 0;
  left: 36px;
  width: 5px;
  height: 95px;
  background: var(--cord-gradient);
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.45);
  z-index: 15;
}

.bulla-seal-active .markdown-preview-view .markdown-rendered::after,
.bulla-seal .markdown-preview-view .markdown-rendered::after {
  content: "SPQR";
  position: absolute;
  bottom: 14px;
  left: 18px;
  width: 46px;
  height: 46px;
  background: radial-gradient(circle at 35% 35%, var(--bulla-terracotta-bright), var(--bulla-terracotta) 60%, var(--bulla-shadow) 100%);
  border-radius: 46% 54% 52% 48% / 48% 46% 54% 52%;
  box-shadow: 2px 3px 8px rgba(0, 0, 0, 0.65), inset 1.5px 1.5px 3px rgba(255, 255, 255, 0.25), inset -2.5px -3px 5px rgba(0, 0, 0, 0.75);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Marcellus', 'Cinzel', serif;
  font-size: 0.62rem;
  font-weight: bold;
  color: rgba(50, 15, 8, 0.9);
  text-shadow: 1px 1px 1px rgba(255, 255, 255, 0.2);
  z-index: 16;
  transform: rotate(-10deg);
}
/* }}} */

/* +++ CLASSICAL SCRIPTS & TYPOGRAPHY {{{ */
body {
  --font-text-theme: "Cinzel", "Marcellus", "Palatino Linotype", "Palatino", "Book Antiqua", Georgia, serif;
  --font-interface-theme: "Cinzel", "Marcellus", "Palatino Linotype", "Palatino", serif;
  --font-editor-theme: "IM Fell English", "Palatino Linotype", "Palatino", Georgia, serif;
  --font-editor: var(--font-editor-theme), var(--font-text-theme), var(--font-editor-default);
  --font-monospace-default: "JetBrains Mono", "iA Writer Mono V", monospace;
  --font-monospace: var(--font-monospace-override), var(--font-monospace-theme), var(--font-monospace-default);

  font-variant-emoji: unicode !important;

  --font-normal-size: 1.05em;
  --font-small: 0.85em;
  --font-smaller: 0.72em;
  --font-smallest: 0.64em;

  --h1: 1.85em;
  --h2: 1.5em;
  --h3: 1.28em;
  --h4: 1.12em;
  --h5: 1em;
  --h6: 0.9em;

  --h1-weight: 700;
  --h2-weight: 600;
  --h3-weight: 600;
  --h4-weight: 550;
  --h5-weight: 550;
  --h6-weight: 550;

  --h1-color: var(--text-normal);
  --h2-color: var(--text-normal);
  --h3-color: var(--text-normal);
  --h4-color: var(--text-normal);
  --h5-color: var(--text-normal);
  --h6-color: var(--text-normal);

  --line-width: 44rem;
  --line-height: 1.6;
  --max-width: 88%;

  --radius-s: 2px;
  --radius-m: 4px;
  --radius-l: 8px;

  /* Classical Roman Pigments */
  --yellow: var(--roman-gold-bright);
  --green: var(--roman-malachite);
  --orange: var(--bulla-terracotta-bright);
  --purple: var(--roman-purple);
  --pink: var(--roman-purple-bright);
  --blue: var(--roman-lapis);
}

/* Headings in Classical Monumental Roman Style */
h1, h2, h3, h4, h5, h6,
.markdown-rendered h1, .markdown-rendered h2, .markdown-rendered h3,
.markdown-rendered h4, .markdown-rendered h5, .markdown-rendered h6,
.cm-header-1, .cm-header-2, .cm-header-3, .cm-header-4 {
  font-family: 'Cinzel', 'Marcellus', serif;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  text-shadow: var(--ink-shadow);
}

h1, .cm-header-1 {
  letter-spacing: 0.12em;
  border-bottom: 1px solid var(--divider-color);
  padding-bottom: 0.3em;
  margin-top: 1.2em;
}

h2, .cm-header-2 {
  letter-spacing: 0.09em;
  border-bottom: 1px dashed var(--divider-color);
  padding-bottom: 0.25em;
  margin-top: 1em;
}

/* 1. Old Roman Cursive (Currens) */
.script-cursive, .roman-cursive, body.script-cursive-default {
  font-family: 'IM Fell English', 'Baskerville', cursive, serif !important;
  font-style: italic !important;
  transform: skewX(-3deg);
  line-height: 1.55 !important;
}

/* 2. Capitalis Monumentalis */
.script-monumentalis, .roman-monumentalis, body.script-monumentalis-default {
  font-family: 'Marcellus', 'Cinzel', serif !important;
  text-transform: uppercase !important;
  letter-spacing: 0.16em !important;
  line-height: 1.4 !important;
}

/* 3. Scriptio Continua (Imperial Capital) */
.script-capital, .roman-capital {
  font-family: 'Cinzel', serif !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
  line-height: 1.45 !important;
}

/* Interpuncts & Linea Supera */
.interpunct {
  font-style: normal;
  font-weight: 700;
  margin: 0 0.15em;
  opacity: 0.85;
}

.linea-supera {
  text-decoration: overline;
}

/* Drop Caps (Initial Capitals) */
.markdown-rendered p:first-of-type::first-letter {
  font-family: 'Cinzel', serif;
  font-size: 2.8em;
  float: left;
  line-height: 0.85;
  margin-right: 0.12em;
  margin-top: 0.08em;
  color: var(--color-accent);
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.15);
}
/* }}} */

/* +++ CALLOUTS & IMPERIAL DECREES {{{ */
.callout[data-callout="decree"],
.callout[data-callout="edictum"],
.callout[data-callout="senatus"],
.callout[data-callout="epistula"],
.callout[data-callout="sacrum"],
.callout[data-callout="legio"] {
  position: relative;
  overflow: visible;
  padding-bottom: 24px;
  background: var(--papyrus-bg-active);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  border-radius: 2px 4px 2px 4px;
}

.callout[data-callout="decree"]::after,
.callout[data-callout="edictum"]::after {
  content: "AVG";
  position: absolute;
  top: -12px;
  right: 16px;
  width: 38px;
  height: 38px;
  background: radial-gradient(circle at 35% 35%, #b25333, #8c3b24 60%, #3b140b 100%);
  border-radius: 50%;
  box-shadow: 2px 3px 6px rgba(0,0,0,0.5), inset 1px 1px 2px rgba(255,255,255,0.2), inset -2px -2px 4px rgba(0,0,0,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Marcellus', serif;
  font-size: 0.55rem;
  font-weight: bold;
  color: rgba(60, 20, 10, 0.9);
  text-shadow: 1px 1px 1px rgba(255,255,255,0.15);
}

.callout[data-callout="senatus"]::after {
  content: "SEN";
  position: absolute;
  top: -12px;
  right: 16px;
  width: 38px;
  height: 38px;
  background: radial-gradient(circle at 35% 35%, #dfb743, #c59b27 60%, #5a420b 100%);
  border-radius: 50%;
  box-shadow: 2px 3px 6px rgba(0,0,0,0.5), inset 1px 1px 2px rgba(255,255,255,0.3), inset -2px -2px 4px rgba(0,0,0,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Marcellus', serif;
  font-size: 0.55rem;
  font-weight: bold;
  color: #3b2804;
  text-shadow: 1px 1px 1px rgba(255,255,255,0.2);
}

.callout[data-callout="epistula"]::after {
  content: "LIV";
  position: absolute;
  top: -12px;
  right: 16px;
  width: 38px;
  height: 38px;
  background: radial-gradient(circle at 35% 35%, #b25333, #8c3b24 60%, #3b140b 100%);
  border-radius: 50%;
  box-shadow: 2px 3px 6px rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Marcellus', serif;
  font-size: 0.55rem;
  font-weight: bold;
  color: rgba(60, 20, 10, 0.9);
}

.callout[data-callout="legio"]::after {
  content: "LEG";
  position: absolute;
  top: -12px;
  right: 16px;
  width: 38px;
  height: 38px;
  background: radial-gradient(circle at 35% 35%, #a83222, #751a0e 60%, #3b0a04 100%);
  border-radius: 50%;
  box-shadow: 2px 3px 6px rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Marcellus', serif;
  font-size: 0.55rem;
  font-weight: bold;
  color: rgba(255, 230, 210, 0.85);
}

.callout[data-callout="sacrum"]::after {
  content: "SAC";
  position: absolute;
  top: -12px;
  right: 16px;
  width: 38px;
  height: 38px;
  background: radial-gradient(circle at 35% 35%, #842342, #5a142b 60%, #290511 100%);
  border-radius: 50%;
  box-shadow: 2px 3px 6px rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Marcellus', serif;
  font-size: 0.55rem;
  font-weight: bold;
  color: #f7d5de;
}
/* }}} */

/* +++ WAX TABLET CHECKBOXES {{{ */
input[type="checkbox"] {
  border: 1.5px solid var(--text-muted);
  border-radius: 2px;
  background-color: rgba(0, 0, 0, 0.04);
  transition: all 0.15s ease;
}

input[type="checkbox"]:checked {
  background-color: var(--bulla-terracotta);
  border-color: var(--bulla-terracotta);
}

/* Custom checkbox icons */
input[data-task=">"]:checked,
input[data-task="!"]:checked,
input[data-task="-"]:checked,
input[data-task="<"]:checked,
input[data-task="*"]:checked,
li[data-task=">"] > input:checked,
li[data-task="!"] > input:checked,
li[data-task="-"] > input:checked,
li[data-task="<"] > input:checked,
li[data-task="*"] > input:checked {
  --checkbox-marker-color: transparent;
  border: none;
  background-color: currentColor;
  -webkit-mask-size: var(--checkbox-icon);
  -webkit-mask-position: 50% 50%;
}

/* [!] Important */
input[data-task="!"]:checked,
li[data-task="!"] > input:checked {
  color: var(--color-orange);
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor'%3E%3Cpath fill-rule='evenodd' d='M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z' clip-rule='evenodd' /%3E%3C/svg%3E");
}

/* [*] Star */
input[data-task="*"]:checked,
li[data-task="*"] > input:checked {
  color: var(--roman-gold-bright);
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor'%3E%3Cpath d='M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z' /%3E%3C/svg%3E");
}

/* [-] Cancelled */
input[data-task="-"]:checked,
li[data-task="-"] > input:checked {
  color: var(--text-faint);
  -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20' fill='currentColor'%3E%3Cpath fill-rule='evenodd' d='M3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z' clip-rule='evenodd' /%3E%3C/svg%3E");
}
/* }}} */

/* +++ UI COMPONENTS (TABS, SIDEBARS, MODALS, SCROLLBARS) {{{ */

/* Horizontal Dividers */
hr {
  border: none;
  height: 2px;
  background: linear-gradient(to right, transparent, var(--divider-color) 20%, var(--divider-color) 80%, transparent);
  position: relative;
  margin: 2.2em 0;
}

hr::after {
  content: "🏛️";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: var(--background-primary);
  padding: 0 10px;
  font-size: 0.9em;
  color: var(--text-muted);
}

/* Antique Cursive Blockquotes */
blockquote, .markdown-rendered blockquote {
  font-family: 'IM Fell English', 'Baskerville', cursive, serif;
  font-style: italic;
  transform: skewX(-2deg);
  border-left: 3px solid var(--bulla-terracotta);
  background: rgba(140, 59, 36, 0.04);
  padding: 10px 18px;
  border-radius: 0 4px 4px 0;
  margin: 1.4em 0;
  color: var(--text-normal);
  line-height: 1.6;
}

/* Tabularium Tables */
.markdown-rendered table {
  border-collapse: collapse;
  width: 100%;
  margin: 1.5em 0;
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid var(--divider-color);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.markdown-rendered th {
  font-family: 'Cinzel', serif;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  font-weight: 700;
  background: rgba(140, 59, 36, 0.1);
  border-bottom: 2px solid var(--bulla-terracotta);
  padding: 8px 14px;
}

.markdown-rendered td {
  border-bottom: 1px solid var(--divider-color);
  padding: 6px 14px;
}

/* Inscribed Epigraphic Code Blocks */
.markdown-rendered pre, .markdown-source-view.mod-cm6 .cm-embed-block:not(.cm-callout) {
  background-color: var(--code-background);
  border: 1px solid var(--divider-color);
  border-radius: 4px;
  box-shadow: inset 1px 1px 4px rgba(0, 0, 0, 0.1);
}

.markdown-rendered code {
  color: var(--code-normal);
  background-color: rgba(140, 59, 36, 0.08);
  padding: 0.15em 0.35em;
  border-radius: 3px;
  font-family: var(--font-monospace);
  font-size: 0.9em;
}

/* Tituli & Tags as Roman Clay Bullae / Papyrus Slips */
.tag, a.tag {
  background-color: rgba(140, 59, 36, 0.12);
  color: var(--text-accent) !important;
  border: 1px solid rgba(140, 59, 36, 0.25);
  font-family: 'Cinzel', serif;
  font-size: 0.75em;
  letter-spacing: 0.05em;
  padding: 2px 8px;
  border-radius: 12px;
  text-decoration: none;
  transition: all 0.2s ease;
}

.tag:hover, a.tag:hover {
  background-color: var(--bulla-terracotta);
  color: #fff !important;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* Scrollbars Styled as Ancient Reed Stalks */
::-webkit-scrollbar {
  width: 9px;
  height: 9px;
}

::-webkit-scrollbar-track {
  background: var(--scrollbar-bg);
}

::-webkit-scrollbar-thumb {
  background: var(--scrollbar-thumb-bg);
  border-radius: 4px;
  border: 2px solid var(--scrollbar-bg);
}

::-webkit-scrollbar-thumb:hover {
  background: var(--scrollbar-active-thumb-bg);
}

/* Modals styled like Stone Inscription Tablets */
body .modal {
  background: var(--background-primary) !important;
  border: 1px solid var(--divider-color) !important;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45) !important;
  border-radius: 6px !important;
}

body .modal-bg {
  background-color: rgba(15, 12, 10, 0.7) !important;
}

/* Active Line Highlight */
.active-line-highlight .markdown-source-view.mod-cm6 .cm-active.cm-line {
  background: rgba(197, 155, 39, 0.12) !important;
  border-radius: 3px;
}

/* Fade formatting tags */
.shrink-formatting .cm-formatting {
  color: var(--text-faint) !important;
  font-size: var(--font-smaller) !important;
}
/* }}} */

/* +++ STYLE SETTINGS CONFIGURATION {{{ */
/* @settings

name: Roman Papyrus
id: obsidian-roman-papyrus
settings:
    -
        id: papyrus-grade-heading
        title: Pliny's Six Papyrus Grades (Naturalis Historia XIII.74–82)
        type: heading
        level: 1
    -
        id: default-papyrus-grade
        title: Default Papyrus Grade
        description: Choose the historical quality grade described by Pliny the Elder and Isidore
        type: class-select
        default: grade-augusta
        options:
            -
                label: I. Augusta — 13 Digits (Superfine Imperial White Pith)
                value: grade-augusta
            -
                label: II. Liviana — 12 Digits (Golden Ivory, Empress Livia's Grade)
                value: grade-liviana
            -
                label: III. Hieratica / Fanniana — 9 Digits (Thin Priestly & Literary Parchment)
                value: grade-hieratica
            -
                label: IV. Saitica — 7-8 Digits (Provincial Delta Knotty Amber)
                value: grade-saitica
            -
                label: V. Taeneotica — 6 Digits (Coarse Outer Bark, Sold by Bulk Weight)
                value: grade-taeneotica
            -
                label: VI. Emporetica — <6 Digits (Merchant Wrapping Scrap)
                value: grade-emporetica
    -
        id: papyrus-layout-heading
        title: Document Architecture & Scroll Mode
        type: heading
        level: 2
    -
        id: papyrus-document-layout
        title: Document Display Mode
        description: Choose between Plagula (card sheet on desk) or Volumen (continuous joined scroll)
        type: class-select
        default: papyrus-mode-plagula
        options:
            -
                label: Plagula (Bounded Papyrus Sheet with Deckle Edge Shadows)
                value: papyrus-mode-plagula
            -
                label: Volumen (Continuous Unrolled Scroll Roll with Kollesis Seams)
                value: papyrus-mode-volumen
            -
                label: Modern Full Width (Standard Obsidian Editor Layout)
                value: papyrus-mode-standard
    -
        id: papyrus-fibers-on
        title: Recto & Verso Fiber Weave Layering
        description: Overlays cross-grained Egyptian cyperus pith striations
        type: class-toggle
        default: on
    -
        id: papyrus-kollesis-seams
        title: Kollesis Glue Seams
        description: Display the historical joined plagulae overlap seam
        type: class-toggle
        default: on
    -
        id: bulla-seal-active
        title: Stamped Bulla Seals
        description: Display terracotta bulla seal and fastening cord
        type: class-toggle
        default: on
    -
        id: papyrus-ink-physics-heading
        title: Atramentum Ink Physics
        type: heading
        level: 2
    -
        id: ink-capillary-bleed
        title: Scribe Atramentum Bleed & Feathering
        description: Simulates the natural capillary diffusion of reed pen gall ink on porous cyperus pith
        type: class-select
        default: ink-bleed-historical
        options:
            -
                label: Historical Calibration (Authentic Reed Ink Feathering)
                value: ink-bleed-historical
            -
                label: Subtle Micro-Bleed (Very Light)
                value: ink-bleed-subtle
            -
                label: Porous / Heavy Bleed (Coarse Paper Running)
                value: ink-bleed-heavy
            -
                label: Crisp Modern (No Bleed)
                value: ink-bleed-none
    -
        id: typography-heading
        title: Classical Roman Typography & Epigraphy
        type: heading
        level: 2
    -
        id: shrink-formatting
        title: Fade & shrink Markdown formatting symbols
        type: class-toggle
        default: on
    -
        id: active-line-highlight
        title: Highlight active line in amber wash
        type: class-toggle
        default: on
*/
/* }}} */

/* +++ OBSIDIAN HUB {{{ */
/* @plugins
core:
- audio-recorder
- backlink
- command-palette
- daily-notes
- file-explorer
- global-search
- graph
- note-composer
- open-with-default-app
- outgoing-links
- outline
- page-preview
- random-note
- slash-commands
- switcher
- tag-pane
- templates
- word-count
- workspaces
- zk-prefixer

community:
- calendar
- obsidian-kanban
- sliding-panes-obsidian
- tag-wrangler
- cm-typewriter-scroll-obsidian
- better-word-count
- obsidian-day-planner
- workbench-obsidian
- obsidian-citation-plugin
- obsidian-journey-plugin
- obsidian-banners
- obsidian-dataview
- obsidian-style-settings
- obsidian-plugin-todo
*/
/* }}} */
"""

    full_css = front_matter + "\n\n" + fonts_block + "\n\n" + css_body

    with open('theme.css', 'w', encoding='utf-8') as f:
        f.write(full_css)

    with open('obsidian.css', 'w', encoding='utf-8') as f:
        f.write(full_css)

    print("Successfully built theme.css and obsidian.css! Size:", len(full_css), "bytes")

if __name__ == '__main__':
    build_theme()
