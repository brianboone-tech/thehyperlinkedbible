#!/usr/bin/env python3
"""
Extract and clean Andrew Bonar's Commentary on Leviticus into chapter files.
"""
import re
import os

# Read the raw text file
with open(r"C:\Obsidian Vaults\thehyperlinkedbible\content\bonar_leviticus_raw.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Output folder
output_dir = r"C:\Obsidian Vaults\thehyperlinkedbible\content\Books - Public\Andrew Bonar\Commentary on Leviticus"
os.makedirs(output_dir, exist_ok=True)

def clean_text(text):
    """Clean OCR artifacts from text."""
    # Remove Google artifacts on their own lines
    text = re.sub(r'\n\s*\.y\s+Google\s*\n', '\n', text)
    text = re.sub(r'\n\s*ijGoogle\s*\n', '\n', text)
    text = re.sub(r'\n\s*ijGoogie\s*\n', '\n', text)

    # Remove page number headers like "CHAPTER I. 19" or "CHAPTER II. 47"
    text = re.sub(r'\nCHAPTER\s+[IVXLC]+\.?\s+\d+\s*\n', '\n', text)
    text = re.sub(r'\nCHAPTEE\s+[IVXLC]+\.?\s+\d+\s*\n', '\n', text)
    text = re.sub(r'\nCHAPTEa\s+[IVXLC]+\.?\s+\d+\s*\n', '\n', text)
    text = re.sub(r'\nCITAPTER\s+[IVXLC]+\.?\s+\d+\s*\n', '\n', text)
    text = re.sub(r'\nCHAPTEB\s+[IVXLC]+\.?\s+\d+\s*\n', '\n', text)

    # Remove standalone page numbers
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
    text = re.sub(r'\n\s*\d+\*?\s*\n', '\n', text)

    # Fix common OCR errors
    text = text.replace("Vet.", "Ver.")
    text = text.replace("Yar.", "Ver.")
    text = text.replace("Ter,", "Ver.")
    text = text.replace("Ter.", "Ver.")
    text = text.replace("Vem", "Vers")
    text = text.replace("Vera", "Vers")

    # Remove double spaces
    text = re.sub(r'  +', ' ', text)

    # Clean up excessive blank lines (more than 2)
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    # Remove page header lines like "THE BURNT-OFFERING. 19"
    text = re.sub(r'\n[A-Z][A-Z\s\-]+\.\s+\d+\s*\n', '\n', text)

    return text.strip()

def extract_section(start_line, end_line):
    """Extract lines from start to end and clean them."""
    section_lines = lines[start_line-1:end_line]
    text = ''.join(section_lines)
    return clean_text(text)

# Chapter definitions: (start_line, end_line, filename, title)
chapters = [
    (159, 209, "00 - Preface.md", "Preface"),
    (211, 558, "01 - Nature of the Book.md", "The Nature of the Book"),
    (564, 1463, "02 - Chapter 1 - The Burnt-Offering.md", "Chapter I: The Burnt-Offering"),
    (1464, 2279, "03 - Chapter 2 - The Meat-Offering.md", "Chapter II: The Meat-Offering"),
    (2280, 2784, "04 - Chapter 3 - The Peace-Offerings.md", "Chapter III: The Peace-Offerings"),
    (2785, 3675, "05 - Chapter 4 - The Sin-Offering.md", "Chapter IV: The Sin-Offering"),
    (3676, 4209, "06 - Chapter 5 - Sin-Offering for Sins of Inadvertency.md", "Chapter V: Sin-Offering for Sins of Inadvertency"),
    (4211, 4737, "07 - Chapter 6 - The Trespass-Offering.md", "Chapter VI: The Trespass-Offering"),
    (4738, 5442, "08 - Chapter 7 - Special Rules for Priests.md", "Chapter VII: Special Rules for Priests"),
    (5443, 6340, "09 - Chapter 8 - Same Subject Continued.md", "Chapter VIII: Same Subject Continued"),
    (6341, 7760, "10 - Chapter 9 - The Priesthood Entering on their Office.md", "Chapter IX: The Priesthood Entering on their Office"),
    (7761, 8247, "11 - Chapter 10 - Aarons Entrance on his Office.md", "Chapter X: Aaron's Entrance on his Office"),
    (8248, 8876, "12 - Chapter 11 - The Fencing of the Priestly Ritual.md", "Chapter XI: The Fencing of the Priestly Ritual"),
    (8877, 9981, "13 - Chapter 12 - The Clean and the Unclean.md", "Chapter XII: The Clean and the Unclean"),
    (9974, 10153, "14 - Chapter 13 - Original Sin.md", "Chapter XIII: Original Sin"),
    (10154, 11207, "15 - Chapter 14 - The Leprosy.md", "Chapter XIV: The Leprosy"),
    (11208, 12101, "16 - Chapter 15 - The Leprosy Removed.md", "Chapter XV: The Leprosy Removed"),
    (12097, 12591, "17 - Chapter 16 - The Secret Flow of Sin.md", "Chapter XVI: The Secret Flow of Sin"),
    (12589, 13455, "18 - Chapter 17 - The Day of Atonement.md", "Chapter XVII: The Day of Atonement"),
    (13453, 13864, "19 - Chapter 18 - The Use of Animal Food Regulated.md", "Chapter XVIII: The Use of Animal Food Regulated"),
    (13865, 14410, "20 - Chapter 19 - Private and Domestic Obligations.md", "Chapter XIX: Private and Domestic Obligations"),
    (14408, 15108, "21 - Chapter 20 - Duties in Every Day Relations.md", "Chapter XX: Duties in Every Day Relations"),
    (15106, 15548, "22 - Chapter 21 - Warnings Against Sins of Former Inhabitants.md", "Chapter XXI: Warnings Against Sins of Former Inhabitants"),
    (15546, 16028, "23 - Chapter 22 - Personal Duties of the Priests.md", "Chapter XXII: Personal Duties of the Priests"),
    (16026, 16536, "24 - Chapter 23 - Household Laws regarding Holy Things.md", "Chapter XXIII: Household Laws regarding Holy Things"),
    (16537, 17806, "25 - Chapter 24 - The Public Festivals.md", "Chapter XXIV: The Public Festivals"),
    (17808, 18513, "26 - Chapter 25 - Duty of Priests when out of Public View.md", "Chapter XXV: Duty of Priests when out of Public View"),
    (18514, 19694, "27 - Chapter 26 - The Sabbatic Year and Jubilee.md", "Chapter XXVI: The Sabbatic Year and Jubilee"),
    (19695, 20589, "28 - Chapter 27 - Israels Temporal Blessings vs the Curse.md", "Chapter XXVII: Israel's Temporal Blessings vs the Curse"),
    (20585, 21354, "29 - Chapter 28 - Entire Devotion to God.md", "Chapter XXVIII: Entire Devotion to God"),
]

# Create each chapter file
for i, (start, end, filename, title) in enumerate(chapters):
    content = extract_section(start, end)

    # Build navigation
    prev_link = ""
    next_link = ""

    if i > 0:
        prev_name = chapters[i-1][2].replace(".md", "")
        prev_link = f"[[{prev_name}|← Previous Chapter]]"

    if i < len(chapters) - 1:
        next_name = chapters[i+1][2].replace(".md", "")
        next_link = f"[[{next_name}|Next Chapter →]]"

    if prev_link and next_link:
        nav = f"{prev_link} | {next_link}"
    elif prev_link:
        nav = prev_link
    elif next_link:
        nav = next_link
    else:
        nav = ""

    # Build the full markdown file
    md_content = f"# {title}\n\n"
    if nav:
        md_content += f"{nav}\n\n"
    md_content += "---\n\n"
    md_content += content

    # Write the file
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Created: {filename}")

print(f"\nDone! Created {len(chapters)} chapter files.")
