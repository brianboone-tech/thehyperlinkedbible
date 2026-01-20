# Chiasm Subagent - Quick Reference

**Version:** 2.2 (Production Ready)
**Last Updated:** 2025-11-01
**Status:** ✅ Tested and Working

---

## What This Does

Automatically converts chiasms from ChiasmusXchange.com to your vault format:
- Downloads and parses HTML
- **Detects and skips chiasms only available as PDF/Word downloads**
- Formats per vault standards
- Creates chiasm file with correct colors and indentation
- Adds links to Reference Pages
- Validates everything
- Cleans up temporary files

**Time:** ~60-90 seconds per chiasm

---

## Quick Start

**To convert a chiasm, tell Claude:**
```
Use the Chiasm subagent to convert Psalm [NUMBER] from this URL: [URL]
```

**Example:**
```
Use the Chiasm subagent to convert Psalm 110 from this URL:
https://www.chiasmusxchange.com/2017/02/26/psalm-110/
```

---

## Files You Need

1. **`Chiasm_Subagent_Prompt.md`** - The complete v2.2 subagent prompt
2. **`Finish Chiasms Start Here.md`** - Detailed guide for next session
3. **`Home/Subagent Creation Guide.md`** - Tutorial on building subagents

---

## What Gets Created

**Chiasm File:**
- Location: `Chiasm/Chiasm - 19 - Psalm [Ch] . [V] - [V].md`
- Format: Each element on ONE line, correct colors, proper indentation

**Reference Page Links:**
- Added to: `Reference Pages/19 - Psalms/Psalm [Ch].md`
- Under: `##### Chiasms` section
- Format: `▸ [[Chiasm/Chiasm - 19 - Psalm [Ch] . [V] - [V]|Chiasm - Psalm [Ch]:[V]-[V]]]`

---

## Formatting Standards (v2.2)

### Color Mapping by Indentation
- **Level 0** (0 spaces): RED `#c0392b`
- **Level 1** (4 spaces): BLUE `#1f618d`
- **Level 2** (8 spaces): TEAL `#16a085`
- **Level 3** (12 spaces): PURPLE `#8e44ad`
- **Level 4** (16 spaces): GOLD `#d68910`

### Key Rules
1. NO markdown header (starts with `- A.`)
2. Each chiasm element = ONE line (bullet + link + full text)
3. ONE blank line between elements
4. ONE blank line at end of file
5. Colors by indentation level (not letter label)
6. Parallel pairs match colors (A/A' same, B/B' same, etc.)

---

## Successfully Converted

✅ **Psalm 80** (1-19) - 5 levels
✅ **Psalm 109** (1-25) - 5 levels
✅ **Psalm 110** (1-7) - 4 levels (Messianic)
✅ **Psalm 113** (1-9) - 7 levels

All validated and working perfectly!

---

## Troubleshooting

**If chiasm has wrong colors:**
- Check that colors map by indentation (0 spaces=red, 4=blue, etc.)
- NOT by letter label (A doesn't always = red)

**If chiasm has multiple lines per element:**
- Each element should be ONE line: `- A. [[Link|1-5]] Full text here.`
- NOT separate lines for each verse

**If URL fails:**
- Verify the URL is accessible
- Some pages on ChiasmusXchange are discussions, not complete chiasms

---

## Next Steps

**To finish Psalms chiasms:**
- Psalm 99 (alternate) - Optional
- Psalm 138 (alternate) - Optional

**To expand:**
- Check ChiasmusXchange for other Bible books
- Use subagent for batch conversions

---

**See Also:**
- Full prompt: `Chiasm_Subagent_Prompt.md`
- Next session guide: `Finish Chiasms Start Here.md`
- Subagent tutorial: `Home/Subagent Creation Guide.md`
