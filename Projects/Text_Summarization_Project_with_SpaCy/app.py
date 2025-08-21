import streamlit as st
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

# =============================
# Summarizer Function
# =============================
def summarize_text_spacy(
    text: str,
    nlp,
    ratio: float = 0.3,
    min_sentences: int = 3,
    max_sentences: int = 8
) -> str:
    if not text or not text.strip():
        return ""
    
    doc = nlp(text)
    sentences = list(doc.sents)
    if not sentences:
        return text.strip()
    
    stopwords = STOP_WORDS
    punct_set = set(punctuation)
    
    word_freq = {}
    for token in doc:
        if token.is_space or token.is_punct:
            continue
        if token.is_stop:
            continue
        if token.text in punct_set:
            continue
        key = token.lemma_.lower()
        if not key or key in stopwords:
            continue
        word_freq[key] = word_freq.get(key, 0) + 1
    
    if not word_freq:
        return " ".join([s.text.strip() for s in sentences[:min_sentences]])
    
    max_f = max(word_freq.values())
    for w in word_freq:
        word_freq[w] = word_freq[w] / max_f
    
    sent_scores = {}
    for sent in sentences:
        score = 0.0
        length = 0
        for token in sent:
            if token.is_space or token.is_punct:
                continue
            key = token.lemma_.lower()
            if key in word_freq:
                score += word_freq[key]
            length += 1
        if length > 0:
            score /= length
            sent_scores[sent] = score
    
    K = max(min_sentences, int(len(sentences) * ratio))
    K = min(K, max_sentences, len(sentences))
    
    top = nlargest(K, sent_scores, key=sent_scores.get)
    chosen = sorted(top, key=lambda s: s.start)
    
    return " ".join([s.text.strip() for s in chosen])

# =============================
# Streamlit Frontend
# =============================
st.set_page_config(page_title="Text Summarizer", page_icon="📝", layout="wide")
st.title("📝 Extractive Text Summarizer")
st.write("Upload a file or paste text below to generate a summary.")

# Load spaCy model once
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# Sidebar controls
st.sidebar.header("⚙️ Settings")
ratio = st.sidebar.slider("Summary Length (ratio of original)", 0.1, 0.9, 0.3, 0.05)
min_sents = st.sidebar.number_input("Minimum Sentences", 1, 10, 3)
max_sents = st.sidebar.number_input("Maximum Sentences", 1, 20, 8)

# Input section
input_method = st.radio("Choose Input Method:", ["Paste Text", "Upload File"])

input_text = ""
if input_method == "Paste Text":
    input_text = st.text_area("Enter your text here:", height=200)
elif input_method == "Upload File":
    uploaded_file = st.file_uploader("Upload a .txt, .pdf, or .docx file", type=["txt", "pdf", "docx"])
    if uploaded_file:
        ext = uploaded_file.name.split(".")[-1].lower()
        if ext == "txt":
            input_text = uploaded_file.read().decode("utf-8")
        elif ext == "pdf":
            import pdfplumber
            with pdfplumber.open(uploaded_file) as pdf:
                input_text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        elif ext == "docx":
            from docx import Document
            doc = Document(uploaded_file)
            input_text = "\n".join(p.text for p in doc.paragraphs)

# Run summarization
if st.button("Generate Summary"):
    if input_text.strip():
        summary = summarize_text_spacy(input_text, nlp, ratio=ratio, min_sentences=min_sents, max_sentences=max_sents)
        st.subheader("📄 Original Text")
        st.write(input_text)
        st.subheader("✂️ Generated Summary")
        st.success(summary)
    else:
        st.warning("Please provide text or upload a file first.")
