# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault containing a reference collection from the Septuagint (LXX - the Greek Old Testament). Each chapter is stored as an individual markdown file. This includes Psalms, Proverbs, and other books.

## File Structure

- **File naming**:
  - Psalms: `Psalms N.md` where N is the Psalm number (1-178, plus some additional numbered psalms up to 206)
  - Proverbs: `Proverbs N.md` where N is the chapter number (1-31)
  - Other books follow the same pattern: `[Book Name] N.md`
- **Frontmatter**: Each file contains YAML frontmatter with:
  - `cssClasses: lxx`
  - `Book: [Book Name]` (e.g., "Psalms", "Proverbs", "Job")
  - `Chapter: "N"` (the chapter/psalm number as a string)
  - `Testament: Old`

## Content Format

Each chapter file follows a consistent structure:

1. **Header**: YAML frontmatter and title (e.g., `# Psalms N`, `# Proverbs N`)
2. **Navigation**: Obsidian-style internal links to previous/next chapters:
   - Psalms: `[[LXX Reference/19 - Psalms/Psalms N|←]] • [[LXX Reference/19 - Psalms/Psalms N|→]]`
   - Proverbs: `[[LXX Reference/20 - Proverbs/Proverbs N|←]] • [[LXX Reference/20 - Proverbs/Proverbs N|→]]`
   - For chapter 1, only the forward arrow is shown
3. **Verses**: Each verse is formatted as:
   - Header: `#### [Book Name] N - V` (where N is chapter number, V is verse number)
   - Content: English glosses with Strong's number references in the format `[[G####|English gloss]]`
   - **IMPORTANT**: Use English glosses/translations in the link text, NOT Greek words

## Strong's Number References

Greek words are tagged with Strong's Concordance numbers (G prefix) linking the Greek text to its semantic meaning. Format: `[[G####|translation/gloss]]`

Examples:
- `[[G2962|The Lord]]` - Strong's G2962 (Kyrios/Lord)
- `[[G3756|not]]` - Strong's G3756 (ou/not)

## File States

Some files are placeholder files (~173 bytes) containing only frontmatter and header, awaiting content to be added.

## Working with This Repository

When editing or creating chapter files:
- Maintain the exact YAML frontmatter structure
- Preserve the navigation link format for Obsidian compatibility
- Use the verse header format `#### [Book Name] N - V`
- Format references as `[[G####|English gloss]]` with double brackets and no spaces inside
- Use English glosses/translations, NOT Greek words
- Keep verse text concise and maintain the interlinear structure

## Adding Content from BibleHub

To populate a chapter with Greek text and Strong's references:

1. **Fetch from BibleHub**: Use the URL pattern `https://biblehub.com/interlinear/apostolic/[book]/[chapter].htm`
   - Example for Proverbs 1: `https://biblehub.com/interlinear/apostolic/proverbs/1.htm`
   - Book names should be lowercase in the URL

2. **Extract data**: From the BibleHub page, extract:
   - Verse numbers
   - Strong's numbers (G#### format)
   - English glosses/translations for each word

3. **Format verses**: Create verse entries as:
   ```
   #### [Book Name] N - V
   [[G####|English gloss]] [[G####|English gloss]] ...
   ```

4. **Important**: Always use the English translation/gloss in the link text, never the Greek word

## Fixing Formatting Issues

### Converting Single Brackets to Double Brackets

If Psalm files have incorrect single-bracket format `[G####|text]` instead of double brackets `[[G####|text]]`, use this process:

1. **Add opening double brackets**:
   ```bash
   perl -i -pe 's/\[G/[[G/g' "Psalms N.md"
   ```

2. **Add closing double brackets**:
   ```bash
   perl -i -pe 's/\|([^\]]+)\]/|$1]]/g' "Psalms N.md"
   ```

3. **Fix navigation links** (removes extra brackets added to arrows):
   ```bash
   perl -i -pe 's/\|←\]\]\]/|←]]/g; s/\|→\]\]\]/|→]]/g' "Psalms N.md"
   ```

### Removing Morphological Codes

