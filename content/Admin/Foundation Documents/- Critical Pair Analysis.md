# Critical Pair Analysis for Trajectory Tables

**Last Updated**: 2025-12-18
**Purpose**: Methodology for identifying CRITICAL intertextuality pairs in Trajectory Tables
**Related**: [[- Formatting.md]] | [[- Hermeneutics.md]] | [[- Vision.md]] | [[CLAUDE.md]]

---

## Overview

**CRITICAL** markers in Trajectory Tables identify rows that contain foundational intertextual connections grounding the typological trajectory in explicit biblical cross-references. Not all rows in a trajectory table are CRITICAL—many represent theological development or contextual stages that support but do not establish the typology.

**The Purpose of CRITICAL Markers**:
1. Distinguish foundational connections from supporting context
2. Identify rows with documented intertextuality pair links
3. Guide readers to the most important biblical anchors for each trajectory
4. Enable filtered views (e.g., video inputs) showing only essential stages

---

## The Five CRITICAL Criteria

A trajectory table row is marked **CRITICAL:** if it meets **ONE OR MORE** of these criteria:

### Criterion 1: Direct NT Quotation/Citation

The NT text explicitly quotes or cites the OT text with a quotation formula or clear verbal correspondence.

**Indicators**:
- NT uses quotation formula ("as it is written," "to fulfill what was spoken")
- NT author identifies the connection as fulfilled/accomplished
- Direct verbal parallel between NT and OT texts

**Examples**:
- John 19:36 quoting Exodus 12:46 ("Not one of his bones will be broken")
- Matthew 2:15 quoting Hosea 11:1 ("Out of Egypt I called my son")
- Hebrews 1:5 quoting Psalm 2:7 ("You are my Son")

### Criterion 2: Key Typological Establishment

The pair establishes the foundational type-antitype relationship—the "origin point" of the typology.

**Indicators**:
- First biblical occurrence of the typological pattern
- Establishes the vocabulary or imagery that later texts develop
- Creates the "shadow" that subsequent stages elaborate

**Examples**:
- Genesis 3:15 establishing the Seed Promise (protoevangelium)
- Exodus 12:1-14 establishing the Passover type
- Leviticus 16 establishing the Day of Atonement pattern

### Criterion 3: Escalation Demonstration

The pair shows how Christ surpasses the OT shadow—demonstrating the "how much more" principle.

**Indicators**:
- Explicit comparison showing Christ's superiority
- Hebrews-style "greater than" language
- Once-for-all vs. repeated pattern
- Eternal vs. temporal contrast

**Examples**:
- Hebrews 9:11-14 showing Christ's blood superior to animal sacrifices
- Hebrews 7:23-25 showing Christ's permanent priesthood vs. mortal priests
- 2 Corinthians 3:7-11 showing new covenant glory exceeding old

### Criterion 4: Core Prophetic Development

The pair shows prophetic anticipation of fulfillment with explicit Messianic connection.

**Indicators**:
- Prophetic text explicitly anticipating future fulfillment
- Isaiah 53 and other Servant Song connections
- Messianic prophecies (Davidic, priestly, prophetic)
- Forward-looking expectational language in original context

**Examples**:
- Isaiah 53:7 ("like a lamb to the slaughter") anticipating Christ
- Zechariah 9:9 (king riding on donkey) fulfilled in Matthew 21:5
- Malachi 3:1 (messenger preparing the way) fulfilled in John the Baptist

### Criterion 5: Verbal/Thematic Anchor

The pair contains the primary vocabulary that defines the trajectory—direct verbal links using same Hebrew/Greek terms.

**Indicators**:
- Same Hebrew root word in OT source and later OT/NT usage
- LXX translation using identical Greek term picked up by NT
- Technical theological vocabulary specific to this trajectory
- Rare or distinctive terms that create unmistakable verbal link

**Examples**:
- H3722 כָּפַר (kaphar, "to atone") linking Leviticus 16 to Day of Atonement trajectory
- G2435 ἱλαστήριον (hilasterion, "mercy seat/propitiation") linking Leviticus 16:2 LXX to Romans 3:25
- "Lamb of God" vocabulary linking Passover lamb to John 1:29

---

## What is NOT CRITICAL

Pairs that should NOT be marked CRITICAL:

| Category | Description | Example |
|----------|-------------|---------|
| **General Thematic** | Broad thematic connections without direct verbal links | Psalm praising God's forgiveness (supports but doesn't establish atonement typology) |
| **Parallel/Supporting** | Passages that reinforce but don't establish the typology | Chronicles describing temple worship (context, not core typology) |
| **Liturgical/Commemorative** | References to remembering or celebrating | Psalm 135:8 remembering firstborn judgment |
| **Extended Applications** | Later applications without core typological function | Ethical applications of sacrificial imagery |
| **Coincidental Similarity** | Similar language without intentional connection | Common words appearing in unrelated contexts |

---

## The Decision Framework

For each intertextuality pair in a trajectory table, ask these questions in order:

```
1. Does the NT EXPLICITLY QUOTE this OT text?
   → YES = CRITICAL (Criterion 1)

2. Does this pair ESTABLISH the foundational typology?
   → YES = CRITICAL (Criterion 2)

3. Does this pair demonstrate Christ's SUPERIORITY over the type?
   → YES = CRITICAL (Criterion 3)

4. Is this a PROPHETIC text with explicit Messianic anticipation?
   → YES = CRITICAL (Criterion 4)

5. Does this pair contain PRIMARY VOCABULARY of the trajectory?
   → YES = CRITICAL (Criterion 5)

6. Is this pair merely SUPPORTING or CONTEXTUAL?
   → YES = NOT CRITICAL
```

