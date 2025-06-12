## Day 23 – My First Streamlit App (with a Secret Message)

This is a simple Streamlit app created using Notepad and CMD — no IDE!

---

## Code (Save as `app.py`)

```python
import streamlit as st

st.title("👋 Welcome to my app")
st.subheader("This is my first Streamlit app with a surprise! 🎉")

if st.button("Click me for a secret 🎁"):
    st.success("🎊 You’re awesome! Keep learning and coding 🚀")
````

---

## How to Run This App (From Scratch)

1. **Install Streamlit**

Open CMD and run:

```bash
pip install streamlit
```

2. **Create the Python File**

* Open Notepad
* Paste the code above
* Save the file as: `app.py`

3. **Open CMD and go to your folder**

Replace the path below with your folder path:

```bash
cd "C:\Users\aksha\OneDrive\Desktop\Full stack Data Science course\GITHUB Uploads\4_EDA_Exploratory_Data_Analysis"
```

4. **Run the App**

```bash
streamlit run app.py
```

5. **App Opens in Browser Automatically**

That’s it! Your first Streamlit app is live and interactive 🎉

---

## Author

**Akshay Bhujbal**
Learning Streamlit one day at a time!

\#Python #Streamlit #DataScience #EDA #BeginnerToPro
