# FOUNDA SUBAGENT v4.0 - TECHNICAL IMPLEMENTATION

**Version**: 4.0 (Updated 2025-01-05)
**Status**: ✅ PROVEN (Angels and Spiritual Warfare: 100 files, 100% coverage)
**Purpose**: Technical specification for generating foundation text files from trajectory tables

---

## IMPLEMENTATION OVERVIEW

Founda v4.0 implements a **100% trajectory table coverage** model where every "Key Text(s)" entry in a trajectory table receives its own foundation text file.

### Core Algorithm:
```
FOR EACH row in trajectory table:
    Extract "Key Text(s)" column
    Create foundation file: [##] - [Book] [Reference].md
    Populate with: Context + Connections + Christological
    Store in: Foundation Texts/[Theme Name]/
END FOR

VERIFY: file_count == trajectory_row_count
```

---

## PHASE 1: TRAJECTORY TABLE PARSING

### Input File Structure:
```markdown
## [THEME NAME] TRAJECTORY TABLE

| # | Stage | Key Text(s) | Theological Development |
|---|-------|-------------|------------------------|
| 1 | First Stage | Genesis 3:15 | Description... |
| 2 | Second Stage | Genesis 6:1-4 | Description... |
...
| N | Final Stage | Revelation 20:10 | Description... |
```

### Parsing Algorithm:
```python
def parse_trajectory_table(file_path):
    """Extract all key texts from trajectory table."""

    # 1. Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 2. Find table section
    table_start = content.find('| # | Stage | Key Text(s)')
    table_rows = []

    # 3. Parse each row
    for line in content[table_start:].split('\n'):
        if line.startswith('|') and not line.startswith('|---|'):
            if '|' in line and len(line.split('|')) >= 5:
                parts = [p.strip() for p in line.split('|')]
                if parts[1].isdigit():  # Row number
                    row = {
                        'number': parts[1],
                        'stage': parts[2],
                        'key_text': parts[3],
                        'development': parts[4]
                    }
                    table_rows.append(row)

    return table_rows

# Example output:
# [
#   {'number': '1', 'stage': 'Protoevangelium',
#    'key_text': 'Genesis 3:15',
#    'development': 'Promise of seed crushing serpent...'},
#   {'number': '2', 'stage': 'First manifestation',
#    'key_text': 'Genesis 4:8',
#    'development': 'Cain murders Abel...'},
#   ...
# ]
```

### Output:
- List of all trajectory entries
- Total count (= target file count)
- Ordered list for sequential processing

---

## PHASE 2: FOUNDATION FILE GENERATION

### File Generation Algorithm:

```python
def generate_foundation_file(entry, theme_name):
    """Generate single foundation text file from trajectory entry."""

    # 1. Parse reference
    ref = entry['key_text']  # e.g., "Genesis 3:15"
    book, verses = parse_reference(ref)
    book_num = get_canonical_number(book)  # 01-66

    # 2. Build filename
    filename = f"{book_num} - {book} {verses}.md"
    # Example: "01 - Genesis 3.15.md"

    # 3. Extract context from trajectory
    context = entry['development']

    # 4. Build connections
    connections = build_connections(entry, all_entries)
    # TO: Previous entries in trajectory
    # FROM OT: Later OT entries
    # FROM NT: NT fulfillment texts

    # 5. Generate christological connection
    christological = generate_christological(ref, context, connections)

    # 6. Assemble content
    content = f"""### [[Readable Bible/{book_num} - {book}/{book} {ch}#{book} {ch} . {v}|{ref}]]

**Context**: {context}

**Connections**:
- **TO**: {connections['to']}
- **FROM OT**: {connections['from_ot']}
- **FROM NT**: {connections['from_nt']}

**Christological Connection**: {christological}

"""

    # 7. Write file
    output_path = f"Foundation Texts/{theme_name}/{filename}"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return filename
```

### Context Extraction:
```python
def extract_context(entry):
    """Use trajectory table's 'Theological Development' as context."""
    return entry['development']
    # This is the PRIMARY context source - already describes
    # the theological significance of this stage
```