Some files may contain morphological codes like `[[G3788|-1473|eyes]]` which should be removed:

1. **Remove simple hyphenated codes**:
   ```bash
   perl -i -pe 's/\[\[G([0-9]+)\|-[0-9]+\|/[[G$1|/g' "Psalms N.md"
   ```

2. **Remove complex codes with decimals** (e.g., `-1510.8.3`):
   ```bash
   perl -i -pe 's/\[\[G([0-9.]+)\|-[0-9.]+\|/[[G$1|/g' "Psalms N.md"
   ```

### Fix Hanging Brackets

Files may have hanging closing brackets (more `]` than `[`) due to various malformed patterns. Common issues include:

**Problem Patterns:**
- Triple closing brackets: `]]]` should be `]]`
- Bracket-comma-bracket: `],]]` should be `,]]`
- Bracket-exclamation-bracket: `]!]]` should be `!]]`
- Bracket-period-bracket: `].]]` should be `.]]`
- Bracket-semicolon-bracket: `];]]` should be `;]]`

**Solution:**

Use this Python script to detect and fix all hanging bracket issues:

```python
#!/usr/bin/env python3
"""Fix hanging closing brackets in LXX files."""

import re
from pathlib import Path

def fix_brackets(file_path):
    """Fix malformed brackets in a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix punctuation patterns: ],]] -> ,]]
    content = re.sub(r'\],\]\]', ',]]', content)
    content = re.sub(r'\]!\]\]', '!]]', content)
    content = re.sub(r'\]\?\]\]', '?]]', content)
    content = re.sub(r'\];\]\]', ';]]', content)
    content = re.sub(r'\]\.\]\]', '.]]', content)

    # Fix any remaining sequences of 3+ closing brackets
    content = re.sub(r'\]{3,}', ']]', content)

    # Write if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process all chapter files in current directory
from pathlib import Path
files = sorted(Path('.').glob('[A-Z]* *.md'))
for file_path in files:
    if fix_brackets(file_path):
        print(f"✓ Fixed: {file_path.name}")
```

**Verification:**

To check for bracket imbalances before/after fixes:

```python
#!/usr/bin/env python3
"""Check files for hanging closing brackets."""

from pathlib import Path

for file_path in sorted(Path('.').glob('[A-Z]* *.md')):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    opening = content.count('[')
    closing = content.count(']')
    diff = closing - opening

    status = "✓ OK" if diff == 0 else f"❌ +{diff} extra ]"
    print(f"{file_path.name:<25} | Opening: {opening:>4} | Closing: {closing:>4} | {status}")
```

**Expected Result:** All files should show "✓ OK" with perfectly balanced brackets.

### Batch Processing Multiple Files

Process multiple Psalm files at once:

```bash
cd "/path/to/LXX Reference/19 - Psalms"
perl -i -pe 's/\[G/[[G/g' "Psalms 114.md" "Psalms 115.md" "Psalms 116.md"
perl -i -pe 's/\|([^\]]+)\]/|$1]]/g' "Psalms 114.md" "Psalms 115.md" "Psalms 116.md"
perl -i -pe 's/\|←\]\]\]/|←]]/g; s/\|→\]\]\]/|→]]/g' "Psalms 114.md" "Psalms 115.md" "Psalms 116.md"
perl -i -pe 's/\[\[G([0-9.]+)\|-[0-9.]+\|/[[G$1|/g' "Psalms 114.md" "Psalms 115.md" "Psalms 116.md"
```

### Verification

After formatting corrections, verify the output matches the standard format:
- Strong's references: `[[G####|text]]` (double brackets, no morphological codes)
- Navigation links: `[[LXX Reference/19 - Psalms/Psalms N|←]]` (proper arrow symbols)
- No trailing spaces or malformed brackets

## File Cleanup

This section documents comprehensive cleanup procedures for fixing common formatting issues in LXX files.

### Step 1: Remove Word Order Indicators

Files may contain word order indicators (numbers like `[ 2`, `1`, etc.) embedded in Strong's reference link text. These should be removed.

**Problem Patterns:**
- `[[G####|[ N text]]` → should be `[[G####|text]]`
- `[[G####|N text]]` → should be `[[G####|text]]`

