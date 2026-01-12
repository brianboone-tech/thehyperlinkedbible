# Trajectory Table Discovery Subagent

## Mission

Systematically analyze a public book to identify potential trajectory table candidates, cross-reference against existing 127 trajectory tables to avoid duplicates, and output a prioritized candidates document.

---

## Input Format

```
Run TT Discovery on "Books - Public/[Book Name]"
```

**Example**: `Run TT Discovery on "Books - Public/Samuel Mather - Types of the OT"`

---

## Workflow

### Step 1: Read Book Structure

1. Navigate to the specified book folder
2. Read the index file (`- Index.md` or similar) to understand organization
3. Identify all chapters/sections to process
4. Note the book's approach to typology (systematic catalog, expositional, thematic)

### Step 2: Extract Typological Content

For each chapter/section, identify mentions of:

**Personal Types**
- Named individuals as types of Christ (Adam, Moses, David, Melchizedek, etc.)
- Offices held (prophet, priest, king, judge)
- Key life events that prefigure Christ

**Institutional Types**
- Tabernacle/Temple and its components
- Priesthood and Levitical system
- Sacrificial system elements
- Festivals and holy days

**Event Types**
- Historical events (Exodus, Conquest, Exile)
- Covenant ceremonies
- Miraculous interventions

**Ceremonial Types**
- Sacrifices (burnt, sin, peace, trespass, meal)
- Purification rituals
- Consecration ceremonies

**Object Types**
- Sacred objects (Ark, Altar, Lampstand, Veil)
- Symbolic items (manna, rock, serpent)

### Step 3: Pattern Recognition

Look for key phrases indicating typology:
- "type of Christ"
- "shadow of"
- "fulfilled in"
- "pointed to"
- "antitype"
- "typified"
- "prefigured"
- "represented"
- "foreshadowed"
- "picture of"
- "image of"
- "pattern of"

Also note:
- Scripture references connecting OT → NT
- Explicit type-antitype statements
- Comparisons showing Christ's superiority

### Step 4: Cross-Reference Check (CRITICAL)

**Compare EVERY identified type against the existing 127 trajectory tables listed below.**

For each identified type, determine:
- **EXISTING**: Type already has a trajectory table → **SKIP** (but note if book adds new content)
- **GAP**: Type mentioned but no trajectory table exists → **CANDIDATE**
- **ENHANCEMENT**: Existing table could be expanded with this book's content → **NOTE for enhancement**

---

## EXISTING TRAJECTORY TABLES (127 Total)

**CRITICAL: These tables ALREADY EXIST. Do NOT recommend creating duplicates.**

