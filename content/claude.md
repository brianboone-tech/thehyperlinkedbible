# Claude Code Work Log

This document tracks the work done with Claude Code on The Hyperlinked Bible project.

---

## Project Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        INTERNET / CLOUD / GITHUB                            │
│                                                                             │
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
│              │                                                              │
│   ┌──────────────────────┐         ┌──────────────────────┐                │
│   │  Local Quartz Folder │ ──────► │  Obsidian Content    │                │
│   │ C:\Obsidian Vaults\  │         │  Folder              │                │
│   │ thehyperlinkedbible  │         │ ...\content          │                │
│   └──────────────────────┘         └──────────────────────┘                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Locations

| Component | Location |
|-----------|----------|
| Local Quartz Root | `C:\Obsidian Vaults\thehyperlinkedbible` |
| Content Folder | `C:\Obsidian Vaults\thehyperlinkedbible\content` |
| GitHub Repo | https://github.com/brianboone-tech/thehyperlinkedbible |
| Live Website | https://brianboone-tech.github.io/thehyperlinkedbible/ |

### How It Works

1. **Obsidian Vault**: Markdown notes are created and edited in the `content` folder
2. **Quartz**: Static site generator converts Obsidian markdown into a navigable website
3. **Sync**: Running `npx quartz sync` pushes changes to GitHub
4. **GitHub Pages**: Automatically builds and deploys the site

---

## Site Structure

### Navigation Hierarchy

```
index.md (Welcome)
├── Home/01 - Getting Started.md (Learning Hub)
│   ├── Home/02 - Site Layout.md
│   ├── Home/03 - Understanding Links.md
│   ├── Home/04 - Video Resources.md
│   ├── Home/05 - For Different Users.md
│   ├── Home/06 - Why Chiasms Matter.md
│   ├── Home/07 - Why Cross-References Matter.md
│   └── Home/08 - Scripture Index.md ← THE HUB (browse all 66 books)
├── Home/Indexes/
│   ├── Readable Bible/ [66 book index pages]
│   ├── Chiasm Index.md
│   ├── Intertextuality Pairs Index.md
│   ├── Trajectory Tables Index.md
│   └── TOSK Index.md
├── Home/Archive/ [Archived tutorial pages]
├── Readable Bible/ [1,255 chapter files]
├── Trajectory Tables/ [126 typological studies]
├── Chiasm/ [1,732 structural analyses]
└── Intertextuality Pairs/ [2,587 cross-references]
```

### Explorer Folder Order (Custom)

Configured in `quartz.layout.ts` with custom `sortFn`:

1. Readable Bible (the hub)
2. Trajectory Tables
3. Chiasm
4. Intertextuality Pairs
5. Reference Bible
6. Lexicon
7. The Treasury of Scripture Knowledge
8. LXX Reference
9. Redemptive-Historical Cycles
10. Trajectory Tables - Foundation Texts
11. Home
12. Resources

### Content Statistics

| Resource | Count |
|----------|------:|
| Books | 66 |
| Chapters | 1,189 |
| Chiasms | 1,732 |
| Intertextuality Pairs | 2,587 |
| Trajectory Tables | 126 |
| Trajectory Tables with Videos | 103 |
| TOSK Cross-References | 500,000+ |

---

## Work Log

### Session 1 - January 13, 2026

