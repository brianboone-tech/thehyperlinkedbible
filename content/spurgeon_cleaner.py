#!/usr/bin/env python3
"""
Spurgeon Sermon Cleaner - Automated Processing Script

This script automates Steps 2, 4, and 5 of the Spurgeon Sermon Cleaner:
- Step 2: Fix the Main Text (look up in Readable Bible, format with link)
- Step 4: Apply Color (scripture quotes → blue, hymns → teal)
- Step 5: Add Inline Links (parse references, create Readable Bible links)

Step 3 (Write Summary) requires human/AI input and is NOT automated.
"""

import re
import os
from pathlib import Path

# Book name to number mapping
BOOK_MAP = {
    'genesis': ('01', 'Genesis'), 'gen': ('01', 'Genesis'),
    'exodus': ('02', 'Exodus'), 'exod': ('02', 'Exodus'), 'ex': ('02', 'Exodus'),
    'leviticus': ('03', 'Leviticus'), 'lev': ('03', 'Leviticus'),
    'numbers': ('04', 'Numbers'), 'num': ('04', 'Numbers'),
    'deuteronomy': ('05', 'Deuteronomy'), 'deut': ('05', 'Deuteronomy'),
    'joshua': ('06', 'Joshua'), 'josh': ('06', 'Joshua'),
    'judges': ('07', 'Judges'), 'judg': ('07', 'Judges'),
    'ruth': ('08', 'Ruth'),
    '1 samuel': ('09', '1 Samuel'), '1samuel': ('09', '1 Samuel'), '1 sam': ('09', '1 Samuel'), '1sam': ('09', '1 Samuel'),
    '2 samuel': ('10', '2 Samuel'), '2samuel': ('10', '2 Samuel'), '2 sam': ('10', '2 Samuel'), '2sam': ('10', '2 Samuel'),
    '1 kings': ('11', '1 Kings'), '1kings': ('11', '1 Kings'), '1 kgs': ('11', '1 Kings'),
    '2 kings': ('12', '2 Kings'), '2kings': ('12', '2 Kings'), '2 kgs': ('12', '2 Kings'),
    '1 chronicles': ('13', '1 Chronicles'), '1chronicles': ('13', '1 Chronicles'), '1 chron': ('13', '1 Chronicles'), '1 chr': ('13', '1 Chronicles'),
    '2 chronicles': ('14', '2 Chronicles'), '2chronicles': ('14', '2 Chronicles'), '2 chron': ('14', '2 Chronicles'), '2 chr': ('14', '2 Chronicles'),
    'ezra': ('15', 'Ezra'),
    'nehemiah': ('16', 'Nehemiah'), 'neh': ('16', 'Nehemiah'),
    'esther': ('17', 'Esther'), 'esth': ('17', 'Esther'),
    'job': ('18', 'Job'),
    'psalms': ('19', 'Psalms'), 'psalm': ('19', 'Psalms'), 'ps': ('19', 'Psalms'), 'psa': ('19', 'Psalms'),
    'proverbs': ('20', 'Proverbs'), 'prov': ('20', 'Proverbs'),
    'ecclesiastes': ('21', 'Ecclesiastes'), 'eccl': ('21', 'Ecclesiastes'), 'eccles': ('21', 'Ecclesiastes'),
    'song of solomon': ('22', 'Song of Solomon'), 'song': ('22', 'Song of Solomon'), 'songs': ('22', 'Song of Solomon'), 'canticles': ('22', 'Song of Solomon'),
    'isaiah': ('23', 'Isaiah'), 'isa': ('23', 'Isaiah'),
    'jeremiah': ('24', 'Jeremiah'), 'jer': ('24', 'Jeremiah'),
    'lamentations': ('25', 'Lamentations'), 'lam': ('25', 'Lamentations'),
    'ezekiel': ('26', 'Ezekiel'), 'ezek': ('26', 'Ezekiel'),
    'daniel': ('27', 'Daniel'), 'dan': ('27', 'Daniel'),
    'hosea': ('28', 'Hosea'), 'hos': ('28', 'Hosea'),
    'joel': ('29', 'Joel'),
    'amos': ('30', 'Amos'),
    'obadiah': ('31', 'Obadiah'), 'obad': ('31', 'Obadiah'),
    'jonah': ('32', 'Jonah'), 'jon': ('32', 'Jonah'),
    'micah': ('33', 'Micah'), 'mic': ('33', 'Micah'),
    'nahum': ('34', 'Nahum'), 'nah': ('34', 'Nahum'),
    'habakkuk': ('35', 'Habakkuk'), 'hab': ('35', 'Habakkuk'),
    'zephaniah': ('36', 'Zephaniah'), 'zeph': ('36', 'Zephaniah'),
    'haggai': ('37', 'Haggai'), 'hag': ('37', 'Haggai'),
    'zechariah': ('38', 'Zechariah'), 'zech': ('38', 'Zechariah'),
    'malachi': ('39', 'Malachi'), 'mal': ('39', 'Malachi'),
    'matthew': ('40', 'Matthew'), 'matt': ('40', 'Matthew'), 'mt': ('40', 'Matthew'),
    'mark': ('41', 'Mark'), 'mk': ('41', 'Mark'),
    'luke': ('42', 'Luke'), 'lk': ('42', 'Luke'),
    'john': ('43', 'John'), 'jn': ('43', 'John'),
    'acts': ('44', 'Acts'),
    'romans': ('45', 'Romans'), 'rom': ('45', 'Romans'),
    '1 corinthians': ('46', '1 Corinthians'), '1corinthians': ('46', '1 Corinthians'), '1 cor': ('46', '1 Corinthians'), '1cor': ('46', '1 Corinthians'),
    '2 corinthians': ('47', '2 Corinthians'), '2corinthians': ('47', '2 Corinthians'), '2 cor': ('47', '2 Corinthians'), '2cor': ('47', '2 Corinthians'),
    'galatians': ('48', 'Galatians'), 'gal': ('48', 'Galatians'),
    'ephesians': ('49', 'Ephesians'), 'eph': ('49', 'Ephesians'),
    'philippians': ('50', 'Philippians'), 'phil': ('50', 'Philippians'),
    'colossians': ('51', 'Colossians'), 'col': ('51', 'Colossians'),
    '1 thessalonians': ('52', '1 Thessalonians'), '1thessalonians': ('52', '1 Thessalonians'), '1 thess': ('52', '1 Thessalonians'), '1thess': ('52', '1 Thessalonians'),
    '2 thessalonians': ('53', '2 Thessalonians'), '2thessalonians': ('53', '2 Thessalonians'), '2 thess': ('53', '2 Thessalonians'), '2thess': ('53', '2 Thessalonians'),
    '1 timothy': ('54', '1 Timothy'), '1timothy': ('54', '1 Timothy'), '1 tim': ('54', '1 Timothy'), '1tim': ('54', '1 Timothy'),
    '2 timothy': ('55', '2 Timothy'), '2timothy': ('55', '2 Timothy'), '2 tim': ('55', '2 Timothy'), '2tim': ('55', '2 Timothy'),
    'titus': ('56', 'Titus'), 'tit': ('56', 'Titus'),
    'philemon': ('57', 'Philemon'), 'phlm': ('57', 'Philemon'), 'phm': ('57', 'Philemon'),
    'hebrews': ('58', 'Hebrews'), 'heb': ('58', 'Hebrews'),
    'james': ('59', 'James'), 'jas': ('59', 'James'),
    '1 peter': ('60', '1 Peter'), '1peter': ('60', '1 Peter'), '1 pet': ('60', '1 Peter'), '1pet': ('60', '1 Peter'),
    '2 peter': ('61', '2 Peter'), '2peter': ('61', '2 Peter'), '2 pet': ('61', '2 Peter'), '2pet': ('61', '2 Peter'),
    '1 john': ('62', '1 John'), '1john': ('62', '1 John'), '1 jn': ('62', '1 John'),
    '2 john': ('63', '2 John'), '2john': ('63', '2 John'), '2 jn': ('63', '2 John'),
    '3 john': ('64', '3 John'), '3john': ('64', '3 John'), '3 jn': ('64', '3 John'),
    'jude': ('65', 'Jude'),
    'revelation': ('66', 'Revelation'), 'rev': ('66', 'Revelation'),
}

