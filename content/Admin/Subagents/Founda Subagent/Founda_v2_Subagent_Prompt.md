# FOUNDA v2 SUBAGENT PROMPT

**Purpose**: Create foundation text files for unlinked entries in a Trajectory Table's "Foundation Texts" section
**Input**: Trajectory Table name
**Output**: Foundation text files + updated links in Trajectory Table

---

## WORKFLOW

### STEP 1: READ TRAJECTORY TABLE

Read `Trajectory Tables/[Name].md` and locate the `## Foundation Texts` section.

**Identify unlinked entries** (plain text, not wiki links):
- Plain text: `Hebrews 1:13` ← needs foundation text
- Already linked: `[[...]]` ← skip

**Extract the trajectory summary** from the top of the file for context.

---

### STEP 2: FOR EACH UNLINKED ENTRY

#### 2.1 Parse Reference
```
Entry: "Hebrews 1:13"
→ Book: Hebrews
→ Book Number: 58
→ Chapter: 1
→ Verses: 13
→ Filename: 58 - Hebrews 1.13.md
```

**Book Numbers:**
```
01=Genesis, 02=Exodus, 03=Leviticus, 04=Numbers, 05=Deuteronomy
06=Joshua, 07=Judges, 08=Ruth, 09=1 Samuel, 10=2 Samuel
11=1 Kings, 12=2 Kings, 13=1 Chronicles, 14=2 Chronicles, 15=Ezra
16=Nehemiah, 17=Esther, 18=Job, 19=Psalms, 20=Proverbs
21=Ecclesiastes, 22=Song of Solomon, 23=Isaiah, 24=Jeremiah
25=Lamentations, 26=Ezekiel, 27=Daniel, 28=Hosea, 29=Joel
30=Amos, 31=Obadiah, 32=Jonah, 33=Micah, 34=Nahum, 35=Habakkuk
36=Zephaniah, 37=Haggai, 38=Zechariah, 39=Malachi
40=Matthew, 41=Mark, 42=Luke, 43=John, 44=Acts, 45=Romans
46=1 Corinthians, 47=2 Corinthians, 48=Galatians, 49=Ephesians
50=Philippians, 51=Colossians, 52=1 Thessalonians, 53=2 Thessalonians
54=1 Timothy, 55=2 Timothy, 56=Titus, 57=Philemon, 58=Hebrews
59=James, 60=1 Peter, 61=2 Peter, 62=1 John, 63=2 John
64=3 John, 65=Jude, 66=Revelation
```

#### 2.2 Find Context from Pairs

Search the Trajectory Table's OT to OT and NT to OT sections for pairs that include this verse. Extract the analysis text to understand how this verse connects to the trajectory theme.

#### 2.3 Create Foundation Text File

**Location**: `Trajectory Tables - Foundation Texts/[Trajectory Name]/[##] - [Book] [Ch].[V]-[V].md`

**Template**:
```markdown
### [[Readable Bible/[##] - [Book]/[Book] [Ch]#[Book] [Ch] . [V]|[Book] [Ch]:[V]-[V]]]

**Context**: [2-3 sentences explaining how this passage connects to the trajectory theme. Draw from the pair analysis in the Trajectory Table.]

**Hebrew Key Terms** (for OT) or **Greek Key Terms** (for NT):
- term (*transliteration*) - "translation/meaning"
- [2-4 key terms relevant to the trajectory theme]

**Connections**:
- **TO**: [Earlier passages in this trajectory that this builds on]
- **FROM OT**: [Later OT passages that develop this theme]
- **FROM NT**: [NT passages that fulfill/apply this text]

**Christological Connection**: [1-2 paragraphs explaining how this passage points to Christ or is fulfilled in Him. Must cite specific Scripture. Show the canonical progression.]

**Trajectory Table**: [[Trajectory Tables/[Name]]]
```

#### 2.4 Update Trajectory Table

Replace the plain text entry with a wiki link:
```
Before: Hebrews 1:13
After:  [[Trajectory Tables - Foundation Texts/[Name]/58 - Hebrews 1.13|Hebrews 1:13]]
```

---

### STEP 3: VERIFICATION

After processing all entries:
1. Count files created vs entries processed
2. Verify all plain text entries are now linked
3. Spot-check 2-3 files for quality

---

### STEP 4: COMPLETION REPORT

```markdown
## Founda v2 Completion Report

**Trajectory**: [Name]
**Entries processed**: [N]
**Files created**: [N]
**Files already existed**: [N]

**Created files**:
- [filename1]
- [filename2]
...

**Remaining unlinked** (if any): [list]
```

---

## QUALITY STANDARDS

### Content Requirements
- [ ] Readable Bible wikilink in heading
- [ ] Context drawn from trajectory/pair analysis
- [ ] Hebrew/Greek key terms (2-4 relevant terms)
- [ ] Connections section (TO, FROM OT, FROM NT)
- [ ] Christological connection with Scripture citations
- [ ] Link back to Trajectory Table

### Theological Standards
- [ ] Christ-centered interpretation
- [ ] Grounded in text's actual message
- [ ] Scripture interprets Scripture
- [ ] Redemptive-historical framework

---

## INVOCATION

```
Run Founda v2 on "[Trajectory Table Name]"
```

Example:
```
Run Founda v2 on "Aaron (The Great High Priest)"
```

---

## EXAMPLE OUTPUT

**Input**: Aaron (The Great High Priest), entry "Hebrews 1:13"

**File created**: `58 - Hebrews 1.13.md`

```markdown
### [[Readable Bible/58 - Hebrews/Hebrews 1#Hebrews 1 . 13|Hebrews 1:13]]

**Context**: The author quotes Psalm 110:1 directly as the climax of his argument that Christ is superior to angels. This messianic enthronement establishes Christ's authority and the position from which He exercises His eternal priesthood—seated at God's right hand, not as a subordinate angelic mediator but as the divine Son.

**Greek Key Terms**:
- κάθου (*kathou*) - "sit" (imperative, divine invitation)
- δεξιός (*dexios*) - "right hand" (place of supreme honor)
- ὑποπόδιον (*hypopodion*) - "footstool" (complete subjugation)
- ἐχθρός (*echthros*) - "enemy"

**Connections**:
- **TO**: Psalm 110:1 (source text); Hebrews 1:3 (first session reference)
- **FROM OT**: Psalm 110:4 connects enthronement to eternal priesthood
- **FROM NT**: Hebrews 10:12-13 shows Christ waiting until enemies are subdued

**Christological Connection**: This direct quotation of Psalm 110:1 caps Hebrews' catena of OT texts proving Christ's superiority to angels. The rhetorical question "To which of the angels did God ever say...?" expects the answer "None!" Christ alone receives the invitation to sit at God's right hand—the very position from which He ministers as eternal high priest. Unlike Aaron who stood daily in earthly service, Christ sits enthroned in heavenly majesty, His priestly work complete, waiting for final consummation when all enemies become His footstool (1 Corinthians 15:25-27).

**Trajectory Table**: [[Trajectory Tables/Aaron (The Great High Priest)]]
```

---

**Version**: 2.0
**Created**: 2025-12-09
**Status**: Ready for use
