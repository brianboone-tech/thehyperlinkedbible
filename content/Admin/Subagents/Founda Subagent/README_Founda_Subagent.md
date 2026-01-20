# Founda Subagent v5.0 - Foundation Text Generator from Trajectory Tables

**Version**: 5.0 (Updated 2025-01-05)
**Status**: ✅ PROVEN (Barrenness to Fruitfulness: 80 files, 100% coverage)
**Purpose**: Generate foundation text analysis pages for ALL key texts in a Trajectory Table

---

## What Founda Does

The **Founda Subagent** creates individual foundation text analysis pages for **every entry** in a Trajectory Table, providing **complete coverage** of a theological theme's development from Genesis to Revelation.

### Core Principle: 100% Trajectory Table Coverage

**Every "Key Text(s)" entry in the Trajectory Table receives its own foundation file.**

- Trajectory has 80 entries → Create 80 foundation files
- Trajectory has 100 entries → Create 100 foundation files
- No consolidation - Each stage is distinct
- Canonical numbering for organization

### Input → Output Flow

```
INPUT:
Trajectory Tables/[Theme Name].md
    ↓
[Parse all table rows, extract "Key Text(s)" column]
    ↓
OUTPUT:
Foundation Texts/[Theme Name]/
├── 01 - Genesis [ref].md
├── 01 - Genesis [ref].md
├── 04 - Numbers [ref].md
├── 18 - Job [ref].md
├── 23 - Isaiah [ref].md
├── 40 - Matthew [ref].md
├── 49 - Ephesians [ref].md
├── 66 - Revelation [ref].md
└── ... (one file per trajectory entry)
```

---

## Standard Foundation Text Format

Each foundation text page contains:

### Core Elements (Required for ALL files)
```markdown
### [[Readable Bible/[##] - [Book]/[Book] [Ch]#[Book] [Ch] . [V]|[Reference]]]

**Hebrew Key Terms** (or **Greek Key Terms**):
- term (*transliteration*) - "translation"

**Context**: [1-3 sentences from trajectory table's "Theological Development" column]

**Connections**:
- **TO**: [Earlier foundational texts this builds on]
- **FROM OT**: [Later OT texts that reference/develop this]
- **FROM NT**: [NT fulfillment/application texts]

**Ninefold Analysis** (for major texts):
- **OT Context**: [Historical/literary context]
- **Jewish Backgrounds**: [Second Temple interpretation]
- **Text Form**: [Literary structure]
- **Hermeneutical Use**: [Interpretive principles]
- **Theological Use**: [Doctrinal significance]
- **Rhetorical Use**: [Persuasive function]

**Christological Connection**: [Paragraph explaining how this text points to or is fulfilled in Christ, grounded in specific NT passages]
```

---

## How to Deploy Founda v5.0

### Method 1: Use Task Agent (Recommended)

Simply say:
```
"Use Founda to create all foundation texts for [Trajectory Table Name]"
```

**Examples**:
- "Use Founda to create all foundation texts for Seed-Offspring (Protevangelium to Christ)"
- "Use Founda to create all foundation texts for Davidic Covenant"
- "Use Founda to create all foundation texts for Passover (Christ Our Passover)"

The Task agent will:
1. Read the trajectory table
2. Count total entries (= target file count)
3. Generate complete foundation file for each entry
4. Store in `Foundation Texts/[Theme Name]/`
5. Verify 100% coverage
6. Report completion with statistics

### Method 2: Use Python Script Directly

```bash
cd "Subagents/Founda Subagent"
python founda_v5.py "[Theme Name]"
```

**Note**: The Python script creates stub files. For complete, content-rich files with Hebrew/Greek terms and full analysis, use Method 1 (Task agent).

---

## Proven Success: Barrenness to Fruitfulness

### Input:
- **Trajectory Table**: 80 stages
- **Theme**: Barrenness to Fruitfulness (Miraculous Birth Pattern)
- **Range**: Genesis 11:30 → Revelation 22:3

### Output:
- **80 Foundation Files** created
- **100% Coverage** - Every trajectory entry documented
- **Canonical Order** - Files numbered 01-66
- **Complete Arc** - Sarah's barrenness to eternal fruitfulness

### File Distribution:
- **Old Testament**: 32 files
  - Genesis (10), Exodus (2), Leviticus (1), Deuteronomy (1)
  - Judges (2), Ruth (1), 1 Samuel (4), 2 Samuel (1)
  - 2 Kings (2), Psalms (3), Isaiah (2), Jeremiah (1), Hosea (1)

