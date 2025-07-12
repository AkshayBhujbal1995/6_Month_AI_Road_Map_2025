📅 **Date:** July 13, 2025  
🛠️ **Project Type:** Multimodal AI Web App using Streamlit and Google Gemini

---

## 🚀 Project Overview

This project demonstrates how to build a **multimodal AI application** using **Google's Generative AI (Gemini)** and **Streamlit**.  
The app accepts both **text** and **image** inputs and generates intelligent responses accordingly.

Users can:
- Ask any question using text and get AI-generated answers.
- Upload an image to receive a detailed description from the AI.
- Interact through a simple and clean web interface.

---

## 📚 What You’ll Learn

- How to use `google-generativeai` Python SDK
- How to send text and image input to Google Gemini
- How to use Gemini Flash and Thinking models
- How to create an interactive web UI using Streamlit
- How to deploy a beginner-friendly multimodal AI tool

---

## 🧰 Technologies Used

- **Python**
- **Google Generative AI (Gemini 2.5 Flash model)**
- **Streamlit** for UI
- **PIL** for handling image uploads

---

## ⚙️ Setup Instructions

### 1. Install Required Packages

```bash
pip install streamlit google-generativeai pillow
````

### 2. Get Your API Key

* Go to: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
* Enable **Generative Language API** in Google Cloud
* Copy your API key and replace it in the code:

```python
genai.configure(api_key="YOUR_API_KEY")
```

---

## ▶️ How to Run the App

1. Save the code in a file named `app.py`
2. In terminal or command prompt, run:

```bash
streamlit run app.py
```

---

## 🧪 Features

* Text-only prompt support
* Image-only description support
* Dual input mode supported
* Clear output button to reset interface
* Works completely offline after model/API setup

---

## 🧾 Output Example

* **Question Input:** *"What is Artificial Intelligence?"*
  → AI explains the concept in simple terms.

* **Image Input:** Upload of a temple image
  → AI describes the architecture, symbols, and cultural relevance.

---

## ✅ Conclusion

* Successfully built a beginner-friendly **multimodal AI app** using Gemini.
* Learned how to handle both **textual and visual input** for content generation.
* Great foundation for future **AI-powered assistants**, **document readers**, or **creative tools**.

---

## 📂 Project Structure

```
📦 Multi_Model_With_streamlit/
├── app.py
├── README.md
```

---

## 👤 Author

**Akshay Bhujbal**
🔗 [GitHub Profile](https://github.com/AkshayBhujbal1995)

---

## 📌 Project Links

* 🔹 [Text Generation Project](https://github.com/AkshayBhujbal1995/6_Month_AI_Road_Map_2025/tree/main/Projects/Text_Generation_with_AI)
* 🔹 [Image to Text Project](https://github.com/AkshayBhujbal1995/6_Month_AI_Road_Map_2025/tree/main/Projects/Image_To_Text_Generation_with_AI)
* 🔹 [Multimodal Streamlit App](https://github.com/AkshayBhujbal1995/6_Month_AI_Road_Map_2025/tree/main/Projects/Multi_Model_With_streamlit)
---