# For Psalms, use "Psalm" not "Psalms" in file names
def get_book_folder_and_file(book_num, book_name, chapter):
    """Get the correct folder and file name for a book/chapter."""
    if book_name == 'Psalms':
        folder = f"{book_num} - Psalms"
        file_name = f"Psalm {chapter}"
    else:
        folder = f"{book_num} - {book_name}"
        file_name = f"{book_name} {chapter}"
    return folder, file_name

def parse_reference(ref_text):
    """
    Parse a scripture reference like 'Malachi 3:6' or 'Genesis 2:17' or 'Psalm 23:1'
    Returns (book_num, book_name, chapter, verse, verse_end) or None
    """
    # Clean up the reference
    ref_text = ref_text.strip()
    ref_text = ref_text.replace('.', ':')  # Handle "Malachi 3.6" format

    # Pattern for book chapter:verse or book chapter:verse-verse_end
    pattern = r'^(\d?\s*[A-Za-z]+(?:\s+of\s+[A-Za-z]+)?)\s*(\d+)[:\s]+(\d+)(?:\s*[-–—]\s*(\d+))?'
    match = re.match(pattern, ref_text)

    if not match:
        return None

    book_raw = match.group(1).strip().lower()
    chapter = match.group(2)
    verse = match.group(3)
    verse_end = match.group(4) if match.group(4) else None

    # Look up book
    if book_raw in BOOK_MAP:
        book_num, book_name = BOOK_MAP[book_raw]
        return (book_num, book_name, chapter, verse, verse_end)

    return None

