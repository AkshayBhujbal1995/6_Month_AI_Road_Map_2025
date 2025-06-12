````markdown
# 📊 Day 23 – My First Streamlit App (with a Secret Message)

Welcome to my first Streamlit mini project!  
This was part of my **Full Stack Data Science Course – EDA Module**  
I built it using **Notepad, CMD, and Streamlit** — no IDE! 🚀

---

## 💡 What This App Does

- Displays a welcome title and subtitle  
- Includes a fun button  
- When clicked, reveals a secret success message

---

## 💻 Code (app.py)

```python
import streamlit as st

# Title
st.title("👋 Welcome to my app")

# Subtitle
st.subheader("This is my first Streamlit app with a surprise! 🎉")

# Button
if st.button("Click me for a secret 🎁"):
    st.success("🎊 You’re awesome! Keep learning and coding 🚀")
````

---

## ▶️ How to Run This App

1. Make sure Python and Streamlit are installed:

```bash
pip install streamlit
```

2. Save the code above as `app.py` in your folder.

3. Open CMD and navigate to your folder:

```bash
cd "C:\Users\aksha\OneDrive\Desktop\Full stack Data Science course\GITHUB Uploads\4_EDA_Exploratory_Data_Analysis"
```

4. Run the app:

```bash
streamlit run app.py
```

5. It will open in your browser automatically!

---

## 🖼️ Screenshot

> *(If you have screenshots, upload them to this repo and update the file path below)*

```markdown
![My Streamlit App](Streamlit_My_1st_App_1.png)
```

---

## 👨‍💻 Author

**Akshay Bhujbal**
Learning Streamlit, EDA, and Python one day at a time!

---

## 🔖 Tags

\#Python #Streamlit #DataScience #EDA #100DaysOfCode #BeginnerToPro #AkshayBhujbal
