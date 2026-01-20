# Foundation Text Linking Plan

## Overview

This document tracks the linking of Foundation Texts to Trajectory Tables. The goal is to connect each Trajectory Table to its relevant Foundation Texts, enabling navigation from the trajectory analysis to detailed verse-by-verse study.

---

## Completed Work (2025-12-09)

### Phase 1: Add Foundation Texts Sections

**Script:** `add_foundation_texts_section.py`

**What it does:**
1. Extracts all verse references from Intertextuality Pair links in each Trajectory Table
2. Consolidates overlapping verse ranges
3. Checks the corresponding `Trajectory Tables - Foundation Texts/[Name]/` folder for existing files
4. Creates a "Foundation Texts" section at the bottom with:
   - Linked entries (where matching foundation text files exist)
   - Plain text entries (where no foundation text exists yet)
5. Creates an "Extra Foundation Texts" section for files that exist but don't match pair-derived verses

**Results:**
- **115 Trajectory Tables processed** - Foundation Texts sections added
- **11 Trajectory Tables skipped** - See edge cases below

---

## Edge Cases (Require Manual Review)

### 1. Already Has Foundation Texts Section
| Trajectory Table | Status | Notes |
|------------------|--------|-------|
| Aaron (The Great High Priest) | ✅ Done manually | First test case, completed before script |

### 2. No Pair Links Found
These trajectory tables have no Intertextuality Pair links in them, so no verse references could be extracted.

