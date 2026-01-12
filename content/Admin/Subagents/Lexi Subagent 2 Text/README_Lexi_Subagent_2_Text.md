# Lexi Subagent 2 Text

**Created:** 2026-01-02
**Purpose:** Trace Hebrew/Greek lexical connections between two Scripture texts

---

## Overview

Lexi 2 Text (λέξις, "word/speech") is a focused lexical analysis subagent that:

1. Takes two Scripture references as input
2. Reads both passages from Readable Bible/
3. Identifies Hebrew/Greek terms creating verbal unity
4. Traces LXX translation patterns (OT → LXX → NT)
5. Classifies the type of connection (verbal/conceptual/both)
6. Produces a **200-word summary** of lexical findings

---

## Difference from Lexi - Trajectory Table

| Lexi - Trajectory Table | Lexi 2 Text |
|------------------------|-------------|
| Input: Trajectory table file | Input: Two Scripture references |
| Analyzes multiple verses across stages | Analyzes exactly two passages |
| Appends to existing trajectory file | Outputs standalone analysis |
| Traces theme across redemptive history | Traces connection between two texts |

---

## Method (Based on Thema Steps 1, 2, 4)

### Step 1: Identify the Two Texts
- Read both passages
- Determine relationship type (OT→OT, NT→OT, etc.)
- Identify source and target texts
- Note thematic connection

### Step 2: Extract Lexical Elements
- Hebrew/Greek terminology from both texts
- Root words and grammatical forms
- Strong's numbers from Lexicon/
- Connection type classification

### Step 3: Trace LXX Mediation
- How LXX translates Hebrew terms
- NT dependence on LXX vocabulary
- Textual variants if significant

---

## Connection Types

Lexi 2 Text classifies connections as:

- **Exact verbal match** - Same Hebrew/Greek word
- **Same root, different form** - Cognate forms
- **LXX-mediated** - Hebrew → LXX Greek → NT Greek
- **Conceptual parallel** - Different words, same idea
- **Multiple connections** - Both verbal and conceptual

---

## Output Format

Lexi 2 Text produces:

```markdown
## Lexical Analysis: [Text A] → [Text B]

### Summary
[200-word summary of lexical connections]

### Lexical Data

**Text A: [Reference]**
- **Term**: [Hebrew/Greek] (*transliteration*) = "[translation]"
- **Strong's**: [[Lexicon/H####|H####]]

**Text B: [Reference]**
- **Term**: [Hebrew/Greek] (*transliteration*) = "[translation]"
- **Strong's**: [[Lexicon/G####|G####]]

**Connection Type**: [Classification]

**LXX Bridge** (if applicable):
- Hebrew → LXX: [term] → [term]
- NT matches LXX: [Yes/No/Partially]

### Lexicon References
- [[Lexicon/H####|H####]] - [Hebrew term]
- [[Lexicon/G####|G####]] - [Greek term]
```

---

## How to Invoke

```
Use the Task tool with:
- subagent_type: "general-purpose"
- description: "Lexi 2 Text lexicon analysis"
- model: "sonnet"
- prompt: [Full prompt from Lexi_Subagent_2_Text_Prompt.md]

Add request: "Analyze [Text A reference] and [Text B reference]"
```

---

## Input Formats

```
# Two references
"Use Lexi 2 Text on Genesis 3:15 and Romans 16:20"

# Intertextuality pair file
"Use Lexi 2 Text on Intertextuality Pairs/NT to OT/45 - Romans/Romans 16.20 to Genesis 3.15.md"

# Descriptive
"Trace lexical connections between Psalm 22:1 and Matthew 27:46"
```

---

## When to Use Lexi 2 Text

- Analyzing a specific intertextual connection
- Filling in "[Source Text to be added]" placeholders
- Understanding verbal links between two passages
- Preparing lexical data for an intertextuality pair file
- Quick analysis without full trajectory table context

---

## What Lexi 2 Text Does NOT Do

- Does NOT create trajectory tables
- Does NOT analyze more than two texts at once
- Does NOT perform full ninefold exegetical analysis
- Does NOT write extensive theological essays
- Does NOT modify existing vault files

---

## Related Subagents

- **Lexi - Trajectory Table** - Lexical analysis across trajectory table verses
- **Thema** - Comprehensive thematic network builder
- **Founda** - Foundation text creation
- **Hermes** - Interactive Q&A learning

---

## Files

- `Lexi_Subagent_2_Text_Prompt.md` - Complete prompt for invocation
- `README_Lexi_Subagent_2_Text.md` - This file
