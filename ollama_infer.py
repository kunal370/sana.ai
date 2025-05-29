import subprocess
import os

def analyze_code_with_ollama(code: str) -> str:
    prompt = f"""
You are a Python expert AI. Your task is to do the following:
1. Review the Python code below for bugs or poor practices.
2. List issues found.
3. Suggest how to fix them.
4. Return the corrected code.

Use the following format:
### Issues
- Issue 1
- Issue 2

### Fix Suggestions
- Fix 1
- Fix 2

### Fixed Code
```python
# fixed code here
```

Here is the code:
```python
{code}
```
"""

    try:
        process = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return process.stdout.decode()
    except subprocess.CalledProcessError as e:
        return f"❌ Error during Ollama execution:\n```\n{e.stderr.decode()}\n```"