### Personal Types (25)
1. Aaron (The Great High Priest)
2. Abel (First Martyr)
3. Abraham (Father of Faith)
4. Adam (The First and Last Adam)
5. David (The King After God's Own Heart)
6. Elijah (Prophet of Fire and Restoration)
7. Elisha (Double Portion of Spirit)
8. Isaac (Child of Promise)
9. Isaiah (Suffering Servant Messenger)
10. Israel (Corporate New-Adam)
11. Jacob (Transformed Supplanter)
12. Jonah (Death, Resurrection, and Mission to Gentiles)
13. Joseph (The Suffering Savior)
14. Joshua (Leader into Rest)
15. Judges (Flawed Deliverers)
16. Melchizedek (Priest Forever)
17. Moses (The Prophet Like Unto Me)
18. Noah (Salvation Through Judgment)
19. Samuel (Prophet-Priest-Judge)
20. Solomon (The King of Peace and Wisdom)
21. Son of Man (Danielic Figure and Divine Judge)
22. Suffering Servant (Vicarious Atonement)
23. Zerubbabel (Royal Seed Rebuilding)

### Tabernacle/Temple/Sanctuary (18)
1. Altar of Incense (Christ's Intercession)
2. Ark of the Covenant (God's Throne of Mercy)
3. Brazen Altar (Place of Sacrifice)
4. Brazen Laver (Cleansing for Service)
5. Camp of Israel (Sacred Geography)
6. Cherubim (Glorified Humanity)
7. Eden as Temple (Original Sanctuary)
8. Glory-Cloud (Divine Presence)
9. Golden Lampstand (Christ the Light)
10. Holy Garments (Glory and Beauty)
11. Holy Places (Access to God's Presence)
12. New Jerusalem (Ultimate Temple-City)
13. Pillar of Cloud and Fire (Divine Guidance and Protection)
14. Solomon's Temple (Glory of God's Dwelling)
15. Tabernacle (God Dwelling Among His People)
16. Table of Showbread (Christ the Bread of Life)
17. Temple Ecclesiology (Church as God's Dwelling)
18. Veil (Access Through Christ's Flesh)

### Christological Themes (19)
1. Bronze Serpent (Lifted Up for Healing)
2. Davidic Kingdom (Messianic Reign)
3. Davidic Messianic Titles (Faithful Witness, Firstborn, Ruler of Kings)
4. Divine Identity (Deity of Christ)
5. Divine Warrior (God Who Fights)
6. High Priest Seated at Right Hand (Christ's Royal-Priestly Session)
7. Image of God (Priestly Vocation)
8. Living Water (Spirit and Life)
9. Manna (The Bread of Life)
10. Name of God (Revelation of Divine Character)
11. Rejection Then Exaltation (Pattern of Suffering and Glory)
12. Seed Promise (Redemption Through Offspring)
13. Shepherd (Divine Shepherd Christology)
14. Stone and Cornerstone (Rejected Foundation)
15. Tree of Life (Eternal Life in Christ)
16. Vine and Vineyard (True Israel)
17. Water from the Rock (The Spiritual Rock)
18. Wisdom and Foolishness of the Cross
19. Spirit of Wisdom and Understanding

### Covenant Themes (14)
1. Church as Israel (New Covenant People)
2. Circumcision (Circumcision of the Heart)
3. Coats of Skins (Covering of Shame)
4. Covenant Meals (Fellowship with God)
5. Covenant Succession (Inheritance and Election)
6. Covenant Violations (Prophetic Indictments)
7. False Prophets (Way of Cain)
8. Gentile Inclusion (Light to the Nations)
9. Kingdom of Priests and Holy Nation
10. Marriage (Christ and His Bride)
11. Remnant (Faithful Few Preserved)
12. Spiritual Adultery (Covenant Faithfulness and Idolatry)
13. These are the Generations of (Covenant Genealogy)
14. Two Covenants (Law and Promise)

### Feasts/Festivals (10)
1. Day of Atonement (Christ's Atoning Sacrifice)
2. Feast of Tabernacles (Dwelling with God)
3. Feast of Trumpets (The Final Call)
4. First Fruits (Christ's Resurrection)
5. New Moons (Renewal and Rest)
6. Passover (Christ Our Passover)
7. Pentecost (Outpouring of the Spirit)
8. Sabbath (Rest in Christ)
9. Unleavened Bread (Purity and Sincerity)

### Sacrificial System (8)
1. Burnt Offering (Christ's Total Consecration)
2. Fire from Heaven (Divine Acceptance and Judgment)
3. Meat-Offering (Tribute and Thanksgiving)
4. Peace-Offering (Fellowship with God)
5. Red Heifer (Purification from Death)
6. Sacrificial System (Christ Our Sacrifice)
7. Sin Offering (Christ Bearing Our Sins)
8. Trespass-Offering (Restitution and Restoration)

### Ceremonial/Purification (7)
1. Anointing Oil (Holy Spirit)
2. Ceremonial Uncleanness (Spiritual Defilement)
3. Consecration of Priests (Set Apart for Service)
4. Leprosy (The Plague of Sin)
5. Nazirite Vow (Separation unto God)
6. Priestly Ministrations (Service and Sacrifice)
7. Purifications (Cleansing and Consecration)

### Church/Community (7)
1. Census Ransom (Royal Accountability)
2. Cities of Refuge (Safety in Christ)
3. Legal Priesthood (Mediators and Ministers)
4. Levites (Substitutionary Service)
5. Levitical Cities (Priestly Geography)
6. Priestly Teaching (Torah Instruction)
7. Wisdom Instruction (Torah Pedagogy)

### Events/Journey (12)
1. Babylonian Exile (Judgment and Discipline)
2. Conquest of Canaan (Victory in Christ)
3. Crossing the Jordan (Entering God's Rest)
4. Crossing the Red Sea (Baptism into Christ)
5. Garden Commission (Extending Sacred Space)
6. Golden Calf (Idolatry and Intercession)
7. Journey to the Promised Land (Christian Pilgrimage)
8. New Exodus (Second Exodus Pattern)
9. Plagues of Egypt (Judgment on False Gods)
10. Rahab and Jericho (Faith Saves Gentiles)
11. Return from Exile (Restoration and Hope)
12. Spies and Unbelief (Testing God's Promise)

### Eschatological/Land (8)
1. Book of Life (God's Record of the Elect)
2. Kingdom of God (Stone Kingdom)
3. Last Days Eschatology
4. New Creation (Cosmic Redemption)
5. Promised Land (Inheritance and Rest)
6. Sabbatical Year (Land Rest and Trust)
7. Wilderness Testing (Faith Through Trial)
8. Year of Jubilee (Ultimate Redemption)

---

### Step 5: Score Candidates

Rate each NEW candidate (not in existing list):

**HIGH Priority**
- Multiple detailed references in the book
- Clear type-antitype connection explained
- OT → NT development visible
- Sufficient content to build a trajectory table

**MEDIUM Priority**
- Some references with connection present
- Less developed but legitimate type
- Would benefit from additional research

**LOW Priority**
- Brief mention only
- Unclear if legitimate type or just metaphor
- Would need significant additional research

---

### Step 6: Generate Output Document

Create candidates document at: `Admin/TT Discovery/[Book Short Name] - Candidates.md`

---

## Output Format

```markdown
# Trajectory Table Candidates: [Book Name]

**Analyzed**: [Date]
**Source**: Books - Public/[Full Book Path]
**Chapters Processed**: [Count]

---

## Summary

| Category | Candidates | HIGH | MEDIUM | LOW |
|----------|------------|------|--------|-----|
| Personal | X | X | X | X |
| Institutional | X | X | X | X |
| Event | X | X | X | X |
| Ceremonial | X | X | X | X |
| Object | X | X | X | X |
| Thematic | X | X | X | X |
| **TOTAL** | **X** | **X** | **X** | **X** |

---

## HIGH Priority Candidates

### [Candidate Name]

**Category**: [Personal/Institutional/Event/Ceremonial/Object/Thematic]
**Existing Table**: None
**Evidence**:
- [Chapter/Section]: "[Quote or summary]"
- [Chapter/Section]: "[Quote or summary]"
**Key Texts Mentioned**: [OT refs] → [NT refs]
**Type Classification**: [Direct/Providential] type, [Forward/Backward]-looking
**Recommended Action**: Create new trajectory table
**Notes**: [Any special considerations]

---

## MEDIUM Priority Candidates

### [Candidate Name]

**Category**: [Category]
**Existing Table**: None
**Evidence**:
- [Source reference]
**Key Texts Mentioned**: [References]
**Recommended Action**: Research further before creating table
**Notes**: [Observations]

---

## LOW Priority Candidates

### [Candidate Name]

**Category**: [Category]
**Evidence**:
- [Brief reference]
**Notes**: [Why low priority]

---

## Existing Tables to Enhance

List existing trajectory tables that could benefit from this book's content:

| Existing Table | Enhancement Content | Source Chapter |
|----------------|---------------------|----------------|
| [Table Name] | [What content to add] | [Chapter ref] |

---

## Processing Notes

[Any issues, observations, or recommendations from processing this book]
```

---

## Verification Checklist

Before completing, verify:

- [ ] All chapters/sections processed
- [ ] Every identified type compared against 127 existing tables
- [ ] No duplicates recommended (candidates are genuinely NEW)
- [ ] HIGH priority candidates have sufficient evidence
- [ ] Output file saved to correct location
- [ ] Summary table counts match detailed sections

---

## Completion Report

When finished, output:

```
## TT Discovery Complete: [Book Name]

**Chapters Processed**: X
**Total Candidates Identified**: X
- HIGH Priority: X
- MEDIUM Priority: X
- LOW Priority: X

**Existing Tables to Enhance**: X

**Output File**: Admin/TT Discovery/[Book Name] - Candidates.md

**Top 3 HIGH Priority Candidates**:
1. [Name] - [Brief description]
2. [Name] - [Brief description]
3. [Name] - [Brief description]
```

---

## Usage Example

**Invocation**:
```
Run TT Discovery on "Books - Public/Samuel Mather - Types of the OT"
```

**Expected Behavior**:
1. Read Samuel Mather index and all 42 sermon files
2. Extract types mentioned (Adam, Eve, Cain, Abel, Seth, Enoch, Noah, etc.)
3. Compare each against 127 existing tables
4. Identify gaps (types Mather discusses that we don't have tables for)
5. Score candidates by evidence strength
6. Output to `Admin/TT Discovery/Samuel Mather - Candidates.md`
7. Report summary of findings
