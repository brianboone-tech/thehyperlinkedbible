# Trajectory Table Conversion Plan

## Overview

**Goal:** Convert all files from `Trajectory Tables/` format to `Trajectory Tables/` (Standard) format.

**STATUS: ✅ COMPLETE** (2025-01-09)

**Final Results:**
- **Total files converted:** 175 files (001-175)
- **All files now in:** `Trajectory Tables/` (Standard format)
- **Combined folder:** Can be archived

**Files Converted:** All 175 files successfully converted across 10 batches

---

## Conversion Strategy

### Phase 1: Verify Existing Files (001-046)
Check if files 001-046 in `Trajectory Tables/` are already in Standard format or need reconversion.

**Verification Checklist:**
- [ ] Header: `| # | Stage | Key Text(s) / Text Analysis | ... | Intertextuality Pairs |`
- [ ] Column 3 has `**Key Text:**<br>` and `**Text Analysis:**<br>` labels
- [ ] Column 5 has pairs with `**OT to OT:**` / `**NT to OT:**` headers
- [ ] NO `## Canonical Intertextuality Pairs` section

**Action:** Sample check 3-5 files. If already Standard format, skip. If Combined format, reconvert.

### Phase 2: Batch Conversion (047-174)
Convert remaining ~130 files using the TT_Combined_to_Standard_Converter subagent.

---

## Recommended Batch Approach

### Option A: Sequential Batches (Recommended)
Process in batches of 10-15 files per session to allow for quality checks.

**Batch Schedule:**
| Batch | Files | Count |
|-------|-------|-------|
| 1 | 047-060 | 14 |
| 2 | 061-075 | 15 |
| 3 | 076-090 | 15 |
| 4 | 091-105 | 15 |
| 5 | 106-120 | 15 |
| 6 | 121-135 | 15 |
| 7 | 136-150 | 15 |
| 8 | 151-165 | 15 |
| 9 | 166-174+ | ~10 |

**Per-Batch Process:**
1. Convert files using subagent
2. Spot-check 2-3 files for accuracy
3. Report any issues before proceeding

### Option B: Parallel Agent Processing
Launch multiple Task agents in parallel (4-5 at a time), each processing a batch.

**Advantages:** Faster completion
**Disadvantages:** Harder to monitor, potential for errors to compound

---

## File List by Number Range

### Already in Trajectory Tables/ (001-046)
Files exist but may need verification:
```
001 - Aaron (The Great High Priest)
002 - Abel (First Martyr)
003 - Abraham (Father of Faith)
004 - Absalom (The Rebellious Son)
005 - Adam (The First and Last Adam)
006 - Altar of Incense (Christ's Intercession)
007 - Anointing Oil (Holy Spirit)
008 - Ark of Noah (Salvation Through Judgment)
009 - Ark of the Covenant (God's Throne of Mercy)
010 - Ashes of Red Heifer (Continual Cleansing)
011 - Babylonian Exile (Judgment and Discipline)
012 - Barak (Faith in Prophetic Word)
013 - Benjamin (Son of the Right Hand)
014 - Bethel (House of God)
015 - Boaz (Kinsman-Redeemer)
016 - Book of Life (God's Record of the Elect)
017 - Brazen Altar (Place of Sacrifice)
018 - Brazen Laver (Cleansing for Service)
019 - Brazen Pillars - Jachin and Boaz (Stability and Strength)
020 - Breastplate of Judgment (Bearing the Names on the Heart)
021 - Bronze Serpent (Lifted Up for Healing)
022 - Burning Bush (Divine Presence in Fire)
023 - Burnt Offering (Christ's Total Consecration)
024 - Cain (Seed of Serpent)
025 - Camp of Israel (Sacred Geography)
026 - Census Ransom (Royal Accountability)
027 - Ceremonial Uncleanness (Spiritual Defilement)
028 - Cherubim (Glorified Humanity)
029 - Church as Israel (New Covenant People)
030 - Circumcision (Circumcision of the Heart)
031 - Cities of Refuge (Safety in Christ)
032 - Coats of Skins (Covering of Shame)
033 - Conquest of Canaan (Victory in Christ)
034 - Consecration of Priests (Set Apart for Service)
035 - Covenant Meals (Fellowship with God)
036 - Covenant Succession (Inheritance and Election)
037 - Covenant Violations (Prophetic Indictments)
038 - Crossing the Jordan (Entering God's Rest)
039 - Crossing the Red Sea (Baptism into Christ)
040 - Cyrus (Gentile Deliverer)
041 - David (The King After God's Own Heart)
042 - Davidic Kingdom (Messianic Reign)
043 - Davidic Messianic Titles (Faithful Witness, Firstborn, Ruler of Kings)
044 - Day of Atonement (Christ's Atoning Sacrifice)
045 - Day of Midian (Gospel Victory Pattern)
046 - Divine Identity (Deity of Christ) ✅ CONVERTED
```

