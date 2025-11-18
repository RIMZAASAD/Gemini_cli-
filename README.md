
---

# 🌟 **Gemini CLI – Complete Guide (Setup + Usage + Commands)**

Gemini CLI is an open-source AI agent that runs directly in your terminal. It can write code, analyze files, debug programs, create folders, automate workflows, and communicate with MCP servers.

This guide provides everything you need to install, configure, and fully use the Gemini CLI with proper explanations.

---

# 🚀 **What is Gemini CLI?**

Gemini CLI is a command-line interface that gives you direct access to Google’s Gemini models.
You can:

* Generate and edit code
* Read/write files
* Run shell commands
* Automate tasks
* Use tools like Google Search, file operations, and more
* Work with GEMINI.md context files

### ✅ **Free Tier Limits**

* **60 requests per minute**
* **1,000 requests per day** (when logged in with a Google account)

---

# 🛠️ **Installation & Setup**

### **Requirements**

* Node.js **20+**

### **Installation Commands**

```bash
npm install -g @google/gemini-cli
gemini -v
npm upgrade -g @google/gemini-cli
```

---

# 🧩 **First Launch**

Start Gemini CLI:

```bash
gemini
```

### **Initial Setup Steps**

1. Choose a **Theme** (Light/Dark)
2. Select **Authentication Method**:

   * Google Login (recommended)
   * Gemini API Key
   * Vertex AI Service Account

---

# 🖥️ **Interface Overview**

Gemini CLI works like a chat inside your terminal with extra tools & file control.

### **Essential Commands**

```bash
/help        → Show all commands
/docs        → Documentation
/stats       → Usage stats
/tools       → List available tools
/quit        → Exit the CLI
```

### **File Referencing**

Use **@filename** to give Gemini access to files.

```bash
@app.py
@README.md
@components/Header.tsx
```

### **Shell Mode**

```bash
!      → Enter shell mode
pwd    → Run commands
ESC    → Exit shell mode
```

Shell mode allows running system commands without leaving Gemini.

---

# ⚙️ **Command Line Options**

### **Version Check**

```bash
gemini -v
gemini --version
```

### **Model Selection**

```bash
gemini -m "gemini-flash-2.5"
gemini -m "gemini-pro-2.5"
```

### **Prompt Without Opening Chat**

```bash
gemini -p "write a python function"
gemini "convert js to ts"
```

### **Debug Mode**

Shows detailed logs.

```bash
gemini -d
gemini -d -p "your prompt"
```

### **Save Summary to File**

```bash
gemini --session-summary "session.txt"
```

### **YOLO Mode**

Runs tools without asking permission.

```bash
gemini -y
gemini --yolo
```

⚠️ Not recommended unless needed.

---

# 📁 **GEMINI.md Files**

Gemini reads context from special files named **GEMINI.md**.

### **Hierarchy (Priority Order)**

1. **Global file** → `~/.gemini/GEMINI.md`
2. **Project root folder**
3. **Local subfolders**

### **Memory/Context Commands**

```bash
/memory show
/memory refresh
```

---

# 🧰 **Available Tools**

List tools:

```bash
/tools
```

Common tools:

* GoogleSearch
* ReadFile
* WriteFile
* mkdir
* Shell

Each tool may need permissions unless running in YOLO mode.

---

# ⭐ **Best Practices**

### ✅ **DO**

* Open Gemini from **your project folder**
* Add project rules to **GEMINI.md**
* Allow tool permissions after reviewing

### ❌ **DON’T**

* Start Gemini from your home directory (`~`)
* Use YOLO mode all the time
* Place GEMINI.md randomly

---

# 🔄 **Common Workflows**

### **1. Ask for Git Help**

```bash
gemini "show me git commands for rebasing"
```

### **2. Generate Code in a Project**

```bash
cd my-project
gemini
```

### **3. Modify a File**

```bash
gemini
> In @app.py add error handling logic
```

### **4. Restore a Checkpoint**

```bash
gemini -c
/restore
```

---

# 🛠️ **Troubleshooting**

### **Flash Model Issue**

If quota is low, Gemini CLI may auto-switch to **Flash model**.

### **Context Not Loading**

Use debug mode:

```bash
gemini -d
```

### **Port Already in Use**

Gemini will suggest a new port automatically.

---

# 📚 **Extra Commands**

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

# ⚡ **Quick Reference (Cheat Sheet)**

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

---
\
