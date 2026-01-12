# Intertextuality Pair Link Repair Plan

## Problem Summary

**Total Broken Links**: 136 out of 196 (69.4%)
- OT→OT: 52 broken (26.8% success rate)
- NT→OT: 84 broken (32.8% success rate)

**Affected Files**: 36 trajectory tables (-- prefixed files)
**Working Files**: 7 trajectory tables have 100% link integrity

---

## Issue Categories

### Category 1: Missing IP Files (Primary Issue)
Most links reference IP files that simply don't exist yet. The trajectory tables were created with links anticipating files that need to be created.

**Example**:
```
[[Intertextuality Pairs/OT to OT/10 - 2 Samuel/2 Samuel 15.30 to Zechariah 14.4|...]]
```
This file path doesn't exist in `Intertextuality Pairs/OT to OT/10 - 2 Samuel/`.

### Category 2: Trailing Backslashes
Some links end with `\` causing link resolution failures.

**Example**:
```
to Judges 4-5\
```
Should be:
```
to Judges 4-5
```

### Category 3: Chapter Ranges vs Specific Verses
Some links use chapter ranges (Genesis 6-8) instead of specific verse references.

**Example**:
```
Genesis 6-8 to 1 Peter 3.20
```
Should specify a primary verse:
```
Genesis 6.14 to 1 Peter 3.20
```

### Category 4: Conceptual Links
Some links are marked `(conceptual)` indicating thematic connections without specific textual parallels.

**Example**:
```
[[Intertextuality Pairs/NT to OT/58 - Hebrews/Hebrews 2.14-17 to Ruth (conceptual)|...]]
```
These may need special handling or removal.

---

## Repair Strategy

### Phase 1: Inventory & Categorize (Do First)

1. **Generate Complete Broken Link List**
   - Run script to extract all IP links from 36 broken trajectory tables
   - Categorize each link by issue type:
     - Missing file (needs creation)
     - Trailing backslash (needs cleanup)
     - Chapter range (needs verse specification)
     - Conceptual (needs decision)
   - Output to `Admin/Reports/broken-ip-links-inventory.md`

2. **Verify Existing IP Files**
   - List all existing files in `Intertextuality Pairs/OT to OT/` and `Intertextuality Pairs/NT to OT/`
   - Cross-reference with trajectory table links
   - Identify any near-matches (similar but different naming)

### Phase 2: Fix Link Format Issues (Quick Wins)

3. **Remove Trailing Backslashes**
   - Search all trajectory tables for links ending with `\`
   - Clean up formatting
   - Estimated: ~5-10 links

4. **Standardize Verse References**
   - Convert chapter ranges to primary verse references where applicable
   - Example: `Genesis 6-8` → `Genesis 6.14` (primary ark verse)
   - Requires theological judgment for each case

5. **Handle Conceptual Links**
   - Decision point: Create conceptual IP files OR remove links?
   - Recommendation: Create brief conceptual IP files with thematic explanation
   - Alternative: Change link format to note rather than file reference

### Phase 3: Create Missing IP Files (Bulk Work)

6. **Batch Create OT→OT IP Files** (52 files needed)

   For each missing file:
   - Create file in `Intertextuality Pairs/OT to OT/[Book Number] - [Book Name]/`
   - Use standard IP format from `- Standard Format.md`
   - Include:
     - Source text quotation
     - Target text quotation
     - Connection type (verbal, thematic, structural)
     - Brief annotation

   **Processing Order** (by trajectory table):
   | Priority | Trajectory Table | Missing OT→OT |
   |----------|-----------------|---------------|
   | 1 | Theophanies | 5 |
   | 2 | Josiah | 3 |
   | 3 | Cyrus | 3 |
   | 4 | Hezekiah | 3 |
   | 5 | Judah's Scepter | 3 |
   | 6 | Boaz | 3 |
   | ... | (remaining files) | ... |

7. **Batch Create NT→OT IP Files** (84 files needed)

   For each missing file:
   - Create file in `Intertextuality Pairs/NT to OT/[Book Number] - [Book Name]/`
   - Use standard IP format
   - Include NT quotation/allusion analysis

   **Processing Order** (by trajectory table):
   | Priority | Trajectory Table | Missing NT→OT |
   |----------|-----------------|---------------|
   | 1 | Theophanies | 6 |
   | 2 | Hagar and Ishmael | 6 |
   | 3 | Eve | 5 |
   | 4 | Sarah | 4 |
   | 5 | Scapegoat | 4 |
   | 6 | Enoch | 4 |
   | 7 | Absalom | 4 |
   | ... | (remaining files) | ... |

### Phase 4: Verification

8. **Run Link Verification Script**
   - Re-run the verification script from previous session
   - Confirm 100% link resolution
   - Document any remaining issues

9. **Spot Check Quality**
   - Read 5-10 newly created IP files
   - Verify content accuracy
   - Confirm formatting compliance

---

## File Naming Convention

**Standard IP filename format**:
```
[Source Book] [Chapter].[Verse(s)] to [Target Book] [Chapter].[Verse(s)].md
```

**Examples**:
- `Genesis 18.1 to Genesis 19.24.md`
- `Matthew 27.5 to 2 Samuel 17.23.md`
- `Hebrews 2.14-17 to Ruth 2.1.md` (for conceptual, use primary verse)

**Folder structure**:
```
Intertextuality Pairs/
├── OT to OT/
│   ├── 01 - Genesis/
│   ├── 02 - Exodus/
│   └── ...
└── NT to OT/
    ├── 40 - Matthew/
    ├── 43 - John/
    └── ...