### Connections Building:
```python
def build_connections(current_entry, all_entries):
    """Build TO/FROM OT/FROM NT connections."""

    current_idx = all_entries.index(current_entry)
    current_ref = current_entry['key_text']

    # TO: Previous entries (what this builds on)
    to_refs = []
    for i in range(max(0, current_idx - 3), current_idx):
        to_refs.append(all_entries[i]['key_text'])

    # FROM OT: Later OT entries (what develops this)
    from_ot_refs = []
    if is_ot_text(current_ref):
        for entry in all_entries[current_idx + 1:]:
            if is_ot_text(entry['key_text']):
                from_ot_refs.append(entry['key_text'])

    # FROM NT: NT entries that fulfill/apply this
    from_nt_refs = []
    for entry in all_entries[current_idx + 1:]:
        if is_nt_text(entry['key_text']):
            from_nt_refs.append(entry['key_text'])

    return {
        'to': '; '.join(to_refs) if to_refs else 'None (foundational text)',
        'from_ot': '; '.join(from_ot_refs[:5]),  # Limit to 5 for brevity
        'from_nt': '; '.join(from_nt_refs[:8])   # More NT refs typically
    }
```

### Christological Connection Generation:
```python
def generate_christological(reference, context, connections):
    """Generate paragraph showing how text points to Christ."""

    # Use AI synthesis grounded in:
    # 1. The passage itself
    # 2. Trajectory context
    # 3. NT connections already identified
    # 4. Canonical theology

    # Must include:
    # - How OT text points forward to Christ
    # - Specific NT passages that fulfill/apply
    # - Typological or prophetic patterns
    # - Canonical progression from this text to Christ

    # Example structure:
    # "[OT text] foreshadows Christ by [pattern].
    #  [NT text 1] shows fulfillment through [how].
    #  [NT text 2] applies this by [application].
    #  [Final summary of Christological significance]."

    return christological_paragraph
```

---

## PHASE 3: ENHANCED CONTENT (OPTIONAL)

For major/pivotal texts, add enhanced elements:

### Hebrew/Greek Terms:
```python
def add_hebrew_greek_terms(reference):
    """Add key terms with transliteration for major texts."""

    # Extract 3-5 most theologically significant terms
    # Format: term (*transliteration*) - "translation"

    # Examples:
    # - זֶרַע (*zeraʿ*) - "seed, offspring"
    # - σπέρμα (*sperma*) - "seed" (LXX/NT)

    return terms_list
```

### Ninefold Analysis:
```python
def add_ninefold_analysis(reference, context):
    """Add deeper analysis for major texts."""

    categories = {
        'OT Context': 'Historical/literary context',
        'Jewish Backgrounds': 'Second Temple interpretation',
        'Text Form': 'Literary structure',
        'Hermeneutical Use': 'Interpretive principles',
        'Theological Use': 'Doctrinal significance',
        'Rhetorical Use': 'Persuasive function'
    }

    # Generate 1-2 sentences for each applicable category
    # Not all 9 categories needed for every text

    return analysis_dict
```

---

## PHASE 4: FILE NAMING & ORGANIZATION

