# Thema Subagent - Quick Reference

**Version:** 3.0 (REVISED - Matches Actual Format)
**Last Updated:** 2025-11-02
**Status:** 🎯 Ready for Testing

**Name Origin:** "Thema" is Greek (θέμα) meaning "theme" - tracking biblical themes through redemptive history

---

## What This Does

**Thema builds comprehensive Thematic Network documents (400-900+ lines) by mining scholarly sources.**

Thema doesn't ask you questions or require deep interaction. Instead, Thema systematically reads through scholarly analysis in the "OT use of OT" and "NT use of OT" folders, extracts thematic connections identified by Schnittjer and Beale/Carson, and produces **extensive, publication-quality** Thematic Network documents matching the format of existing files in your vault.

**Think of Thema as:**
- A theological researcher mining scholarly sources
- A comprehensive document builder (not a brief summarizer)
- A systematic extractor of thematic trajectories
- A production tool for publication-ready biblical theology

**What Thema Does:**
- ✅ Mines Schnittjer's "OT use of OT" scholarly analysis
- ✅ Mines Beale & Carson's "NT use of OT" commentary
- ✅ Follows network markers: `(* see [theme] network)`
- ✅ Produces **400-900+ line comprehensive documents**
- ✅ Writes **extensive theological introductions** (100-500 lines)
- ✅ Provides **full ninefold exegetical analysis** for foundation texts (100-300 lines)
- ✅ Creates **THEOLOGY TRAJECTORY TABLES**
- ✅ Includes **Hebrew/Greek lexical analysis**
- ✅ Documents all Schnittjer reference pairs
- ✅ Matches format of existing Thematic Networks files

**What Thema Does NOT Do:**
- ❌ Produce brief 50-100 word summaries (that was v2.0 - now corrected)
- ❌ Ask interactive questions (that's Hermes's job)
- ❌ Invent connections not in scholarly sources
- ❌ Skip foundation text deep analysis
- ❌ Provide shallow theological content

**Time:** 15-30 minutes per network (depending on complexity and network size)

---

## Quick Start

**To build a single thematic network:**

```
Use Thema to build the "Judah-King" network
```

**To extract all networks from a biblical book:**

```
Use Thema to extract all thematic networks from the book of Genesis
```

**To build from a starting verse:**

```
Use Thema to build the network starting from Genesis 49:8-10
```

---

## Understanding the Output

### Actual Examples from Your Vault

The Thematic Networks folder already contains excellent examples:

**"Judah-King (Messianic Expectation).md"** - 907 lines
- Full ninefold analysis of Genesis 49:8-12 (250 lines)
- Extensive network overview (200 lines)
- Detailed OT development (300 lines)
- NT fulfillment analysis (150 lines)
- Synthesis, application, conclusion

**"Last Days.md"** - 409 lines
- Simpler format with verse-by-verse structure
- THEOLOGY TRAJECTORY TABLE
- Hebrew/Greek lexical analysis
- Connections (TO/FROM OT/NT)

**"Seed-Offspring (Protevangelium to Christ).md"** - 854 lines
- Extended theological introduction (100+ lines)
- Progressive revelation traced
- Comprehensive network structure

### What Thema Produces