def build_readable_bible_link(book_num, book_name, chapter, verse, display_text=None, verse_end=None):
    """Build a Readable Bible link with proper format."""
    folder, file_name = get_book_folder_and_file(book_num, book_name, chapter)
    anchor = f"{file_name} . {verse}"

    if display_text is None:
        if verse_end:
            display_text = f"{book_name} {chapter}:{verse}–{verse_end}"
        else:
            display_text = f"{book_name} {chapter}:{verse}"

    return f"[[Readable Bible/{folder}/{file_name}#{anchor}|{display_text}]]"

def get_verse_text(readable_bible_path, book_num, book_name, chapter, verse):
    """Look up the actual verse text from the Readable Bible."""
    folder, file_name = get_book_folder_and_file(book_num, book_name, chapter)
    file_path = os.path.join(readable_bible_path, folder, f"{file_name}.md")

    if not os.path.exists(file_path):
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the verse heading
        anchor_pattern = f"##### {file_name} . {verse}"

        # Find the line with this heading
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.strip().startswith(anchor_pattern):
                # Next line has the verse content
                if i + 1 < len(lines):
                    verse_line = lines[i + 1]
                    # Remove the Reference Bible link prefix and any trailing links
                    # Format: [[Reference Bible/path#anchor|verse_num]] text | [[links...]]
                    # We want to extract just the text part

                    # Remove leading Reference Bible link (the verse number is inside the link)
                    verse_line = re.sub(r'^\[\[Reference Bible[^\]]+\|[^\]]+\]\]\s*', '', verse_line)

                    # Remove trailing links (| [[...]])
                    verse_line = re.sub(r'\s*\|\s*\[\[[^\]]+\]\].*$', '', verse_line)

                    return verse_line.strip()
        return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def detect_hymn_stanzas(content):
    """
    Detect hymn stanzas in the content.
    Hymns are typically:
    - Short lines (poetry)
    - Multiple consecutive short lines
    - Often in quotation marks or italics
    """
    lines = content.split('\n')
    hymn_blocks = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Check if this looks like the start of a hymn stanza
        # Characteristics: short line, possibly quoted, followed by similar lines
        if len(line) > 0 and len(line) < 60:
            # Check if it's a short poetic line (not a paragraph)
            # Look for patterns like lines starting with quotes and being short
            if (line.startswith('"') or line.startswith("'") or
                line.startswith('"') or line.startswith("'")):

                # Check next few lines
                stanza_lines = [i]
                j = i + 1
                while j < len(lines) and j < i + 10:
                    next_line = lines[j].strip()
                    # Empty line between stanza lines is OK
                    if next_line == '':
                        j += 1
                        continue
                    # Short poetic lines
                    if len(next_line) > 0 and len(next_line) < 60:
                        stanza_lines.append(j)
                        j += 1
                    else:
                        break

                # If we found 2+ short lines together, it's likely a hymn
                if len(stanza_lines) >= 2:
                    hymn_blocks.append(stanza_lines)
                    i = j
                    continue

        i += 1

    return hymn_blocks

