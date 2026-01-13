# Claude Code Work Log

This document tracks the work done with Claude Code on The Hyperlinked Bible project.

## Project Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        INTERNET / CLOUD / GITHUB                            │
│                                                                             │
│   ┌──────────────────────┐         ┌──────────────────────┐                │
│   │   GitHub Repository  │ ──────► │    Public Website    │                │
│   │ github.com/brianboone│         │ brianboone-tech.     │                │
│   │ -tech/thehyperlinked │         │ github.io/           │                │
│   │ bible                │         │ thehyperlinkedbible  │                │
│   └──────────────────────┘         └──────────────────────┘                │
│              ▲                                                              │
│              │ npx quartz sync                                              │
└──────────────┼──────────────────────────────────────────────────────────────┘
               │
┌──────────────┼──────────────────────────────────────────────────────────────┐
│              │                         LOCAL                                │
│              │                                                              │
│   ┌──────────────────────┐         ┌──────────────────────┐                │
│   │  Local Quartz Folder │ ──────► │  Obsidian Content    │                │
│   │ C:\Obsidian Vaults\  │         │  Folder              │                │
│   │ thehyperlinkedbible  │         │ ...\content          │                │
│   └──────────────────────┘         └──────────────────────┘                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### How It Works

1. **Obsidian Vault**: Markdown notes are created and edited in the `content` folder using Obsidian
2. **Quartz**: A static site generator that converts Obsidian markdown into a navigable website
3. **Sync**: Running `npx quartz sync` pushes changes to the GitHub repository
4. **GitHub Pages**: Automatically builds and deploys the site to the public URL

### Key Locations

| Component | Location |
|-----------|----------|
| Local Quartz Root | `C:\Obsidian Vaults\thehyperlinkedbible` |
| Content Folder | `C:\Obsidian Vaults\thehyperlinkedbible\content` |
| GitHub Repo | https://github.com/brianboone-tech/thehyperlinkedbible |
| Live Website | https://brianboone-tech.github.io/thehyperlinkedbible/ |

---

## Work Log

### Session 1 - January 13, 2026

- **Created this file** (`claude.md`) to document project architecture and track work
- Reviewed project structure and confirmed understanding of the Quartz + Obsidian + GitHub Pages workflow
- **Identified bracket rendering bug** - Wiki links with `[text]` in display text (e.g., `[[path|[the] will]]`) were not rendering as links on the website
- **Fixed Colossians 1.md** as a test - Replaced square brackets `[text]` with parentheses `(text)` in wiki link display text (27 instances fixed)
- **Pending**: If test succeeds, apply same fix to all Reference Bible files
