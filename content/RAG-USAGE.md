# RAG Search Tools for The Hyperlinked Bible

This vault includes a semantic search system that helps Claude Code find relevant content across all 17,290 indexed files instantly.

## Getting Started

The RAG system activates automatically when you start Claude Code in this project. No manual setup required.

**First time setup was completed January 19, 2026:**
- 17,290 files indexed
- 205,652 searchable chunks created
- Index stored locally at `content/Admin/mcp_server/data/chroma_db/`

---

## Available Tools

### 1. `vault_search`
**Semantic search across all content**

Use this to find content by meaning, not just keywords. Great for theological concepts, themes, or topics.

**Example queries:**
- "Melchizedek priesthood"
- "Christ as the new Adam"
- "temple symbolism in Revelation"
- "suffering servant prophecy"

**What it returns:** Top 10 most relevant files with snippets and metadata.

---

### 2. `search_by_reference`
**Find content by Bible reference**

Searches for all content related to a specific Bible verse or passage.

**Example queries:**
- "Genesis 1:26"
- "Hebrews 7:17"
- "Psalm 110:4"
- "Romans 5:14"

**What it returns:** All indexed content mentioning or related to that reference (TOSK cross-references, Trajectory Tables, IPs, sermons, etc.).

---

### 3. `find_trajectory_tables`
**Find Trajectory Tables by theological topic**

Searches specifically within the 181 Trajectory Tables for typological studies.

**Example queries:**
- "priesthood"
- "sacrifice"
- "temple"
- "covenant"
- "Davidic king"

**What it returns:** Relevant Trajectory Tables with their stage progressions and key texts.

---

### 4. `find_related`
**Find content related to a specific file**

Given a file path, finds other content in the vault that is semantically similar.

**Example usage:**
- Find files related to "Trajectory Tables/102 - Melchizedek (Priest Forever).md"
- Find files related to "Readable Bible/58 - Hebrews/Hebrews 7.md"

**What it returns:** Top 10 most similar files based on content.

---

### 5. `index_stats`
**View index statistics**

Shows current state of the search index.

**Returns:**
- Total chunks indexed
- Number of files
- Last index date
- Last update time

---

## Content Types Indexed

| Content Type | Files | What's Searchable |
|--------------|-------|-------------------|
| Readable Bible | ~1,255 | Individual verses |
| Trajectory Tables | 181 | Intro, table content, lexicon findings |
| Intertextuality Pairs | ~2,960 | Full connection descriptions |
| TOSK | ~1,190 | Cross-references by verse |
| Chiasms | ~1,733 | Full chiastic structures |
| Spurgeon Sermons | ~4,400 | Paragraph groups |
| Books & Foundation Texts | ~5,500 | Paragraph groups |

---

## Updating the Index

The index updates automatically when Claude Code starts if files have changed. You can also manually update:

```bash
cd "C:\Obsidian Vaults\thehyperlinkedbible\content\Admin\mcp_server"

# Update only changed files (fast)
python indexer.py --update

# Full rebuild (takes ~55 minutes)
python indexer.py --rebuild

# View stats
python indexer.py --stats
```

---

## Skipped Content

The following are intentionally excluded from the index:
- `Admin/` folder (scripts, not content)
- `Spurgeon Sermon - Whole Volumes/` (too large, individual sermons are indexed)
- Files larger than 500KB
- Hidden files and folders

---

## Troubleshooting

**Tools not appearing after restart?**
- Check that `.mcp.json` exists in the project root
- Verify Python is in your PATH
- Check `content/Admin/mcp_server/` folder exists with all files

**Search returning no results?**
- Run `python indexer.py --stats` to verify index exists
- Try `python indexer.py --rebuild` if index is corrupted

**Index out of date?**
- Run `python indexer.py --update` to re-index changed files