### Need Conversion (047-174+)
Files in Combined/ but not yet converted:
```
050 - Elijah (Prophet of Fire and Restoration)
051 - Elisha (Double Portion of Spirit)
052 - Enoch (Translation Without Death)
053 - Ephod (High Priest's Garment of Representation)
054 - Esau (The Profane Person)
055 - Eve (Mother of All Living)
060 - First Fruits (Christ's Resurrection)
061 - First-Born Redemption (Consecration to God)
062 - Garden Commission (Extending Sacred Space)
063 - Gentile Inclusion (Light to the Nations)
066 - Golden Calf (Idolatry and Intercession)
069 - Hannah (Barren Mother of Promise)
101 - Meat-Offering (Tribute and Thanksgiving)
103 - Miriam (Prophetess and Worshiper)
104 - Moses (The Prophet Like Unto Me)
112 - Noah (Salvation Through Judgment)
114 - Passover (Christ Our Passover Lamb)
117 - Pentecost (Outpouring of the Spirit)
120 - Pleasing Aroma (Divine Acceptance and Propitiation)
121 - Pool of Bethesda (Ineffective Ritual vs Christ's Power)
123 - Priestly Teaching (Torah Instruction)
124 - Promised Land (Inheritance and Rest)
127 - Rebekah (Bride Sought for the Son)
128 - Red Heifer (Purification from Death)
129 - Rejection Then Exaltation (Pattern of Suffering and Glory)
130 - Remnant (Faithful Few Preserved)
132 - Righteous Branch (Messianic Sprout)
133 - Ruth (Gentile Bride)
134 - Sabbath (Rest in Christ)
135 - Sabbatical Year (Land Rest and Trust)
136 - Sacrificial System (Christ Our Sacrifice)
137 - Samson (Spirit-Empowered Deliverer)
138 - Samuel (Prophet-Priest-Judge)
139 - Sarah (Mother of Promise)
144 - Seth (Appointed Seed)
145 - Shem (Blessed Line of YHWH)
146 - Shepherd (Divine Shepherd Christology)
147 - Sin Offering (Christ Bearing Our Sins)
148 - Solomon (The King of Peace and Wisdom)
149 - Solomon's Temple (Glory of God's Dwelling)
150 - Son of Man (Danielic Figure and Divine Judge)
151 - Spies and Unbelief (Testing God's Promise)
152 - Spirit of Wisdom and Understanding
153 - Spiritual Adultery (Covenant Faithfulness and Idolatry)
154 - Stone and Cornerstone (Rejected Foundation)
155 - Suffering Servant (Vicarious Atonement)
156 - Tabernacle (God Dwelling Among His People)
157 - Table of Showbread (Christ the Bread of Life)
158 - Temple Ecclesiology (Church as God's Dwelling)
159 - Theophanies (Pre-Incarnate Appearances of Christ)
160 - These are the Generations of (Covenant Genealogy)
161 - Tower of Babel (Division Reversed)
162 - Tree of Life (Eternal Life in Christ)
163 - Trespass-Offering (Restitution and Restoration)
164 - Two Covenants (Law and Promise)
165 - Unleavened Bread (Purity and Sincerity)
166 - Urim and Thummim (Divine Guidance and Perfect Light)
167 - Veil (Access Through Christ's Flesh)
168 - Vine and Vineyard (True Israel)
169 - Water from the Rock (The Spiritual Rock)
170 - Water of Purification (Living Water and Ashes)
171 - Wilderness Testing (Faith Through Trial)
172 - Wisdom and Foolishness of the Cross
173 - Wisdom Instruction (Torah Pedagogy)
174 - Year of Jubilee (Ultimate Redemption)
```