def apply_teal_to_hymns(content):
    """Apply teal color to detected hymn stanzas."""
    # This is a simplified approach - detect quoted poetic blocks
    # Pattern: lines starting with quotes that are short (poetry-like)

    lines = content.split('\n')
    result_lines = []
    in_hymn = False
    hymn_buffer = []

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Detect hymn start: short quoted line
        if (not in_hymn and
            len(stripped) > 0 and len(stripped) < 70 and
            (stripped.startswith('"') or stripped.startswith("'") or
             stripped.startswith('"') or stripped.startswith("'"))):

            # Look ahead - is next non-empty line also short?
            next_idx = i + 1
            while next_idx < len(lines) and lines[next_idx].strip() == '':
                next_idx += 1

            if next_idx < len(lines):
                next_line = lines[next_idx].strip()
                if len(next_line) > 0 and len(next_line) < 70:
                    # Likely start of hymn
                    in_hymn = True
                    hymn_buffer = [line]
                    continue

        if in_hymn:
            if stripped == '':
                hymn_buffer.append(line)
            elif len(stripped) < 70:
                hymn_buffer.append(line)
            else:
                # End of hymn - apply teal color
                hymn_text = '\n'.join(hymn_buffer)
                # Only apply teal if not already colored
                if '<span style="color:' not in hymn_text:
                    hymn_text = f'<span style="color: #008080;">{hymn_text}</span>'
                result_lines.append(hymn_text)
                result_lines.append(line)
                in_hymn = False
                hymn_buffer = []
                continue
        else:
            result_lines.append(line)

    # Handle any remaining hymn buffer
    if hymn_buffer:
        hymn_text = '\n'.join(hymn_buffer)
        if '<span style="color:' not in hymn_text:
            hymn_text = f'<span style="color: #008080;">{hymn_text}</span>'
        result_lines.append(hymn_text)

    return '\n'.join(result_lines)

