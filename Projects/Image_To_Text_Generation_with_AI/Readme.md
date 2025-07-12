
# Project_Image_to_Text_Using_Google_Generative_AI

This project demonstrates how to extract text-based insights from images using **Google’s Generative AI (Gemini 2.5 Flash model)**.  
You’ll upload an image and receive a description, analysis, or answer from Gemini — all done through Python.

---

## 📚 What You’ll Learn

- How to work with multimodal AI (image + text)
- How to use `google-generativeai` Python SDK
- How to send image prompts and receive text responses
- How to build an image-to-text system using Gemini models
- How to style and print responses with IPython Markdown

---

## 🔧 Technologies Used

- Python
- Google Generative AI (google-generativeai)
- Gemini 2.5 Flash model
- PIL (Python Imaging Library)
- IPython for Markdown output

---

## ⚙️ Setup Instructions

> 📌 Prerequisites:
- Python installed
- API key from [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
- Generative Language API enabled in Google Cloud

### 1. Install the Required Library

```bash
pip install -U google-generativeai
````

---

### 2. Import Required Libraries

```python
import google.generativeai as genai
from PIL import Image
from IPython.display import Markdown
import textwrap
```

---

### 3. Configure API Key

```python
genai.configure(api_key="YOUR_API_KEY")
```

---

### 4. Load the Gemini Model

```python
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
```

---

### 5. Upload Image and Get Text Response

```python
img = Image.open("your_image_path.png")

response = model.generate_content(
    [img],
    generation_config={"temperature": 0.4}
)

print(response.text)
```

---

### 6. Format the Output Nicely (Markdown Style)

```python
def to_markdown(text):
    text = text.replace('*', '•')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

to_markdown(response.text)
```

---

## ✅ Example Use Cases

* Image captioning
* Visual question answering
* Scene description or understanding
* Extracting text or context from photos, screenshots, charts, etc.

---

## 📌 Conclusion

* We successfully built an **image-to-text AI system** using Gemini 2.5 Flash.
* Learned how to use multimodal capabilities of Generative AI.
* This opens the door for powerful apps like AI tutors, visual agents, and intelligent assistants!

---

🔁 **Next Steps:** Try combining both text and image prompts for complex tasks!

---
