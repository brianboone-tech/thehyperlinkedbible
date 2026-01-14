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
├── Readable Bible Index.md ← THE HUB
│   └── [66 book folders → chapter files]
├── Home/01 - Getting Started.md
│   ├── Home/02 - Site Layout.md
│   ├── Home/03 - Understanding Links.md
│   ├── Home/04 - Video Resources.md
│   └── Home/05 - For Different Users.md
├── Home/Indexes/
│   ├── Readable Bible/
│   │   └── [66 book index pages: 01 - Genesis through 66 - Revelation]
│   ├── Chiasm Index.md
│   ├── Intertextuality Pairs Index.md
│   ├── Trajectory Tables Index.md
│   └── TOSK Index.md
├── Home/06 - How Chiasms - Overview.md
│   └── [13 chiasm deep dive pages]
└── Home/20 - How Quotations - Overview.md
    └── [8 quotation deep dive pages]
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
| `Readable Bible Index.md` | THE HUB - main entry point for reading Scripture |
| `Home/01 - Getting Started.md` | Learning hub with links to sub-pages |
| `Home/02 - Site Layout.md` | Explains hub-and-spoke architecture |
| `Home/03 - Understanding Links.md` | Explains IP, C, TOSK, TT link types |
| `Home/04 - Video Resources.md` | Explains YouTube videos on Trajectory Tables |

**Files Modified (6):**
| File | Changes |
|------|---------|
| `quartz.layout.ts` | Added custom folder ordering (Readable Bible first) |
| `index.md` | Simplified - removed 66-book tables, added Quick Start section |
| `Home/05 - For Different Users.md` | Updated navigation links |
| `Home/06 - How Chiasms - Overview.md` | Added Getting Started breadcrumb |
| `Home/20 - How Quotations - Overview.md` | Added Getting Started breadcrumb |
| `Home/08 - Scripture Index.md` | Added Readable Bible Index link |

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
