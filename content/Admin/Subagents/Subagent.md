# Subagents Documentation

**Purpose:** This folder contains specialized subagent prompts for automating complex, multi-step tasks in the vault.

**Last Updated:** 2025-11-02

---

## What Are Subagents?

Subagents are specialized AI agents that run autonomously in isolated sessions to complete specific tasks. Think of them like hiring a contractor - you provide complete instructions, they execute the work independently, and then report back with results.

### Key Characteristics:
- **Isolated Execution:** Runs in its own separate session
- **Autonomous:** Makes its own decisions based on the prompt
- **One-Time Communication:** Receives instructions once, executes fully, reports back
- **Tool Access:** Has access to all tools (Read, Write, Edit, Bash, Grep, etc.)
- **Parallel Capable:** Multiple subagents can run simultaneously

---

## Available Subagents

### 1. Hermes Subagent

**Version:** 2.0 (Interactive Socratic Guide)
**Status:** 🎯 Ready for Testing
**Location:** `Subagents/Hermes Subagent/`

#### What It Does

Hermes is your **Socratic guide for biblical interpretation**. Named after "Hermeneutics" (the art of biblical interpretation), Hermes guides you through the Ninefold Methodology by asking thoughtful questions that help YOU discover insights yourself.

**CRITICAL:** Hermes does NOT write analysis reports. Instead, Hermes asks questions that teach you how to think hermeneutically.

**Capabilities:**
- Guides you through all 9 steps of Ninefold Methodology
- Asks probing questions for each step
- Helps you discover insights yourself
- Validates typological connections interactively
- Ensures gospel-centered application (avoiding moralism)
- Celebrates discoveries and redirects gently when needed
- Develops your interpretive skill through Socratic questioning

**Time:** ~20-40 minutes per text pair (interactive learning session)

#### How to Use

**Quick Command:**
```
Use Hermes to help me analyze [NT REFERENCE] quoting/alluding to [OT REFERENCE]
```

**Examples:**
```
Use Hermes to help me analyze Matthew 2:15 quoting Hosea 11:1
```
```
Use Hermes to guide me through Hebrews 1:5 referencing 2 Samuel 7:14
```

**With Initial Thoughts:**
```
Use Hermes to help me analyze Matthew 2:15 and Hosea 11:1.
I'm confused because Hosea seems to be talking about Israel, not Jesus.
```

**IMPORTANT:** Hermes is interactive - you'll engage in question-and-answer dialogue, not receive a report.

#### The Ninefold Methodology

Hermes systematically works through nine steps:

1. **Identify OT Reference** - Classify as quotation/allusion/echo; validate using Hays's criteria
2. **Analyze NT Context** - Book structure, argument flow, purpose
3. **Analyze OT Context** ⭐ **MOST CRITICAL** - Thorough original context analysis
4. **Survey Jewish Backgrounds** - 8 major sources (LXX, Qumran, Philo, etc.)
5. **Compare Text Forms** - MT vs. LXX vs. variants
6. **Analyze Textual Use** - Why NT author chose this text form
7. **Analyze Hermeneutical Use** 🎯 - Which of 12 uses; typology validation
8. **Analyze Theological Use** - Doctrinal implications; gospel connections
9. **Analyze Rhetorical Use** - Pastoral purpose; contemporary application

#### Theological Framework

**Five Presuppositions** (from Hermeneutics.md):
1. Corporate Solidarity (individuals represent groups)
2. Christ Represents True Israel
3. History Unified by Divine Design (foundation for typology)
4. Eschatological Fulfillment Has Come (already/not yet)
5. Later Parts Interpret Earlier (canonical unity)

**Twelve Uses of OT in NT:**
1. Direct Fulfillment | 2. Typological Fulfillment | 3. Future Fulfillment
4. Analogical Use | 5. Symbolic Use | 6. Abiding Authority
7. Proverbial Use | 8. Rhetorical Use | 9. Blueprint/Prototype
10. Alternate Textual | 11. Assimilated Use | 12. Ironic/Inverted Use

#### Documentation Files

**Essential Files:**
- **`README_Hermes_Subagent.md`** - Quick reference guide
- **`Hermes_Subagent_Prompt.md`** - Complete v1.0 prompt
- **`Home/Hermeneutics.md`** - Theological foundation (referenced by Hermes)

**Location:** `Subagents/Hermes Subagent/`