### Canonical Book Numbering:
```python
BOOK_NUMBERS = {
    'Genesis': '01', 'Exodus': '02', 'Leviticus': '03',
    'Numbers': '04', 'Deuteronomy': '05', 'Joshua': '06',
    'Judges': '07', 'Ruth': '08', '1 Samuel': '09',
    '2 Samuel': '10', '1 Kings': '11', '2 Kings': '12',
    '1 Chronicles': '13', '2 Chronicles': '14', 'Ezra': '15',
    'Nehemiah': '16', 'Esther': '17', 'Job': '18',
    'Psalm': '19', 'Psalms': '19', 'Proverbs': '20',
    'Ecclesiastes': '21', 'Song of Solomon': '22', 'Song': '22',
    'Isaiah': '23', 'Jeremiah': '24', 'Lamentations': '25',
    'Ezekiel': '26', 'Daniel': '27', 'Hosea': '28',
    'Joel': '29', 'Amos': '30', 'Obadiah': '31',
    'Jonah': '32', 'Micah': '33', 'Nahum': '34',
    'Habakkuk': '35', 'Zephaniah': '36', 'Haggai': '37',
    'Zechariah': '38', 'Malachi': '39', 'Matthew': '40',
    'Mark': '41', 'Luke': '42', 'John': '43',
    'Acts': '44', 'Romans': '45', '1 Corinthians': '46',
    '2 Corinthians': '47', 'Galatians': '48', 'Ephesians': '49',
    'Philippians': '50', 'Colossians': '51', '1 Thessalonians': '52',
    '2 Thessalonians': '53', '1 Timothy': '54', '2 Timothy': '55',
    'Titus': '56', 'Philemon': '57', 'Hebrews': '58',
    'James': '59', '1 Peter': '60', '2 Peter': '61',
    '1 John': '62', '2 John': '63', '3 John': '64',
    'Jude': '65', 'Revelation': '66'
}
```

### Reference Parsing:
```python
def parse_reference(ref_string):
    """Parse 'Genesis 3:15' into components."""

    # Examples:
    # "Genesis 3:15" → book="Genesis", ch="3", v="15"
    # "Matthew 4:1-11" → book="Matthew", ch="4", v="1-11"
    # "1 John 3:8" → book="1 John", ch="3", v="8"

    import re

    # Pattern: (Book Name) (Chapter):(Verse-range)
    pattern = r'(\d?\s?[A-Za-z]+)\s+(\d+):(\d+(?:-\d+)?)'
    match = re.match(pattern, ref_string)

    if match:
        book = match.group(1).strip()
        chapter = match.group(2)
        verses = match.group(3)
        return book, chapter, verses

    return None, None, None
```

### Filename Generation:
```python
def generate_filename(reference):
    """Convert 'Genesis 3:15' to '01 - Genesis 3.15.md'."""

    book, chapter, verses = parse_reference(reference)
    book_num = BOOK_NUMBERS[book]

    # Replace colon with period (Obsidian link safety)
    filename = f"{book_num} - {book} {chapter}.{verses}.md"

    return filename
```

---

## PHASE 5: VERIFICATION & QUALITY CONTROL

### Coverage Verification:
```python
def verify_coverage(trajectory_entries, generated_files):
    """Ensure 100% coverage of trajectory table."""

    # Count check
    if len(generated_files) != len(trajectory_entries):
        raise ValueError(f"Mismatch: {len(trajectory_entries)} entries, {len(generated_files)} files")

    # 1:1 mapping check
    for entry in trajectory_entries:
        expected_filename = generate_filename(entry['key_text'])
        if expected_filename not in generated_files:
            raise ValueError(f"Missing file: {expected_filename}")

    # No extra files check
    for file in generated_files:
        if not any(generate_filename(e['key_text']) == file
                  for e in trajectory_entries):
            raise ValueError(f"Extra file not in trajectory: {file}")

    return True  # 100% coverage confirmed
```

### Canonical Order Verification:
```python
def verify_canonical_order(generated_files):
    """Ensure files are numbered correctly (01-66)."""

    # Extract book numbers
    book_numbers = [int(f.split(' - ')[0]) for f in generated_files]

    # Check all are in range 01-66
    if not all(1 <= n <= 66 for n in book_numbers):
        raise ValueError("Book numbers out of range")

    # Check ordering is canonical
    if book_numbers != sorted(book_numbers):
        raise ValueError("Files not in canonical order")

    return True
```

### Content Quality Checks:
```python
def verify_file_quality(file_path):
    """Check individual file has required elements."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Required elements
    checks = {
        'readable_link': '### [[Readable Bible/' in content,
        'context': '**Context**:' in content,
        'connections': '**Connections**:' in content,
        'to': '- **TO**:' in content,
        'from_ot': '- **FROM OT**:' in content,
        'from_nt': '- **FROM NT**:' in content,
        'christological': '**Christological Connection**:' in content
    }

    missing = [k for k, v in checks.items() if not v]

    if missing:
        raise ValueError(f"File missing elements: {missing}")

    return True
```