**Solution:**

```python
#!/usr/bin/env python3
"""Fix word order indicators in files."""

import re
from pathlib import Path

def fix_word_order_numbers(content):
    """Remove word order indicators from Strong's references."""

    # Pattern 1: [[G####|[ N text]] → [[G####|text]]
    # Matches: [ followed by digit(s) and space at start of link text
    content = re.sub(r'\[\[G(\d+)\|\[\s*\d+\s+', r'[[G\1|', content)

    # Pattern 2: [[G####|N text]] → [[G####|text]]
    # Matches: digit(s) and space at start of link text (not after [)
    content = re.sub(r'\[\[G(\d+)\|(\d+)\s+', r'[[G\1|', content)

    return content

def process_file(file_path):
    """Process a single file to fix formatting."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    content = fix_word_order_numbers(content)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process all chapter files in current directory
for file_path in sorted(Path('.').glob('[A-Z]* *.md')):
    if process_file(file_path):
        print(f"✓ Fixed: {file_path.name}")
```

### Step 2: Remove HTML Entities

Files fetched from BibleHub may contain HTML numeric entities (like `&#8212;` for em-dash, `&#160;` for non-breaking space) that should be removed.

**Problem Patterns:**
- `[[G####|text &#8212;]]` → should be `[[G####|text]]`
- `[[G####|text&#160;more]]` → should be `[[G####|text more]]`

**Solution:**

```python
#!/usr/bin/env python3
"""Remove HTML entities from files."""

import re
from pathlib import Path

def remove_html_entities(file_path):
    """Remove HTML entities like &#8212; from file content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove HTML numeric entities (e.g., &#8212;, &#160;, etc.)
    content = re.sub(r'&#\d+;', '', content)

    # Clean up any double spaces that may result
    content = re.sub(r'  +', ' ', content)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process all chapter files in current directory
for file_path in sorted(Path('.').glob('[A-Z]* *.md')):
    if remove_html_entities(file_path):
        print(f"✓ Fixed: {file_path.name}")
```

### Step 3: Fix Bracket Imbalances

After removing word order indicators, files may have bracket imbalances caused by:
- Leftover opening brackets: `[[G####|[text]]` → should be `[[G####|text]]`
- Extra closing brackets in punctuation patterns: `]]]`, `],]]`, `].]]`, etc.

**Check for Imbalances:**

```python
#!/usr/bin/env python3
"""Check files for bracket imbalances."""

from pathlib import Path

for file_path in sorted(Path('.').glob('[A-Z]* *.md')):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    opening = content.count('[')
    closing = content.count(']')
    diff = closing - opening

    status = "✓ OK" if diff == 0 else f"❌ +{diff} extra ]" if diff > 0 else f"❌ {abs(diff)} missing ]"
    print(f"{file_path.name:<25} | Opening: {opening:>4} | Closing: {closing:>4} | {status}")
```

**Fix Imbalances:**

```python
#!/usr/bin/env python3
"""Fix bracket imbalances."""

import re
from pathlib import Path

def fix_brackets(file_path):
    """Fix malformed brackets in a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Fix punctuation patterns: ],]] -> ,]]
    content = re.sub(r'\],\]\]', ',]]', content)
    content = re.sub(r'\]!\]\]', '!]]', content)
    content = re.sub(r'\]\?\]\]', '?]]', content)
    content = re.sub(r'\];\]\]', ';]]', content)
    content = re.sub(r'\]\.\]\]', '.]]', content)
    content = re.sub(r'\]:\]\]', ':]]', content)

    # Fix any remaining sequences of 3+ closing brackets
    content = re.sub(r'\]{3,}', ']]', content)

    # Write if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process affected files
for file_path in sorted(Path('.').glob('[A-Z]* *.md')):
    if fix_brackets(file_path):
        print(f"✓ Fixed: {file_path.name}")
```

### Step 4: Manual Fixes for Remaining Issues

After automated fixes, some files may still have imbalances that require manual correction:

**Find Specific Issues:**

