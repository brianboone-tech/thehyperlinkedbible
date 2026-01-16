# Claude Code Work Log

This document tracks work done with Claude Code on The Hyperlinked Bible project.

---

## Project Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        INTERNET / CLOUD / GITHUB                            │
│   ┌──────────────────────┐         ┌──────────────────────┐                │
│   │   GitHub Repository  │ ──────► │    Public Website    │                │
│   │ github.com/brianboone│         │ brianboone-tech.     │                │
│   │ -tech/thehyperlinked │         │ github.io/           │                │
│   │ bible                │         │ thehyperlinkedbible  │                │
│   └──────────────────────┘         └──────────────────────┘                │
│              ▲                                                              │
│              │ npx quartz sync                                              │
└──────────────┼──────────────────────────────────────────────────────────────┘
               │
┌──────────────┼──────────────────────────────────────────────────────────────┐
│              │                         LOCAL                                │
│   ┌──────────────────────┐         ┌──────────────────────┐                │
│   │  Local Quartz Folder │ ──────► │  Obsidian Content    │                │
│   │ C:\Obsidian Vaults\  │         │  Folder              │                │
│   │ thehyperlinkedbible  │         │ ...\content          │                │
│   └──────────────────────┘         └──────────────────────┘                │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Component | Location |
|-----------|----------|
| Local Quartz Root | `C:\Obsidian Vaults\thehyperlinkedbible` |
| Content Folder | `C:\Obsidian Vaults\thehyperlinkedbible\content` |
| GitHub Repo | https://github.com/brianboone-tech/thehyperlinkedbible |
| Live Website | https://brianboone-tech.github.io/thehyperlinkedbible/ |

---

## Site Structure

```
index.md (Welcome)
├── Home/01 - Getting Started.md (Learning Hub)
│   ├── Home/02 - Site Layout.md
│   ├── Home/03 - Understanding Links.md
│   ├── Home/04 - Video Resources.md
│   ├── Home/05 - For Different Users.md
│   ├── Home/06 - Why Chiasms Matter.md
│   ├── Home/07 - Why Cross-References Matter.md
│   └── Home/08 - Scripture Index.md ← THE HUB
├── Readable Bible/ [1,255 chapter files]
├── Trajectory Tables/ [174 typological studies]
├── Chiasm/ [1,732 structural analyses]
├── Intertextuality Pairs/ [2,587 cross-references]
├── Reference Bible/, Lexicon/, TOSK/, LXX Reference/
└── Books - Private/ [Theological book chapters]
```

### Content Statistics

| Resource | Count |
|----------|------:|
| Bible Books | 66 |
| Bible Chapters | 1,189 |
| Chiasms | 1,732 |
| Intertextuality Pairs | 2,587 |
| Trajectory Tables | 174 |
| TOSK Cross-References | 500,000+ |

---

## Work Log

### Sessions 1-3 (January 13, 2026)

- **Created CLAUDE.md** for project documentation
- **Fixed bracket rendering bug** in 1,168 Reference Bible files
- **Updated Quartz color scheme** - Rosé Pine Dawn (light) / Catppuccin Frappé (dark)
- **Added custom CSS** for headers, lexicon pages, blockquotes, tables
- **Fixed Explorer** - Rainbow folder colors, nested popovers, collapse behavior
- **Added cssclasses** to Chiasm (1,721) and Trajectory Table (174) files
- **Reduced broken links** from 10,939 to 7,290 (~33% reduction)

### Sessions 4-5 (January 14, 2026)

- **Fixed Trajectory Table CSS** - Outer borders, page layout
- **Added Admin folder to .gitignore**
- **Fixed invalid chapter navigation** in Readable Bible and LXX Reference
- **Greek word studies**: proskuneō (G4352) and latreúō (G3000)

### Sessions 6-7 (January 14, 2026) - Home Section Revamp

**Restructured home/introduction section:**
- Created 8 focused Home pages (Getting Started, Site Layout, Understanding Links, etc.)
- Archived 33 obsolete tutorial pages to `Home/Archive/`
- Emphasized Readable Bible as THE HUB throughout

**Readable Bible cleanup (1,255 files):**
- Removed "-R" suffix from chapter titles
- Updated navigation to `← Previous | Next →` format

### Session 8 (January 15, 2026) - Folder Index Pages

**Created custom index.md files to replace auto-generated folder listings:**
- 66 Readable Bible book indexes (with chapter grids and related resources)
- 66 Reference Bible book indexes
- 12 main folder indexes (Chiasm, IP, TT, TOSK, Lexicon, etc.)
- 4 subfolder indexes

**Trajectory Table Width Fix:**
- Modified `renderPage.tsx` to propagate cssclasses to `<body>` element
- Created `trajectory-table-wide` CSS class to hide right sidebar

### Session 9 (January 15, 2026) - Book Splitting + Trajectory Tables

#### Book Chapter Splitting

Split theological books into individual chapter files with navigation links.

**Tremper Longman - "Immanuel in Our Place"** (22 files)
- Location: `Books - Private/Tremper Longman/Immanuel in Our Place/`
- Contents: Front Matter, 19 chapters (Sacred Space, Acts, People, Time), Postscript

**Edmund Clowney - "The Unfolding Mystery"** (13 files)
- Location: `Books - Private/Edmund Clowney/The Unfolding Mystery/`
- Contents: Foreword, Introduction, 9 chapters, Scripture Index
- Note: Chapter 7 manually created (PowerShell regex failed on apostrophe)

**Navigation pattern:** `[[Previous|← Title]] | [[Next|Title →]]`

#### Trajectory Table Format Update (174 files)

Applied new table format to all trajectory tables:

