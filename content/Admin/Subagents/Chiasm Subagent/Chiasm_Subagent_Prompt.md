# Chiasm Conversion Subagent Prompt

**Version:** 2.3 (Production Ready)
**Date:** 2025-11-01
**Status:** ✅ Tested and Working

**Version History:**
- v1.0: Basic functionality (had color mapping bug)
- v2.0: Fixed color assignment based on chiasm nesting level
- v2.1: Fixed line formatting - each chiasm element on ONE line
- v2.2: Added PDF/Word document detection - skip chiasms only available as downloads
- v2.3: Fixed sub-element handling - do NOT create separate lines for thematic subdivisions (CURRENT)

---

## How to Use This Subagent

**Quick Start:** Copy the prompt below and replace:
- `[URL]` with the ChiasmusXchange.com URL
- `[NUMBER]` with the Psalm number

**Tool Call:**
```
Task(
  subagent_type="general-purpose",
  description="Convert Psalm [NUMBER] chiasm",
  model="sonnet",
  prompt="[The complete prompt below]"
)
```

---

## THE COMPLETE PROMPT (v2.2)

Use this exact prompt when invoking the Chiasm subagent:

```markdown
CHIASM CONVERSION SUBAGENT PROMPT - VERSION 2.2:
==================================

MISSION: Convert a chiasm from ChiasmusXchange.com URL to vault format

INPUTS YOU NEED:
- URL: [CHIASMUSXCHANGE_URL]
- Book number: 19
- Book name: Psalms

STEP-BY-STEP PROCESS:

1. DOWNLOAD THE PAGE
   - Use Bash tool with curl to download HTML
   - Save as temp_chiasm.html
   - Command: curl -s "[URL]" -o temp_chiasm.html

1a. CHECK FOR PDF/WORD DOCUMENT LINKS
   - Use Bash tool with grep to check if page only links to external documents
   - Command: grep -iE '\.pdf|\.docx?|\.doc"' temp_chiasm.html
   - If the page contains links to PDF or Word documents instead of displaying the chiasm text directly:
     * DELETE temp_chiasm.html
     * REPORT: "This chiasm is only available as a PDF/Word document download, not as webpage text. Skipping conversion per user instructions."
     * EXIT - do not proceed with conversion
   - If no PDF/Word links found, continue to Step 2

2. PARSE THE CHIASM STRUCTURE
   - Use Write tool to create Python parser script
   - Extract from HTML:
     * Chiasm levels (A, B, C, D, E and their primes A', B', C', D', E')
     * Biblical text for each element
     * Verse references (chapter and verse numbers)
     * Keywords to highlight
   - Identify the verse range (first verse to last verse)
   - CRITICAL: Determine the nesting depth for each element
   - CRITICAL: IGNORE sub-elements (a, b, c, etc.) - these are thematic points WITHIN a chiasm level, NOT separate structural levels
     * If you see "Three examples: (a) Israel, (b) Angels, (c) Sodom" - combine all three into ONE chiasm element
     * ONLY create separate lines for CAPITAL LETTER chiasm levels (A, B, C, D, E and their primes)
     * DO NOT create lines for lowercase sub-elements (a, b, c, a', b', c')
   - Run script with Bash tool

3. FORMAT ACCORDING TO VAULT STANDARDS
   Rules from Formatting.md:
   - NO markdown header (start directly with "- A.")
   - Use markdown bullets (-)
   - 4-space indentation per level (A=0 spaces, B=4, C=8, D=12, E=16)
   - ONE blank line between each element
   - ONE blank line at end of file
   - Color ONLY keywords (not entire clauses)

   CRITICAL FORMATTING RULE - EACH CHIASM ELEMENT ON ONE LINE:
   Each chiasm element (A, B, C, etc.) MUST be formatted as a SINGLE LINE containing:
   - The bullet and label (e.g., "- A.")
   - The Readable Bible link with verse range
   - ALL the biblical text for those verses on the SAME line
   - Keywords highlighted with color spans

   CORRECT FORMAT (all on ONE line):
   - A. [[Link|1-5]] Text of verse 1. Text of verse 2. Text of verse 3. <span>keyword</span>. Text continues.

   WRONG FORMAT (breaking verses onto separate lines):
   - A.
   [[Link|1]] Text of verse 1.
   [[Link|2]] Text of verse 2.

   EXAMPLE OF CORRECT SINGLE-LINE FORMAT:
   - A. [[Readable Bible/19 - Psalms/Psalm 22#Psalm 22 . 1|1-11]] My God, my God, why hast thou <span style="color: #c0392b; font-weight: bold;">forsaken me</span>? O my God, I cry in the daytime, but thou hearest not; and in the night season, and am not silent. But thou art holy, O thou that inhabitest the praises of Israel. Our fathers <span style="color: #c0392b; font-weight: bold;">trusted</span> in thee: they trusted, and thou didst <span style="color: #c0392b; font-weight: bold;">deliver</span> them.

   After each element, add ONE blank line before the next element.

   CRITICAL COLOR PALETTE MAPPING:
   You MUST map colors based on the NESTING LEVEL (indentation depth), NOT the letter label.

   Level 0 (outermost, 0 spaces) → RED #c0392b
   Level 1 (second level, 4 spaces) → BLUE #1f618d
   Level 2 (third level, 8 spaces) → TEAL #16a085
   Level 3 (fourth level, 12 spaces) → PURPLE #8e44ad
   Level 4 (center, 16 spaces) → GOLD #d68910

   EXAMPLES OF CORRECT COLOR MAPPING:

   Simple 3-level chiasm (A-B-A'):
   - A. (Level 0, 0 spaces) → Use RED #c0392b
       - B. (Level 1, 4 spaces) → Use BLUE #1f618d
   - A'. (Level 0, 0 spaces) → Use RED #c0392b

   Standard 5-level chiasm (A-B-C-B'-A'):
   - A. (Level 0, 0 spaces) → Use RED #c0392b
       - B. (Level 1, 4 spaces) → Use BLUE #1f618d
           - C. (Level 2, 8 spaces) → Use TEAL #16a085
       - B'. (Level 1, 4 spaces) → Use BLUE #1f618d
   - A'. (Level 0, 0 spaces) → Use RED #c0392b

   Complex 7-level chiasm (A-B-C-D-C'-B'-A'):
   - A. (Level 0, 0 spaces) → Use RED #c0392b
       - B. (Level 1, 4 spaces) → Use BLUE #1f618d
           - C. (Level 2, 8 spaces) → Use TEAL #16a085
               - D. (Level 3, 12 spaces) → Use PURPLE #8e44ad
           - C'. (Level 2, 8 spaces) → Use TEAL #16a085
       - B'. (Level 1, 4 spaces) → Use BLUE #1f618d
   - A'. (Level 0, 0 spaces) → Use RED #c0392b

   PARALLEL PAIRS MUST HAVE MATCHING COLORS:
   - A and A' → Same color (RED)
   - B and B' → Same color (BLUE)
   - C and C' → Same color (TEAL)
   - D and D' → Same color (PURPLE)
   - E and E' → Same color (GOLD)

   Color span format (ALWAYS include font-weight: bold;):
   <span style="color: #HEXCODE; font-weight: bold;">KEYWORD</span>

   Readable Bible links:
   - Format: [[Readable Bible/19 - Psalms/Psalm [Ch]#Psalm [Ch] . [V]|[V]]]
   - Place at START of each line (before text)
   - Example: [[Readable Bible/19 - Psalms/Psalm 80#Psalm 80 . 1|1]]

4. CREATE THE CHIASM FILE
   - Filename format: Chiasm - 19 - Psalm [Ch] . [StartV] - [EndV].md
   - Location: Chiasm/ folder (in current working directory)
   - Use Write tool to create file with formatted content

5. ADD LINK TO REFERENCE PAGE(S)
   - Determine which Reference Page(s) need the link (based on verse range)
   - For the verse range covered by the chiasm:
     * Read: Reference Pages/19 - Psalms/Psalm [Ch].md
     * Find verse anchors that fall within the chiasm range
     * For each verse, locate the "##### Chiasms" section
     * Add link with exact formatting:
       ▸ [[Chiasm/Chiasm - 19 - Psalm [Ch] . [V] - [V]|Chiasm - Psalm [Ch]:[V]-[V]]]
     * Note: Use 2 spaces + ▸ + 1 space before link
   - Use Edit tool to add the link (not Write, since file exists)

6. VALIDATE THE RESULT
   - Check chiasm file formatting:
     * Starts with "- A." (no header)
     * Correct indentation (4 spaces per level)
     * ONE blank line between elements
     * ONE blank line at end of file
     * CRITICAL: Each chiasm element is ONE line (not multiple lines per element)
     * Each line contains: bullet + label + link + full text
     * Colors use exact hex codes from palette
     * Colors include "font-weight: bold;"
     * Readable Bible links present at start of each chiasm element line
     * CRITICAL: Verify color mapping matches nesting level:
       - Level 0 elements = RED #c0392b
       - Level 1 elements = BLUE #1f618d
       - Level 2 elements = TEAL #16a085
       - Level 3 elements = PURPLE #8e44ad
       - Level 4 elements = GOLD #d68910
     * Count the number of lines: Should equal (number of chiasm elements × 2) - 1
       Example: 5-element chiasm (A-B-C-B'-A') = 9 lines (5 content + 4 blank lines + 1 final blank)
   - Check Reference Page link:
     * Link added under "##### Chiasms" section
     * Correct formatting with ▸ bullet
     * Link points to correct chiasm file

7. CLEANUP
   - Delete temp_chiasm.html (use Bash: rm temp_chiasm.html)
   - Delete any Python scripts created (use Bash: rm parse_chiasm.py or similar)

8. REPORT BACK
   Provide:
   - Chiasm file created: [full filename]
   - Verse range: Psalm [Ch]:[StartV]-[EndV]
   - Chiasm structure: [describe levels, e.g., "A-B-C-D-C'-B'-A' (7 levels)"]
   - Color mapping verification: [confirm each level has correct color]
   - Link added to Reference Page(s): [list pages modified]
   - Validation: [passed/failed with specific details]
   - Any errors or warnings encountered

ERROR HANDLING:
- If URL fails to download: Report "Failed to download URL: [error message]. Please verify URL is correct."
- If chiasm is only available as PDF/Word document: Report "This chiasm is only available as a PDF/Word document download, not as webpage text. Skipping conversion per user instructions." and EXIT
- If parsing fails: Report "Failed to parse chiasm structure: [error]. Raw HTML excerpt: [first 500 chars]"
- If Reference Page doesn't exist: Report "Reference Page not found: [filename]. Cannot add link."
- If formatting validation fails: Report "Validation failed: [specific issue found]"
- If cannot determine verse range: Report "Could not extract verse range from chiasm structure"
- If color mapping is incorrect: Report "Color validation failed: [which level has wrong color]"

TOOLS YOU'LL USE:
- Bash: Download page with curl, run Python scripts, cleanup files
- Write: Create Python parser script, create formatted chiasm file
- Read: Read Reference Page(s) to find insertion point
- Edit: Add links to Reference Page(s)
- Bash: Delete temporary files

CRITICAL NOTES:
- ALWAYS use EXACT biblical text from website (do NOT paraphrase or modernize)
- ALWAYS include "font-weight: bold;" in color spans
- ALWAYS use periods in anchors: "Ch . V" not "Ch-V"
- ALWAYS use 2 spaces before pipes in Reference Page links
- ALWAYS map colors by INDENTATION LEVEL (0 spaces=red, 4 spaces=blue, 8 spaces=teal, etc.)
- Matching colors for parallel pairs (A and A' same color, B and B' same color, etc.)
- Count indentation carefully: Level 0=0 spaces, Level 1=4 spaces, Level 2=8 spaces, Level 3=12 spaces, Level 4=16 spaces

CURRENT WORKING DIRECTORY: C:\Users\Boone\Desktop\OT to OT Use

Begin conversion of Psalm [NUMBER] now.
```

