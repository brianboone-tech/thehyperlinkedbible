# Spurgeon Sermon Cleaner

This document outlines the process for enhancing a Spurgeon sermon with a summary, color formatting, and inline Scripture links.

---

## Step 1: Read the Sermon

Read the full sermon to understand:
- The main text and theme
- The typological/Christological connections
- All Scripture references cited (note these for Step 5)

---

## Step 2: Fix the Main Text

Replace the sermon's main text with the exact wording from the Readable Bible and add a link to it.

### Why This Step Matters

Spurgeon often quoted from the KJV, but his printed sermons sometimes contain:
- Transcription errors
- Archaic spelling variations
- Slight paraphrases

Using the exact text from Readable Bible ensures consistency across the site.

### Process

1. **Identify the reference** in the existing Text section (e.g., "Galatians 4:24")
2. **Open the Readable Bible** chapter and find the exact verse text
3. **Copy the verse text** exactly as it appears in Readable Bible
4. **Replace** the quoted text in the Text section
5. **Add a link** to the verse after the reference
6. **Apply blue color** to the quoted text (same as other scripture quotes)

### Format

```markdown
##### Text
*<span style="color: #1e90ff;">"Exact verse text from Readable Bible"</span>—[[Readable Bible/## - Book/Book Chapter#Book Chapter . Verse|Reference]].*
```

### Example

**Before (original sermon):**
```markdown
##### Text
*"These are the two covenants."—Galatians 4:24.*
```

**After (corrected and linked):**
```markdown
##### Text
*<span style="color: #1e90ff;">"Which things are an allegory: for these are the two covenants"</span>—[[Readable Bible/48 - Galatians/Galatians 4#Galatians 4 . 24|Galatians 4:24]].*
```

### Multiple Verses

If the main text spans multiple verses, include all verse text and link to the first verse:

```markdown
##### Text
*<span style="color: #1e90ff;">"Verse 1 text. Verse 2 text."</span>—[[Readable Bible/## - Book/Book Chapter#Book Chapter . Verse|Reference 1:1–2]].*
```

---

## Step 3: Write a Summary

Add a **Summary** section immediately after the Text section (after the first `---` following the scripture reference).

### Summary Guidelines

- 4-5 lines maximum
- Written from The Hyperlinked Bible's hermeneutical perspective:
  - Trace Christ through Scripture's types, themes, and trajectories
  - Show how the sermon connects OT types to NT fulfillment
  - Emphasize the unified redemptive story
- Focus on the typological and Christological significance

### Format

```markdown
##### Text
*<span style="color: #1e90ff;">"Scripture verse"</span>—[[link|Reference]].*

---

##### Summary

[4-5 line summary here]

---

[Sermon body begins...]
```

---

## Step 4: Apply Color Formatting

Apply color to scripture quotations and hymns in the sermon body.

### Color Codes

| Color | Hex Code | Use For |
|-------|----------|---------|
| Blue | `#1e90ff` | Scripture quotations only |
| Teal | `#008080` | Hymns and songs only |

### Format

```html
<span style="color: #1e90ff;">"Scripture quote here"</span>
<span style="color: #008080;">"Hymn stanza here"</span>
```

### What Gets Blue (#1e90ff)

- Direct scripture quotations (e.g., "In the day that thou eatest thereof thou shalt surely die.")
- Scripture references embedded in Spurgeon's text
- Biblical phrases Spurgeon quotes verbatim

### What Gets Teal (#008080)

- Hymn stanzas (multi-line poetry)
- Song lyrics
- Poetic verses Spurgeon quotes

### What Does NOT Get Color

- Spurgeon's own emphatic points or key phrases
- Spurgeon's summaries or applications
- Single-word emphasis
- Rhetorical flourishes
- Any text that is Spurgeon's own words, not scripture or hymn

### Example

**Scripture (blue):**
```html
<span style="color: #1e90ff;">"We are not under the law, but under grace."</span>
```

**Hymn (teal):**
```html
<span style="color: #008080;">"Grace all the work shall crown
Through everlasting days;
It lays in heaven the topmost stone,
And well deserves the praise."</span>
```

---

## Step 5: Add Inline Scripture Links

After each colored scripture quotation, add an inline Readable Bible link immediately following the closing `</span>` tag.

### Link Format

All links must use the Readable Bible format with proper anchors:

```markdown
[[Readable Bible/## - Book/Book Chapter#Book Chapter . Verse|Display Text]]
```

### Rules

1. **Verse anchors**: Use format `#Book Chapter . Verse` (spaces around the period)
2. **Verse spans**: Link to the first verse only (e.g., Romans 9:30–32 links to verse 30)
3. **Chapter-only references**: Link to verse 1 (e.g., Genesis 16 links to `#Genesis 16 . 1`)
4. **Multiple verses**: Use comma-separated display text (e.g., `Matthew 6:2, 5, 16`)

### Placement

Place the link **immediately after** the closing `</span>` tag, with a single space between:

```html
<span style="color: #1e90ff;">"Quote here"</span> [[Readable Bible/##/Book Chapter#Book Chapter . Verse|Reference]]
```

### Examples