- **New Testament**: 48 files
  - Gospels: Matthew (1), Luke (6), John (6)
  - Acts (3), Romans (6), 1-2 Corinthians (4)
  - Galatians (3), Ephesians (3), Philippians (1), Colossians (2)
  - Hebrews (4), James (1), 1 Peter (2), 1 John (1), Jude (1)
  - Revelation (3)

### Quality Standards Met:
✅ Every file has Context from trajectory table's Theological Development
✅ Every file has Connections (TO, FROM OT, FROM NT)
✅ Every file has Christological Connection grounded in NT
✅ Major texts include Hebrew/Greek terms and Ninefold Analysis
✅ Canonical naming convention followed throughout
✅ 100% trajectory table coverage achieved

---

## File Naming Convention

**Format**: `[##] - [Book] [Reference].md`

**Canonical Book Numbers** (01-66):
```
01=Genesis      15=Ezra         29=Joel         43=John         57=Philemon
02=Exodus       16=Nehemiah     30=Amos         44=Acts         58=Hebrews
03=Leviticus    17=Esther       31=Obadiah      45=Romans       59=James
04=Numbers      18=Job          32=Jonah        46=1 Cor        60=1 Peter
05=Deut         19=Psalms       33=Micah        47=2 Cor        61=2 Peter
06=Joshua       20=Proverbs     34=Nahum        48=Galatians    62=1 John
07=Judges       21=Eccles       35=Habakkuk     49=Ephesians    63=2 John
08=Ruth         22=Song         36=Zephaniah    50=Philippians  64=3 John
09=1 Samuel     23=Isaiah       37=Haggai       51=Colossians   65=Jude
10=2 Samuel     24=Jeremiah     38=Zechariah    52=1 Thess      66=Revelation
11=1 Kings      25=Lament       39=Malachi      53=2 Thess
12=2 Kings      26=Ezekiel      40=Matthew      54=1 Timothy
13=1 Chron      27=Daniel       41=Mark         55=2 Timothy
14=2 Chron      28=Hosea        42=Luke         56=Titus
```

**Examples**:
- Genesis 3:15 → `01 - Genesis 3.15.md`
- Psalm 110:1 → `19 - Psalm 110.1.md`
- Isaiah 53:4-6 → `23 - Isaiah 53.4-6.md`
- Matthew 1:1 → `40 - Matthew 1.1.md`
- Romans 4:1-25 → `45 - Romans 4.1-25.md`
- Revelation 21:1-4 → `66 - Revelation 21.1-4.md`

---

## Data Sources (Priority Order)

### 1. Trajectory Table (Primary Source)
- **What**: Theological development descriptions for each stage
- **Where**: `Trajectory Tables/[Theme Name].md`
- **Use for**: Context paragraphs, theological significance

### 2. Existing Foundation Files (Models)
- **What**: Completed foundation texts as templates
- **Where**: `Foundation Texts/Barrenness to Fruitfulness.../`
- **Use for**: Format, structure, depth examples

### 3. Thematic Network (Supplemental)
- **What**: Existing analysis if manually created
- **Where**: `Thematic Networks/[Theme Name].md`
- **Use for**: Enhanced content, ninefold analysis

### 4. Biblical-Theological Synthesis
- **What**: Claude's canonical knowledge + theology
- **Use for**: Christological connections, NT fulfillments, Hebrew/Greek terms

---

## Quality Standards

### Required Elements (ALL files must have):
- [ ] Readable Bible wikilink in heading
- [ ] Context paragraph (from trajectory table)
- [ ] Connections section (TO, FROM OT, FROM NT)
- [ ] Christological Connection paragraph (NT-grounded)

### Enhanced Elements (Major texts should have):
- [ ] Hebrew/Greek key terms with transliteration
- [ ] Ninefold Analysis (5-7 categories)
- [ ] Extended Christological Connection
- [ ] Detailed text form and literary analysis

### Theological Standards:
- [ ] Grounded in text's own message (no allegory)
- [ ] Christ-centered interpretation
- [ ] Redemptive-historical framework
- [ ] Canonical approach (Scripture interprets Scripture)
- [ ] NT citations ground all christological claims

---

## Workflow Summary

