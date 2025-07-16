import streamlit as st
from gtts import gTTS
from gtts.lang import tts_langs
import numpy as np
import os

# 📘 Get all supported languages as a dictionary: {'en': 'English', 'hi': 'Hindi', ...}
languages = tts_langs()

# 🧾 Create dropdown-friendly list like: ['English (en)', 'Hindi (hi)', ...]
language_options = [f"{name} ({code})" for code, name in languages.items()]

# 🌟 Streamlit App Title
st.markdown("<h1 style='color:#4b8bff;'>🗣️ Text-to-Speech App</h1>", unsafe_allow_html=True)
st.markdown("Convert your text into spoken words using Google Text-to-Speech.")
st.markdown("---")

# 📝 Text input
user_text = st.text_area("✏️ Enter the text to convert to speech:", height=150)

# 🌍 Language selector from full list
selected_lang = st.selectbox("🌐 Choose a language", options=language_options)

# Extract code from selection (e.g., 'English (en)' → 'en')
lang_code = selected_lang.split("(")[-1].replace(")", "").strip()

# 🎤 Convert and play
if st.button("🔊 Convert and Play"):
    if user_text.strip() == "":
        st.warning("Please enter some text to convert.")
    else:
        tts = gTTS(text=user_text, lang=lang_code)
        file_path = "tts_output.mp3"
        tts.save(file_path)

        # Play audio
        with open(file_path, "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3")

        st.success(f"✅ Speech generated in {selected_lang}!")
