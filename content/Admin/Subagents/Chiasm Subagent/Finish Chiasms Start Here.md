# Finish Chiasms - Session Startup Guide

**Purpose:** Complete the remaining Psalm chiasms to reach 100% coverage of ChiasmusXchange.com

**Date Created:** 2025-11-01

---

## Session Overview

This guide will help you (or Claude) systematically convert the remaining missing Psalm chiasms using the **Chiasm Conversion Subagent** we built together.

### What You'll Learn:
- How subagents work (they run in isolated sessions)
- How to invoke the Task tool to launch subagents
- How to verify subagent results
- How to batch process multiple chiasms

---

## Current Status

### Missing Chiasms (as of 2025-11-01)

**HIGH PRIORITY - 4 Complete Psalms:**
1. ✅ ~~Psalm 80~~ - **COMPLETED** (2025-11-01)
2. ❌ **Psalm 108** - https://www.chiasmusxchange.com/2018/04/13/psalm-108/
3. ❌ **Psalm 109** - https://www.chiasmusxchange.com/2018/03/02/psalm-109/
4. ❌ **Psalm 110** - https://www.chiasmusxchange.com/2017/02/26/psalm-110/ (Major Messianic!)
5. ❌ **Psalm 113** - https://www.chiasmusxchange.com/2015/03/02/psalm-1133-9/

**LOW PRIORITY - 2 Alternate Versions:**
6. ❌ Psalm 99 (alternate) - https://www.chiasmusxchange.com/2017/02/20/psalm-99/
7. ❌ Psalm 138 (alternate) - https://www.chiasmusxchange.com/2017/03/27/psalm138/

**Current Coverage:** 96% (189 of 195 unique chiasms)

---

## How Subagents Work

### Key Concepts:

1. **Isolated Session:** When you launch a subagent using the `Task` tool, it runs in its own separate session. Think of it like hiring a contractor - you give them complete instructions, they go do the work, and then report back with the results.

2. **Autonomous Execution:** The subagent has access to all the same tools you do (Read, Write, Edit, Bash, Grep, etc.) and makes its own decisions based on the prompt you give it.

3. **One-Time Communication:** You can't communicate with a subagent mid-task. It receives your prompt once, executes the entire workflow, and then sends you a final report. That's why the prompt must be **completely self-contained**.

4. **Parallel Execution:** You can launch multiple subagents at once (in a single message with multiple Task tool calls), and they'll all run simultaneously.

5. **Return to Main Session:** When the subagent finishes, control returns to your main session with a report of what happened.

---

## The Chiasm Conversion Subagent

We built a specialized subagent that:
1. Downloads a ChiasmusXchange.com page
2. Parses the HTML to extract the chiasm structure
3. Formats it according to your vault's exact standards
4. Creates the chiasm file with proper naming
5. Adds the link to the appropriate Reference Page(s)
6. Validates the formatting
7. Cleans up temporary files
8. Reports success/failure

**Full Prompt:** See `Home/Subagent Creation Guide.md` for the complete prompt structure.

---

## Step-by-Step: Converting Missing Chiasms

### STEP 1: Verify Current Status

Before starting, run the verification script to confirm which chiasms are still missing:

```bash
python identify_missing_chiasms.py > missing_chiasms_report.txt
```

This ensures you don't duplicate work and shows you the current gap.

### STEP 2: Choose Conversion Method

You have three options:

#### **Option A: Convert One at a Time** (Recommended for learning)
- Launch one subagent
- Verify the result
- Launch the next subagent
- **Advantage:** You can monitor each conversion and learn the process
- **Time:** ~2-3 minutes per chiasm

#### **Option B: Batch Convert in Parallel** (Fastest)
- Launch all 4 subagents simultaneously in one message
- Wait for all to complete
- Verify all results at once
- **Advantage:** Fastest completion (all done in ~3-4 minutes)
- **Time:** ~3-4 minutes total

#### **Option C: Manual Invocation** (Maximum control)
- You manually construct each Task tool call
- **Advantage:** Full understanding and control
- **Time:** ~5 minutes per chiasm (includes manual work)

---

## TEMPLATE: How to Invoke the Chiasm Subagent

### Basic Syntax

When you want Claude to convert a chiasm, say:

```
"Use the Chiasm subagent to convert Psalm [NUMBER] from this URL: [URL]"
```

Claude will then use the Task tool with the complete prompt.

### Manual Task Tool Invocation

If you want to invoke it yourself (or tell Claude exactly how), here's the structure:

```
Use the Task tool with these parameters:
- subagent_type: "general-purpose"
- description: "Convert Psalm [NUMBER] chiasm"
- model: "sonnet"
- prompt: [The complete chiasm conversion prompt with the specific URL]
```