#### What Gets Created

**NOTHING - Hermes doesn't write reports!**

Instead, Hermes creates:
- **Learning experience** through question-and-answer dialogue
- **Personal discoveries** you make yourself
- **Interpretive skill** developed through practice
- **Deeper understanding** of hermeneutical methodology

**If you want a report instead of interactive learning, use the Thema subagent for thematic analysis.**

#### Typology Validation

When analyzing typological fulfillment, Hermes validates using:

**Five Essential Criteria:**
1. Analogical Correspondence
2. Historicity
3. Escalation
4. Pointing-Forwardness
5. Retrospective Interpretation

**Hamilton's Micro-Level Indicators:**
- Reuse of significant terms
- Quotations of phrases/lines
- Repeated event sequences
- Salvation-historical significance

#### Gospel-Centered Application

Hermes ALWAYS avoids moralism:

**Three-Step Pattern:**
1. Identify virtue/command
2. Expose moralistic trap
3. Apply gospel:
   - What has Christ DONE? (Indicative)
   - What does Christ GIVE? (Provision)
   - How do we RECEIVE? (Faith-response)

**Result:** Transformation from gospel security, not self-effort

#### When to Use Hermes

**Perfect For:**
- **Learning** hermeneutical methodology by practice
- Deep study of specific NT→OT connections
- Teaching/preaching preparation
- Training yourself in sound interpretation
- Understanding WHY and HOW NT uses OT
- Validating typological connections interactively

**Not Needed For:**
- Quick reference lookups (just read commentaries)
- When you just need an answer (not learning the method)
- Building comprehensive thematic networks (use Thema instead)

#### Example Interaction

**User:** "Use Hermes to analyze Matthew 2:15 quoting Hosea 11:1"

**Hermes:** "Hello! I'm Hermes - your hermeneutical guide. Let's work through the Ninefold Methodology together... Ready to begin? Let's start with Step 1: How would you classify this connection - formal quotation, informal quotation, allusion, or echo?"

**User:** "It seems like a formal quotation because Matthew says 'to fulfill what the Lord had spoken.'"

**Hermes:** "Excellent observation! You caught the fulfillment formula. Now, what specific words in Matthew match Hosea 11:1?"

**[Interactive dialogue continues through all 9 steps]**

**Result:** YOU discover that this is typological fulfillment where Jesus recapitulates Israel's experience as true Israel.

---

### 2. Thema Subagent

**Version:** 3.0 (REVISED - Matches Actual Format)
**Status:** 🎯 Ready for Testing
**Location:** `Subagents/Thema Subagent/`

#### What It Does

Thema builds **comprehensive, publication-quality Thematic Network documents (400-900+ lines)** by systematically mining scholarly sources in the vault. Named after the Greek word for "theme" (θέμα), Thema extracts thematic trajectories from "OT use of OT" and "NT use of OT" folders and produces extensive theological documents matching the format of existing Thematic Networks files.

**CRITICAL:** Thema is a **report-writer**, not an interactive guide. It produces extensive, finished documents (400-900+ lines) with minimal user input.

**Capabilities:**
- Mines Schnittjer's "OT use of OT" scholarly analysis
- Mines Beale & Carson's "NT use of OT" commentary
- Follows network markers: `(* see [theme] network)`
- Produces **400-900+ line comprehensive documents**
- Writes **extensive theological introductions** (100-500 lines)
- Provides **full ninefold exegetical analysis** for foundation texts (100-300 lines)
- Creates **THEOLOGY TRAJECTORY TABLES**
- Includes **Hebrew/Greek lexical analysis** throughout
- Documents all Schnittjer reference pairs
- Matches format of existing Thematic Networks files

**Time:** ~15-30 minutes per network (depending on complexity)

#### How to Use

**Single Network by Name:**
```
Use Thema to build the "Judah-King" network
```

**Single Network by Starting Verse:**
```
Use Thema to build the network starting from Genesis 49:8-10
```

**Extract All Networks from Book:**
```
Use Thema to extract all thematic networks from Genesis
```

**Batch Processing:**
```
Use Thema to extract all networks from the Pentateuch (Genesis-Deuteronomy)
```

#### The Five-Stage Workflow

Thema systematically works through five stages:

