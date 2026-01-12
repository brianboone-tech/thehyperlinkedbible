# Intertextuality Pairs Standard Format

**Last Updated**: 2025-12-13
**Purpose**: Standards for Intertextuality Pairs and inline cross-reference links
**Goal**: Balance quick navigation with theological insight

---

## Current Architecture

The vault now uses **inline links** at the end of each verse in the Readable Bible, with detailed analysis in dedicated files:

```
Readable Bible verse → | [[IP]] | [[C]] | [[TOSK]] | [[TT]] |
                              ↓
              Intertextuality Pairs/OT to OT/[Book]/
              Intertextuality Pairs/NT to OT/[Book]/
```

**Link Types**:
| Abbrev | Meaning | Target Folder |
|--------|---------|---------------|
| **IP** | Intertextual Pair | `Intertextuality Pairs/OT to OT/` or `Intertextuality Pairs/NT to OT/` |
| **C** | Chiasm | `Chiasm/` |
| **TOSK** | Treasury of Scripture Knowledge | `The Treasury of Scripture Knowledge/` |
| **TT** | Trajectory Table | `Trajectory Tables/` |

---

## Intertextuality Pair File Format

### OT to OT Pairs

**Location**: `Intertextuality Pairs/OT to OT/[##] - [Book]/[Source Verse] to [Target Verse].md`

**Example**: `Intertextuality Pairs/OT to OT/01 - Genesis/Genesis 1.1 to Psalm 104.1.md`

```markdown
# Genesis 1:1 to Psalm 104:1

**Source Text**: [[Readable Bible/01 - Genesis/Genesis 1#Genesis 1 . 1|Genesis 1:1]]

**Target Text**: [[Readable Bible/19 - Psalms/Psalm 104#Psalm 104 . 1|Psalm 104:1]]

**Confidence**: B - Probable

**Type**: ~ Allusion

**Subject**: Creation hymn echoing Genesis narrative

**Explanation**: [50-100 words explaining the hermeneutical connection, verbal parallels, and theological significance]

---

**Related**:
- [[Trajectory Tables/[Trajectory Name]|Trajectory Table]]
- [[Chiasm/Chiasm - [##] - [Book] [Ch] . [V] - [V]|Related Chiasm]]
```

### NT to OT Pairs

**Location**: `Intertextuality Pairs/NT to OT/[##] - [Book]/[NT Verse] to [OT Verse].md`

**Example**: `Intertextuality Pairs/NT to OT/43 - John/John 1.1 to Genesis 1.1.md`

```markdown
# John 1:1 to Genesis 1:1

**NT Text**: [[Readable Bible/43 - John/John 1#John 1 . 1|John 1:1]]

**OT Source**: [[Readable Bible/01 - Genesis/Genesis 1#Genesis 1 . 1|Genesis 1:1]]

**Type**: Direct Quotation / Allusion / Typology / Echo

**Subject**: [One-line description]

**Explanation**: [50-100 words explaining how the NT author uses the OT text]

**Christological Connection**: [One sentence showing how this points to Christ]

---

**Related**:
- [[Trajectory Tables/[Trajectory Name]|Trajectory Table]]
```

---

## Formatting Standards

### 1. Confidence Levels (OT to OT only)

Use Schnittjer's four-level system:

- **A - Certain**: Verbal parallels, explicit quotations, marked citations
- **B - Probable**: Strong thematic/verbal connections, likely intentional
- **C - Possible**: Plausible connections but uncertain
- **D - Unlikely**: Suggested by some scholars but doubtful

### 2. Relationship Types

Use Schnittjer's notation system:

- **~** - Allusion/interpretive use
- **//** - Direct verbal parallel or quotation
- **/~/** - Synoptic parallel
- **+** - Interpretive blend (combining multiple sources)
- **>/<** - More or less similar

### 3. NT Usage Types

For NT to OT pairs, classify the usage:

- **Direct Quotation**: Explicit citation with verbal correspondence
- **Allusion**: Indirect reference without quotation formula
- **Typology**: OT person/event/institution as type of NT antitype
- **Echo**: Subtle resonance without clear intentionality
- **Fulfillment**: Prophetic text explicitly fulfilled

### 4. Explanation Length

**Target**: 50-100 words per pair

**Focus on**:
- Hermeneutical method (how the text is used)
- Theological significance (why it matters)
- Key verbal/thematic connections
- Canonical/redemptive-historical development

**Avoid**:
- Extensive commentary (>150 words)
- Multiple paragraphs
- Repeating obvious information

### 5. Christological Connections (NT to OT only)

**Format**: One sentence showing how the connection points to Christ

**Example**: "Christ is THE promised seed who defeats Satan and reverses the curse."

---

## Inline Link Format

Each verse in `Readable Bible/` ends with inline abbreviated links:

```
[[Ref|V]] Verse text.  | [[...|IP]] | [[...|C]] | [[...|TOSK]] | [[...|TT]] |
```

**Format Rules**:
- Two spaces before first `|`
- Leading and trailing `|` around all links
- Multiple links of same type use superscripts: `IP¹`, `IP²`, `TT¹`, `TT²`
- Links separated by ` | `
- No links = verse ends with just text (no pipes)

**Example** (Genesis 1:1):
```
...earth.  | [[...|IP¹]] | [[...|IP²]] | [[...|TOSK]] | [[...|TT¹]] | [[...|TT²]] |
```

---

## File Naming Conventions

### Intertextuality Pairs
- **Format**: `[Source Book] [Ch].[V] to [Target Book] [Ch].[V].md`
- **Example**: `Genesis 3.15 to Revelation 12.9.md`

### Trajectory Tables
- **Location**: `Trajectory Tables/[Topic Name].md`
- **Example**: `Trajectory Tables/Seed Promise (Redemption Through Offspring).md`

### Foundation Texts
- **Location**: `Trajectory Tables - Foundation Texts/[Topic Name]/[##] - [Book] [Ch].[V][-V].md`
- **Example**: `Trajectory Tables - Foundation Texts/Seed Promise/01 - Genesis 3.15.md`

---

## Quality Control Checklist

Before marking any intertextuality pair as complete, verify:

- [ ] Source and target texts correctly linked
- [ ] Confidence level included (A/B/C/D) for OT to OT pairs
- [ ] Type notation included (~, //, /~/, +, >/<)
- [ ] Subject line present (one line)
- [ ] Explanation is 50-100 words
- [ ] Christological connection included (NT to OT pairs only)
- [ ] Related trajectory tables linked (if applicable)
- [ ] File naming follows convention

---

## Sources for Content

### Primary Sources
1. **Schnittjer** - OT use of OT methodology and pairs
2. **Carson & Beale** - NT use of OT commentary
3. **Treasury of Scripture Knowledge** - Cross-reference database

### Secondary Sources
1. **G.K. Beale** - Biblical theology and hermeneutics
2. **Fairbairn** - Typology principles
3. **Geerhardus Vos** - Redemptive-historical theology

---

## Related Documents

- [[- Vision]] - Project vision and roadmap
- [[- Hermeneutics]] - Biblical interpretation methodology
- [[- Formatting]] - Complete formatting standards
- [[- How to Study the Bible's Use of the Bible]] - Schnittjer & Harmon methodology
- [[- Fairbairn]] - Typological principles

---

**This standard format defines the structure for all intertextuality analysis in the vault.**