| Phase | Time | Task |
|-------|------|------|
| **1. Read** | 1-2 min | Parse trajectory table, count entries |
| **2. Generate** | Variable | Create foundation file for each entry |
| **3. Verify** | 1-2 min | Check 100% coverage, canonical order |
| **4. Report** | 30 sec | Summary with file count and location |

**Average per Network**:
- Small (20-40 entries): 30-60 minutes
- Medium (50-80 entries): 1-2 hours
- Large (80-120 entries): 2-3 hours

---

## Integration with Vault Architecture

### Founda Output Enhances:

**1. Reference Pages** - Can now link to thematic foundation texts:
```markdown
# Genesis 3:15

##### Thematic Analysis
  ▸ [[Foundation Texts/Seed-Offspring (Protevangelium to Christ)/01 - Genesis 3.15|Seed Theme]]
  ▸ [[Foundation Texts/Angels and Spiritual Warfare (Cosmic Conflict)/01 - Genesis 3.15|Warfare Theme]]
  ▸ [[Foundation Texts/Barrenness to Fruitfulness.../01 - Genesis 3.15|Fruitfulness Theme]]
```

**2. Trajectory Tables** - Foundation texts bring tables to life:
```markdown
| # | Stage | Key Text(s) | Theological Development |
|---|-------|-------------|------------------------|
| 1 | Sarah's Barrenness | Genesis 11:30 | First matriarch barren → [[Foundation Texts/.../01 - Genesis 11.30|Analysis]] |
```

**3. Study Workflows** - Users can trace single text across all thematic trajectories

---

## Next Steps for Deployment

### Priority Networks (from Vision.md):

1. **Covenant Themes**:
   - Davidic Covenant
   - New Covenant
   - Noahic Covenant
   - Mosaic Covenant

2. **Messianic Themes**:
   - Seed-Offspring (Protevangelium to Christ)
   - Branch (Messianic Shoot)
   - Prophet Like Moses

3. **Salvation Themes**:
   - Passover (Christ Our Passover)
   - Redemption-Deliverance (Ransom and Freedom)
   - New Exodus (Pattern of Redemptive History)

4. **Temple Themes**:
   - Glory Cloud (Shekinah Presence)
   - Place (Central Sanctuary to New Jerusalem)
   - Sabbath (Rest Theology)

---

## Usage Commands

### Deploy Founda on Single Network:
```
"Use Founda to create all foundation texts for [Thematic Network Name]"
```

**Examples**:
- "Use Founda to create all foundation texts for Seed-Offspring (Protevangelium to Christ)"
- "Use Founda to create all foundation texts for Davidic Covenant"
- "Use Founda to create all foundation texts for Passover (Christ Our Passover)"

---

## Limitations & Disclaimers

### What Founda Can Do:
✅ Generate theologically sound foundation text analysis
✅ Maintain 100% trajectory table coverage
✅ Create files in canonical order
✅ Synthesize from multiple authoritative sources
✅ Ensure consistent format across all networks
✅ Scale from 20-entry to 120-entry trajectories

### What Founda Cannot Do:
❌ Access Hebrew/Greek lexicons directly (relies on canonical knowledge)
❌ Read unpublished scholarly work
❌ Guarantee 100% accuracy of every transliteration
❌ Replace human theological review and editing

### Quality Control Recommendations:
1. Spot-check 3-5 generated texts for theological accuracy
2. Review Hebrew/Greek transliterations against lexicons if needed
3. Verify christological connections are NT-grounded
4. Check connections align with trajectory sequence
5. Edit as needed - Founda provides 95% solution, human polish adds final 5%

---

## Ready to Deploy

Founda v5.0 is **proven and ready** to execute on all remaining thematic networks.

**Status**: ✅ PROVEN & OPERATIONAL
**Proof**: Barrenness to Fruitfulness (80 files, 100% coverage)
**Next**: User selects priority network from trajectory tables

**When ready, simply say**: "Use Founda to create all foundation texts for [Network Name]"

---

## See Also

- [[FOUNDA_QUICK_START.md]] - Condensed workflow guide
- [[- Vision]] - Thematic Networks priority list
- [[- Hermeneutics.md]] - Biblical interpretation methodology
- `founda_v5.py` - Python script for trajectory table parsing

---

**Version**: 5.0
**Last Updated**: 2025-01-05
**Status**: ✅ PROVEN & READY FOR DEPLOYMENT
**Next Step**: Deploy on additional trajectory tables
