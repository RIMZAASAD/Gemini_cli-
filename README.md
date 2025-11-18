# Gemini CLI Complete Guide: Setup & Configuration

## What is Gemini CLI?

Gemini CLI is an open-source AI agent that runs directly in your terminal. It assists with coding, file operations, debugging, server setup, and automation. It also supports MCP servers.

### Free Tier Benefits:

* 60 requests per minute
* 1,000 requests per day (with Google account login)

---

## Installation & Setup

### Requirements

* Node.js 20+

### Installation Steps

```bash
npm install -g @google/gemini-cli
gemini -v
npm upgrade -g @google/gemini-cli
```

---

## First Launch

```bash
gemini
```

### Initial Setup

1. Choose Theme
2. Choose Authentication Method:

   * Google Login
   * Gemini API Key
   * Vertex AI

---

## Interface Overview

### Essential Commands

```bash
/help
/docs
/stats
/tools
/quit
```

### File Referencing

```bash
@app.py
@README.md
```

### Shell Mode

```bash
!
pwd
ESC
```

---

## Command Line Options

### Version Check

```bash
gemini -v
gemini --version
```

### Model Selection

```bash
gemini -m "gemini-flash-2.5"
gemini -m "gemini-pro-2.5"
```

### Single Prompt Mode

```bash
gemini -p "your prompt"
gemini "your prompt"
```

### Debug Mode

```bash
gemini -d
gemini -d -p "your prompt"
```

### Session Summary

```bash
gemini --session-summary "session.txt"
```

### YOLO Mode

```bash
gemini -y
gemini --yolo
```

---

## GEMINI.md Files

### File Hierarchy

1. Global → `~/.gemini/GEMINI.md`
2. Project Root
3. Local Folder Rules

### Context Management

```bash
/memory show
/memory refresh
```

---

## Tools

```bash
/tools
```

Tools include:

* GoogleSearch
* ReadFile
* WriteFile
* mkdir
* Shell

---

## Best Practices

### DO:

* Start Gemini CLI from your project directory
* Review tool permissions
* Use GEMINI.md for consistency

### DON'T:

* Run from the home directory
* Use YOLO mode by default

---

## Common Workflows

### Quick Git Help

```bash
gemini "show me git commands for rebasing"
```

### Generate Code

```bash
cd my-project
gemini
```

### Modify Files

```bash
gemini
> In @app.py add error handling
```

### Restore Checkpoint

```bash
gemini -c
/restore
```

---

## Troubleshooting

### Flash Model Issue

* Free tier quota may auto-switch to Flash model.

### Context Not Loading

```bash
gemini -d
```

### Port Conflict

* Gemini CLI will suggest a new port.

---

## Extra Commands

```bash
/checkpoint save
/checkpoint list
/checkpoint load
/history
/history clear
/clear
/restart
/files
/folders
/search "keyword"
/format
/scan project
/scan errors
/upgrade
/reinstall
/theme
/login
/logout
```

---

## Quick Reference

```bash
npm install -g @google/gemini-cli
gemini
gemini -m "model"
gemini -d
gemini -c
/help
/tools
/memory show
/restore
!
@file
```