**Document Structure:**
```markdown
# [Network Theme Name]

**Hebrew Term**: [term] (*transliteration*) - "translation"
**Greek Term**: [term] (*transliteration*) - "translation"
**Core Theme**: [description]
**Foundation Text**: [[Readable Bible link]]
**Eschatological Fulfillment**: [[NT link]]

---

## I. NETWORK OVERVIEW (100-500 lines)

### A. The Generative Power of [Foundation Text]
[Extensive theological introduction explaining why this text matters,
how it generates interpretations, what theological questions it raises,
what promises it establishes...]

### B. Hermeneutical Development
[How later texts interpret foundation, interpretive patterns,
progressive revelation traced...]

### C. Theological Stakes
[Why network matters, doctrines established, God's character revealed...]

---

## II. FOUNDATION TEXT: [VERSE] (100-300 lines)

### Ninefold Exegetical Analysis

#### 1. HISTORICAL CONTEXT
[Original setting, historical background, covenant framework...]

#### 2. LITERARY STRUCTURE
[Parallelism, chiastic structure, poetic features...]

#### 3. LEXICAL ANALYSIS
**Key Hebrew/Greek Terms:**
- **[Hebrew]** (*transliteration*) = "[translation]"
  - Etymology, usage, theological significance

#### 4. THEOLOGICAL THEMES
[Major doctrinal themes...]

#### 5. INTERTEXTUAL CONNECTIONS
[How text connects to others...]

#### 6. CANONICAL TRAJECTORY
[How fulfilled/developed later...]

#### 7. EARLY JEWISH INTERPRETATION
[Targums, LXX, Qumran, Rabbinic...]

#### 8. NEW TESTAMENT FULFILLMENT
[How NT uses text...]

#### 9. CHRISTOLOGICAL SYNTHESIS
[How points to Christ and gospel...]

---

## III. OLD TESTAMENT DEVELOPMENT

### [[Readable Bible Link|Book Ch:V]]

**Hebrew**: [term] (*transliteration*)
**LXX**: [Greek] (*transliteration*)

**Context**: [Paragraph on original context and meaning]

**Connections**:
- **TO OT**: [Earlier texts]
- **FROM OT**: [Later OT texts]
- **FROM NT**: [NT fulfillment]

**Ninefold Analysis**:
- **OT Context**: [Brief]
- **Hermeneutical Use**: [How used]
- **Theological Use**: [Doctrinal implications]

**Christological Connection**: [How points to Christ]

---

[Repeat for all verses in network]

---

## IV. [THEME] THEOLOGY TRAJECTORY TABLE

| # | Stage | Key Text(s) | Theological Development |
|---|-------|-------------|------------------------|
| 1 | [Stage] | [Genesis X:X] | [Development] |
| 2 | [Stage] | [Exodus X:X] | [Development] |
...

---

## V. NEW TESTAMENT FULFILLMENT

### [[NT Link|Book Ch:V]] - [Title]

**Context**: [How NT uses OT theme]
**OT Background**: [Which OT texts in mind]
**Hermeneutical Method**: [Typology, fulfillment, etc.]
**Christological Focus**: [How Christ fulfills]

---

## VI. SYNTHESIS: THE [THEME] NETWORK

**Trajectory Arc**: [Genesis to Revelation overview]
**Christological Culmination**: [Christ as fulfillment]
**Canonical Unity**: [Scripture's coherence demonstrated]

---

## VII. PRACTICAL APPLICATION

**Gospel Connection**: [How reveals gospel truth]
**Avoiding Moralism**: [Three-step pattern]
**Pastoral Takeaways**: [Teaching/preaching applications]

---

## VIII. CONCLUSION

[3-5 paragraphs synthesizing everything]

---

## IX. SCHNITTJER REFERENCE PAIRS

1. **[OT Verse] ~ [OT Verse]** (Confidence) - [Description]
2. [Continue listing all pairs...]

**Total Reference Pairs**: [Number]

---

## X. TREASURY OF SCRIPTURE KNOWLEDGE REFERENCES

[Additional cross-references if applicable]
```

**Total Length:** 400-900+ lines depending on network complexity

---

## The Five-Stage Workflow

Thema works systematically through five stages:

### Stage 1: Discover the Network
- Searches "OT use of OT" for `(* see [theme] network)` markers
- Extracts all verses Schnittjer identifies
- Notes confidence levels (A/B/C/D)
- Records scholarly insights

### Stage 2: Mine NT Fulfillment
- Searches "NT use of OT" for NT interpretation
- Extracts Beale & Carson's analysis
- Identifies Christological focus
- Notes eschatological dimensions

### Stage 3: Create Theology Trajectory Table
- Groups verses into redemptive-historical stages
- Shows progressive development
- Creates clear table format

