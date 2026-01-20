# Subagent Creation Guide

**A Step-by-Step Tutorial for Building Custom Claude Code Subagents**

Created: 2025-11-01
Updated: 2025-11-01 (Version 2.0 - Color Mapping Fix)
Example Project: Chiasm Batch Processor

---

## 🚨 IMPORTANT UPDATE - Version 2.0

**Bug Found During Testing:** The original Chiasm subagent (v1.0) incorrectly assigned colors based on letter labels instead of indentation depth.

**Example of the Bug:**
```
- A. (0 spaces) → Got RED ✅
- A. (0 spaces) → Got RED (should be RED) ✅
    - B. (4 spaces) → Got NONE (should be BLUE) ❌
    - B. (4 spaces) → Got RED (should be BLUE) ❌
        - C. (8 spaces) → Got BLUE (should be TEAL) ❌
```

**Fix Applied:** Version 2.0 explicitly instructs the subagent to map colors by indentation level (0 spaces=red, 4 spaces=blue, 8 spaces=teal, etc.)

**Lesson Learned:** Always test subagents with one example before batch processing! We caught this bug after converting Psalm 80 and fixed it before converting the remaining 4 Psalms.

**See:** `Chiasm_Subagent_Prompt.md` for the complete v2.1 prompt.

---

## What is a Subagent?

A **subagent** is a specialized autonomous agent that Claude Code can launch to handle complex, multi-step tasks. Think of it as delegating work to a focused assistant who:
- Has access to the same tools (Read, Write, Edit, Bash, Grep, etc.)
- Operates independently to complete a specific goal
- Returns a final report when finished
- Cannot ask questions mid-execution (must be fully autonomous)

**Key Benefits:**
- Handles 7+ sequential steps automatically
- Can make decisions based on what it discovers
- Runs in parallel with other subagents
- Reduces token usage in main conversation
- Perfect for repetitive, complex workflows

---

## When to Use Subagents

### ✅ Good Use Cases:
- Complex multi-step tasks (7+ steps)
- Repetitive workflows you'll run multiple times
- Tasks requiring autonomous decision-making
- Batch processing operations
- Tasks with conditional logic based on file contents

### ❌ Not Ideal For:
- Simple 1-3 step tasks
- Tasks requiring user input mid-process
- Exploratory work where requirements are unclear
- One-time operations

---

## Subagent Types Available

Claude Code offers several specialized subagent types:

| Type | Best For | Tools Available |
|------|----------|-----------------|
| **general-purpose** | Complex multi-step tasks, varied operations | All tools (*) |
| **Explore** | Searching codebases, finding files/patterns | All tools |
| **Plan** | Planning code changes, analyzing structure | All tools |

**For our example:** We chose `general-purpose` because the Chiasm processor needs to download web content, parse HTML, create files, edit existing files, and validate results.

---

## Step-by-Step: Building the Chiasm Subagent

### Step 1: Define the Subagent's Purpose

**Ask:**
- What is the complete workflow from start to finish?
- What are the inputs and outputs?
- What decisions will it need to make autonomously?

**Our Example:**
- **Purpose:** Convert chiasms from ChiasmusXchange.com to vault format
- **Inputs:** URL, book number, book name
- **Outputs:** Formatted chiasm file, updated Reference Pages
- **Workflow:** Download → Parse → Format → Create File → Update Links → Validate → Cleanup

### Step 2: Choose the Subagent Type

Review the available types and match to your needs:
- Need to search codebase? → `Explore`
- Need to plan code changes? → `Plan`
- Complex varied operations? → `general-purpose`

**Our Choice:** `general-purpose` (handles web fetching, file creation, editing, validation)

### Step 3: Gather Required Standards/Rules

Before writing the prompt, collect all the information the subagent needs:
- Formatting standards
- Validation rules
- Example files
- Error handling requirements
- Color palettes, naming conventions, etc.

**What We Gathered:**
1. Read `Home/Formatting.md` for exact chiasm formatting rules
2. Examined existing chiasm files for structure examples
3. Identified Reference Page link format requirements
4. Noted color palette hex codes
5. Defined validation checkpoints

**Critical:** The subagent can't ask you questions, so you must provide EVERYTHING upfront.

### Step 4: Write the Subagent Prompt

This is the most important step. Your prompt must be:

#### A. Self-Contained
- No assumptions about prior context
- All rules stated explicitly
- No reliance on "you should know" information

#### B. Sequential and Detailed
- Step 1, Step 2, Step 3 format
- Exact commands to run
- Specific tool calls to make

#### C. Error Handling
- What to do if URL fails
- How to handle missing files
- Validation failure responses