- **Created CLAUDE.md** to document project architecture and track work
- **Fixed bracket rendering bug** - Wiki links with `[text]` in display text weren't rendering
- **Applied fix to 1,168 Reference Bible files** (Genesis through Revelation)
- **Updated Quartz color scheme** to match AnuPpuccin theme:
  - Light mode: Rosé Pine Dawn palette with custom teal accent (#1A7DA4)
  - Dark mode: Catppuccin Frappé palette with custom teal accent (#11B7C5)
- **Added custom CSS** (`quartz/styles/custom.scss`) for headers, lexicon pages, blockquotes

### Session 2 - January 13, 2026

- **Fixed Explorer rainbow folder colors** - Corrected CSS selectors
- **Enabled nested popovers** - Modified `popover.inline.ts` for popover-from-popover
- **Added table styling CSS** - Borders, hover effects, cell padding
- **Added Scripture Index to homepage** - 66 books by category
- **Added cssclasses to Chiasm files** (1,721 files) and Trajectory Table files (175 files)
- **Set folder click behavior to "collapse"** in Explorer

### Session 3 - January 13, 2026 (Broken Links)

- **Created broken links checker script** (`check-broken-links.ps1`)
- **Reduced broken links from 10,939 to 7,290** (~33% reduction)
- Key fixes:
  - Fixed `[[Home]]` → `[[index|Home]]` in 65 files
  - Converted 1,345 decimal G-number links to range-based Lexicon links
  - Fixed chapter navigation in last chapters of multiple books

### Session 4 - January 14, 2026

- **Fixed Trajectory Table outer border CSS**
- **Added Admin folder to .gitignore**
- **Removed TOSK links from 66 Scripture pages**
- **Fixed invalid chapter navigation** in Readable Bible (9 files) and LXX Reference (14 files)

### Session 5 - January 14, 2026

- **Greek word studies**: proskuneō (G4352) and latreúō (G3000)
- **Fixed Trajectory Table page layout** (sidebar issue)

### Session 6 - January 14, 2026 (Home Section Revamp)

**Major restructure of home/introduction section to emphasize Readable Bible as the center.**

**New Files Created (5):**
| File | Purpose |
|------|---------|
| `Readable Bible Index.md` | Main entry point (later merged into Scripture Index - see Session 7) |
| `Home/01 - Getting Started.md` | Learning hub with links to sub-pages |
| `Home/02 - Site Layout.md` | Explains hub-and-spoke architecture |
| `Home/03 - Understanding Links.md` | Explains IP, C, TOSK, TT link types |
| `Home/04 - Video Resources.md` | Explains YouTube videos on Trajectory Tables |

**Files Modified (5):**
| File | Changes |
|------|---------|
| `quartz.layout.ts` | Added custom folder ordering (Readable Bible first) |
| `index.md` | Simplified - removed 66-book tables, added Quick Start section |
| `Home/05 - For Different Users.md` | Updated navigation links |
| `Home/06 - How Chiasms - Overview.md` | Added Getting Started breadcrumb (later archived) |
| `Home/20 - How Quotations - Overview.md` | Added Getting Started breadcrumb (later archived) |

**Key Design Decisions:**
- Readable Bible emphasized as THE HUB throughout all pages
- Explorer sidebar shows Readable Bible first
- Clean welcome page with prominent "Read the Bible" link
- Getting Started hub with focused sub-pages (not one massive page)
- Old tutorial files (02-12) preserved as backup

**Folder Reorganization:**
- Renamed `Home/Scripture` → `Home/Indexes` (clearer naming)
- Created `Home/Indexes/Readable Bible/` subfolder
- Moved 66 book index pages (01 - Genesis through 66 - Revelation) into subfolder
- Updated ~4,429 file references to use new paths

### Session 7 - January 14, 2026 (Content Simplification & Cleanup)

**Readable Bible Chapter Cleanup (1,255 files):**
- Removed "-R" suffix from all chapter titles (e.g., "Genesis-R 1" → "Genesis 1")
- Updated navigation to use arrows with pipe separators: `← Previous | Next →`
- Removed book index links from chapter headers
- Commands used:
  ```bash
  sed -i 's/^# \(.*\)-R \([0-9]*\) *$/# \1 \2/' */*.md
  sed -i 's/\[\[.*|← \(.*\)\]\] - \[\[.*|\(.*\) →\]\]/[[path|← \1]] | [[path|\2 →]]/' */*.md
  ```

**Home Section Simplification:**

Archived 33 obsolete pages to `Home/Archive/`:
- Old tutorials: 02-10, 12 (10 files)
- Chiasm deep dives: 13-26 (14 files)
- Quotation deep dives: 27-35 (9 files)

Renumbered remaining pages to clean sequence (01-08):

| # | Page | Purpose |
|---|------|---------|
| 01 | Getting Started | Learning hub |
| 02 | Site Layout | Architecture explanation |
| 03 | Understanding Links | IP, C, TOSK, TT guide |
| 04 | Video Resources | YouTube content explanation |
| 05 | For Different Users | Layperson/Pastor/Scholar paths |
| 06 | Why Chiasms Matter | Macro-level indicators (NEW) |
| 07 | Why Cross-References Matter | Micro-level indicators (NEW) |
| 08 | Scripture Index | Browse all 66 books |

**New Content Created (based on Hermeneutics document):**

`Home/06 - Why Chiasms Matter.md`:
- Explains chiasms as "macro-level indicators" of authorial intent
- Uses real example: Genesis 1:26-28 chiasm
- References the Flood narrative (Genesis 6-9) center point
- Links to actual chiasm files on the site

`Home/07 - Why Cross-References Matter.md`:
- Explains four "micro-level indicators": Quotations, Shared Key Words, Repeated Event Sequences, Covenantal Significance
- Uses real examples: Matthew 1:22-23 → Isaiah 7:14, Noah's ark / Moses's basket connection
- Links to actual Intertextuality Pairs on the site

**Final Cleanup:**
- Deleted redundant `Readable Bible Index.md` from content root
- Updated 8 files to point to `Home/08 - Scripture Index` instead
- Fixed self-referential links in Scripture Index
- Fixed stray "please" typo in Why Cross-References Matter
- Added images to Site Layout and Understanding Links pages
- Added YouTube embed to Video Resources page

### Session 8 - January 15, 2026 (Trajectory Table Width Fix + Folder Index Pages)

#### Part 1: Trajectory Table Width Fix

**Problem:** Trajectory tables overflow the center content area on desktop, extending past the right sidebar.

**Solution:** Created new CSS class `trajectory-table-wide` that:
- Hides right sidebar on trajectory table pages (desktop only)
- Uses `minmax(0, 1fr)` for center column to prevent overflow behind left sidebar
- Keeps horizontal scroll on table container as fallback

**Initial Issue:** CSS wasn't working because Quartz only applied `cssclasses` to the `<article>` element, not `<body>`. CSS can't select parent/sibling elements, so the sidebar couldn't be hidden.

**Fix:** Modified `renderPage.tsx` to propagate `cssclasses` from frontmatter to the `<body>` element.

**Files Modified:**
| File | Changes |
|------|---------|
| `quartz/components/renderPage.tsx` | Added cssclasses to `<body>` element (lines 262-263, 267) |
| `quartz/styles/custom.scss` | Changed selector to `body.trajectory-table-wide` (lines 195-231) |
| `content/Trajectory Tables/003 - Abraham (Father of Faith).md` | Added `trajectory-table-wide` class for testing |

**Test Page:** Abraham trajectory table (003)

**Next Steps:**
1. Test Abraham page layout
2. If successful, apply `trajectory-table-wide` to all 175 trajectory table files

#### Part 2: Folder Index Pages (Eliminate Auto-Generated Folder Listings)

**Goal:** Replace all Quartz auto-generated folder listing pages with custom index.md files.

**Created/Modified Files:**

| Category | Count | Description |
|----------|------:|-------------|
| Readable Bible book indexes | 66 | Enhanced indexes with overview, chapters grid, and related resources links |
| Reference Bible book indexes | 66 | Simple indexes with chapters grid |
| Main folder indexes | 12 | Index pages for top-level content folders |
| Subfolder indexes | 4 | For IP subfolders, Home subfolders |

**Readable Bible Book Index Template:**
- Book title and back link to Scripture Index
- Overview table (Testament, Chapters, Category)
- 10-column chapter grid
- Related Resources section linking to Chiasms, Intertextuality, and Trajectories for that book

**Reference Bible Book Index Template:**
- Book title and back link to Scripture Index
- Simple chapter grid

**Main Folder Indexes Created:**
| Folder | Source |
|--------|--------|
| `Chiasm/index.md` | Moved from Home/Indexes/Chiasm Index.md |
| `Intertextuality Pairs/index.md` | Moved from Home/Indexes/IP Index.md |
| `Trajectory Tables/index.md` | Moved from Home/Indexes/TT Index.md |
| `The Treasury of Scripture Knowledge/index.md` | Moved from Home/Indexes/TOSK Index.md |
| `Readable Bible/index.md` | New - overview with categorized book links |
| `Reference Bible/index.md` | New - overview with book links |
| `Lexicon/index.md` | New - explains how to access lexicon |
| `LXX Reference/index.md` | New - explains Septuagint resources |
| `Trajectory Tables - Foundation Texts/index.md` | New - explains supporting materials |
| `Redemptive-Historical Cycles/index.md` | Copied from existing overview file |
| `Home/index.md` | New - links to Getting Started and resources |
| `Intertextuality Pairs/NT to OT/index.md` | New |
| `Intertextuality Pairs/OT to OT/index.md` | New |
| `Home/Indexes/index.md` | New |
| `Home/Archive/index.md` | New |

**Deleted Files:**
- 66 old book files from Readable Bible (Genesis.md, Exodus.md, etc.) - replaced by index.md

---

## Broken Links Status

**Last Updated**: January 14, 2026
**Remaining**: ~7,290 (down from 10,939)

### Resolved
- `[[Home]]` → `[[index|Home]]` links (65 files)
- Decimal G-number links (1,345 links in 61 files)
- Invalid chapter navigation links

### Remaining (by priority)

**Low Priority (can ignore):**
- Admin folder placeholders (~300 links) - template files, not public

**Medium Priority:**
- Missing image files in Resources folder (~16 links)
- Trajectory Tables - Missing IP/Lexicon entries (~500+ links)

**Low Priority:**
- Invalid chapter references (Exodus 168, etc.)
- Reference Bible missing verses (~130 links)

---

## Technical Notes

### Quartz Configuration

**Explorer Folder Ordering** (`quartz.layout.ts`):
```typescript
Component.Explorer({
  folderClickBehavior: "collapse",
  sortFn: (a, b) => {
    const folderOrder = [
      "Readable Bible",
      "Trajectory Tables",
      "Chiasm",
      // ... etc
    ]
    // Custom sort logic
  },
})
```

### CSS Classes Used

| Class | Applied To | Purpose |
|-------|------------|---------|
| `cssclasses: chiasm` | 1,721 chiasm files | Extra list spacing |
| `cssclasses: trajectory-table` | 175 TT files | Enhanced table borders |
| `cssclasses: trajectory-table-wide` | TT files (testing) | Hides right sidebar, widens content |
| `cssclasses: lexicon` | Readable Bible chapters | Lexicon styling |

### Key Files

| File | Purpose |
|------|---------|
| `quartz.layout.ts` | Page layout and Explorer config |
| `quartz/styles/custom.scss` | Custom CSS styling |
| `quartz.config.ts` | Site configuration |
| `Admin/Foundation Documents/- Vision.md` | Project vision and methodology |
| `Admin/Foundation Documents/- Hermeneutics.md` | Interpretation framework |

---

## Sync Command

```bash
cd "C:\Obsidian Vaults\thehyperlinkedbible"
npx quartz sync
```

If EBUSY error occurs (Obsidian has folder open), use:
```bash
git push origin v4
```