---

## COMPLETE PROMPT TEMPLATE

⚠️ **IMPORTANT:** This prompt has been updated to Version 2.1 to fix formatting issues discovered during testing.

**Change Log:**
- **Version 1.0 Bug:** Colors were incorrectly mapped by letter label instead of indentation level
- **Version 2.0 Fix:** Colors now correctly map by nesting depth (0 spaces=red, 4 spaces=blue, etc.)
- **Version 2.1 Fix:** Each chiasm element must be ONE line (link + full text together), not split across multiple lines

**See:** `Chiasm_Subagent_Prompt.md` for the complete v2.1 prompt.

---

When invoking the subagent, use this exact prompt structure (replace variables in brackets):

```markdown
CHIASM CONVERSION SUBAGENT PROMPT - VERSION 2.1:
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

2. PARSE THE CHIASM STRUCTURE
   - Use Write tool to create Python parser script
   - Extract from HTML:
     * Chiasm levels (A, B, C, D, E and their primes A', B', C', D', E')
     * Biblical text for each element
     * Verse references (chapter and verse numbers)
     * Keywords to highlight
   - Identify the verse range (first verse to last verse)
   - CRITICAL: Determine the nesting depth for each element
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
           - C. (Level 2, 8 spaces) → TEAL #16a085
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
     * Colors use exact hex codes from palette
     * Colors include "font-weight: bold;"
     * Readable Bible links present at start of each line
     * CRITICAL: Verify color mapping matches nesting level:
       - Level 0 elements = RED #c0392b
       - Level 1 elements = BLUE #1f618d
       - Level 2 elements = TEAL #16a085
       - Level 3 elements = PURPLE #8e44ad
       - Level 4 elements = GOLD #d68910
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

## QUICK START COMMANDS

Copy and paste these commands to start your session:

### Option A: Convert One Chiasm at a Time

**For your first chiasm (Psalm 108):**
```
Use the Chiasm subagent to convert Psalm 108 from this URL:
https://www.chiasmusxchange.com/2018/04/13/psalm-108/
```

After it completes and you verify, do the next one:
```
Use the Chiasm subagent to convert Psalm 109 from this URL:
https://www.chiasmusxchange.com/2018/03/02/psalm-109/
```

Then:
```
Use the Chiasm subagent to convert Psalm 110 from this URL:
https://www.chiasmusxchange.com/2017/02/26/psalm-110/
```

Finally:
```
Use the Chiasm subagent to convert Psalm 113 from this URL:
https://www.chiasmusxchange.com/2015/03/02/psalm-1133-9/
```

### Option B: Convert All 4 in Parallel (Fastest)

**Single command to convert all 4 at once:**
```
Use the Chiasm subagent to convert these 4 Psalms in parallel:

1. Psalm 108 - https://www.chiasmusxchange.com/2018/04/13/psalm-108/
2. Psalm 109 - https://www.chiasmusxchange.com/2018/03/02/psalm-109/
3. Psalm 110 - https://www.chiasmusxchange.com/2017/02/26/psalm-110/
4. Psalm 113 - https://www.chiasmusxchange.com/2015/03/02/psalm-1133-9/

Launch all 4 subagents simultaneously in a single message.
```

---

## VERIFICATION CHECKLIST

After each chiasm conversion (or batch), verify:

### 1. Check the Chiasm File Was Created
```bash
ls "Chiasm/Chiasm - 19 - Psalm [NUMBER]"*
```

### 2. Verify File Contents
```bash
head -20 "Chiasm/Chiasm - 19 - Psalm [NUMBER]*.md"
```

**Check for:**
- ✅ Starts with `- A.` (no header)
- ✅ Proper indentation (4 spaces per level)
- ✅ One blank line between elements
- ✅ Colors with `font-weight: bold;`
- ✅ Readable Bible links at start of each line

### 3. Verify Reference Page Link
```bash
grep "Chiasm - 19 - Psalm [NUMBER]" "Reference Pages/19 - Psalms/Psalm [NUMBER].md"
```

**Check for:**
- ✅ Link appears under `##### Chiasms` section
- ✅ Uses `▸` bullet with 2 spaces before it
- ✅ Correct link format

### 4. Run Full Vault Verification (Optional)
```bash
python "Scripts to Keep/verify_references.py"
```

This ensures no broken links were introduced.

---

## EXAMPLE: Completed Conversion (Psalm 80)

### What Happened:
1. **Subagent launched** with URL for Psalm 80
2. **Ran autonomously** for ~60-90 seconds
3. **Created file:** `Chiasm/Chiasm - 19 - Psalm 80 . 1 - 19.md`
4. **Added link** to `Reference Pages/19 - Psalms/Psalm 80.md` at verse 1
5. **Reported back** with success and validation details