### Stage 4: Write Comprehensive Document
- **Section I:** Extensive network overview (100-500 lines)
- **Section II:** Full ninefold of foundation text (100-300 lines)
- **Section III:** Detailed OT development (verse-by-verse)
- **Section IV:** Trajectory table
- **Section V:** NT fulfillment analysis
- **Section VI:** Synthesis
- **Section VII:** Gospel-centered application
- **Section VIII:** Conclusion
- **Section IX:** Schnittjer reference pairs
- **Section X:** TOSK references (if applicable)

### Stage 5: Validate and Finalize
- Format validation (headers, links, syntax)
- Content validation (all verses, Hebrew/Greek, ninefold, etc.)
- Scholarly grounding (citations accurate)
- Theological accuracy (Christ-centered, gospel clarity)

**Output:** Complete, publication-ready markdown document

---

## Understanding the Sources

### "OT use of OT" Folder (Schnittjer)

**Structure:**
- One file per OT book (e.g., `01 - Genesis.md`, `23 - Isaiah.md`)
- Scholarly analysis of intertextual connections
- Network markers: `(* see [theme] network)`

**Example Entry:**
```
49:8, 10*~27:29 (B)+37:5–11 (C) (blessing of Judah) (* see Judah-king network)
```

**Notation:**
- `*` = part of interpretive network
- `~` = interpretive allusion
- `//` = synoptic parallel
- `+` = interpretive blend
- `(A)` = certain, `(B)` = probable, `(C)` = possible, `(D)` = probably not

### "NT use of OT" Folder (Beale & Carson)

**Structure:**
- One file per NT book (currently: `66 - Revelation.md`)
- Commentary on NT use of OT
- More may be added as vault develops

**Example:**
```
5:5~Gen 49:9-10 (Lion of Judah; Root of David)
```

---

## When to Use Thema

**Perfect For:**
- Building comprehensive thematic networks (400-900+ lines)
- Extracting all networks from biblical books
- Creating publication-quality theological documents
- Teaching/preaching series on biblical themes
- Systematic biblical theology study
- Adding detailed networks to vault collection

**Not Needed For:**
- Deep interactive study (use Hermes instead)
- Quick reference lookups
- Brief summaries
- Single verse cross-reference checks

**Best Use:** When you want **comprehensive, publication-quality thematic documentation** covering entire biblical trajectory from Genesis to Revelation

---

## Comparison: Thema vs. Hermes

| Aspect | Thema | Hermes |
|--------|-------|--------|
| **Purpose** | Build thematic networks | Guide hermeneutical study |
| **Approach** | Report-writer | Interactive questioner |
| **Input** | Theme name or book | Two specific verses |
| **Output** | 400-900+ line document | Learning dialogue |
| **Depth** | Breadth (many verses) | Depth (few verses, thorough) |
| **Format** | Publication-ready document | Questions and answers |
| **Interaction** | Minimal (just invoke) | Extensive (20-40 min dialogue) |
| **Foundation Text** | Full ninefold (100-300 lines) | You discover through questions |
| **Network Overview** | Extensive (100-500 lines) | Not applicable |
| **Use Case** | Building systematic collection | Deep interpretive learning |
| **Time** | 15-30 min per network | 20-40 min per connection |
| **Skill Level** | Produces ready-to-use output | Teaches you the method |

**Simple Rule:**
- **Need a comprehensive network document?** → Use Thema
- **Need to learn hermeneutical methodology?** → Use Hermes

---

## How to Invoke

### Method 1: Single Network by Name

```
Use Thema to build the "Judah-King" network
```

**Thema will:**
1. Search "OT use of OT" for `(* see Judah-king network)` markers
2. Extract all verses Schnittjer identifies
3. Search "NT use of OT" for fulfillment
4. Build comprehensive 900+ line document

### Method 2: Single Network by Starting Verse

```
Use Thema to build the network starting from Genesis 49:8-10
```

