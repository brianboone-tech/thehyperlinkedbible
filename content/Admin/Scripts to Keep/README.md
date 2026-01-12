# Scripts to Keep

This folder is reserved for permanent, reusable scripts that should **NEVER** be deleted.

---

## Current Status

**No permanent scripts currently exist.** Scripts are created as needed for specific tasks and deleted after use.

---

## Script Management Policy

### ✅ Save to This Folder:
- Scripts referenced in documentation (Formatting.md, CLAUDE.md)
- Scripts needed for recurring formatting tasks
- Scripts providing reusable functionality across sessions

### ❌ Delete After Use:
- One-time processing scripts
- Test scripts
- Single-session task scripts
- Any script in vault root NOT in this folder

### 🧹 Session End Cleanup:
At the end of every session, Claude should:
1. Check vault root for orphaned .py and .js files
2. Delete ALL scripts in vault root
3. Keep ONLY scripts in `Scripts to Keep/` folder

---

## Potential Future Scripts

If needed, scripts could be created for:
- Standardizing formatting across folders
- Verifying link integrity
- Batch processing cross-references
- Migrating content between structures

---

**Last Updated**: 2025-12-13
**Maintained By**: Claude Code Automation
