# Vault Formatting Standards

**Quick Reference Guide for Consistent Formatting**

This document defines the exact formatting standards for all content in the vault. When asked to "ensure formatting is consistent," apply these standards.

**Last Updated**: 2025-12-13

---

## Current Vault Architecture

The vault uses **inline links** at the end of each verse in the Readable Bible:

```
Readable Bible verse → | [[...|IP]] | [[...|C]] | [[...|TOSK]] | [[...|TT]] |
```

**Link Types**:
| Abbrev | Meaning | Target Folder |
|--------|---------|---------------|
| **IP** | Intertextual Pair | `Intertextuality Pairs/OT to OT/` or `Intertextuality Pairs/NT to OT/` |
| **C** | Chiasm | `Chiasm/` |
| **TOSK** | Treasury of Scripture Knowledge | `The Treasury of Scripture Knowledge/` |
| **TT** | Trajectory Table | `Trajectory Tables/` |

---

## 1. Readable Bible (~1,189 files)

**Location**: `Readable Bible/[##] - [Book]/[Book] [Ch].md`

**Status**: Primary reading interface with inline cross-reference links

### Template:
```markdown
---
Chapter: "1"
Book: Genesis
Folder: Readable Bible
cssClasses: lexicon
---

# Genesis-R 1

**[[Home/Indexes/Readable Bible/01 - Genesis|Genesis]]**

[[Readable Bible/01 - Genesis/Genesis 2#Genesis-R 2| Genesis 2]]

---
##### Genesis 1 . 1
[[Reference Bible/1 - Genesis/Genesis 1#Genesis 1 - 1|1]] In the beginning God created the heavens and the earth.  | [[Intertextuality Pairs/OT to OT/01 - Genesis/Genesis 1.1 to Psalm 104.1|IP]] | [[Chiasm/Chiasm - 01 - Genesis 1 . 1 - 31|C]] | [[The Treasury of Scripture Knowledge/01. Genesis TOSK/Genesis - 1 - TOSK#Verse 1|TOSK]] | [[Trajectory Tables/Creation (New Heavens and Earth)|TT]] |

##### Genesis 1 . 2
[[Reference Bible/1 - Genesis/Genesis 1#Genesis 1 - 2|2]] Now the earth was formless and void...  | [[The Treasury of Scripture Knowledge/01. Genesis TOSK/Genesis - 1 - TOSK#Verse 2|TOSK]] |
```

### Inline Link Format Rules:
1. Two spaces before first `|`
2. Leading and trailing `|` around all links
3. Multiple links of same type use superscripts: `IP¹`, `IP²`, `TT¹`, `TT²`
4. Links separated by ` | `
5. No links = verse ends with just text (no pipes)

**Example** (multiple links):
```
...earth.  | [[...|IP¹]] | [[...|IP²]] | [[...|TOSK]] | [[...|TT¹]] | [[...|TT²]] |
```

---

## 2. Chiasms (~1,732 files)

**Location**: `Chiasm/Chiasm - [##] - [Book] [Ch] . [V] - [V].md`

**Status**: STANDARDIZED (100% complete)

**Format**: Markdown bullets with 4-space indentation

### Template:
```markdown
- A. [[Readable Bible/01 - Genesis/Genesis 2#Genesis 2 . 15|15]] The man is placed in the <span style="color: #c0392b; font-weight: bold;">garden of Eden</span>

    - B. [[Readable Bible/01 - Genesis/Genesis 2#Genesis 2 . 16|16-17]] God <span style="color: #1f618d; font-weight: bold;">commands the man</span>: You may surely eat of every tree of the garden

        - C. [[Readable Bible/01 - Genesis/Genesis 2#Genesis 2 . 18|18-25]] The <span style="color: #16a085; font-weight: bold;">creation of woman</span>: The LORD God said, It is not good that the man should be alone

            - D. [[Readable Bible/01 - Genesis/Genesis 3#Genesis 3 . 1|1-5]] The <span style="color: #8e44ad; font-weight: bold;">serpent tempts Eve</span>: You will not surely die

                - E. [[Readable Bible/01 - Genesis/Genesis 3#Genesis 3 . 6|6-7]] <span style="color: #d68910; font-weight: bold;">The first sin</span>: She took of its fruit and ate

            - D'. [[Readable Bible/01 - Genesis/Genesis 3#Genesis 3 . 14|14-15]] The <span style="color: #8e44ad; font-weight: bold;">serpent is punished</span>: The LORD God said to the serpent

        - C'. [[Readable Bible/01 - Genesis/Genesis 3#Genesis 3 . 16|16]] The <span style="color: #16a085; font-weight: bold;">woman is punished</span>: To the woman he said

    - B'. [[Readable Bible/01 - Genesis/Genesis 3#Genesis 3 . 17|17-19]] The <span style="color: #1f618d; font-weight: bold;">man is punished</span>: To Adam he said

- A'. [[Readable Bible/01 - Genesis/Genesis 3#Genesis 3 . 24|24]] The man is <span style="color: #c0392b; font-weight: bold;">driven out</span> of the garden

```