```

---

## IP File Template

```markdown
# [Source Reference] → [Target Reference]

## Source Text
> "[Quotation from source]"
> — [Source Reference]

**Hebrew/Greek Terms**: [Key terms with Strong's numbers]

## Target Text
> "[Quotation from target]"
> — [Target Reference]

**Hebrew/Greek Terms**: [Key terms with Strong's numbers]

## Connection Analysis

**Type**: [Direct Quotation / Allusion / Echo / Thematic / Structural]

**Verbal Links**: [Shared vocabulary, LXX connections]

**Contextual Links**: [Shared themes, narrative parallels]

## Theological Significance

[1-2 paragraphs explaining the intertextual relationship and its significance for biblical theology]

---

**Related Trajectory Tables**: [[Trajectory Tables/[Name]|[Name]]]
```

---

## Execution Timeline

### Session 1: Inventory & Quick Fixes
- [ ] Generate complete broken link inventory
- [ ] Fix trailing backslashes
- [ ] Standardize chapter range references
- [ ] Decide on conceptual link handling

### Session 2: OT→OT IP Creation (52 files)
- [ ] Create Theophanies OT→OT pairs (5)
- [ ] Create Josiah OT→OT pairs (3)
- [ ] Create remaining OT→OT pairs (44)

### Session 3: NT→OT IP Creation Part 1 (42 files)
- [ ] Create Theophanies NT→OT pairs (6)
- [ ] Create Hagar/Ishmael NT→OT pairs (6)
- [ ] Create Eve, Sarah, Scapegoat NT→OT pairs (13)
- [ ] Create additional NT→OT pairs (17)

### Session 4: NT→OT IP Creation Part 2 (42 files)
- [ ] Complete remaining NT→OT pairs
- [ ] Run verification
- [ ] Quality check

---

## Scripts Needed

1. **extract_broken_links.py** - Parse trajectory tables, extract IP links, check existence
2. **create_ip_file.py** - Generate IP file from template with parameters
3. **fix_trailing_backslash.py** - Clean up formatting issues
4. **verify_all_links.py** - Final verification scan

---

## Files with Perfect Integrity (Reference)

These 7 files have 100% working links - use as formatting reference:

1. `-- Ashes of Red Heifer (Continual Cleansing).md`
2. `-- Burning Bush (Divine Presence in Fire).md`
3. `-- Cain (Seed of Serpent).md`
4. `-- Ephod (High Priest's Garment of Representation).md`
5. `-- First-Born Redemption (Consecration to God).md`
6. `-- Hyssop (Instrument of Blood Application).md`
7. `-- Oath of God (Unchangeable Counsel).md`

---

## Success Criteria

- [ ] 0 broken IP links in trajectory tables
- [ ] All IP files follow standard format
- [ ] All IP files contain accurate biblical content
- [ ] Bidirectional links verified (trajectory tables ↔ IP files)