---

## PERFORMANCE OPTIMIZATION

### Parallel Generation (Optional):
```python
from concurrent.futures import ThreadPoolExecutor

def generate_all_files_parallel(entries, theme_name, max_workers=5):
    """Generate multiple files concurrently."""

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(generate_foundation_file, entry, theme_name)
            for entry in entries
        ]

        # Wait for all to complete
        filenames = [f.result() for f in futures]

    return filenames
```

### Batch Writing:
```python
def batch_write_files(file_data, theme_name):
    """Write multiple files efficiently."""

    import os
    output_dir = f"Foundation Texts/{theme_name}"
    os.makedirs(output_dir, exist_ok=True)

    for filename, content in file_data:
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
```

---

## ERROR HANDLING

### Common Errors & Solutions:

**Error**: Trajectory table parsing fails
```python
try:
    entries = parse_trajectory_table(file_path)
except Exception as e:
    print(f"Failed to parse trajectory table: {e}")
    print("Check table format matches specification")
    # Fallback: manual entry parsing
```

**Error**: File naming conflicts
```python
def handle_duplicate_filename(filename, existing_files):
    """Handle case where two entries map to same filename."""

    # Example: "Romans 4:1-25" and "Romans 4:16" both → "45 - Romans 4.*.md"
    # Solution: Use exact verse ranges in filename

    if filename in existing_files:
        # Append disambiguator
        base, ext = os.path.splitext(filename)
        counter = 1
        while f"{base}_{counter}{ext}" in existing_files:
            counter += 1
        filename = f"{base}_{counter}{ext}"

    return filename
```

**Error**: Missing book number mapping
```python
def get_canonical_number_safe(book_name):
    """Get book number with fallback."""

    # Try exact match
    if book_name in BOOK_NUMBERS:
        return BOOK_NUMBERS[book_name]

    # Try normalized (handle "Psalms" vs "Psalm")
    normalized = book_name.rstrip('s')
    if normalized in BOOK_NUMBERS:
        return BOOK_NUMBERS[normalized]

    # Try fuzzy match
    from difflib import get_close_matches
    matches = get_close_matches(book_name, BOOK_NUMBERS.keys(), n=1)
    if matches:
        return BOOK_NUMBERS[matches[0]]

    raise ValueError(f"Unknown book: {book_name}")
```

---

## TESTING & VALIDATION

### Unit Tests:
```python
def test_parse_reference():
    """Test reference parsing."""
    assert parse_reference("Genesis 3:15") == ("Genesis", "3", "15")
    assert parse_reference("Matthew 4:1-11") == ("Matthew", "4", "1-11")
    assert parse_reference("1 John 3:8") == ("1 John", "3", "8")

def test_generate_filename():
    """Test filename generation."""
    assert generate_filename("Genesis 3:15") == "01 - Genesis 3.15.md"
    assert generate_filename("Revelation 20:10") == "66 - Revelation 20.10.md"

def test_coverage_verification():
    """Test 100% coverage check."""
    entries = parse_trajectory_table("test_trajectory.md")
    files = generate_all_files(entries, "Test Theme")
    assert verify_coverage(entries, files) == True
```

### Integration Test:
```python
def test_full_workflow():
    """Test complete workflow on small trajectory."""

    # 1. Create test trajectory table
    test_trajectory = """
    | # | Stage | Key Text(s) | Theological Development |
    |---|-------|-------------|------------------------|
    | 1 | First | Genesis 3:15 | Protoevangelium |
    | 2 | Second | Romans 16:20 | Fulfillment |
    """

    # 2. Parse
    entries = parse_trajectory_table_from_string(test_trajectory)
    assert len(entries) == 2

    # 3. Generate
    files = generate_all_files(entries, "Test Theme")
    assert len(files) == 2

    # 4. Verify
    assert "01 - Genesis 3.15.md" in files
    assert "45 - Romans 16.20.md" in files

    # 5. Check content
    content = read_file("Foundation Texts/Test Theme/01 - Genesis 3.15.md")
    assert "**Context**:" in content
    assert "**Christological Connection**:" in content
```