### Result File Structure:
```markdown
- A. [[Readable Bible/19 - Psalms/Psalm 80#Psalm 80 . 1|1-2]] Give ear, O Shepherd...

- A. [[Readable Bible/19 - Psalms/Psalm 80#Psalm 80 . 3|3]] <span style="color: #c0392b; font-weight: bold;">Turn us again,</span>...

    - B. [[Readable Bible/19 - Psalms/Psalm 80#Psalm 80 . 4|4-6]] O LORD God of hosts...

    [etc.]
```

### Reference Page Link Added:
```markdown
##### Chiasms
  ▸ [[Chiasm/Chiasm - 19 - Psalm 80 . 1 - 19|Chiasm - Psalm 80:1-19]]
```

---

## TROUBLESHOOTING

### Issue: Subagent reports URL download failed
**Solution:** Verify the URL is accessible. Try visiting it in a browser first.

### Issue: Parsing fails
**Solution:** The chiasm structure on ChiasmusXchange may be unusual. The subagent will report the issue. You may need to convert manually or adjust the parser.

### Issue: Reference Page doesn't exist
**Solution:** The Reference Page must exist before adding links. Verify the file exists at `Reference Pages/19 - Psalms/Psalm [NUMBER].md`

### Issue: Formatting validation fails
**Solution:** The subagent will report specific issues. Review the created file and fix manually if needed.

---

## POST-COMPLETION TASKS

### After All 4 Chiasms Are Converted:

1. **Run final verification:**
```bash
python identify_missing_chiasms.py > final_report.txt
cat final_report.txt
```

Expected result: **0 missing high-priority chiasms** (100% coverage of complete Psalms)

2. **Run vault link verification:**
```bash
python "Scripts to Keep/verify_references.py"
```

Expected result: **100% accuracy**

3. **Optional: Add alternate versions** (Psalm 99, 138)
If you want multiple chiastic structures for comparison, convert the 2 low-priority alternates using the same process.

4. **Update Vision.md:**
Update the Phase 4 chiasm count in `Home/Vision.md`:
- Before: ~1,469 chiasms
- After: ~1,473-1,475 chiasms (depending on whether you add alternates)

5. **Commit to Git:**
```bash
git add .
git commit -m "Session XX - Completed Psalm chiasms to 100% ChiasmusXchange coverage

Added chiasms:
- Psalm 108
- Psalm 109
- Psalm 110 (Messianic)
- Psalm 113

Coverage: 100% of complete Psalm chiasms from ChiasmusXchange.com

🤖 Generated with Claude Code https://claude.com/claude-code

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

## NEXT SESSION RECOMMENDATIONS

Once Psalm chiasms are complete, consider:

1. **Other Book Chiasms:** Check ChiasmusXchange for chiasms in other books (Genesis, Isaiah, etc.)

2. **Expand to Other Sources:** Look for chiasms from scholarly sources beyond ChiasmusXchange

3. **Reference Page Completion:** Continue Phase 1 (create Reference Pages for remaining books)

4. **Thematic Network Expansion:** Build out additional thematic networks

---

## REFERENCE MATERIALS

- **Subagent Creation Guide:** `Home/Subagent Creation Guide.md`
- **Formatting Standards:** `Home/Formatting.md`
- **Vault Vision:** `Home/Vision.md`
- **Missing Chiasms Script:** `identify_missing_chiasms.py`
- **Missing Chiasms Report:** `Psalms_Chiasms_Missing_Analysis.md`

---

## SESSION CHECKLIST

Use this checklist when you start your next session:

- [ ] Read `Finish Chiasms Start Here.md` (this file)
- [ ] Review current missing chiasms list
- [ ] Choose conversion method (one-at-a-time or parallel)
- [ ] Convert Psalm 108
- [ ] Verify Psalm 108 conversion
- [ ] Convert Psalm 109
- [ ] Verify Psalm 109 conversion
- [ ] Convert Psalm 110
- [ ] Verify Psalm 110 conversion
- [ ] Convert Psalm 113
- [ ] Verify Psalm 113 conversion
- [ ] Run final verification script
- [ ] Run vault link verification
- [ ] Optional: Add alternates (Psalm 99, 138)
- [ ] Update Vision.md
- [ ] Commit changes to git
- [ ] Celebrate 100% coverage! 🎉

---

**Good luck! You're only 4 chiasms away from 100% coverage of ChiasmusXchange Psalm chiasms!**

**Estimated Time to Complete:** 8-15 minutes (depending on method chosen)

---

**Last Updated:** 2025-11-01
**Created By:** Claude Code (Session documenting Chiasm Subagent creation and testing)