### Formatting Rules:
1. **NO markdown header** at top (file starts with `- A.`)
2. **Markdown bullets** (`-`) for each chiasm element
3. **4-space indentation** per nesting level (A=0, B=4, C=8, D=12, etc.)
4. **ONE blank line** after each chiasm element
5. **ONE blank line** at end of file
6. **Color formatting preserved** with matching colors for parallel pairs
7. **Wikilinks required** at start of each line
8. **No HTML tags** (no `<div>`, no `&nbsp;` entities)

### Color Palette:
- **A/A' (outer)**: `#c0392b` (red)
- **B/B' (second)**: `#1f618d` (blue)
- **C/C' (third)**: `#16a085` (teal)
- **D/D' (fourth)**: `#8e44ad` (purple)
- **E/E' (center)**: `#d68910` (gold)

---

## 3. Intertextuality Pairs

Cross-references are now stored in dedicated pair files with detailed analysis.

### OT to OT Pairs

**Location**: `Intertextuality Pairs/OT to OT/[##] - [Book]/[Source] to [Target].md`

**Example**: `Intertextuality Pairs/OT to OT/01 - Genesis/Genesis 1.1 to Psalm 104.1.md`

```markdown
# Genesis 1:1 to Psalm 104:1

**Source Text**: [[Readable Bible/01 - Genesis/Genesis 1#Genesis 1 . 1|Genesis 1:1]]

**Target Text**: [[Readable Bible/19 - Psalms/Psalm 104#Psalm 104 . 1|Psalm 104:1]]

**Confidence**: B - Probable

**Type**: ~ Allusion

**Subject**: Creation hymn echoing Genesis narrative

**Explanation**: [50-100 words explaining the hermeneutical connection]

---

**Related**:
- [[Trajectory Tables/[Trajectory Name]|Trajectory Table]]
```

### NT to OT Pairs

**Location**: `Intertextuality Pairs/NT to OT/[##] - [Book]/[NT Verse] to [OT Verse].md`

**Example**: `Intertextuality Pairs/NT to OT/43 - John/John 1.1 to Genesis 1.1.md`

```markdown
# John 1:1 to Genesis 1:1

**NT Text**: [[Readable Bible/43 - John/John 1#John 1 . 1|John 1:1]]

**OT Source**: [[Readable Bible/01 - Genesis/Genesis 1#Genesis 1 . 1|Genesis 1:1]]

**Type**: Allusion

**Subject**: [One-line description]

**Explanation**: [50-100 words explaining how the NT author uses the OT text]

**Christological Connection**: [One sentence showing how this points to Christ]

---

**Related**:
- [[Trajectory Tables/[Trajectory Name]|Trajectory Table]]
```

### Confidence Levels (OT to OT):
- **A - Certain**: Verbal parallels, explicit quotations
- **B - Probable**: Strong thematic/verbal connections
- **C - Possible**: Plausible but uncertain
- **D - Unlikely**: Doubtful connection