**Principle**: Err on the side of fewer CRITICAL designations. Only pairs truly foundational to the typology should be marked. Quality over quantity.

---

## How to Mark CRITICAL Pairs

### In the Trajectory Table Row

Add **CRITICAL:** followed by the intertextuality pair link at the end of the Theological Development column:

```markdown
| 2 | **Stage Name** | [[Key Text]] | Theological explanation. **CRITICAL:** [[Intertextuality Pairs/.../From to To\|Display]] | [[Foundation Text]] |
```

**Important**: Use backslash-pipe (`\|`) inside table cells.

### In the Canonical Intertextuality Pairs Section

Add **CRITICAL:** after the pair link, before the annotation:

```markdown
- [[Intertextuality Pairs/NT to OT/43 - John/John 3.14 to Numbers 21.8-9|John 3:14 → Numbers 21:8-9]] - **CRITICAL:** Jesus explicitly applies the bronze serpent to His crucifixion...
```

### Multiple CRITICAL Pairs Per Row

If multiple CRITICAL pairs apply to one row:

```markdown
| 2 | **Stage** | [[Text]] | Explanation. **CRITICAL:** [[Pair1\|Display1]] **CRITICAL:** [[Pair2\|Display2]] | [[Foundation]] |
```

---

## Analysis Workflow

### Step 1: Identify the Trajectory Theme
- Read the trajectory table title and introduction
- Note the type classification (Direct/Providential, Forward/Backward-Looking)
- Identify the core theological concept being traced

### Step 2: Catalog Primary Vocabulary
- Read associated Foundation Texts if available
- List Hebrew key terms (with Strong's numbers)
- List Greek key terms (with Strong's numbers)
- Identify distinctive vocabulary unique to this trajectory

### Step 3: Analyze Each Pair
For each intertextuality pair listed:
1. Read the pair annotation
2. Apply the 5-criterion framework
3. Determine if CRITICAL or supporting
4. Note which criterion(s) apply

### Step 4: Mark CRITICAL Pairs
- Add **CRITICAL:** markers to qualifying pairs in appendix
- Add inline **CRITICAL:** references to matching table rows
- Verify backslash-pipe formatting in tables

### Step 5: Verify
- [ ] All CRITICAL pairs identified using the 5 criteria
- [ ] **CRITICAL:** label added to pairs in appendix section
- [ ] Inline **CRITICAL:** references added to matching table rows
- [ ] No duplicate CRITICAL references
- [ ] Backslash-pipe (`\|`) used in table cell links

---

## Example Analysis: Bronze Serpent Trajectory

**Theme**: Christ lifted up for healing, fulfilling Numbers 21 bronze serpent

**Primary Vocabulary**:
- H5375 נָשָׂא (nasa) - "to lift up"
- H7311 רוּם (rum) - "to be high, exalted"
- G5312 ὑψόω (hypsoo) - "to lift up, exalt"

**CRITICAL Pairs Identified**:

| Pair | Criterion | Reasoning |
|------|-----------|-----------|
| John 3:14 → Numbers 21:8-9 | 1, 2 | Jesus EXPLICITLY applies bronze serpent to crucifixion; ESTABLISHES the typology |
| Isaiah 52:13 → Numbers 21:8-9 | 4, 5 | PROPHETIC anticipation using same "lifted up" (רוּם) vocabulary |
| Galatians 3:13 → Deuteronomy 21:23 | 1, 3 | NT QUOTES Deuteronomy; shows ESCALATION (Christ became curse) |
| Hebrews 12:2 → Psalm 110:1 | 3, 5 | ESCALATION demonstration; "looking to Jesus" parallels looking to serpent |

**NOT CRITICAL**:
- General references to Christ's crucifixion without explicit typological connection
- Supporting Leviticus 16 scapegoat material (related but different trajectory)

---

## Batch Processing Command

To run Critical Pair analysis on multiple tables:

```
Run Critical Pairs on all tables without CRITICAL markers
```

Or for a single table:

```
Run Critical Pairs on "[Trajectory Table Name]"
```

---

## Integration with Video Inputs

The `Trajectory Table Inputs/` folder contains simplified versions of trajectory tables for Google LLM video generation. These input files include:
- Instruction paragraph for video creation
- Introduction paragraph from trajectory table
- Table rows containing ONLY **CRITICAL** marked stages

**Tables without CRITICAL markers** are tracked in:
```
Trajectory Table Inputs/- Tables Without Critical Elements.md
```

After running Critical Pair analysis:
1. Tables that gain CRITICAL markers should have video inputs regenerated
2. Tables that remain without CRITICAL markers may need:
   - Intertextuality pair files created first
   - Manual review to determine if the trajectory lacks explicit biblical anchors
   - Alternative approach for video input (use all rows, not just CRITICAL)

---

## Related Documents

- [[- Formatting.md]] - Trajectory table formatting standards
- [[- Hermeneutics.md]] - Biblical interpretation methodology
- [[- Vision.md]] - Project roadmap and quality standards
- [[- Standard Format.md]] - Intertextuality pair format standards
- [[CLAUDE.md]] - Technical procedures and commands

---

## Version History

- **v1.0** (2025-12-18): Initial creation, consolidating Critical Pairs Subagent methodology

---

**This methodology defines how CRITICAL pairs are identified and marked in all Trajectory Tables throughout the vault.**