---

## Execution Commands

### Single File Conversion
```
Use the Combined-to-Standard converter subagent on "050 - Elijah (Prophet of Fire and Restoration)"
```

### Batch Conversion (Multiple Files)
```
Use the Combined-to-Standard converter subagent on these files in parallel:
1. 050 - Elijah (Prophet of Fire and Restoration)
2. 051 - Elisha (Double Portion of Spirit)
3. 052 - Enoch (Translation Without Death)
4. 053 - Ephod (High Priest's Garment of Representation)
5. 054 - Esau (The Profane Person)
```

---

## Quality Assurance

### Per-File Verification
After each conversion, verify:
- [ ] Table header correct
- [ ] Column 3 has merged Key Text + Text Analysis
- [ ] Column 4 cleaned (no CRITICAL markers)
- [ ] Column 5 has organized pairs
- [ ] Canonical Pairs section removed
- [ ] Four-Step Application preserved
- [ ] Lexicon Findings preserved

### Spot-Check Sample
After each batch, manually open 2-3 files in Obsidian and:
1. Click links to verify they work
2. Check table rendering
3. Confirm no broken formatting

---

## Post-Conversion Cleanup

After all conversions complete:

1. **Verify file counts match:**
   - `Trajectory Tables/` should have same count as `Trajectory Tables/`

2. **Archive or delete Combined folder:**
   - Option A: Rename to `Trajectory Tables - ARCHIVED/`
   - Option B: Delete after full verification

3. **Update CLAUDE.md:**
   - Remove references to Combined format
   - Update commands to reference only `Trajectory Tables/`

---

## Risk Mitigation

1. **Backup before starting:**
   ```bash
   cp -r "Trajectory Tables" "Trajectory Tables - BACKUP"
   ```

2. **Process in small batches:**
   - Allows catching errors early
   - Easier to rollback if needed

3. **Verify before overwriting:**
   - Check if target file exists
   - Compare formats before replacing

---

## Completion Summary

**Conversion completed:** 2025-01-09

### Batch Execution Log

| Batch | Files | Status |
|-------|-------|--------|
| Batch 1-3 | 001-101 | ✅ Complete |
| Batch 4a | 102-109 | ✅ Complete |
| Batch 4b | 110-117 | ✅ Complete |
| Batch 5a | 118-125 | ✅ Complete |
| Batch 5b | 126-133 | ✅ Complete |
| Batch 6a | 134-141 | ✅ Complete |
| Batch 6b | 142-149 | ✅ Complete |
| Batch 7a | 150-157 | ✅ Complete |
| Batch 7b | 158-165 | ✅ Complete |
| Batch 8 | 166-175 | ✅ Complete |

### Conversion Details

Each file converted with the following transformations:
1. **Column merge:** Key Text(s) + Text Analysis → single Column 3 with labeled sections
2. **Pair extraction:** `**CRITICAL:**` pairs moved from Theological Development to Column 5
3. **Pair categorization:** Organized as `**OT to OT:**` or `**NT to OT:**` based on wikilink paths
4. **Section removal:** `## Canonical Intertextuality Pairs` section removed
5. **Preservation:** Four-Step Application and Lexicon Findings sections kept intact

### Next Steps

1. ✅ All 175 files converted
2. [ ] Archive `Trajectory Tables/` folder (optional)
3. [ ] Update CLAUDE.md to remove Combined format references (optional)
4. [ ] Sync to website `content/Trajectory Tables/` folder for rebuild

---

**Created:** 2025-01-08
**Completed:** 2025-01-09
**Status:** ✅ COMPLETE