#### D. Clear Output Requirements
- What to report back
- Success/failure indicators
- Specific details to include

### Step 5: Structure the Prompt

Use this template structure:

```markdown
[SUBAGENT NAME] PROMPT:
==================================

MISSION: [One sentence describing the goal]

INPUTS YOU NEED:
- Input 1: [Description]
- Input 2: [Description]

STEP-BY-STEP PROCESS:

1. [STEP NAME IN CAPS]
   - Specific action 1
   - Specific action 2
   - Tool to use: [Tool name]
   - Command example: [Exact command]

2. [NEXT STEP]
   - Actions...
   - Validation checks...

[Continue for all steps]

FORMATTING RULES:
- Rule 1: [Exact specification]
- Rule 2: [Exact specification]
- Examples: [Show concrete examples]

ERROR HANDLING:
- If [scenario]: [What to do]
- If [scenario]: [What to do]

VALIDATION CHECKLIST:
- ✅ Check 1: [What to verify]
- ✅ Check 2: [What to verify]

TOOLS YOU'LL USE:
- [Tool]: [Purpose]
- [Tool]: [Purpose]

REPORT BACK:
Provide:
- ✅ [Success indicator 1]
- ✅ [Success indicator 2]
- ❌ [Any errors or warnings]
```

---

## Our Chiasm Subagent Prompt

Here's the complete prompt we built:

```markdown
CHIASM CONVERSION SUBAGENT PROMPT:
==================================

MISSION: Convert a chiasm from ChiasmusXchange.com URL to vault format

INPUTS YOU NEED:
- URL: The ChiasmusXchange.com page URL
- Book number: (e.g., "01" for Genesis)
- Book name: (e.g., "Genesis")

STEP-BY-STEP PROCESS:

1. DOWNLOAD THE PAGE
   - Use Bash tool with curl to download HTML
   - Save as temp_chiasm.html
   - Command: curl -s "[URL]" -o temp_chiasm.html

2. PARSE THE CHIASM STRUCTURE
   - Use Write tool to create Python parser script
   - Extract from HTML:
     * Chiasm levels (A, B, C, D, E and their primes)
     * Biblical text for each element
     * Verse references (chapter and verse numbers)
     * Keywords to highlight
   - Identify the verse range (first verse to last verse)
   - Run script with Bash tool

3. FORMAT ACCORDING TO VAULT STANDARDS
   Rules from Formatting.md:
   - NO markdown header (start directly with "- A.")
   - Use markdown bullets (-)
   - 4-space indentation per level (A=0 spaces, B=4, C=8, D=12, E=16)
   - ONE blank line between each element
   - ONE blank line at end of file
   - Color ONLY keywords (not entire clauses)

   Color palette (EXACT hex codes required):
   - A/A' (outermost): <span style="color: #c0392b; font-weight: bold;">TEXT</span>
   - B/B' (second): <span style="color: #1f618d; font-weight: bold;">TEXT</span>
   - C/C' (third): <span style="color: #16a085; font-weight: bold;">TEXT</span>
   - D/D' (fourth): <span style="color: #8e44ad; font-weight: bold;">TEXT</span>
   - E/E' (center): <span style="color: #d68910; font-weight: bold;">TEXT</span>

   Readable Bible links:
   - Format: [[Readable Bible/[##] - [Book]/[Book] [Ch]#[Book] [Ch] . [V]|[V]]]
   - Place at START of each line (before text)
   - Example: [[Readable Bible/01 - Genesis/Genesis 1#Genesis 1 . 27|27]]

4. CREATE THE CHIASM FILE
   - Filename format: Chiasm - [##] - [Book] [Ch] . [StartV] - [EndV].md
   - Location: Chiasm/ folder (in current working directory)
   - Use Write tool to create file with formatted content

5. ADD LINK TO REFERENCE PAGE(S)
   - Determine which Reference Page(s) need the link (based on verse range)
   - For each verse in the chiasm range:
     * Read: Reference Pages/[##] - [Book]/[Book] [Ch].md
     * Find the verse anchor: #### [Book] [Ch] . [V]
     * Locate the "##### Chiasms" section
     * Add link with exact formatting:
       ▸ [[Chiasm/Chiasm - [##] - [Book] [Ch] . [V] - [V]|Chiasm - [Book] [Ch]:[V]-[V]]]
     * Note: Use 2 spaces + ▸ + 1 space before link
   - Use Edit tool to add the link (not Write, since file exists)

6. VALIDATE THE RESULT
   - Check chiasm file formatting:
     * ✅ Starts with "- A." (no header)
     * ✅ Correct indentation (4 spaces per level)
     * ✅ ONE blank line between elements
     * ✅ ONE blank line at end of file
     * ✅ Colors use exact hex codes from palette
     * ✅ Colors include "font-weight: bold;"
     * ✅ Readable Bible links present at start of each line
   - Check Reference Page link:
     * ✅ Link added under "##### Chiasms" section
     * ✅ Correct formatting with ▸ bullet
     * ✅ Link points to correct chiasm file

7. CLEANUP
   - Delete temp_chiasm.html (use Bash: rm temp_chiasm.html)
   - Delete any Python scripts created (use Bash: rm *.py)

8. REPORT BACK
   Provide:
   - ✅ Chiasm file created: [full filename]
   - ✅ Verse range: [Book] [Ch]:[StartV]-[EndV]
   - ✅ Link added to Reference Page(s): [list pages modified]
   - ✅ Validation: [passed/failed with specific details]
   - ❌ Any errors or warnings encountered

ERROR HANDLING:
- If URL fails to download: Report "❌ Failed to download URL: [error message]. Please verify URL is correct."
- If parsing fails: Report "❌ Failed to parse chiasm structure: [error]. Raw HTML excerpt: [first 500 chars]"
- If Reference Page doesn't exist: Report "❌ Reference Page not found: [filename]. Cannot add link."
- If formatting validation fails: Report "❌ Validation failed: [specific issue found]"
- If cannot determine verse range: Report "❌ Could not extract verse range from chiasm structure"

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
- Matching colors for parallel pairs (A and A' same color, B and B' same color, etc.)
```