```python
#!/usr/bin/env python3
"""Find exact locations of bracket mismatches."""

import re
from pathlib import Path

def find_bracket_issues(file_path):
    """Find lines with bracket issues."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    issues = []

    for i, line in enumerate(lines, 1):
        # Skip frontmatter and headers
        if line.startswith('---') or line.startswith('#') or line.strip() == '':
            continue

        opening = line.count('[')
        closing = line.count(']')

        if opening != closing:
            issues.append((i, line.strip(), f"Opening: {opening}, Closing: {closing}"))

    return issues

# Check problem files
for file_path in sorted(Path('.').glob('[A-Z]* *.md')):
    issues = find_bracket_issues(file_path)
    if issues:
        print(f"\n{file_path.name}:")
        for line_num, text, count in issues:
            print(f"  Line {line_num}: {count}")
            print(f"    {text[:80]}...")
```

**Common Manual Fixes:**
- `[[G####|[text]]` → `[[G####|text]]` (leftover opening bracket in link text)
- `text]].` → `text.` (extra closing bracket before punctuation)
- Missing closing brackets in truncated text

### Step 5: Final Verification

After all fixes, run the bracket check again to ensure all files are balanced:

```bash
python3 check_brackets.py | grep -v "✓ OK"
```

**Expected Result:** Empty output (all files pass)

**Delete temporary scripts:**

```bash
rm check_brackets.py fix_brackets.py find_bracket_issues.py fix_word_order.py
```

### Complete Workflow Example

For a batch cleanup of Genesis files:

```bash
cd "/path/to/LXX Reference/1 - Genesis"

# Step 1: Remove word order indicators
python3 fix_word_order.py

# Step 2: Remove HTML entities
python3 remove_html_entities.py

# Step 3: Check for bracket imbalances
python3 check_brackets.py | grep "❌"

# Step 4: Fix automated bracket issues
python3 fix_brackets.py

# Step 5: Find remaining issues
python3 find_bracket_issues.py

# Step 6: Make manual corrections using Edit tool
# Fix any remaining issues identified in Step 5

# Step 7: Final verification
python3 check_brackets.py

# Step 8: Clean up temporary scripts
rm *.py
```

## File Generation

This section documents how to generate or regenerate chapter files from BibleHub's Apostolic Bible Polyglot interlinear pages.

### Overview

When chapter files have incorrect information or need to be created from scratch, use BibleHub as the authoritative source. The Apostolic Bible Polyglot provides Greek Septuagint text with Strong's concordance numbers and English glosses.

**Source URL Pattern**: `https://biblehub.com/interlinear/apostolic/{book}/{chapter}.htm`

Example: `https://biblehub.com/interlinear/apostolic/genesis/15.htm`

### Step 1: Create the BibleHub Fetcher Script

