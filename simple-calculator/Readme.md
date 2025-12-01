# Gemini CLI Streamlit Calculator

This is a simple AI-powered calculator built using Gemini CLI and Streamlit. It allows users to enter any mathematical expression and get instant results generated through Google's Gemini model. The interface is clean, minimal, and designed for quick calculations without any complexity. The project also includes a live deployed version so anyone can use the calculator directly without running the code locally.

Live Demo Link: https://gyaznevgtxxwcba8wlmt2w.streamlit.app/

To use this project locally, make sure Python 3.9 or above is installed. You can optionally create a virtual environment by running `python -m venv venv` and activating it. After that, install the required packages using `pip install -r requirements.txt` or install them manually by running `pip install streamlit google-genai`.

Before running the calculator, set your Gemini API key as an environment variable. On macOS or Linux, use `export GOOGLE_API_KEY="your_api_key"`, and on Windows, use `set GOOGLE_API_KEY="your_api_key"`. This key is necessary for the calculator to communicate with the Gemini model.

To start the app, simply run `streamlit run app.py`. This will launch the application in your browser at `http://localhost:8501`. Once opened, type any math expression such as `25 * 12 / 3` and Gemini will return the output instantly. The app handles both basic and slightly advanced expressions and includes simple error handling to avoid crashes.

The project structure is very simple: an `app.py` file for the logic, a `requirements.txt` for dependencies, and a `README.md` for documentation. The goal of this project is to demonstrate how Streamlit can be combined with Gemini to build small, useful AI tools quickly and easily.

This calculator is ideal for beginners learning Streamlit, students practicing AI integration, or anyone wanting an example of Gemini CLI usage. Make sure to keep your API key private and do not push it to GitHub. Also note that while Gemini handles math well, it is always safer to double-check important calculations.

Created by Rimza using Gemini + Streamlit.
