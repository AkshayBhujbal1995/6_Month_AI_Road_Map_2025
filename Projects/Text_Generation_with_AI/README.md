
# 📘 Day43_Text_Generation_Using_Google_Generative_AI

This project demonstrates how to build a simple text generation system using **Google’s Gemini 2.5 Flash model** via the `google-generativeai` Python SDK.  
You’ll connect to Gemini using Python, send a prompt, and receive an AI-generated response.

---

## 📚 What You'll Learn

- What is Generative AI and how it works  
- How to use the `google-generativeai` Python SDK  
- How to send text prompts and receive creative/informative replies  
- How to print, style, and format model outputs using IPython

---

## 🛠️ Technologies Used

- Python  
- Google Generative AI (Gemini 2.5 Flash)  
- `google-generativeai` SDK  
- `IPython.display` for Markdown output  

---

## ⚙️ Setup Instructions

### ✅ Step 1: Install Required Libraries
```bash
pip install -U google-generativeai
````

### ✅ Step 2: Get API Key

* Go to [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
* Enable **Generative Language API** in Google Cloud

### ✅ Step 3: Add API Key in Code

```python
import google.generativeai as genai
genai.configure(api_key="your_api_key_here")
```

---

## 📄 How It Works

1. Load the Gemini 2.5 Flash model:

```python
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
```

2. Send a prompt and generate a response:

```python
response = model.generate_content("Hello! How are you doing today?")
print(response.text)
```

3. Format output using Markdown:

```python
from IPython.display import Markdown
import textwrap

def to_markdown(text):
    text = text.replace('-', ' *')
    return Markdown(textwrap.indent(text, '> ', lambda _: True))

to_markdown(response.text)
```

---

## 💡 Example Prompt

```python
prompt = """
Explain in simple words:
1. What is Artificial Intelligence (AI)?
2. What is Generative AI?
3. What is Agentic AI?
4. How are they different from each other?
"""

response = model.generate_content(prompt)
to_markdown(response.text)
```

---

## ✅ Conclusion

* ✅ Built a working text generation app using **Gemini 2.5 Flash**
* ✅ Learned how to prompt Gemini and print formatted output
* ✅ This sets the foundation for building **chatbots**, **creative writers**, and **text-based agents**

---
