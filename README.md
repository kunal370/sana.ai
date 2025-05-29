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
## 🔐 Security / Offline Mode

- ✅ Fully offline and secure
- 🧠 No API keys required
- 🔌 No internet dependency
- 🖥️ All inference happens on your local machine
---

## ⚙️ How It Works (Execution Flow)

### 1. User Interface (Streamlit)
- Run with: `streamlit run app.py`
- User uploads Python code directly to sana.ai
- Code is displayed in the UI

### 2. Analyze the Code
- On clicking the **"Review Code with AI"** button:
  - The input is sent to `analyze_code_with_ollama()` in `ollama_infer.py`

### 3. AI Inference via Ollama
- `ollama_infer.py` builds a prompt and runs:
  ```bash
  ollama run mistral
  
**Mistral returns:**
- A list of issues
- Fix suggestions
- Fixed code

**4. Result Display**
Streamlit displays the result as markdown:

- 🔍 Issues
- 💡 Fix Suggestions
- ✅ Fixed Code in a code block

## 💡 Example

![image](https://github.com/user-attachments/assets/2ad63545-7bea-49da-adbd-30030ac0c567)

![image](https://github.com/user-attachments/assets/e5dcdc2e-11fe-4804-ac84-87602bd58659)

![image](https://github.com/user-attachments/assets/9252059b-6ec2-4269-8630-d598be508c83)