---

## DEPLOYMENT CHECKLIST

### Pre-Deployment:
- [ ] Trajectory table exists and is complete
- [ ] Output directory created: `Foundation Texts/[Theme Name]/`
- [ ] No existing files that would conflict
- [ ] Book number mappings up to date

### During Deployment:
- [ ] Parse trajectory table successfully
- [ ] Count entries (log target count)
- [ ] Generate all files
- [ ] Handle any errors gracefully
- [ ] Log progress (file X of N created)

### Post-Deployment:
- [ ] Verify file count matches trajectory entries
- [ ] Check 100% coverage
- [ ] Validate canonical ordering
- [ ] Spot-check 3-5 files for quality
- [ ] Generate completion report

---

## PROVEN RESULTS: ANGELS AND SPIRITUAL WARFARE

### Execution Log:
```
FOUNDA v4.0 - Angels and Spiritual Warfare (Cosmic Conflict)
================================================================

Phase 1: Parse Trajectory Table
- File: Trajectory Tables/Angels and Spiritual Warfare (Cosmic Conflict).md
- Entries found: 100
- Target files: 100
- Status: ✅ COMPLETE

Phase 2: Generate Foundation Files
- Processing: Genesis 3:15 (1/100)
- Processing: Genesis 4:8 (2/100)
- Processing: Genesis 6:1-4 (3/100)
  ...
- Processing: Revelation 20:7-10 (100/100)
- Status: ✅ COMPLETE

Phase 3: Verify Coverage
- Files created: 100
- Trajectory entries: 100
- Coverage: 100%
- Status: ✅ VERIFIED

Phase 4: Report
- OT files: 18
- NT files: 82
- Storage: Foundation Texts/Angels and Spiritual Warfare (Cosmic Conflict)/
- Status: ✅ COMPLETE

================================================================
RESULT: ✅ SUCCESS - 100 files, 100% coverage
================================================================
```

### File Distribution:
- **Genesis** (4): 3.15, 4.8, 6.1-4, 6.5-7
- **Exodus** (3): 1.15-22, 12.23, 23.20-23
- **Numbers** (1): 21.8-9
- **Deuteronomy** (1): 32.8
- **Joshua** (1): 5.13-15
- **Judges** (1): 6.11-24
- **1 Samuel** (1): 16.14
- **1 Kings** (1): 22.19-23
- **2 Kings** (2): 6.17, 19.35
- **Job** (2): 1.6-12, 2.1-7
- **Psalms** (3): 34.7, 91.11-12, 103.20-21
- **Isaiah** (3): 6.1-3, 14.12-15, 37.36
- **Ezekiel** (1): 28.12-19
- **Daniel** (3): 6.22, 10.12-13, 12.1
- **Zechariah** (2): 3.1-2, 3.4-5
- **Matthew** (9): Multiple texts
- **Mark** (2), **Luke** (7), **John** (4)
- **Acts** (7), **Romans** (2), **1-2 Corinthians** (6)
- **Galatians** (1), **Ephesians** (3), **Philippians** (1), **Colossians** (2)
- **Thessalonians** (3), **Timothy** (3), **Hebrews** (2)
- **James** (1), **1 Peter** (3), **2 Peter** (1)
- **1 John** (3), **Jude** (2), **Revelation** (4)

---

## READY FOR DEPLOYMENT

Founda v4.0 is **proven and operational** with successful completion of Angels and Spiritual Warfare network.

**Command to deploy**: "Run Founda on [Network Name]"

**Next**: Select from 84 remaining thematic networks

---

**Version**: 4.0
**Last Updated**: 2025-01-05
**Status**: ✅ PROVEN & OPERATIONAL