---

## Step 6: Construct the Task Tool Call

The actual tool call uses three required parameters:

```python
Task(
  subagent_type="general-purpose",  # Type from Step 2
  description="Convert ChiasmusXchange chiasm",  # Short 3-5 word summary
  prompt="""[Your complete prompt from Step 4]"""  # The detailed instructions
)
```

**Optional parameter:**
```python
model="sonnet"  # Use "sonnet" for accuracy, "haiku" for speed
```

**For our example:**
```python
Task(
  subagent_type="general-purpose",
  description="Convert ChiasmusXchange chiasm",
  model="sonnet",  # We chose sonnet for parsing accuracy
  prompt="""
  [The entire CHIASM CONVERSION SUBAGENT PROMPT goes here]

  URL: https://www.chiasmusxchange.com/example-url
  Book number: 01
  Book name: Genesis
  """
)
```

---

## Step 7: Test the Subagent

**First Test:**
1. Launch subagent with a simple example
2. Observe the output report
3. Manually verify the results match expectations
4. Check for any errors or edge cases

**Refinement:**
- Add error handling for issues discovered
- Clarify ambiguous instructions
- Add validation steps for common mistakes
- Update prompt based on failures

**Iteration:**
- Test with 2-3 different examples
- Verify it handles variations correctly
- Ensure autonomous decision-making works

---

## Step 8: Make It Reusable (Optional)

Once tested and working, you have options:

### Option A: Python Script Wrapper

Create `convert_chiasm.py`:
```python
import sys
import subprocess

def main():
    if len(sys.argv) < 4:
        print("Usage: python convert_chiasm.py <url> <book_num> <book_name>")
        sys.exit(1)

    url = sys.argv[1]
    book_num = sys.argv[2]
    book_name = sys.argv[3]

    # Launch Claude Code with Task tool
    # (Implementation would call Claude Code API)
    pass

if __name__ == "__main__":
    main()
```

**Usage:** `python convert_chiasm.py "https://..." "01" "Genesis"`

### Option B: Claude Code Slash Command

Create `.claude/commands/convert-chiasm.md`:
```markdown
When user provides a ChiasmusXchange URL, use the Task tool to launch the Chiasm Conversion subagent with the following prompt:

[Paste complete subagent prompt here]
```

**Usage:** `/convert-chiasm https://www.chiasmusxchange.com/...`

### Option C: Just Save the Prompt

Keep this guide and copy/paste the prompt into Task tool calls when needed.

---

## Tips for Creating Other Subagents

### 1. Start with Clear Boundaries
- Define EXACTLY what the subagent does
- Define what it does NOT do (scope limits)

### 2. Think Like a Recipe
- No steps should require interpretation
- Include actual commands to run
- Show example outputs

### 3. Plan for Failure
- Every step should have error handling
- Validation after critical operations
- Clear failure reporting

### 4. Test Incrementally
- Don't build the entire workflow at once
- Test each major step separately
- Add complexity gradually

### 5. Document Assumptions
- What files must exist beforehand?
- What format must inputs follow?
- What dependencies are required?