---

## What Changed in Version 2.0:

### 1. Explicit Color Mapping Rules
Added clear instructions to map colors by **nesting level** (indentation depth), not by letter label.

### 2. Visual Examples
Provided three concrete examples showing correct color mapping for:
- Simple 3-level chiasm
- Standard 5-level chiasm
- Complex 7-level chiasm

### 3. Color Mapping Table
Created a simple lookup:
- Level 0 (0 spaces) → RED
- Level 1 (4 spaces) → BLUE
- Level 2 (8 spaces) → TEAL
- Level 3 (12 spaces) → PURPLE
- Level 4 (16 spaces) → GOLD

### 4. Enhanced Validation
Added specific color validation step that checks:
- Each level has the correct color for its indentation depth
- Parallel pairs have matching colors

### 5. Better Error Reporting
Subagent now reports:
- Chiasm structure description
- Color mapping verification
- Which level has wrong color (if validation fails)

---

## Why Version 1.0 Failed:

The original prompt said "A/A' use red, B/B' use blue" but didn't specify that this depends on **indentation level**.

In a chiasm like:
```
- A. (level 0)
- A. (level 0)  ← This is still level 0, not level 1!
    - B. (level 1)
    - B. (level 1)
```

The parser saw two "A" elements and thought they were different levels. Version 2.0 fixes this by saying "count the spaces, not the letters."

---

## Usage:

When invoking the subagent, replace:
- `[CHIASMUSXCHANGE_URL]` with the actual URL
- `[NUMBER]` with the Psalm number

Then use the Task tool with this corrected prompt.