### Relationship Types:
- **~** - Allusion/interpretive use
- **//** - Direct verbal parallel or quotation
- **/~/** - Synoptic parallel
- **+** - Interpretive blend (combining sources)
- **>/<** - More or less similar

---

## 4. Trajectory Tables (~126 files)

**Location**: `Trajectory Tables/[Topic Name].md`

**Status**: STANDARDIZED

### Template:
```markdown
## [TOPIC NAME] TRAJECTORY TABLE


**Related Books:** [[Home/Indexes/Readable Bible/02 - Exodus|Exodus]] · [[Home/Indexes/Readable Bible/03 - Leviticus|Leviticus]]

[Introduction paragraph explaining the typology and its fulfillment]

| # | Stage | Key Text(s) | Theological Development | Text Analysis |
|---|-------|-------------|------------------------|---------------|
| 1 | **OT Type - [Label]** | [[Readable Bible/02 - Exodus/Exodus 28#Exodus 28 . 1\|Exodus 28:1-5]] | Explanation. **CRITICAL:** [[Pair link]] | [[Trajectory Tables - Foundation Texts/[Topic]/02 - Exodus 28.1-5\|Exodus 28:1-5]] |
| 2 | **OT Development** | [[...]] | [...] | [[...]] |
...

---

## Canonical Intertextuality Pairs

### OT to OT


**02 - Exodus**
- [[Intertextuality Pairs/OT to OT/02 - Exodus/...|Display]] - **CRITICAL:** Annotation paragraph

---

### NT to OT


**58 - Hebrews**
- [[Intertextuality Pairs/NT to OT/58 - Hebrews/...|Display]] - Annotation paragraph

---

## Foundation Texts

[[Trajectory Tables - Foundation Texts/[Topic]/02 - Exodus 28.1-5|Exodus 28:1-5]]
[[Trajectory Tables - Foundation Texts/[Topic]/03 - Leviticus 16.1-34|Leviticus 16:1-34]]
```

### Formatting Rules:
1. Title format: `## [TOPIC NAME] TRAJECTORY TABLE`
2. Two blank lines after title
3. **Related Books** line with navigation links
4. Introduction paragraph with type classification (Direct/Providential, Forward/Backward-Looking)
5. Table has 5 columns: `#`, `Stage`, `Key Text(s)`, `Theological Development`, `Text Analysis`
6. **All links use `\|`** (backslash-pipe) inside table cells
7. **Anchors use periods**: `#[Book] [Ch] . [V]`
8. Stage names are **bold**
9. `## Canonical Intertextuality Pairs` section with OT to OT and NT to OT subsections
10. `## Foundation Texts` section at bottom

### Stage Progression (typical):
1. OT Type/Institution - Original establishment
2. OT Development/Crisis - (if applicable)
3. Prophetic Anticipation
4. NT Fulfillment - Christ's accomplishment
5. NT Superiority - Christ transcends type
6. NT Application - Believers' participation
7. Eschatological Consummation - Final fulfillment (Revelation)

---

## 5. Foundation Texts (~320+ files)

**Location**: `Trajectory Tables - Foundation Texts/[Topic Name]/[##] - [Book] [Ch].[V][-V].md`

**Status**: STANDARDIZED

### Template:
```markdown
### [[Readable Bible/[##] - [Book]/[Book] [Ch]#[Book] [Ch] . [V]|[Book] [Ch]:[V]]]

**Hebrew/Greek Key Terms**:
- [[Lexicon/H####|H####]] term (*transliteration*) - "English meaning"
- [[Lexicon/G####|G####]] term (*transliteration*) - "English meaning"

**Context**: [1-2 paragraphs explaining the passage's context]

**OT-to-OT Development**:
- How did later OT authors interpret this text?
- What canonical trajectory exists within the OT?

**Connections**:
- **TO**: [Earlier passages this builds upon]
- **FROM OT**: [Later OT passages that reference this text]
- **FROM NT**: [NT passages that fulfill/apply this text]

**Ninefold Analysis**:
- **OT Context**: [Historical/literary setting]
- **OT-to-OT Development**: [How later OT texts interpret this]
- **Jewish Backgrounds**: [Second Temple interpretation - secondary]
- **Text Form**: [Hebrew MT vs. LXX; literary features]
- **Hermeneutical Use**: [How NT interprets this text]
- **Theological Use**: [Christology, soteriology, ecclesiology, eschatology]
- **Rhetorical Use**: [Pastoral/persuasive function]

**Type Classification**: [Forward/Backward-looking] [Direct/Providential]

**Christological Connection**: [How this text points to Christ]

**Trajectory Table**: [[Trajectory Tables/[Topic Name]]]
```

### Formatting Rules:
1. File naming: `[##] - [Book] [Ch].[V][-V].md` (book number prefix)
2. Header links to Readable Bible verse
3. **Hebrew/Greek Key Terms** section with Lexicon links
4. **Context** section (1-2 paragraphs)
5. **OT-to-OT Development** section (trace within OT first)
6. **Connections** section with TO/FROM OT/FROM NT structure
7. **Ninefold Analysis** with subsections
8. **Type Classification** line
9. **Christological Connection** as final analysis section
10. Back-link to trajectory table at bottom

---

## 6. The Treasury of Scripture Knowledge (~1,189 files)

**Location**: `The Treasury of Scripture Knowledge/[##]. [Book] TOSK/[Book] - [Ch] - TOSK.md`

**Status**: Imported, linked via inline TOSK links

### Format:
```markdown
---
Folder: TOSK
Name: Genesis 1 TOSK
---

#### Verse 1

beginning .  [[Readable Bible/20 - Proverbs/Proverbs 8#Proverbs 8 . 22|Proverbs 8 . 22-24]] , [[...]]

God .  [[Readable Bible/02 - Exodus/Exodus 20#Exodus 20 . 11|Exodus 20 . 11]] , [[...]]

#### Verse 2

without .  [[Readable Bible/18 - Job/Job 26#Job 26 . 7|Job 26 . 7]] , [[...]]
```

---

## 7. Supporting Resources

### Lexicon
**Location**: `Lexicon/H####.md` (Hebrew) or `Lexicon/G####.md` (Greek)

### LXX Reference
**Location**: `LXX Reference/[#] - [Book]/[Book] [Ch].md`

### Reference Bible (Interlinear)
**Location**: `Reference Bible/[#] - [Book]/[Book] [Ch].md`

---

## Universal Formatting Standards

### Anchors
- **ALWAYS use periods**: `#Genesis 1 . 1` (NOT `#Genesis 1-1`)
- Spaces around period: `Ch . V`

### Table Links
- **Use backslash-pipe**: `[[path\|display]]` inside table cells
- Regular pipe works outside tables: `[[path|display]]`

### Inline Links (Readable Bible)
- **Spacing**: `text  | [[link]] |` (2 spaces before first pipe)
- **Multiple same-type**: Use superscripts `IP¹`, `IP²`, `TT¹`, `TT²`

### YAML Frontmatter
- Chapter numbers as strings: `Chapter: "1"` (quoted)
- Arrays use hyphen format:
  ```yaml
  cssClasses:
    - lexicon
  ```

---

## Deprecated Folders

The following folders are **deprecated** and should not be used:

| Old Location | Replaced By |
|--------------|-------------|
| `Reference Pages/` | Inline links in Readable Bible |
| `OT to OT References/` | `Intertextuality Pairs/OT to OT/` |
| `NT to OT References/` | `Intertextuality Pairs/NT to OT/` |
| `TOSK Trajectory Tables/` | `Trajectory Tables/` |
| `Trajectory Tables/` (old) | `Trajectory Tables/` |

---

## Automation Scripts

**Location**: `Admin/Scripts to Keep/`

**Key Scripts**:
- `standardize_vault.py` - Master formatting script
- `create_tosk_trajectory.py` - Trajectory table generator
- `migrate_to_inline_links.py` - Migrate to inline verse links

---

## Status Summary

**Active Folders**:
- Readable Bible: ~1,189 files (with inline links)
- Chiasms: ~1,732 files
- Intertextuality Pairs: ~3,000+ files (OT to OT + NT to OT)
- Trajectory Tables: ~126 files
- Trajectory Tables - Foundation Texts: ~320+ files
- The Treasury of Scripture Knowledge: ~1,189 files
- Lexicon: Hebrew (H#) and Greek (G#) entries
- Reference Bible: ~1,189 files (interlinear)
- LXX Reference: ~1,189 files

---

**Maintained By**: Claude Code Automation
