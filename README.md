# sana.ai - Local AI Bug Fix & Code Review Tool

🛠️ **sana.ai** is a Streamlit-based local AI-powered tool to **review**, **detect bugs**, and **suggest fixes** for Python code. It uses the powerful **Mistral model** via the **Ollama CLI** for **local inference**, enabling fast, secure, and completely offline code analysis.

---

## 🔍 Features

- ✅ Directly input Python code in the app
- 🧠 Analyzes code using Ollama’s Mistral model locally
- 🐛 Detects bugs and poor practices
- 💡 Suggests improvements and provides corrected code
- 🌐 No internet or external APIs needed
- 🎛️ Simple and interactive UI powered by Streamlit

---

## 📁 Project Overview

This app allows you to:

1. Input Python code via the Streamlit interface.
2. The code is passed to a locally running Mistral model via the Ollama CLI.
3. The AI returns:
   - A list of bugs/issues
   - Suggestions to fix them
   - A corrected version of the code

**⚡️ Everything runs locally – no OpenAI, Gemini, or cloud APIs.**

---


---

## ⚙️ How It Works (Execution Flow)

### 1. User Interface (Streamlit)
- Run with: `streamlit run app.py`
- User inputs Python code directly in the text area
- Code is displayed in the UI

### 2. Analyze the Code
- On clicking the **"Review Code with AI"** button:
  - The input is sent to `analyze_code_with_ollama()` in `ollama_infer.py`

### 3. AI Inference via Ollama
- `ollama_infer.py` builds a prompt and runs:
  ```bash
  ollama run mistral
  
Mistral returns:

A list of issues

Fix suggestions

Fixed code

4. Result Display
Streamlit displays the result as markdown:

🔍 Issues

💡 Fix Suggestions

✅ Fixed Code in a code block

💡 Example
#Input:
  ```bash

def calc():
    print(x)

calc()
```

#Output:
  ```bash
### Issues
- Variable `x` is undefined
- Might cause a NameError

### Fix Suggestions
- Define variable `x` before using it

### Fixed Code
```python
def calc():
    x = 5
    print(x)

calc()

```

## 🧰 Requirements

- Python 3.x
- [Ollama](https://ollama.com) installed and running
- Mistral model pulled via:
  ```bash
  ollama pull mistral
Install dependencies:

pip install -r requirements.txt
🚀 Running the Application
Start the Ollama service (make sure mistral is available).

Run the Streamlit app:

streamlit run app.py
Open the local Streamlit URL in your browser.

Paste your Python code and click Review Code with AI.

🔐 Security / Offline Mode
✅ Fully offline and secure

🧠 No API keys required

🔌 No internet dependency

🖥️ All inference happens on your local machine


🙌 Acknowledgments
Mistral AI – for the amazing open-source LLMs

Ollama – for making local inference accessible

Streamlit – for the slick, interactive UI

Happy Debugging with sana.ai! ⚡





