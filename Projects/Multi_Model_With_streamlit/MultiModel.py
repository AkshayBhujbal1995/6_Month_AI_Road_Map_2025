# Day 44 – Text and Image AI App Using Gemini
# Final Version: With answer persistence using session_state

import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import google.generativeai as genai
from PIL import Image

# Step 1: Configure Gemini API Key
genai.configure(api_key="AIzaSyDCxXIK9T9xR1HusdKvKCZPQ6NciKDiXhQ")  # Replace with your key

# Step 2: Load Model
model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

# Step 3: Set up Page
st.set_page_config(page_title="Gemini AI - Text or Image")
st.title("Gemini AI - Ask a Question or Upload an Image")
st.write("You can either ask a question or upload an image. Gemini will respond accordingly.")

# Step 4: Initialize session state for answers
if "text_answer" not in st.session_state:
    st.session_state.text_answer = ""
if "image_answer" not in st.session_state:
    st.session_state.image_answer = ""
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

# Step 5: Inputs
prompt = st.text_area("Ask a question (optional):", placeholder="Example: What is Artificial Intelligence?")
image_file = st.file_uploader("Upload an image (optional):", type=["jpg", "jpeg", "png"])

# Step 6: Clear Button
if st.button("Clear Output"):
    st.session_state.text_answer = ""
    st.session_state.image_answer = ""
    st.session_state.uploaded_image = None
    st.rerun()

# Step 7: Action Buttons
col1, col2 = st.columns(2)

# Generate text response
with col1:
    if st.button("Generate Answer from Question"):
        if not prompt.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Generating answer..."):
                try:
                    response = model.generate_content(prompt.strip())
                    st.session_state.text_answer = response.text
                except Exception as e:
                    st.error(f"Error: {e}")

# Generate image description
with col2:
    if st.button("Describe Uploaded Image"):
        if not image_file:
            st.warning("Please upload an image.")
        else:
            try:
                image = Image.open(image_file)
                st.session_state.uploaded_image = image
                with st.spinner("Describing image..."):
                    response = model.generate_content([image])
                    st.session_state.image_answer = response.text
            except Exception as e:
                st.error(f"Error: {e}")

# Step 8: Show Outputs if present
if st.session_state.text_answer:
    st.subheader("AI Answer:")
    st.markdown(st.session_state.text_answer)

if st.session_state.image_answer:
    st.subheader("Image Description:")
    if st.session_state.uploaded_image:
        st.image(st.session_state.uploaded_image, caption="Uploaded Image", use_column_width=True)
    st.markdown(st.session_state.image_answer)

# Step 9: Instructions (only show if no answers)
if not st.session_state.text_answer and not st.session_state.image_answer:
    st.markdown("""
---
Instructions:
- Use "Generate Answer from Question" if you only want to ask a question.
- Use "Describe Uploaded Image" if you only want to upload and describe an image.
- Both inputs are optional and processed separately.
- Click "Clear Output" to reset the app.

To run this app:
1. Save the code in a file named app.py
2. Open terminal and run: streamlit run app.py
""")