1. **Mine "OT use of OT"** - Searches for network markers `(* see [theme] network)` in Schnittjer's analysis
2. **Mine "NT use of OT"** - Finds NT fulfillment in Beale & Carson's commentary
3. **Create Trajectory Table** - Groups verses into redemptive-historical stages with THEOLOGY TRAJECTORY TABLE
4. **Write Comprehensive Document** - Extensive theological analysis (400-900+ lines):
   - Section I: Network Overview (100-500 lines)
   - Section II: Foundation Text with **full ninefold** (100-300 lines)
   - Section III: OT Development (detailed verse-by-verse)
   - Sections IV-X: Trajectory table, NT fulfillment, synthesis, application, conclusion, Schnittjer pairs
5. **Validate and Finalize** - Ensure format matches existing Thematic Networks files

#### Scholarly Sources

**"OT use of OT" Folder (Schnittjer):**
- One file per OT book (e.g., `01 - Genesis.md`)
- Scholarly analysis with network markers
- Example notation: `49:8, 10*~27:29 (B)+37:5–11 (C) (* see Judah-king network)`
- Confidence levels: (A) = certain, (B) = probable, (C) = possible, (D) = probably not

**"NT use of OT" Folder (Beale & Carson):**
- Commentary on NT use of OT
- Currently: `66 - Revelation.md`
- More may be added as vault develops

#### What Gets Created

**Comprehensive Thematic Network Document (400-900+ lines):**

```markdown
# [Network Theme Name]

**Hebrew/Greek Terms:** [Lexical introduction]
**Core Theme:** [Description]
**Foundation Text:** [[Link]]
**Eschatological Fulfillment:** [[NT Link]]

---

## I. NETWORK OVERVIEW (100-500 lines)
[Extensive theological introduction covering generative power,
hermeneutical development, theological stakes]

## II. FOUNDATION TEXT: [VERSE] (100-300 lines)
### Ninefold Exegetical Analysis
[Complete 9-step analysis with Hebrew/Greek lexical work]

## III. OLD TESTAMENT DEVELOPMENT
[Detailed verse-by-verse analysis with connections,
context, ninefold insights, Christological connections]

## IV. [THEME] THEOLOGY TRAJECTORY TABLE
| # | Stage | Key Text(s) | Theological Development |
|---|-------|-------------|------------------------|
| ... | ... | ... | ... |

## V. NEW TESTAMENT FULFILLMENT
[NT verses with comprehensive analysis]

## VI-X: SYNTHESIS, APPLICATION, CONCLUSION
[Comprehensive summary, gospel-centered application,
Schnittjer reference pairs, TOSK references]
```

**Total Length:** 400-900+ lines
**Saved to:** `Thematic Networks/[Theme Name] Network.md`

#### Documentation Files

**Essential Files:**
- **`README_Thema_Subagent.md`** - Quick reference guide
- **`Thema_Subagent_Prompt.md`** - Complete v3.0 prompt
- **`Home/Hermeneutics.md`** - Theological foundation

**Example Networks (Study These):**
- **`Thematic Networks/Judah-King (Messianic Expectation).md`** - 907 lines, comprehensive format
- **`Thematic Networks/Last Days.md`** - 409 lines, verse-by-verse format
- **`Thematic Networks/Seed-Offspring (Protevangelium to Christ).md`** - 854 lines, extended introduction

**Location:** `Subagents/Thema Subagent/`

#### Key Features

**Publication-Quality Output (400-900+ lines):**
- Extensive theological introduction (100-500 lines)
- Full ninefold for foundation texts (100-300 lines)
- Detailed verse-by-verse OT development
- Hebrew/Greek lexical analysis throughout
- Multiple comprehensive sections (I-X)

**THEOLOGY TRAJECTORY TABLE:**
Shows clear redemptive-historical progression:
```
| # | Stage | Key Text(s) | Theological Development |
|---|-------|-------------|------------------------|
| 1 | Promise | Genesis 3:15 | Initial promise |
| 2 | Patriarchal | Genesis 49:8-10 | Judah line specified |
| 3 | Davidic | 2 Samuel 7:12-16 | Eternal throne |
| ... | ... | ... | ... |
```

**Full Ninefold Exegetical Analysis** (for foundation texts):
All 9 steps with detailed Hebrew/Greek word studies, not brief summaries

**Scholarly Grounding:**
Everything extracted from Schnittjer and Beale-Carson - not invented

#### When to Use Thema