```python
#!/usr/bin/env python3
"""Fetch and format chapters from BibleHub Interlinear."""

import re
import subprocess
import time
from pathlib import Path

def fetch_chapter(book, chapter):
    """Fetch a chapter from BibleHub."""
    url = f"https://biblehub.com/interlinear/apostolic/{book.lower()}/{chapter}.htm"

    try:
        result = subprocess.run(
            ['curl', '-s', url],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout
    except Exception as e:
        print(f"Error fetching {book} {chapter}: {e}")
        return None

def clean_english_text(text):
    """Clean English text from HTML markup."""
    # Remove span class="num" content (word order numbers in brackets)
    text = re.sub(r'<span class="num">.*?</span>', '', text)
    # Remove italic spans but keep content
    text = re.sub(r'<span class="ital">([^<]+)</span>', r'\1', text)
    # Remove small caps spans but keep content
    text = re.sub(r'<span class="smcap">([^<]+)</span>', r'\1', text)
    # Remove remaining span tags
    text = re.sub(r'</?span[^>]*>', '', text)
    # Convert &nbsp; to space
    text = text.replace('&nbsp;', ' ')
    # Clean up whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_biblehub_html(html):
    """Parse BibleHub HTML and extract verses with Strong's numbers."""
    verses = {}

    # Find all table.tablefloat entries
    tables = re.findall(r'<table class="tablefloat">.*?</table>', html, re.DOTALL)

    current_verse = None

    for table in tables:
        # Extract verse number from reftop span (e.g., "15:3")
        verse_match = re.search(r'<span class="reftop">(\d+):(\d+)', table)
        if verse_match:
            current_verse = verse_match.group(2)  # Just the verse number
            if current_verse not in verses:
                verses[current_verse] = []

        # Skip if we don't have a current verse
        if not current_verse:
            continue

        # Check for asterisk (proper name without Strong's number)
        if '<span class="strongs">*</span>' in table:
            # Extract English text
            eng_match = re.search(r'<span class="eng">([^<]+(?:<[^>]+>[^<]*</[^>]+>[^<]*)*)</span>', table, re.DOTALL)
            if eng_match:
                english = clean_english_text(eng_match.group(1))
                if english and english.strip():
                    # For proper names, don't add Strong's number
                    verses[current_verse].append(english)
            continue

        # Extract Strong's number
        strongs_match = re.search(r'strongsnumbers\.com/greek/([\d.-]+)\.htm', table)
        if not strongs_match:
            continue

        # Get the first number from the Strong's reference (ignore hyphens and decimals)
        strongs_full = strongs_match.group(1)
        strongs_base = re.split(r'[-.]', strongs_full)[0]
        strongs = f"G{strongs_base.zfill(4)}"

        # Extract English gloss
        eng_match = re.search(r'<span class="eng">([^<]+(?:<[^>]+>[^<]*</[^>]+>[^<]*)*)</span>', table, re.DOTALL)
        if eng_match:
            english = clean_english_text(eng_match.group(1))

            if english and english.strip():
                verses[current_verse].append(f"[[{strongs}|{english}]]")

    return verses

def format_chapter_content(book, chapter, verses):
    """Format chapter content according to vault standards."""

    # Calculate previous and next chapter numbers
    prev_ch = chapter - 1 if chapter > 1 else 1
    next_ch = chapter + 1

    # Build frontmatter
    content = f"""---
cssClasses: lxx
Book: {book}
Chapter: "{chapter}"
Testament: Old
---

# {book} {chapter}

[[LXX Reference/1 - {book}/{book} {prev_ch}|←]] • [[LXX Reference/1 - {book}/{book} {next_ch}|→]]

---

"""

    # Add verses
    for verse_num in sorted(verses.keys(), key=lambda x: int(x)):
        words = verses[verse_num]
        if words:  # Only add if verse has content
            content += f"#### {book} {chapter} - {verse_num}\n"
            content += " ".join(words) + "\n\n"

    return content.rstrip() + "\n"

def update_chapter_file(book, chapter):
    """Fetch and update a chapter file."""
    print(f"  {book} {chapter}...", end=" ", flush=True)

    # Fetch from BibleHub
    html = fetch_chapter(book, chapter)
    if not html:
        print("❌ Failed to fetch")
        return False

    # Parse HTML
    verses = parse_biblehub_html(html)
    if not verses:
        print("❌ No verses found")
        return False

    # Format content
    content = format_chapter_content(book, chapter, verses)

    # Write to file
    file_path = Path(f"{book} {chapter}.md")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    verse_count = len(verses)
    word_count = sum(len(words) for words in verses.values())
    print(f"✓ ({verse_count} verses, {word_count} words)")
    return True

# Main execution
if __name__ == "__main__":
    book = "Genesis"
    start_chapter = 15
    end_chapter = 30

    print(f"Updating {book} {start_chapter}-{end_chapter} from BibleHub\n")
    print("=" * 60)

    successful = 0
    failed = 0

    for chapter in range(start_chapter, end_chapter + 1):
        if update_chapter_file(book, chapter):
            successful += 1
        else:
            failed += 1

        # Brief pause to be respectful to the server
        time.sleep(0.5)

    print("=" * 60)
    print(f"\n✓ Complete! {successful} chapters updated successfully")
    if failed > 0:
        print(f"⚠️  {failed} chapters failed")
```

### Step 2: Run the Fetcher Script