**Thema will:**
1. Find the network marker at Genesis 49:8-10
2. Extract theme name from marker
3. Follow network through Bible
4. Build complete document

### Method 3: Extract All Networks from Book

```
Use Thema to extract all thematic networks from Genesis
```

**Thema will:**
1. Read `OT use of OT/01 - Genesis.md`
2. Find all `(* see [theme] network)` markers
3. Build document for each unique network
4. Report completion with list

### Method 4: Batch Processing Multiple Books

```
Use Thema to extract all networks from the Pentateuch (Genesis-Deuteronomy)
```

**Thema will:**
1. Process books 01-05 sequentially
2. Track unique network names
3. Build one document per network (no duplicates)
4. Report total networks created

---

## Example Workflow

### User Invokes:
```
Use Thema to build the "Judah-King" network
```

### Thema's Process:

**STAGE 1: DISCOVER**
- Searches `OT use of OT/01 - Genesis.md`
- Finds: `49:8, 10*~27:29 (B)+37:5–11 (C) (blessing of Judah) (* see Judah-king network)`
- Foundation text = Genesis 49:8-10
- Searches all 39 OT books for same network marker
- Finds 12+ connections in Numbers, Samuel, Chronicles, Psalms, Prophets

**STAGE 2: MINE NT**
- Searches `NT use of OT/66 - Revelation.md`
- Finds: `5:5~Gen 49:9-10 (Lion of Judah; Root of David)`
- Notes Matthew 1:1-3, Luke 1:32-33, Hebrews 7:14

**STAGE 3: CREATE TABLE**
```markdown
| # | Stage | Key Text(s) | Theological Development |
|---|-------|-------------|------------------------|
| 1 | Patriarchal Promise | Genesis 49:8-10 | Royal blessing; lion; scepter |
| 2 | Prophetic Confirmation | Numbers 24:9 | Balaam echoes lion/scepter |
| 3 | Davidic Kingdom | 2 Samuel 7:12-16 | Eternal throne established |
| 4 | Prophetic Anticipation | Isaiah 11:1-10 | Root of Jesse; nations rally |
| 5 | NT Fulfillment | Revelation 5:5 | Lion of Judah conquers |
```

**STAGE 4: WRITE DOCUMENT**

*Section I: Network Overview* - 200 lines
- Jacob's blessing as generative text
- Expectational donor context
- Threefold hermeneutical development
- Theological stakes

*Section II: Foundation Text* - 250 lines
- **Complete ninefold exegesis** of Genesis 49:8-12
- Historical context (20 lines)
- Literary structure (15 lines)
- Lexical analysis (60 lines) - Hebrew terms with transliterations
- Theological themes (25 lines)
- Intertextual connections (30 lines)
- Canonical trajectory (30 lines)
- Early Jewish interpretation (30 lines)
- NT fulfillment (20 lines)
- Christological synthesis (20 lines)

*Section III: OT Development* - 300 lines
- Numbers 24:9 (Balaam) - detailed analysis
- 1 Chronicles 5:1-2, 28:4 (Chronicler)
- Micah 5:8-9 (lion imagery)
- 2 Samuel 7:14-15 (covenant loyalty)
- Ezekiel 21:27 (until he comes)
- Psalms 2, 89 (royal psalms)

*Section IV: Trajectory Table* - (see above)