**Perfect For:**
- Building comprehensive, publication-quality thematic networks (400-900+ lines)
- Extracting all networks from biblical books systematically
- Creating extensive teaching/preaching resources on biblical themes
- Producing systematic biblical theology documents
- Adding detailed networks to vault collection
- When you need extensive theological analysis with full ninefold

**Not Needed For:**
- Deep interactive learning (use Hermes for that)
- Quick reference lookups or brief summaries
- Single verse cross-reference checks
- When you want to learn the methodology yourself (use Hermes)

#### Comparison: Thema vs. Hermes

| Aspect | Thema | Hermes |
|--------|-------|--------|
| **Purpose** | Build thematic networks | Guide interpretation |
| **Approach** | Report-writer | Interactive questioner |
| **Input** | Theme name or book | Two specific verses |
| **Output** | 400-900+ line document | Learning dialogue |
| **Depth** | Breadth (many verses, comprehensive) | Depth (few verses, thorough) |
| **Format** | Publication-ready document | Questions and answers |
| **Interaction** | Minimal (just invoke) | Extensive (20-40 min dialogue) |
| **Foundation Text** | Full ninefold (100-300 lines) | You discover through questions |
| **Network Overview** | Extensive (100-500 lines) | Not applicable |
| **Time** | 15-30 min per network | 20-40 min per connection |

**Simple Rule:**
- **Need a comprehensive network document?** → Use Thema
- **Need to learn hermeneutical methodology?** → Use Hermes

#### Example Workflow

**User:** "Use Thema to build the 'Judah-King' network"

**Thema Process:**
1. **STAGE 1:** Searches `OT use of OT/01 - Genesis.md` for `(* see Judah-king network)`, finds 12+ verses
2. **STAGE 2:** Searches `NT use of OT/66 - Revelation.md` for NT fulfillment (Rev 5:5, etc.)
3. **STAGE 3:** Creates THEOLOGY TRAJECTORY TABLE with 5 stages
4. **STAGE 4:** Writes comprehensive document (907 lines):
   - Network overview: 200 lines
   - Foundation text (Gen 49:8-12) full ninefold: 250 lines
   - OT development: 300 lines
   - NT fulfillment: 150 lines
   - Synthesis, application, conclusion, Schnittjer pairs: 107 lines
5. **STAGE 5:** Validates format, saves to `Thematic Networks/Judah-King (Messianic Expectation).md`

**Result:** Publication-quality 907-line Thematic Network document ready for vault integration

---

<<<<<<< HEAD
### 3. Chiasm Subagent
=======
### 3. Spurgeon Sermon Cleaner Subagent

**Version:** 1.0
**Status:** Ready for Testing
**Location:** `Subagents/Spurgeon Sermon Cleaner Subagent/`

#### What It Does

