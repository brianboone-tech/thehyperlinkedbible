# Trajectory Table Combined-to-Standard Converter Subagent

**Version:** 1.0
**Status:** ✅ Ready for Use
**Created:** 2025-01-08

## What It Does

Converts Trajectory Table files from the **Combined format** (`Trajectory Tables/`) to the **Standard format** (`Trajectory Tables/`).

**Time:** ~60-120 seconds per file

## Format Transformation

### Table Structure Change

| Aspect | Combined Format | Standard Format |
|--------|-----------------|-----------------|
| Column 3 | `Key Text(s)` | `Key Text(s) / Text Analysis` |
| Column 5 | `Text Analysis` | `Intertextuality Pairs` |
| IP Location | Inline in Theological Development | Dedicated column |

### Key Changes

1. **Column 3**: Merges Key Texts + Text Analysis with labels (`**Key Text:**<br>` and `**Text Analysis:**<br>`)
2. **Column 4**: Removes all `**CRITICAL:**` markers and pair links
3. **Column 5**: Extracts pairs into dedicated column with `**OT to OT:**` / `**NT to OT:**` headers
4. **Removes**: `## Canonical Intertextuality Pairs` section
5. **Removes**: `## Foundation Texts` section
6. **Preserves**: `## Four-Step Application` and `## Lexicon Findings`

## How to Use

### Single File
```
Use the Combined-to-Standard converter subagent on "046 - Divine Identity (Deity of Christ)"
```

### Batch Processing
```
Use the Combined-to-Standard converter subagent on these files:
1. 046 - Divine Identity (Deity of Christ)
2. 050 - Elijah (Prophet of Fire and Restoration)
3. 114 - Passover (Christ Our Passover Lamb)
```

## Example Conversion

### Before (Combined Format - Column 3)
```
[[Readable Bible/02 - Exodus/Exodus 3#Exodus 3 . 14\|Exodus 3:14]]
```

### After (Standard Format - Column 3)
```
**Key Text:**<br>[[Readable Bible/02 - Exodus/Exodus 3#Exodus 3 . 14\|Exodus 3:14]]<br><br>**Text Analysis:**<br>[[Trajectory Tables - Foundation Texts/.../02 - Exodus 3.14\|Exodus 3:14]]
```

### Before (Combined Format - Column 4)
```
God reveals His covenant name... **CRITICAL:** [[Intertextuality Pairs/NT to OT/.../John 18.5-6 to Exodus 3.14\|...]]
```

### After (Standard Format - Column 4)
```
God reveals His covenant name...
```

### After (Standard Format - Column 5)
```
**NT to OT:**<br>**CRITICAL:**<br>[[Intertextuality Pairs/NT to OT/.../John 18.5-6 to Exodus 3.14\|John 18:5-6 to Exod 3:14]]
```

## Files

- **Prompt:** `TT_Combined_to_Standard_Converter.md`
- **README:** This file

---

**Last Updated:** 2025-01-08