def find_scripture_quotes_with_refs(content):
    """
    Find scripture quotations that have references nearby.
    Returns list of (quote_start, quote_end, reference) tuples.
    """
    # Pattern for quoted text followed by reference
    # E.g., "quoted text"—Reference or "quoted text" (Reference)
    patterns = [
        # "quote"—Book ch:v or "quote"—Book ch:v.
        r'"([^"]+)"[—–-]\s*([1-3]?\s*[A-Za-z]+(?:\s+of\s+[A-Za-z]+)?\s*\d+[:\.\s]\d+(?:\s*[-–—]\s*\d+)?)',
        r'"([^"]+)"[—–-]\s*([1-3]?\s*[A-Za-z]+(?:\s+of\s+[A-Za-z]+)?\s*\d+[:\.\s]\d+(?:\s*[-–—]\s*\d+)?)',
        # "quote" Book ch:v
        r'"([^"]+)"\s+([1-3]?\s*[A-Za-z]+(?:\s+of\s+[A-Za-z]+)?\s*\d+[:\.\s]\d+)',
    ]

    quotes = []
    for pattern in patterns:
        for match in re.finditer(pattern, content):
            quote_text = match.group(1)
            ref_text = match.group(2)
            quotes.append((match.start(), match.end(), quote_text, ref_text, match.group(0)))

    return quotes