Automatically processes raw Spurgeon sermons to add:
- **Summary** - Christ-centered, typological summary (4-5 lines)
- **Text Section** - Formatted with Readable Bible text + link + blue color
- **Scripture Quotes** - Blue (#1e90ff) with Readable Bible links
- **Hymns** - Teal (#008080) color

**Designed for:** Processing all 3,500+ Spurgeon sermons across 63 volumes

**Time:** ~2-5 minutes per sermon

#### How to Use

**Single Sermon:**
```
Use the Spurgeon Sermon Cleaner subagent to process:
C:\Obsidian Vaults\thehyperlinkedbible\content\Books - Public\C.H. Spurgeon\Volume 02 - New Park Street Pulpit (1856)\0054 - Christ Our Passover.md
```

**Multiple Sermons:**
```
Use the Spurgeon Sermon Cleaner subagent to process these sermons:
1. [Path to sermon 1]
2. [Path to sermon 2]
```

**Parallel Processing:**
```
Use the Spurgeon Sermon Cleaner subagent to process sermons 0054-0056 in Volume 02 in parallel.
```

#### Color Codes

| Color | Hex Code | Use For |
|-------|----------|---------|
| Blue | `#1e90ff` | Scripture quotations |
| Teal | `#008080` | Hymns and songs |

#### What Gets Created/Modified

The subagent modifies the sermon file in place:
1. **Text section** - Adds exact Readable Bible verse, blue color, link
2. **Summary section** - Inserts after Text section
3. **Body** - Colors scripture quotes blue with links, hymns teal

#### Documentation Files

- **`README_Spurgeon_Sermon_Cleaner_Subagent.md`** - Quick reference
- **`Spurgeon_Sermon_Cleaner_Subagent_Prompt.md`** - Complete prompt

**Location:** `Subagents/Spurgeon Sermon Cleaner Subagent/`

#### Example Output

**Before:**
```markdown
##### Text
*"These are the two covenants."—Galatians 4:24.*
```

**After:**
```markdown
##### Text
*<span style="color: #1e90ff;">"These things serve as illustrations..."</span>—[[Readable Bible/48 - Galatians/Galatians 4#Galatians 4 . 24|Galatians 4:24]].*

---

##### Summary

Spurgeon expounds Paul's allegory in Galatians 4:24...
```

---

### 4. Chiasm Subagent
>>>>>>> parent of 58b5c30e (Quartz sync: Jan 20, 2026, 11:10 AM)

**Version:** 2.3 (Production Ready)
**Status:** ✅ Tested and Working
**Location:** `Subagents/Chiasm Subagent/`

#### What It Does

Automatically converts chiasms from ChiasmusXchange.com to vault format:
- Downloads and parses HTML from ChiasmusXchange.com
- Detects and skips chiasms only available as PDF/Word downloads
- Formats according to vault standards (Formatting.md)
- Creates chiasm file with correct colors and indentation
- Adds links to Reference Pages
- Validates formatting
- Cleans up temporary files

**Time:** ~60-90 seconds per chiasm

#### How to Use

**Quick Command:**
```
Use the Chiasm subagent to convert Psalm [NUMBER] from this URL: [URL]
```

**Example:**
```
Use the Chiasm subagent to convert Psalm 110 from this URL:
https://www.chiasmusxchange.com/2017/02/26/psalm-110/
```

**Batch Conversion (Parallel):**
```
Use the Chiasm subagent to convert these Psalms in parallel:
1. Psalm 108 - [URL]
2. Psalm 109 - [URL]
3. Psalm 110 - [URL]
```

#### Documentation Files

**Essential Files:**
- **`README_Chiasm_Subagent.md`** - Quick reference and overview
- **`Chiasm_Subagent_Prompt.md`** - Complete v2.3 prompt (copy this to invoke)
- **`Finish Chiasms Start Here.md`** - Detailed session startup guide
- **`Subagent Creation Guide.md`** - Tutorial on building custom subagents

**Location:** `Subagents/Chiasm Subagent/`

#### What Gets Created

**Chiasm File:**
- Location: `Chiasm/Chiasm - [##] - [Book] [Ch] . [V] - [V].md`
- Format: Each element on ONE line, correct colors, proper indentation

**Reference Page Links:**
- Added to: `Reference Pages/[##] - [Book]/[Book] [Ch].md`
- Under: `##### Chiasms` section
- Format: `▸ [[Chiasm/Chiasm - [##] - [Book] [Ch] . [V] - [V]|Chiasm - [Book] [Ch]:[V]-[V]]]`

#### Formatting Standards

**Color Mapping by Indentation:**
- **Level 0** (0 spaces): RED `#c0392b`
- **Level 1** (4 spaces): BLUE `#1f618d`
- **Level 2** (8 spaces): TEAL `#16a085`
- **Level 3** (12 spaces): PURPLE `#8e44ad`
- **Level 4** (16 spaces): GOLD `#d68910`

**Key Rules:**
1. NO markdown header (starts with `- A.`)
2. Each chiasm element = ONE line (bullet + link + full text)
3. ONE blank line between elements
4. ONE blank line at end of file
5. Colors by indentation level (not letter label)
6. Parallel pairs match colors (A/A' same, B/B' same, etc.)

#### Successfully Converted Examples

✅ **Psalm 80** (1-19) - 5 levels
✅ **Psalm 109** (1-25) - 5 levels
✅ **Psalm 110** (1-7) - 4 levels (Messianic)
✅ **Psalm 113** (1-9) - 7 levels

#### Troubleshooting

**Wrong colors:**
- Check that colors map by indentation (0 spaces=red, 4=blue, etc.)
- NOT by letter label (A doesn't always = red)

**Multiple lines per element:**
- Each element should be ONE line: `- A. [[Link|1-5]] Full text here.`
- NOT separate lines for each verse

**URL fails:**
- Verify the URL is accessible in browser
- Some ChiasmusXchange pages are discussions, not complete chiasms
- Subagent will skip PDF/Word-only downloads automatically

---

## How to Invoke Subagents

### Method 1: Natural Language (Recommended)

Simply tell Claude to use the subagent:
```
Use the Chiasm subagent to convert [TASK DESCRIPTION]
```

Claude will automatically use the Task tool with the appropriate prompt.

### Method 2: Manual Task Tool Invocation

For precise control:
```
Use the Task tool with these parameters:
- subagent_type: "general-purpose"
- description: "Convert Psalm [NUMBER] chiasm"
- model: "sonnet"
- prompt: [Copy the complete prompt from Chiasm_Subagent_Prompt.md]
```

### Method 3: Parallel Execution

Launch multiple subagents simultaneously:
```
Use the Chiasm subagent to convert these in parallel:
[LIST OF TASKS]

Launch all subagents simultaneously in a single message.
```

---

## Creating New Subagents

Want to create your own subagent? See the tutorial:

**📘 `Subagent Creation Guide.md`**
Location: `Subagents/Chiasm Subagent/Subagent Creation Guide.md`

This comprehensive guide covers:
- How subagents work
- Prompt structure and requirements
- Best practices
- Testing and iteration
- Real-world example (Chiasm Subagent)

---

## Subagent Best Practices

### 1. Make Prompts Self-Contained

The prompt must include:
- Complete instructions (subagent can't ask for clarification)
- All necessary context (file paths, standards, formats)
- Error handling instructions
- Validation steps
- Cleanup procedures

### 2. Use Specific Tools

Explicitly tell the subagent which tools to use:
- Bash for downloads and scripts
- Write for creating new files
- Edit for modifying existing files
- Read for reading files
- Grep for searching

### 3. Include Validation

Always have the subagent:
- Verify its work
- Report specific results
- List any errors or warnings

### 4. Clean Up After Itself

Ensure the subagent:
- Deletes temporary files
- Removes temporary scripts
- Leaves the vault in a clean state

### 5. Test Incrementally

- Start with simple cases
- Verify results manually
- Iterate and improve the prompt
- Document version changes

---

## Subagent Workflow

```
┌─────────────────────────────────────────────────────────────┐
│ 1. USER: Invokes subagent with Task tool                   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. SUBAGENT: Launches in isolated session                  │
│    - Receives complete prompt                               │
│    - Has access to all tools                                │
│    - Runs autonomously                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. EXECUTION: Subagent completes task                      │
│    - Downloads files                                        │
│    - Processes data                                         │
│    - Creates/edits files                                    │
│    - Validates results                                      │
│    - Cleans up                                              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. REPORT: Subagent sends final report                     │
│    - Success/failure status                                 │
│    - Files created/modified                                 │
│    - Any errors encountered                                 │
│    - Validation results                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. USER: Control returns to main session                   │
│    - Reviews subagent report                                │
│    - Verifies results                                       │
│    - Continues with next task                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Future Subagents (Ideas)

Potential subagents to develop:

- **Reference Page Generator:** Automatically create Reference Pages for a book
- **Cross-Reference Validator:** Check all links in a section
- **Thematic Network Builder:** Extract themes and build connections
- **TOSK Link Adder:** Add Treasury of Scripture Knowledge links
- **Scripture Index Generator:** Create comprehensive scripture indices
- **Formatting Standardizer:** Apply formatting standards to sections

---

## Version History

### v1.0 - Chiasm Subagent Initial Release (2025-11-01)
- Basic chiasm conversion functionality
- Bug: Colors mapped by letter label instead of indentation

### v2.0 - Chiasm Subagent Color Fix (2025-11-01)
- Fixed color mapping to use indentation level
- Added explicit color palette instructions

### v2.1 - Chiasm Subagent Line Format Fix (2025-11-01)
- Fixed formatting: each chiasm element on ONE line
- Improved validation

### v2.2 - Chiasm Subagent PDF Detection (2025-11-01)
- Added PDF/Word document detection
- Skips chiasms only available as downloads

### v2.3 - Chiasm Subagent Sub-Element Fix (2025-11-01)
- Fixed handling of sub-elements (a, b, c)
- Only creates lines for capital letter levels

---

## Support

For questions or issues:
1. Review the specific subagent's README file
2. Check the Subagent Creation Guide
3. Refer to vault documentation in `Home/` folder

---

**Last Updated:** 2025-11-02
**Maintained By:** Claude Code Automation