### 6. Use Validation Checklists
- List what "success" looks like
- Provide specific checks to perform
- Include example correct outputs

---

## Common Subagent Patterns

### Pattern 1: Batch File Processor
```
For each file in folder:
  1. Read file
  2. Transform content
  3. Write back or create new file
  4. Validate result
Report: [N] files processed, [M] errors
```

### Pattern 2: Web Scraper + Formatter
```
1. Fetch URL
2. Parse HTML/JSON
3. Transform to internal format
4. Create/update local files
5. Add cross-references
6. Validate links
7. Cleanup
```

### Pattern 3: Multi-File Refactor
```
1. Find all files matching pattern
2. For each file:
   - Read content
   - Apply transformation
   - Update cross-references
3. Validate all changes
4. Report summary
```

### Pattern 4: Report Generator
```
1. Scan directory structure
2. Collect statistics
3. Identify issues
4. Generate markdown report
5. Optionally fix issues
6. Re-validate
```

---

## Checklist: Is Your Subagent Ready?

Before launching, verify:

- [ ] **Purpose is clear**: One-sentence mission statement
- [ ] **Inputs defined**: All required parameters listed
- [ ] **Steps are sequential**: Numbered, ordered process
- [ ] **Commands are exact**: Actual tool calls, not pseudo-code
- [ ] **Error handling exists**: For every major operation
- [ ] **Validation included**: Checkpoints to verify success
- [ ] **Cleanup specified**: Temporary files deleted
- [ ] **Report format defined**: What to return when complete
- [ ] **Examples provided**: Show what "correct" looks like
- [ ] **No ambiguity**: Every instruction is clear and specific

---

## Example Use Cases for Your Vault

Based on your Obsidian vault workflow, here are other potential subagents:

### 1. Reference Page Batch Creator
**Purpose:** Create Reference Pages for an entire book at once
**Steps:** Generate all chapter files with proper navigation, frontmatter, verse anchors

### 2. Link Validator & Fixer
**Purpose:** Find and repair broken links across the vault
**Steps:** Scan files, identify broken links, suggest or auto-fix, re-validate

### 3. TOSK Entry Formatter
**Purpose:** Convert Treasury of Scripture Knowledge entries to vault format
**Steps:** Parse TOSK text, create Readable Bible links, format with proper headers

### 4. Cross-Reference Duplicator Detector
**Purpose:** Find duplicate cross-references across OT→OT and NT→OT files
**Steps:** Scan all reference files, identify duplicates, report with recommendations

### 5. Chiasm Coverage Reporter
**Purpose:** Generate report of which Bible passages have chiasms
**Steps:** Scan all chiasm files, extract verse ranges, create coverage map by book/chapter

---

## Advanced: Parallel Subagents

You can launch multiple subagents in a single message for parallel processing:

```python
# Launch 3 subagents simultaneously
Task(subagent_type="general-purpose", description="Convert chiasm 1", prompt="...")
Task(subagent_type="general-purpose", description="Convert chiasm 2", prompt="...")
Task(subagent_type="general-purpose", description="Convert chiasm 3", prompt="...")
```

**When to use:**
- Processing multiple independent items
- Different operations on different books
- Parallel validation of different folders

**When NOT to use:**
- Steps depend on each other (must be sequential)
- Editing the same files (risk of conflicts)
- Limited by external API rate limits

---

## Troubleshooting Common Issues

### Issue: Subagent doesn't understand context
**Solution:** Make prompt more explicit, include examples, don't assume prior knowledge

### Issue: Subagent asks questions mid-execution
**Solution:** Anticipate decision points, provide rules for all scenarios

### Issue: Formatting is inconsistent
**Solution:** Include exact format examples, show before/after, specify character-by-character

### Issue: Validation fails but subagent reports success
**Solution:** Add specific validation checkpoints, define what "success" looks like

### Issue: Subagent takes too long
**Solution:** Consider using "haiku" model for simpler tasks, or break into smaller subagents

---

## Learning Resources

- **Claude Code Documentation**: https://docs.claude.com/en/docs/claude-code/
- **Task Tool Reference**: See the Task tool description in Claude Code
- **Your Vault's Standards**: Always reference `Home/Formatting.md` and `Home/Vision.md`

---

## Revision History

- **2025-11-01**: Initial creation based on Chiasm Subagent tutorial

---

**Next Steps:**
1. Test the Chiasm subagent with a real URL
2. Refine based on results
3. Build your next subagent using this guide as template
4. Document learnings and update this guide

---

**Questions to Consider for Future Subagents:**
- What repetitive task do I do most often?
- What multi-step process could be automated?
- Where do I make the most manual errors?
- What would save me the most time if automated?
