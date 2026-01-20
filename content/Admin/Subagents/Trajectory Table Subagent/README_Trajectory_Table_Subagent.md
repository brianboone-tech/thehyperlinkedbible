# Trajectory Table Subagent Suite

**Version:** 2.0
**Last Updated:** 2025-12-04
**Status:** ✅ Production Ready

---

## Overview

This folder contains three complementary subagents for working with TOSK Trajectory Tables:

| Subagent | Purpose | Input | Output |
|----------|---------|-------|--------|
| **NT→OT Research** | Creates trajectory from verse pair | NT verse + OT verse | Full trajectory + foundation texts |
| **Creator** | Creates trajectory from provided data | Complete trajectory info | Trajectory + foundation texts |
| **Standardizer** | Fixes formatting of existing tables | Table filename | Standardized table |

---

## Key Methodological Principle (Schnittjer & Harmon)

All trajectory work should follow this interpretive order:

```
START → Biblical parallels (OT-to-OT, then NT-to-OT)
      → Extrabiblical parallels (for comparison/contrast)
      → RETURN to biblical interpretation as determinative
```

**Why this matters**: NT authors often follow interpretive patterns already established within the OT. Biblical parallels are more determinative than any secondary source.

---

## 1. NT→OT Research Subagent (v2.0)

**File:** `NT_to_OT_Research_Subagent_Prompt.md`

### What It Does
Takes an NT verse and OT verse pair, researches the connection, and creates a complete trajectory table with foundation texts. **Now includes OT-to-OT development tracing and type classification.**

### When to Use
- You have an NT verse that echoes an OT verse
- You want the subagent to research intermediate stages
- You want linguistic analysis (Greek/Hebrew connections)
- You want to trace the canonical trajectory within the OT itself

### How to Invoke
```
Use the trajectory table subagent on Revelation 1:5 and Psalm 89:27,37
```

### Workflow (v2.0)
1. Theme Identification
2. Linguistic Analysis (Lexicon lookup)
3. **OT-to-OT Development** (CRITICAL - trace biblical trajectory before secondary sources)
4. Research Trajectory Stages (search Mather, Fairbairn, Keller)
5. Check Existing Trajectories
6. Build Trajectory Table with **Type Classifications**
7. **Compare with Extrabiblical** (secondary - for comparison/contrast)
8. Create Foundation Texts (one per row, with OT-to-OT section)
9. Link to Reference Pages
10. Verification Checklist

### Time: ~3-5 minutes

---

## 2. Trajectory Creator Subagent (v2.0)

**File:** `Trajectory_Creator_Subagent.md`

### What It Does
Creates a trajectory table when you provide all the stage information upfront. **Now requires type classification for each stage.**

### When to Use
- You've already done the research
- You have a complete list of stages, texts, and theological development
- You want efficient creation without additional research

### How to Invoke
```
Use the Trajectory Creator subagent with this data:
**Trajectory Name:** [Name]
**Intro Paragraph:** [2-4 sentences]
**Entries:**
1. Stage: [Name], Text: [Reference], Development: [Description], Type: [Forward/Backward] | [Direct/Providential]
2. ...
```

### Time: ~2-3 minutes per trajectory

---

## 3. Trajectory Table Standardizer Subagent

**File:** `Trajectory_Table_Standardizer_Prompt.md`

### What It Does
Fixes formatting issues in existing trajectory tables:
- Converts `|` to `\|` in links
- Makes Theological Development concise
- Bolds stage names and key terms
- Restores from backup if needed

### When to Use
- Existing trajectory table has broken links
- Formatting doesn't match standard
- Theological Development is too verbose

### How to Invoke
```
Use the Trajectory Table subagent to standardize "Assembly (Gathered People of God)"
```

### Time: ~60-90 seconds per file

---

## File Structure

```
Trajectory Table Subagent/
├── README_Trajectory_Table_Subagent.md     ← This file (master README)
├── NT_to_OT_Research_Subagent_Prompt.md    ← Research + Create from verse pair (v2.0)
├── Trajectory_Creator_Subagent.md          ← Create from provided data (v2.0)
├── Trajectory_Table_Standardizer_Prompt.md ← Standardize existing tables
└── README_Standardizer_Subagent.md         ← Standardizer quick reference
```

---

## Quick Decision Guide

| Situation | Use This Subagent |
|-----------|-------------------|
| "I found Rev 1:5 echoes Ps 89:27—create a trajectory" | **NT→OT Research** |
| "I have all my stages ready—just create the table" | **Creator** |
| "My trajectory table links are broken" | **Standardizer** |
| "I want to batch-fix 10 trajectory tables" | **Standardizer** |

---

## Standard Format Requirements

All trajectory tables must follow this format:

### Title
```markdown
## [THEME NAME] TRAJECTORY TABLE
```

### Introductory Paragraph
2-4 sentences covering: origin → development → Christ fulfillment → eschatological consummation

### Table Structure
```markdown
| # | Stage | Key Text(s) | Theological Development | Text Analysis |
|---|-------|-------------|------------------------|---------------|
| 1 | **Stage Name** | [[Readable Bible/...#Anchor\|Display]] | Concise; **key terms bolded** | [[Trajectory Tables - Foundation Texts/...\|Display]] |
```

### Critical Requirements
- Links use `\|` (backslash-pipe) inside tables
- Anchors use periods: `#Chapter . Verse`
- Stage names are **bold**
- Theological Development: concise (1-3 sentences), key terms bolded, semicolons separate ideas
- **One foundation text per trajectory row** (1:1 correspondence)

### Foundation Text Requirements (v2.0)
Each foundation text must include:
- **OT-to-OT Development** section
- **Type Classification**: Forward-looking/Backward-looking | Direct/Providential
- Enhanced **Ninefold Analysis** with OT-to-OT Development field

---

## Type Classification Guide

### Forward-Looking vs. Backward-Looking

| Type | Definition | Examples |
|------|------------|----------|
| **Forward-Looking** | Contains textual indicators within original context pointing forward | Deut 18:15-19 (prophet like Moses), Ps 110:4 (priest after Melchizedek) |
| **Backward-Looking** | Recognized as typological only from NT vantage point | Ps 22 → crucifixion, Jonah's three days (Matt 12:40) |

### Direct vs. Providential

| Type | Definition | Examples |
|------|------------|----------|
| **Direct** | Divinely commanded institution | Passover, sacrifices, Day of Atonement, Tabernacle |
| **Providential** | Sovereignly arranged person/event | Adam, Moses, David, Exodus event |

---

## Related Files

- **CLAUDE.md Command 9**: Documents the NT→OT Research workflow
- **- Hermeneutics.md**: Full hermeneutical methodology including Forward/Backward types, Prosopological Exegesis
- **- How to Study the Bible's Use of the Bible.md**: Summary of Schnittjer & Harmon methodology
- **Standard Template**: `TOSK Trajectory Tables/Abrahamic Covenant.md`
- **Example**: `TOSK Trajectory Tables/Other - Thematic/Davidic Messianic Titles.md`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2025-12-04 | Added OT-to-OT Development step; Added Type Classification (Forward/Backward, Direct/Providential); Enhanced Foundation Text template; Added Schnittjer & Harmon methodology |
| 1.0 | 2025-12-03 | Initial release with three subagents |

---

**Created:** 2025-12-03
**Updated:** 2025-12-04