```bash
cd "/path/to/LXX Reference/1 - Genesis"
python3 update_chapters.py
```

**Expected output**: Each chapter will be fetched, parsed, and written to disk with verse count and word count confirmation.

### Step 3: Fix Bracket Issues

The initial fetch may include brackets from BibleHub's word order indicators. Fix these with:

```python
#!/usr/bin/env python3
"""Fix brackets in English glosses."""

import re
from pathlib import Path

def fix_file(file_path):
    """Remove brackets from English glosses."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Pattern: [[G####|[text]]] -> [[G####|text]]
    content = re.sub(r'\[\[G(\d+)\|\[([^\]]+)\]\]\]', r'[[G\1|\2]]', content)

    # Pattern: [[G####|text [ more]] -> [[G####|text more]]
    content = re.sub(r'(\[\[G\d+\|[^\]]*)\[([^\]]*\]\])', r'\1\2', content)

    # Pattern: [[G####|text ] more]] -> [[G####|text more]]
    content = re.sub(r'(\[\[G\d+\|[^\]]*)\]([^\]]*\]\])', r'\1\2', content)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Process files
for chapter in range(15, 31):
    file_path = Path(f'Genesis {chapter}.md')
    if file_path.exists():
        if fix_file(file_path):
            print(f"✓ Fixed Genesis {chapter}.md")
```

### Step 4: Verify Generated Files

```python
#!/usr/bin/env python3
"""Verify generated chapter files."""

from pathlib import Path

print("Verifying chapters...\n")

for chapter in range(15, 31):
    file_path = Path(f'Genesis {chapter}.md')

    if not file_path.exists():
        print(f"❌ Genesis {chapter}.md - File not found")
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    opening = content.count('[')
    closing = content.count(']')
    diff = closing - opening

    # Check for content
    has_strongs = '[[G' in content
    line_count = len(content.splitlines())

    if diff == 0 and has_strongs and line_count > 20:
        print(f"✓ Genesis {chapter}.md - OK ({line_count} lines, {opening//2} links)")
    else:
        issues = []
        if diff != 0:
            issues.append(f"brackets off by {diff}")
        if not has_strongs:
            issues.append("no Strong's refs")
        if line_count < 20:
            issues.append("too short")
        print(f"⚠️  Genesis {chapter}.md - {', '.join(issues)}")
```

### Step 5: Clean Up

```bash
rm update_chapters.py fix_brackets.py verify_chapters.py
```

### Key Points

**HTML Structure Understanding**:
- BibleHub uses `<table class="tablefloat">` for each word
- Verse numbers appear in `<span class="reftop">15:3</span>`
- Strong's numbers in links: `strongsnumbers.com/greek/2532.htm`
- English glosses in `<span class="eng">...</span>`
- Proper names marked with `<span class="strongs">*</span>`
- Word order indicators in `<span class="num">` (must be removed)

**Important Patterns**:
- Combined Strong's numbers: `3326-1161` → use first number only (`3326`)
- Decimal Strong's numbers: `1510.8.3` → use base number only (`1510`)
- Italicized text: Keep content, remove `<span class="ital">` tags
- Small caps (LORD): Keep content, remove `<span class="smcap">` tags

**Output Format**:
```markdown
#### Genesis 15 - 1
[[G3326|And after]] [[G3588|the]] [[G4487|words]] [[G3778|these]] ...
```

**Verification Targets**:
- ✓ Balanced brackets: `[` count = `]` count
- ✓ Strong's references present: Contains `[[G####|text]]` patterns
- ✓ Substantial content: More than 20 lines per chapter
- ✓ No embedded brackets: No `[[G####|text [ more]]` patterns

### Troubleshooting

**No verses found**: Check if BibleHub URL structure has changed or if the book name is incorrect (must be lowercase).

**Bracket imbalances**: Run the bracket fix script multiple times, checking different patterns.

**Missing proper names**: Proper names appear without Strong's numbers on BibleHub (marked with `*`). These should be included as plain text.

**Rate limiting**: If fetching many chapters, include `time.sleep(0.5)` between requests to be respectful to BibleHub's servers.
