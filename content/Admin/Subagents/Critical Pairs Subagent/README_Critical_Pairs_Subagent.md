# Critical Pairs Subagent

## Purpose
Identifies and marks **CRITICAL** intertextuality pairs in Trajectory Tables files. CRITICAL pairs are those foundational to the theological development of the trajectory theme.

## Invocation
```
Run Critical Pairs on "[Trajectory Table Name]"
```

Example:
```
Run Critical Pairs on "Day of Atonement (Christ's Atoning Sacrifice)"
```

## What It Does
1. Reads the Trajectory Table (Combined) file
2. Analyzes each intertextuality pair against 5 CRITICAL criteria
3. Marks CRITICAL pairs with **CRITICAL:** in the appendix section
4. Adds inline **CRITICAL:** references to matching table rows
5. Produces a completion report

## CRITICAL Criteria
A pair is marked CRITICAL if it meets any of these:

| Criterion | Description | Example |
|-----------|-------------|---------|
| **1. Direct NT Quotation** | NT explicitly quotes/cites the OT text | John 19:36 quoting Exodus 12:46 |
| **2. Key Typological Establishment** | Establishes the foundational type-antitype relationship | Exodus 12:46 → Numbers 9:12 (unbroken bones) |
| **3. Escalation Demonstration** | Shows how Christ surpasses the OT shadow | Hebrews 9:28 → Isaiah 53:12 |
| **4. Core Prophetic Development** | Prophetic anticipation with explicit Messianic connection | Isaiah 53:7 lamb imagery |
| **5. Verbal/Thematic Anchor** | Contains primary vocabulary of the trajectory | Same Hebrew/Greek terms |

## Output Format

### In Appendix Section:
```markdown
- [[Pair Link|Display]] - **CRITICAL:** Annotation text...
```

### In Table Rows:
```markdown
| 2 | **Stage** | [[Key Text]] | Explanation. **CRITICAL:** [[Pair\|Display]] | [[Foundation]] |
```

## Batch Processing
To process all trajectory tables without CRITICAL pairs:

```
Run Critical Pairs on all tables without CRITICAL markers
```

The subagent will:
1. List all Trajectory Tables files
2. Identify those without **CRITICAL:** markers
3. Process each one sequentially
4. Produce a summary report

## Files
- `Critical_Pairs_Subagent_Prompt.md` - Full subagent instructions
- `README_Critical_Pairs_Subagent.md` - This file

## Related Subagents
- **TT Analysis Subagent** - Deep analysis with HIGH/MEDIUM/LOW ratings
- **Trajectory Table Subagent** - Creates new trajectory tables
- **Founda Subagent** - Creates foundation text files

## Version History
- **v1.0** (2025-12-11): Initial creation
