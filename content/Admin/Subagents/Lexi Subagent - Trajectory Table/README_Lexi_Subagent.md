# Lexi Subagent

**Created:** 2025-12-22
**Purpose:** Trace Hebrew/Greek lexical connections across trajectory table verses

---

## Overview

Lexi (λέξις, "word/speech") is a focused lexical analysis subagent that:

1. Reads a given trajectory table markdown file
2. Extracts all verse references from the table
3. Identifies Hebrew/Greek terms creating thematic unity
4. Traces LXX translation patterns (OT → LXX → NT)
5. Produces a **200-word summary** of lexical findings
6. Appends the summary to the file under `## Lexicon Findings`

---

## Method (Based on Thema Steps 1, 2, 4)

### Step 1: Identify Theme from Trajectory Table
- Extract theme name from title
- List all verses from "Key Text(s)" column
- Note theological progression

### Step 2: Extract Common Lexical Elements
- Hebrew terminology (roots, forms, occurrences)
- LXX Greek renderings
- NT Greek usage
- Key observation on lexical continuity

### Step 4: Trace LXX Translation Patterns
- How LXX translates Hebrew terms
- Significance of translation choices
- Variations between MT, LXX, and NT

---

## Output Format

Lexi appends the following to the trajectory table file:

```markdown

---

## Lexicon Findings

[200-word summary of lexical connections]

**Key Lexical Threads:**
- **Hebrew**: [term] (*transliteration*) - appears in [verses]
- **LXX**: [term] (*transliteration*) - standard translation
- **NT**: [term] (*transliteration*) - NT continuation

**Lexicon References:**
- [[Lexicon/H####|H####]] - [Hebrew term]
- [[Lexicon/G####|G####]] - [Greek term]
```

---

## How to Invoke

```
Use the Task tool with:
- subagent_type: "general-purpose"
- description: "Lexi lexicon analysis"
- model: "sonnet"
- prompt: [Full prompt from Lexi_Subagent_Prompt.md]

Add request: "Analyze [path/to/trajectory-table.md]"
```

---

## When to Use Lexi

- After creating a new trajectory table
- When wanting to understand verbal connections across a trajectory
- To add lexical analysis to existing trajectory tables
- When tracing word-level links between OT types and NT fulfillment

---

## What Lexi Does NOT Do

- Does NOT modify existing trajectory table content
- Does NOT create new trajectory tables
- Does NOT perform full ninefold exegetical analysis
- Does NOT write extensive theological essays
- Does NOT build thematic networks (use Thema for that)

---

## Related Subagents

- **Thema** - Comprehensive thematic network builder (400-900+ lines)
- **Founda** - Foundation text creation
- **Hermes** - Interactive Q&A learning

---

## Files

- `Lexi_Subagent_Prompt.md` - Complete prompt for invocation
- `README_Lexi_Subagent.md` - This file