| Trajectory Table | Action Needed |
|------------------|---------------|
| Babylonian Exile (Judgment and Discipline) | Add pair links or manually create Foundation Texts section |
| Fire from Heaven (Divine Acceptance and Judgment) | Add pair links or manually create Foundation Texts section |
| Isaiah (Suffering Servant Messenger) - REDISTRIBUTION READY | Duplicate/variant file - review for deletion |
| Israel (Corporate New-Adam) | Add pair links or manually create Foundation Texts section |
| Sabbath (Rest in Christ) | Add pair links or manually create Foundation Texts section |
| Samuel (Prophet-Priest-Judge) | Add pair links or manually create Foundation Texts section |
| Solomon's Temple (Glory of God's Dwelling) | Add pair links or manually create Foundation Texts section |
| Spies and Unbelief (Testing God's Promise) | Add pair links or manually create Foundation Texts section |

### 3. Zero Consolidated Ranges (Parse Failures)
| Trajectory Table | Issue | Action Needed |
|------------------|-------|---------------|
| Levites (Substitutionary Service) | 28 verses found but 0 consolidated - verse format parsing failed | Review verse reference format in pair links |

---

## Current Plan: Founda v2 Subagent

### What is Founda v2?

**Location**: `Admin/Subagents/Founda Subagent/Founda_v2_Subagent_Prompt.md`

Founda v2 is a subagent prompt that automates the creation of foundation text files for unlinked entries in any Trajectory Table's Foundation Texts section.

**What it does:**
1. Reads the Trajectory Table and locates the `## Foundation Texts` section
2. Identifies **unlinked entries** (plain text references like `Hebrews 1:13`) vs **linked entries** (`[[...]]`)
3. For each unlinked entry:
   - Parses the verse reference to determine book number and filename
   - Extracts context from the trajectory's NT to OT / OT to OT pair analysis
   - Creates a foundation text file with:
     - Readable Bible wikilink header
     - Context paragraph (drawn from pair analysis)
     - Greek/Hebrew key terms
     - Connections (TO, FROM OT, FROM NT)
     - Christological connection
     - Link back to trajectory table
4. Updates the Trajectory Table to convert plain text entries to wiki links

### How to Invoke

```
Run Founda v2 on "[Trajectory Table Name]"
```

Example:
```
Run Founda v2 on "Abraham (Father of Faith)"
```

Or use the Task tool with general-purpose subagent to process multiple trajectories.

---

## Execution Plan

### Phase 2: Create Missing Foundation Texts (IN PROGRESS)

**Method**: Run Founda v2 on each trajectory table with unlinked entries.

**Completed:**
| Trajectory Table | Date | Files Created |
|------------------|------|---------------|
| Aaron (The Great High Priest) | 2025-12-09 | 42 files (full completion) |
| Adam (The First and Last Adam) | 2025-12-10 | 21 new files |
| Abel (First Martyr) | 2025-12-10 | 31 new files (40 total) |
| Abraham (Father of Faith) | 2025-12-10 | 36 new files (44 total) |
| Altar of Incense (Christ's Intercession) | 2025-12-10 | 4 new files |
| Anointing Oil (Holy Spirit) | 2025-12-10 | 2 new files |
| Ark of the Covenant (God's Throne of Mercy) | 2025-12-10 | 11 new files |
| Book of Life (God's Record of the Elect) | 2025-12-10 | 9 new files |

**Total Foundation Texts Created:** 156 files across 8 trajectories

**Next Session:** Continue alphabetically starting with **Brazen Altar (Place of Sacrifice)**

**Priority order for remaining:**
1. ~~**High-traffic trajectories** (Adam, Abraham, David, Moses)~~ (Adam & Abraham complete)
2. **Core typological themes** (Passover, Day of Atonement, Tabernacle, Temple)
3. **Remaining trajectories** alphabetically (currently at "B" - Brazen Altar)

**Batch Processing Option:**
To process multiple trajectories efficiently, use the Task tool to spawn agents that run Founda v2 on batches of 3-5 trajectories at a time.

### Phase 3: Review Extra Foundation Texts
The "Extra Foundation Texts" section in each file contains Foundation Text files that were created for the original TOSK Trajectory Table format but don't match any pair-derived verses. Options:
1. Keep as supplementary material
2. Add corresponding pairs to connect them
3. Move to a different trajectory if misplaced

### Phase 4: Edge Case Resolution
- Add pair links to the 8 trajectories with no pairs
- Fix verse parsing in Levites (Substitutionary Service)
- Delete or merge duplicate files (e.g., `Isaiah - REDISTRIBUTION READY`)

---

## Statistics

### Foundation Texts Coverage
- Total Trajectory Tables: 126
- With Foundation Texts section: 116 (92%)
- Pending manual review: 10 (8%)

### Foundation Text Files
- Total folders in `Trajectory Tables - Foundation Texts/`: ~100+
- Matched to pair-derived verses: varies by trajectory
- "Extra" (from original TOSK format): varies by trajectory

---

## File Locations

| Resource | Path |
|----------|------|
| Trajectory Tables | `Trajectory Tables/` |
| Foundation Texts | `Trajectory Tables - Foundation Texts/[Name]/` |
| This plan | `Admin/Subagents/Founda Subagent/Foundation Text Linking Plan.md` |
| Script | `add_foundation_texts_section.py` (can delete after verification) |

---

## Changelog

| Date | Action | Details |
|------|--------|---------|
| 2025-12-09 | Initial setup | Manually completed Aaron (The Great High Priest) as test case |
| 2025-12-09 | Batch processing | Ran script on all 126 trajectory tables; 115 processed, 11 skipped |
| 2025-12-09 | Created plan | Documented edge cases and next steps |
| 2025-12-09 | Created Founda v2 | Wrote subagent prompt at `Admin/Subagents/Founda Subagent/Founda_v2_Subagent_Prompt.md` |
| 2025-12-09 | Completed Aaron | Ran Founda v2 on Aaron - created 18 new foundation texts, updated all links (42 total files) |
| 2025-12-09 | Updated plan | Documented Founda v2 workflow and execution plan for remaining trajectories |
| 2025-12-10 | Completed Adam | Created 21 new foundation texts for Adam (The First and Last Adam) |
| 2025-12-10 | Completed Abel | Created 31 new foundation texts for Abel (First Martyr), total now 40 files |
| 2025-12-10 | Completed Abraham | Created 36 new foundation texts for Abraham (Father of Faith), total now 44 files |
| 2025-12-10 | Session summary | 88 new foundation texts created this session; next trajectory: Altar of Incense |
| 2025-12-10 | Completed Altar of Incense | Created 4 new foundation texts (Genesis 14:17-20, Leviticus 10:10-11, 2 Chronicles 26:18, Hebrews 7:1-4) |
| 2025-12-10 | Completed Anointing Oil | Created 2 new foundation texts (1 Samuel 16:14, Psalm 51:11) |
| 2025-12-10 | Completed Ark of the Covenant | Created 11 new foundation texts (Exodus 25:8-9, 25:40, Leviticus 16:11-19, 16:27, 1 Samuel 6:1-2, 1 Chronicles 28:19, Psalm 132:6-7, John 1:14, Hebrews 8:5, 13:11, 1 John 2:1-2) |
| 2025-12-10 | Completed Book of Life | Created 9 new foundation texts (Numbers 16:5, 27:15-18, 1 Kings 19:10, Isaiah 62:2, John 10:3-4, Acts 13:48, Romans 11:2-4, 2 Timothy 2:19, Revelation 3:12); now at 156 total files across 8 trajectories |
| 2025-12-13 | Moved plan file | Relocated from `Admin/` to `Admin/Subagents/Founda Subagent/` for better organization |