def process_sermon(file_path, readable_bible_path, dry_run=False):
    """
    Process a single sermon file.

    Steps:
    1. Parse the Text section and identify the scripture reference
    2. Look up verse text in Readable Bible
    3. Format Text section with link and blue color
    4. Detect and color hymn stanzas (teal)
    5. Detect scripture quotes and add blue color + links

    Returns: (modified, changes_description)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Error reading file: {e}"

    original_content = content
    changes = []

    # Step 2: Fix the Main Text section
    # Find the Text section
    text_section_match = re.search(
        r'(##### Text\n\*[^\n]+\*)\n',
        content
    )

    if text_section_match:
        text_section = text_section_match.group(1)

        # Check if it already has a Readable Bible link
        if '[[Readable Bible' not in text_section:
            ref_match = None
            ref_text = None

            # Check if this is a placeholder format: *[Scripture Reference]*
            if '[Scripture Reference]' in text_section:
                # Look for the reference in the first paragraph after the Text section
                # It's usually the first line after "---" that contains a quote with reference
                body_start = content.find(text_section) + len(text_section)
                body_section = content[body_start:body_start + 1000]

                # Look for a quoted line with reference at the start of the body
                # Pattern: "quoted text"—Book ch:v or "quoted text."—Book ch:v
                # Unicode quotes: " U+201C, " U+201D, straight quotes: "
                body_ref_match = re.search(
                    r'["\u201c][^"\u201d]+["\u201d]\s*[—–\-\u2014]\s*([1-3]?\s*[A-Za-z]+(?:\s+of\s+[A-Za-z]+)?(?:\.\s*|\s+)\d+[:\.\s]\d+(?:\s*[-–—]\s*\d+)?)',
                    body_section
                )
                if body_ref_match:
                    ref_text = body_ref_match.group(1)
            else:
                # Extract the reference from the text section
                # Pattern: *"text"—Reference.* or similar
                ref_match = re.search(
                    r'[—–-]\s*([1-3]?\s*[A-Za-z]+(?:\.\s*|\s+)\d+[:\.\s]\d+(?:\s*[-–—]\s*\d+)?)',
                    text_section
                )
                if ref_match:
                    ref_text = ref_match.group(1)

            if ref_text:
                parsed = parse_reference(ref_text)

                if parsed:
                    book_num, book_name, chapter, verse, verse_end = parsed

                    # Get the verse text from Readable Bible
                    verse_text = get_verse_text(readable_bible_path, book_num, book_name, chapter, verse)

                    if verse_text:
                        # Build the new Text section
                        link = build_readable_bible_link(book_num, book_name, chapter, verse,
                                                        verse_end=verse_end)

                        # Format reference for display
                        if book_name == 'Psalms':
                            display_ref = f"Psalm {chapter}:{verse}"
                        else:
                            display_ref = f"{book_name} {chapter}:{verse}"
                        if verse_end:
                            display_ref += f"–{verse_end}"

                        new_text_section = f'##### Text\n*<span style="color: #1e90ff;">"{verse_text}"</span>—{link}.*'

                        content = content.replace(text_section, new_text_section)
                        changes.append(f"Fixed Text section with Readable Bible link to {display_ref}")

    # Step 4 & 5: This is more complex and requires careful pattern matching
    # For now, we'll focus on the most common patterns

    # Find scripture quotes with references and add links
    quotes = find_scripture_quotes_with_refs(content)

    for quote_info in quotes:
        start, end, quote_text, ref_text, full_match = quote_info
        parsed = parse_reference(ref_text)

        if parsed:
            book_num, book_name, chapter, verse, verse_end = parsed
            link = build_readable_bible_link(book_num, book_name, chapter, verse, verse_end=verse_end)

            # Check if already has color
            if '<span style="color:' not in full_match:
                # Build replacement with blue color and link
                new_text = f'<span style="color: #1e90ff;">"{quote_text}"</span> {link}'
                content = content.replace(full_match, new_text)
                changes.append(f"Added blue color and link for {ref_text}")

    # Check if content was modified
    if content != original_content:
        if not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        return True, changes

    return False, ["No changes needed"]

def process_volume(volume_path, readable_bible_path, dry_run=False):
    """Process all sermons in a volume folder."""
    results = {
        'processed': 0,
        'modified': 0,
        'errors': [],
        'changes': []
    }

    if not os.path.exists(volume_path):
        results['errors'].append(f"Volume path not found: {volume_path}")
        return results

    for filename in sorted(os.listdir(volume_path)):
        if filename.endswith('.md') and filename[0].isdigit():
            file_path = os.path.join(volume_path, filename)
            results['processed'] += 1

            modified, changes = process_sermon(file_path, readable_bible_path, dry_run)

            if modified:
                results['modified'] += 1
                results['changes'].append({
                    'file': filename,
                    'changes': changes
                })

    return results

def main():
    """Main entry point."""
    import sys

    base_path = r"C:\Obsidian Vaults\thehyperlinkedbible\content"
    readable_bible_path = os.path.join(base_path, "Readable Bible")
    spurgeon_path = os.path.join(base_path, "Books - Public", "C.H. Spurgeon")

    # Volumes to process
    volumes = [
        "Volume 01 - New Park Street Pulpit (1855)",
        "Volume 02 - New Park Street Pulpit (1856)",
        "Volume 03 - New Park Street Pulpit (1857)",
        "Volume 04 - New Park Street Pulpit (1858)",
        "Volume 05 - New Park Street Pulpit (1859)",
        "Volume 06 - New Park Street Pulpit (1860)",
        "Volume 07 - Metropolitan Tabernacle Pulpit (1861)",
        "Volume 08 - Metropolitan Tabernacle Pulpit (1862)",
        "Volume 09 - Metropolitan Tabernacle Pulpit (1863)",
        "Volume 10 - Metropolitan Tabernacle Pulpit (1864)",
        "Volume 11 - Metropolitan Tabernacle Pulpit (1865)",
    ]

    # Check for dry-run flag
    dry_run = '--dry-run' in sys.argv

    if dry_run:
        print("DRY RUN MODE - No files will be modified")

    total_processed = 0
    total_modified = 0

    for volume in volumes:
        volume_path = os.path.join(spurgeon_path, volume)
        print(f"\n{'='*60}")
        print(f"Processing: {volume}")
        print(f"{'='*60}")

        results = process_volume(volume_path, readable_bible_path, dry_run)

        total_processed += results['processed']
        total_modified += results['modified']

        print(f"  Processed: {results['processed']} sermons")
        print(f"  Modified: {results['modified']} sermons")

        if results['errors']:
            for error in results['errors']:
                print(f"  ERROR: {error}")

        # Show first few changes as examples
        for change in results['changes'][:3]:
            print(f"  - {change['file']}: {', '.join(change['changes'][:2])}")
        if len(results['changes']) > 3:
            print(f"  ... and {len(results['changes']) - 3} more")

    print(f"\n{'='*60}")
    print(f"TOTAL: {total_processed} sermons processed, {total_modified} modified")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