**Single verse:**
```html
<span style="color: #1e90ff;">"In the day that thou eatest thereof thou shalt surely die."</span> [[Readable Bible/01 - Genesis/Genesis 2#Genesis 2 . 17|Genesis 2:17]]
```

**Verse span:**
```html
<span style="color: #1e90ff;">"Work out your own salvation with fear and trembling, for it is God that worketh in you to will and to do of his good pleasure."</span> [[Readable Bible/50 - Philippians/Philippians 2#Philippians 2 . 12|Philippians 2:12–13]]
```

**Multiple verses (same book):**
```html
<span style="color: #1e90ff;">"the Pharisees have their reward."</span> [[Readable Bible/40 - Matthew/Matthew 6#Matthew 6 . 2|Matthew 6:2, 5, 16]]
```

**Split quote (link after final part):**
```html
<span style="color: #1e90ff;">"Verily,"</span> said Christ, <span style="color: #1e90ff;">"the Pharisees have their reward."</span> [[Readable Bible/40 - Matthew/Matthew 6#Matthew 6 . 2|Matthew 6:2, 5, 16]]
```

### What to Link

- Every blue-colored scripture quotation should have an inline link
- Hymns (teal) do NOT get links
- If Spurgeon paraphrases rather than quotes, still add the link if the reference is clear

---

## Step 6: Final Structure

The completed sermon should have this structure:

```markdown
**Sermon #XX**
**Delivered in YYYY**
**By The Rev. C. H. Spurgeon**
**At New Park Street Chapel, Southwark**

---

##### Text
*<span style="color: #1e90ff;">"Exact verse from Readable Bible"</span>—[[Readable Bible/## - Book/Book Chapter#Book Chapter . Verse|Reference]].*

---

##### Summary

[4-5 line Christological summary]

---

[Full sermon body with colored quotes and inline links]

---

*Taken from The New Park Street Pulpit C. H. Spurgeon Collection.*
```

---

## Book Number Reference

| # | Book | # | Book | # | Book |
|---|------|---|------|---|------|
| 01 | Genesis | 23 | Isaiah | 45 | Romans |
| 02 | Exodus | 24 | Jeremiah | 46 | 1 Corinthians |
| 03 | Leviticus | 25 | Lamentations | 47 | 2 Corinthians |
| 04 | Numbers | 26 | Ezekiel | 48 | Galatians |
| 05 | Deuteronomy | 27 | Daniel | 49 | Ephesians |
| 06 | Joshua | 28 | Hosea | 50 | Philippians |
| 07 | Judges | 29 | Joel | 51 | Colossians |
| 08 | Ruth | 30 | Amos | 52 | 1 Thessalonians |
| 09 | 1 Samuel | 31 | Obadiah | 53 | 2 Thessalonians |
| 10 | 2 Samuel | 32 | Jonah | 54 | 1 Timothy |
| 11 | 1 Kings | 33 | Micah | 55 | 2 Timothy |
| 12 | 2 Kings | 34 | Nahum | 56 | Titus |
| 13 | 1 Chronicles | 35 | Habakkuk | 57 | Philemon |
| 14 | 2 Chronicles | 36 | Zephaniah | 58 | Hebrews |
| 15 | Ezra | 37 | Haggai | 59 | James |
| 16 | Nehemiah | 38 | Zechariah | 60 | 1 Peter |
| 17 | Esther | 39 | Malachi | 61 | 2 Peter |
| 18 | Job | 40 | Matthew | 62 | 1 John |
| 19 | Psalms | 41 | Mark | 63 | 2 John |
| 20 | Proverbs | 42 | Luke | 64 | 3 John |
| 21 | Ecclesiastes | 43 | John | 65 | Jude |
| 22 | Song of Solomon | 44 | Acts | 66 | Revelation |

---

## Example: Completed Inline Links

From Sermon #69 - The Allegories of Sarah and Hagar:

```markdown
That is the Hagar covenant—the covenant propounded on Sinai, amidst tempests, fire and smoke—or rather, propounded, first of all, in the garden of Eden, where God said to Adam, <span style="color: #1e90ff;">"In the day that thou eatest thereof thou shalt surely die."</span> [[Readable Bible/01 - Genesis/Genesis 2#Genesis 2 . 17|Genesis 2:17]] As long as he did not eat of the tree...
```

```markdown
The law is under a Christian; it is for him to walk on, to be his guide, his rule, his pattern. <span style="color: #1e90ff;">"We are not under the law, but under grace."</span> [[Readable Bible/45 - Romans/Romans 6#Romans 6 . 14|Romans 6:14]] Law is the road which guides us...
```

```markdown
So it is in salvation: he says, <span style="color: #1e90ff;">"My glory I will not give to another."</span> [[Readable Bible/23 - Isaiah/Isaiah 42#Isaiah 42 . 8|Isaiah 42:8]] And I beg to remind thee...
```

---

## Quick Checklist

- [ ] Read sermon and note all Scripture references
- [ ] Replace main Text with exact Readable Bible text + link
- [ ] Write 4-5 line Christological summary
- [ ] Add blue color to all Scripture quotations
- [ ] Add teal color to all hymn quotations
- [ ] Add inline Readable Bible link after each blue quote
- [ ] Verify link format: `#Book Chapter . Verse` (spaces around period)
- [ ] Final review for missed quotes or broken links