*Section V: NT Fulfillment* - 150 lines
- Revelation 5:5 (Lion of Judah) - comprehensive analysis
- Matthew 1:1-3 (genealogy from Judah)
- Luke 1:32-33 (David's throne forever)
- Hebrews 7:14 (descended from Judah)

*Section VI: Synthesis* - 50 lines
- Trajectory arc from Jacob to Revelation
- Christological culmination
- Canonical unity demonstrated

*Section VII: Application* - 50 lines
- Gospel-centered application
- Avoiding moralism (three-step pattern)
- Pastoral takeaways

*Section VIII: Conclusion* - 30 lines
- The Eternal King from Judah

*Section IX: Schnittjer Pairs* - 40 lines
- Lists all 8 reference pairs identified by Schnittjer

**STAGE 5: VALIDATE**
✅ 907 lines total
✅ All sections present
✅ Hebrew/Greek terms included
✅ Full ninefold for foundation text
✅ Trajectory table present
✅ All NT fulfillment documented
✅ Gospel-centered application
✅ Schnittjer pairs listed

**SAVE:** `Thematic Networks/Judah-King (Messianic Expectation).md`

**REPORT TO USER:**
```
✅ NETWORK COMPLETE: Judah-King Network

**Statistics:**
- Total lines: 907
- OT verses analyzed: 12
- NT fulfillment verses: 4
- Schnittjer reference pairs: 8
- Foundation text: Genesis 49:8-12 (full ninefold - 250 lines)
- Network overview: 200 lines

**Saved to:** Thematic Networks/Judah-King (Messianic Expectation).md

**Key Insights:**
- Judah's blessing establishes royal expectation from patriarchal period
- Scepter/lion imagery traces through David to Christ
- "Until Shiloh comes" finds fulfillment in Lion of Judah (Rev 5:5)
- Network demonstrates progressive narrowing of messianic hope from tribe to dynasty to individual
```

---

## Strengths of Thema v3.0

✅ **Comprehensive** - 400-900+ lines per network, not brief summaries
✅ **Scholarly** - Grounded in Schnittjer and Beale/Carson analysis
✅ **Systematic** - Follows five-stage workflow consistently
✅ **Detailed** - Full ninefold for foundation texts (100-300 lines)
✅ **Extensive** - Network overviews provide deep theological introduction (100-500 lines)
✅ **Publication-Quality** - Matches existing Thematic Networks format
✅ **Lexically Rich** - Hebrew/Greek terms with transliterations throughout
✅ **Christocentric** - Always points to Christ as ultimate fulfillment
✅ **Gospel-Centered** - Avoids moralism in application
✅ **Formatted** - Ready for vault integration with proper links

---

## Limitations

**What Thema Can't Do:**
- ❌ Create networks not identified by scholars
- ❌ Teach you hermeneutical methodology interactively (use Hermes)
- ❌ Access sources outside "OT use of OT" and "NT use of OT" folders
- ❌ Invent connections not in Schnittjer or Beale/Carson

**What Thema Requires:**
- ✅ Network markers in scholarly sources
- ✅ Sufficient source material in vault
- ✅ Clear theme name or starting verse
- ✅ Trust in Schnittjer/Beale-Carson scholarship

**Current Vault Limitation:**
- NT use of OT folder currently has limited content (mainly Revelation)
- More NT books may be added to vault over time
- Thema works with available sources

---

## Files You Need

**Essential:**
- **`Thema_Subagent_Prompt.md`** - Complete v3.0 prompt (copy to invoke)
- **`README_Thema_Subagent.md`** - This quick reference
- **`Home/Hermeneutics.md`** - Theological foundation

**Source Folders:**
- **`OT use of OT/`** - Schnittjer's analysis (primary source for OT networks)
- **`NT use of OT/`** - Beale & Carson's commentary (NT fulfillment source)

**Example Networks (Study These):**
- **`Thematic Networks/Judah-King (Messianic Expectation).md`** - 907 lines, comprehensive format
- **`Thematic Networks/Last Days.md`** - 409 lines, verse-by-verse format
- **`Thematic Networks/Seed-Offspring (Protevangelium to Christ).md`** - 854 lines, extended introduction

**Location:** `Subagents/Thema Subagent/`

---

## Quality Assurance

### How to Verify Thema's Output

**Check 1: Length and Depth**
- Is output 400-900+ lines (not 50-100)?
- Is network overview extensive (100-500 lines)?
- Is foundation text ninefold complete (100-300 lines)?

**Check 2: Scholarly Grounding**
- Are all verses from Schnittjer or Beale-Carson?
- Are network markers accurately followed?
- Are confidence levels preserved (A/B/C/D)?
- Are Schnittjer pairs listed at end?

**Check 3: Format Compliance**
- Does output match existing Thematic Network files?
- Are all sections present (I-IX or I-X)?
- Are Readable Bible links properly formatted?
- Is Hebrew/Greek lexical work included?

**Check 4: Theological Soundness**
- Does it trace redemptive-historical trajectory?
- Does it point to Christ throughout?
- Does it avoid moralism in application?
- Is gospel clarity maintained?

---

## Troubleshooting

**"Thema can't find the network"**
- Check if network marker exists in scholarly sources
- Verify spelling of theme name
- Try providing starting verse instead
- Network may not be explicitly marked by Schnittjer

**"Output is too brief (only 100-200 lines)"**
- This indicates v2.0 prompt was used instead of v3.0
- Ensure you're using the **v3.0 prompt** from Thema_Subagent_Prompt.md
- v3.0 produces 400-900+ lines, not brief summaries

**"Missing foundation text ninefold"**
- v3.0 MUST include full ninefold (100-300 lines)
- If missing, prompt wasn't followed correctly
- Regenerate using v3.0 prompt

**"Network overview too brief"**
- Network overview should be 100-500 lines
- Should include subsections: Generative Power, Hermeneutical Development, Theological Stakes
- If only 1-2 paragraphs, v3.0 wasn't followed

**"Missing NT fulfillment"**
- NT use of OT folder currently has limited content
- Thema works with available sources
- More NT books may be added over time

**"No Hebrew/Greek analysis"**
- v3.0 requires lexical analysis throughout
- Foundation text section must have detailed word studies
- Each verse should note Hebrew/LXX terms

---

## Success Metrics

**You'll know Thema v3.0 is working when:**
- ✅ Output is 400-900+ lines (comprehensive, not brief)
- ✅ Network overview is extensive (100-500 lines)
- ✅ Foundation text has full ninefold exegesis (100-300 lines)
- ✅ Hebrew/Greek lexical analysis present throughout
- ✅ All verses grounded in scholarly sources
- ✅ Trajectory table clearly shows theological development
- ✅ NT fulfillment connects to OT trajectory
- ✅ Application is gospel-centered (not moralistic)
- ✅ Document matches format of existing Thematic Network files
- ✅ Publication-quality - ready to use without major edits

---

## The Ultimate Goal

**Thema's mission: Build a comprehensive collection of Thematic Networks covering all major biblical themes identified by Schnittjer.**

By systematically mining scholarly sources, Thema enables the vault to document:
- Redemptive-historical trajectories from Genesis to Revelation
- Christological connections showing how all Scripture points to Christ
- Theological development through canonical progression
- Gospel-centered application for contemporary believers

**The Vision:**
```
Every network marker in Schnittjer's "OT use of OT"
    ↓
Every theme traced comprehensively
    ↓
400-900+ lines of publication-quality analysis
    ↓
Full collection of biblical theology networks
    ↓
All pointing to Christ
```

---

## Version History

**v1.0 (2025-11-02):** Initial design
- Too simple
- 50-100 words per verse
- Brief trajectory tables only

**v2.0 (2025-11-02):** Corrected source folders
- Fixed to use "OT use of OT" and "NT use of OT"
- Still too brief (condensed ninefold)
- Did not match actual Thematic Networks format

**v3.0 (2025-11-02):** **REVISED - Matches Actual Format**
- ✅ Comprehensive documents (400-900+ lines)
- ✅ Extensive network overview (100-500 lines)
- ✅ Full ninefold for foundation texts (100-300 lines)
- ✅ Detailed Hebrew/Greek lexical analysis
- ✅ Matches existing Thematic Networks files
- ✅ Publication-quality theological scholarship

---

**Last Updated:** 2025-11-02
**Purpose:** Build comprehensive Thematic Network documents
**Method:** Mine scholarly sources systematically
**Framework:** Reformed, Christocentric, Gospel-Centered
**Output:** 400-900+ line publication-quality documents

**"Thema" = Theme (θέμα)**
