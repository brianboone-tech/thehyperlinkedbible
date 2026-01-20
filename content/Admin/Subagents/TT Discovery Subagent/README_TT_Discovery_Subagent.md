# TT Discovery Subagent - README

## Purpose

This subagent systematically analyzes public books in the vault to identify potential new trajectory table candidates. It cross-references all discovered types against the existing 127 trajectory tables to avoid duplicates and outputs a prioritized candidates document.

## Usage

```
Run TT Discovery on "Books - Public/[Book Name]"
```

### Examples

```
Run TT Discovery on "Books - Public/Samuel Mather - Types of the OT"
Run TT Discovery on "Books - Public/Fairbairn - The Typology of Scripture"
Run TT Discovery on "Books - Public/John Owen - Exposition of Hebrews"
```

## Input

- Book folder path within `Books - Public/`

## Output

- Candidates document saved to `Admin/TT Discovery/[Book Short Name] - Candidates.md`
- Completion report with summary statistics

## Workflow Summary

1. **Read** - Parse book index and all chapters
2. **Extract** - Identify typological content (personal, institutional, event, ceremonial, object types)
3. **Compare** - Cross-reference against 127 existing trajectory tables
4. **Score** - Rate candidates as HIGH/MEDIUM/LOW priority
5. **Output** - Generate candidates document
6. **Report** - Provide completion summary

## Priority Scoring

| Priority | Criteria |
|----------|----------|
| **HIGH** | Multiple detailed references, clear type-antitype connection, OT→NT development visible |
| **MEDIUM** | Some references, connection present but less developed |
| **LOW** | Brief mention, would need additional research |

## Integration

After running TT Discovery on all books:
1. Review HIGH priority candidates across all books
2. Use Trajectory Table Subagent to create new tables for approved candidates
3. Update existing tables with enhancement content noted

## Books to Process

| Priority | Book | Files |
|----------|------|-------|
| 1 | Samuel Mather - Types of the OT | 42 |
| 2 | Fairbairn - Typology of Scripture | 33 |
| 3 | The Glory of Christ - John Owen | 15+ |
| 4 | John Owen - Exposition of Hebrews | 276 |
| 5 | Jonathan Edwards - History of Redemption | 5 |
| 6 | Seeing Christ in All of Scripture | 8 |
| 7 | Preaching Christ in a Postmodern World | 13 |
| 8 | Spurgeon Sermon Index | varies |

## Related Subagents

- **Trajectory Table Subagent** - Creates trajectory tables from NT→OT pairs
- **TOSK Foundation Text Subagent** - Creates foundation text stubs
