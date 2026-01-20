# Trajectory Table Standardization Subagent

**Version:** 1.0
**Status:** ✅ Ready for Use
**Created:** 2025-11-05

## What It Does

Automatically standardizes Trajectory Table files to match the Abrahamic Covenant template format:
- Fixes broken links (`|` → `\|`)
- Restores from backup if needed
- Converts to 4-column format with row numbers
- Makes Theological Development concise with **bolded key terms**
- Ensures proper title and introductory paragraph

**Time:** ~60-90 seconds per file

## How to Use

### Single File
```
Use the Trajectory Table subagent to standardize "Assembly (Gathered People of God)"
```

### Batch Processing
```
Use the Trajectory Table subagent to standardize these files:
1. Assembly (Gathered People of God)
2. Baptism (Typology of Water Crossing)
3. Branch (Messianic Expectation)
```

## Standard Format

### Title
```markdown
## [THEME NAME] THEOLOGY TRAJECTORY TABLE
```

### Introductory Paragraph
2-4 sentences covering origin → development → Christ → eschatological fulfillment

### Table
```markdown
| # | Stage | Key Text(s) | Theological Development |
|---|-------|-------------|------------------------|
| 1 | **Stage Name** | [[...#Chapter . Verse\|Display]] | Concise; **key terms bold**; semicolons |
```

## Key Fixes

### 1. Link Format
**BEFORE:** `[[Readable Bible/...#Chapter . Verse|Display]]`
**AFTER:** `[[Readable Bible/...#Chapter . Verse\|Display]]`

### 2. Theological Development
**BEFORE (verbose):**
```
"Day of the assembly" at Sinai—Yahweh summons Israel to mountain,
speaks Ten Commandments audibly, establishes covenant. Israel becomes
qahal YHWH. Terror prompts request for mediation (Deut 18:16).
Foundational assembly event.
```

**AFTER (concise with bolding):**
```
**Day of assembly** at Sinai; Yahweh speaks Ten Commandments directly;
Israel becomes qahal YHWH; terror prompts request for **mediation**
```

### 3. Stage Names
**BEFORE:** `Foundation at Sinai`
**AFTER:** `**Foundation at Sinai**`

## What Gets Checked

- ✅ Title format
- ✅ Introductory paragraph present
- ✅ 4-column table structure
- ✅ Row numbering (1, 2, 3...)
- ✅ Link escape characters (`\|`)
- ✅ Stage name bolding
- ✅ Theological Development conciseness
- ✅ Key term bolding

## Report Format

After completion, subagent provides:
```markdown
## TRAJECTORY TABLE STANDARDIZATION REPORT

**File:** [FILENAME]
**Status:** ✅ SUCCESS

### Changes Made:
- [x] Title standardized
- [x] Links fixed to use \| format (23 links corrected)
- [x] Theological Development made concise (16 entries revised)
- [x] Key terms bolded (34 terms)
- [x] Stage names bolded (16 stages)

### Statistics:
- Total rows: 16
- Links corrected: 23
- Theological Development entries revised: 16

### Verification:
- All links use \|: ✅
- Theological Development concise: ✅
- Stage names bolded: ✅
- Matches Abrahamic Covenant standard: ✅
```

## Template File

Standard is: `TOSK Trajectory Tables/Abrahamic Covenant.md`

All Trajectory Tables are standardized to match this format exactly.

## Error Handling

- **No backup available:** Proceeds with current file, notes in report
- **Unusual structure:** Does best standardization, flags for review
- **Theological concerns:** Only formats, doesn't change theology, notes concerns

## Testing Checklist

After subagent runs, manually verify:
1. Open the standardized file in Obsidian
2. Check that all links navigate correctly (Ctrl+Click)
3. Verify Theological Development is readable and concise
4. Confirm key terms are bolded appropriately
5. Check that Stage names are bolded

## Files

- **Prompt:** `Trajectory_Table_Standardizer_Prompt.md`
- **README:** This file
- **Standard:** `TOSK Trajectory Tables/Abrahamic Covenant.md`

---

**Last Updated:** 2025-12-03