```yaml
# Frontmatter: Added trajectory-table-wide class
cssclasses:
  - trajectory-table
  - trajectory-table-wide
```

```markdown
# Table: Removed # column, embedded numbers in Stage
| Stage                        | Key Text(s)... | Theological Development | Intertextuality Pairs |
| **#1 - OT Type - Name...**   | ...            | ...                     | ...                   |
```

### Session 10 (January 15, 2026) - Table Separators + Video Fixes

**Fixed Trajectory Table Separators (174 files):**
- Earlier script corrupted table separator rows (3-column instead of 4-column)
- This caused "Intertextuality Pairs" column to not render
- Fixed all 174 files to have correct 4-column separator

**Fixed Broken YouTube Videos (7 of 9):**
- Updated video IDs for: Camp of Israel, Census Ransom, Ceremonial Uncleanness, Cherubim, Circumcision, Cities of Refuge, Coats of Skins

**Remaining Broken YouTube Videos (need replacement URLs):**

| # | Trajectory Table | Broken Video ID |
|---|------------------|-----------------|
| 029 | Church as Israel (New Covenant People) | NXUn2hLrPYc |
| 043 | Davidic Messianic Titles (Faithful Witness, Firstborn, Ruler of Kings) | vwbyLH4EKsM |

**Created Source Tracking File:**
- `Admin/TT Discovery/Trajectory Table Sources.md` - maps 47 trajectory tables to their source documentation

### Session 11 (January 15, 2026) - TT Discovery + New Trajectory Table

**TT Discovery: Five Books Analysis**

Analyzed 5 theological books for new trajectory table candidates:
1. Tremper Longman - "Immanuel in Our Place" (22 chapters, typological catalog)
2. Christopher Wright - "Knowing Jesus" (9 chapters, methodological)
3. Alec Motyer - "Look to the Rock" (12 chapters, methodological)
4. Edmund Clowney/Keller - "Preaching Christ in a Postmodern World" (15 chapters, homiletical)
5. Geerhardus Vos - "Biblical Theology" (2 files, meta-methodological)

**Finding:** Lower yield than expected - 4 of 5 books are methodological (HOW to see Christ) rather than typological catalogs (listing specific types). Existing 175 TTs are comprehensive.

**New Candidates Identified:**
- **Purim (Divine Reversal)** - from Longman Ch. 19 (HIGH priority, not yet built)
- **The Singing Sufferer (Christ the Choir Master)** - from Clowney Psalm 22 lecture (**IMPLEMENTED**)

**New Trajectory Table Created: The Singing Sufferer (Christ the Choir Master)**

Complete trajectory tracing Christ as the singer of the Psalms:
- 8 stages from Psalm 13 → Psalm 22 → Jonah → Matthew 27:46 → Hebrews 2:12 → Romans 15:8-9 → Revelation 5
- Full lexicon analysis (קָהָל/ἐκκλησία, הָלַל/ὑμνέω, נָגַד)
- 8 foundation text files created
- Four-Step Application included

**Files Created:**
- `Trajectory Tables/-- The Singing Sufferer (Christ the Choir Master).md`
- `Trajectory Tables - Foundation Texts/The Singing Sufferer (Christ the Choir Master)/` (8 files)
- `Admin/TT Discovery/Five Books Analysis - Candidates.md`

**CSS Fix: Trajectory Table Width**

Modified `custom.scss` to extend center column for `trajectory-table-wide` pages:
- Set `.page { max-width: 98vw; }` to use available screen width
- Center content now extends into former right sidebar space

### Session 12 (January 16, 2026) - Trajectory Table Section Order Fix

**Issue Discovered:** Merge script from Session 11 placed sections in wrong order for 168+ files.

**Problem:** The merge script appended backup content (table + IPs + Foundation Texts) AFTER the existing Four-Step and Lexicon sections, resulting in:
- Four-Step Application appearing BEFORE the table (wrong)
- Lexicon Findings appearing BEFORE the table (wrong)
- Duplicate Four-Step and Lexicon sections at the end

**Correct Section Order:**
1. Frontmatter (with cssclasses)
2. Title + YouTube + intro + Type Classification
3. TABLE (5-column format)
4. Canonical Intertextuality Pairs
5. Foundation Texts
6. Four-Step Application
7. Lexicon Findings

**Solution:** Created `Admin/fix_section_order.py` to:
- Parse each file and identify section boundaries
- Extract each section independently
- Reassemble in correct order
- Remove duplicate sections
- Add proper frontmatter with cssclasses

**Results:**
- **168 files** fixed via batch script
- **File 152** (Spirit of Wisdom) manually fixed - had duplicate old-format table
- **File 045** (Day of Midian) frontmatter corrected
- **0 errors**

**Files Created:**
- `Admin/fix_section_order.py` - Batch fix script for section order
- `Admin/fix_section_order_log.txt` - Detailed fix log

---

## Technical Reference

### CSS Classes

| Class | Applied To | Purpose |
|-------|------------|---------|
| `chiasm` | 1,721 chiasm files | Extra list spacing |
| `trajectory-table` | 174 TT files | Enhanced table borders |
| `trajectory-table-wide` | 174 TT files | Hides right sidebar |
| `lexicon` | Readable Bible chapters | Lexicon styling |

### Key Files

| File | Purpose |
|------|---------|
| `quartz.layout.ts` | Page layout, Explorer config, folder ordering |
| `quartz/styles/custom.scss` | Custom CSS styling |
| `quartz/components/renderPage.tsx` | Modified to propagate cssclasses to body |

### Sync Commands

```bash
cd "C:\Obsidian Vaults\thehyperlinkedbible"
npx quartz sync
```

If EBUSY error (Obsidian has folder open):
```bash
git push origin v4
```
