Samajh gayi Rimza — tum chaho ke README **formatted ho**, aur usme yeh bhi mention ho ke project **uv package manager + Gemini CLI + Streamlit + Python** se banaya gaya hai.

Yeh lo **clean, formatted, simple README.md**:

---

````md
# Streamlit Gemini Calculator (Built with uv + Gemini CLI + Python)

This is a simple AI calculator made using **uv package manager**, **Gemini CLI**, **Streamlit**, and **Python**.  
You enter any math expression, and Google Gemini calculates the answer instantly.

---

## 🌐 Live Demo

https://gyaznevgtxxwcba8wlmt2w.streamlit.app/

---

## 📦 Setup Using uv (Recommended)

Make sure you have **uv** installed.  
If not:

```bash
pip install uv
uv init 
````

### Create and install environment using uv

```bash
uv venv
uv pip install streamlit 
```

---

## 🔑 Add Gemini API Key

Windows:

```bash
set GOOGLE_API_KEY="your_api_key"
```

Mac/Linux:

```bash
export GOOGLE_API_KEY="your_api_key"
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser.
Example use:

```
25 * 4 + 10
```

Gemini will return the result.

---

## 📁 Project Files

* app.py
* README.md
* requirements.txt (optional if using uv)

---

## ✨ Tech Used

* **uv** (Python package & environment manager)
* **Gemini CLI / Google GenAI**
* **Streamlit**
* **Python**

---

## 👩‍💻 Author

Made by Rimza.

```

=
