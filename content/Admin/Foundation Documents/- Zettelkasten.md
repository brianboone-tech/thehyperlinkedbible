# Zettelkasten Proposal for Connection Layer

**Purpose**: Apply Zettelkasten methodology to restructure OT-OT and NT-OT connections as atomic, annotatable files.

---

## Current Architecture

![[Vault Architecture - Current.png]]

---

## Proposed Zettelkasten Architecture

![[Vault Architecture - Proposed Zettelkasten.png]]

---

## Background

**Zettelkasten** ("slip box") is a note-taking system emphasizing:
- **Atomicity**: One idea per note
- **Connection over collection**: Links explain WHY things relate
- **Personal ownership**: Your words, your insights

This vault already has Zettelkasten-like elements (Trajectory Tables trace ideas, Foundation Texts focus on single passages). The proposal applies these principles to the **connection layer**.

---

## The Proposal

### Scope

| Layer | Status | Change |
|-------|--------|--------|
| **Readable Bible** | Unchanged | Foundational verse content |
| **Lexicon / LXX** | Unchanged | Word study resources |
| **OT to OT / NT to OT** | **Restructure** | Each pair → atomic Connection Zettel |
| **Chiasms** | Unchanged | Literary structures (kept whole) |
| **TOSK** | Unchanged | Data source for Connection Zettels |
| **Trajectory Tables** | Enhanced | Built from Connection Zettels |
| **Reference Pages** | **Evaluate** | May be redundant (see Decision 1) |

### What Changes

**Before**: `OT to OT References/19 - Psalms.md` contains ALL Psalm connections as sections

**After**: Each connection becomes its own file:
```
Connection Zettels/
├── OT-OT/
│   ├── OT-OT - Psalms 2.6-7 (receptor) - 2 Samuel 7.14-15 (donor).md
│   └── ...
└── NT-OT/
    ├── NT-OT - Romans 1.17 (receptor) - Habakkuk 2.4 (donor).md
    └── ...
```

### Benefits

1. **Atomicity**: Each connection is discrete and expandable
2. **Personal Annotation**: Add YOUR insights to each connection
3. **Inter-Connection Linking**: Link connections to each other
4. **Thematic Tagging**: Filter by covenant, typology, theme
5. **Graph Visualization**: Connections appear as nodes, revealing clusters
6. **Trajectory Building**: Gather tagged Zettels into Trajectory Tables

---

## Decisions Needed

### Decision 1: Reference Pages

Reference Pages currently aggregate 6 content types per verse. With Connection Zettels linking directly to Readable Bible, **Obsidian backlinks provide automatic aggregation**.

| Option | Description | Maintenance |
|--------|-------------|-------------|
| **A: Keep** | Reference Pages remain as curated Structure Notes | High |
| **B: Eliminate** | Delete Reference Pages; rely on backlinks | Low |
| **C: Transform** | Keep only for non-connection content (books, sermons) | Medium |

**Key question**: Do you value the formatted, organized Reference Page view? Or is backlinks + graph sufficient?

### Decision 2: Naming Convention

**Terminology** (from [[- How to Study the Bible's Use of the Bible|Schnittjer & Harmon]]):
- **Donor Text**: The earlier biblical text being cited/alluded to
- **Receptor Text**: The later text making the citation/allusion

| Option | Example | Notes |
|--------|---------|-------|
| **A** | `Psalms 2.6-7 → 2 Samuel 7.14-15.md` | Clear but filesystem issues |
| **B** | `Psalms 2.6-7 - 2 Samuel 7.14-15.md` | Safe but less distinct |
| **C** ★ | `OT-OT - Psalms 2.6-7 (receptor) - 2 Samuel 7.14-15 (donor).md` | Sortable by type, clear direction |
| **D** | `202506051430 - Psalms 2.6-7 to 2 Samuel 7.14-15.md` | Pure Zettelkasten |

**Recommended**: Option C (type prefix with receptor → donor order)

### Decision 3: Pilot Book

| Option | Why |
|--------|-----|
| **Romans** | Rich NT→OT data from Carson & Beale |
| **Psalms** | Many OT→OT connections |
| **Hebrews** | Dense typological arguments |

---

## TOSK and Chiasms Integration

### TOSK

**Role**: Data source (not restructured)

**Approach**: Hybrid
- TOSK remains as reference material
- Create Connection Zettels only for connections you want to annotate
- Zettel cites TOSK as data source: `**Data Source**: Treasury of Scripture Knowledge`

### Chiasms

**Role**: Literary structures (not atomized)

**Approach**: Keep Separate
- Chiasms are holistic - atomizing loses the pattern
- Connection Zettels link TO chiasm files when relevant
- Example: `See also: [[Chiasm - Habakkuk 2]]`

---

## Connection Zettel Template

**Key Terms** (from [[- How to Study the Bible's Use of the Bible|Schnittjer & Harmon]]):
- **Donor Text**: The earlier biblical text being cited/alluded to
- **Receptor Text**: The later text making the citation/allusion

```markdown
---
type: connection
direction: NT-OT | OT-OT
receptor: [later text making the citation]
donor: [earlier text being cited]
category: quotation | allusion | echo | typology
themes: []
---

## [[Receptor Text]] → [[Donor Text]]

**Connection Type**: [Direct quotation / Allusion / Typological / Echo]

**Subject**: [Brief description]

**Data Source**: [Carson & Beale / TOSK / Personal study]

---

### Significance
[WHY does this connection matter? What does the receptor text do with the donor text?]

### Personal Notes
[Your observations]

### Related
- [[Other Connection Zettel]]
- [[Chiasm - ...]] (if applicable)
- [[TOSK Trajectory Tables/...]]
```

---

## Tagging Taxonomy

**Covenantal**: `covenant-adamic`, `covenant-noahic`, `covenant-abrahamic`, `covenant-mosaic`, `covenant-davidic`, `covenant-new`

**Typological**: `type-person`, `type-event`, `type-institution`, `type-object`

**Thematic**: `kingdom`, `temple`, `land`, `seed`, `blessing-curse`, `exile-restoration`, `creation-new-creation`

---

## Migration Plan

### Phase 1: Pilot
- [ ] Choose test book
- [ ] Create `Connection Zettels/` folder structure
- [ ] Write migration script
- [ ] Generate Connection Zettel files
- [ ] Test graph integration

### Phase 2: Evaluate
- [ ] Review graph visualization
- [ ] Assess workflow for personal notes
- [ ] Refine template if needed

### Phase 3: Full Migration
- [ ] Migrate all connections
- [ ] Update/archive Reference Pages
- [ ] Archive original aggregate files

---

## Next Steps

- [x] Research Zettelkasten methodology
- [x] Define scope (connections layer)
- [x] Create architecture diagrams
- [x] Define TOSK integration (Hybrid)
- [x] Define Chiasms integration (Keep Separate)
- [ ] **Decision 1**: Reference Pages (A, B, or C)
- [ ] **Decision 2**: Naming convention (C recommended)
- [ ] **Decision 3**: Pilot book
- [ ] Create migration script
- [ ] Run pilot and evaluate

---

## Sources

- [Introduction to the Zettelkasten Method](https://zettelkasten.de/introduction/)
- [Zettelkasten - Wikipedia](https://en.wikipedia.org/wiki/Zettelkasten)
- [12 Principles for Zettelkasten - Obsidian Forum](https://forum.obsidian.md/t/12-principles-for-using-zettelkasten/51679)
