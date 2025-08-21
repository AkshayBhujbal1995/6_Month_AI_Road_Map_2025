
# 📝 Text Summarizer (spaCy + Streamlit)

An **Extractive Text Summarization App** built as part of my NLP journey 🚀.  
This project falls under **Natural Language Processing (NLP)** — the branch of AI that helps computers understand, interpret, and generate human language.  

With this app, users can **paste text** or **upload documents** (`.txt`, `.pdf`, `.docx`) and instantly get a concise summary.  
It’s simple, interactive, and showcases the power of NLP in real-world applications.  

---

## 📌 What This Project Does
- Accepts **raw text or uploaded files** (TXT, PDF, DOCX)  
- Uses **spaCy NLP pipeline** to process the content  
- Removes stopwords & punctuation, builds a **word frequency table**  
- Scores sentences and extracts the most informative ones  
- Lets users **control summary ratio** (10–90%) and **set min/max sentences**  
- Presents the final summary through a clean **Streamlit frontend**  

---

## 🧠 Why This Matters (NLP Context)
Text Summarization is a **core NLP task** that saves time by reducing large documents into their **key insights**.  
This project uses **Extractive Summarization**, where important sentences are pulled directly from the text (instead of generating new ones).  

👉 Applications of NLP Summarization:
- 📚 Education: Summarizing long study notes or research papers  
- 📰 Media: Condensing news articles into quick reads  
- 💼 Business: Creating short reports from long documents  
- ⚖️ Legal: Reducing lengthy case documents into highlights  

---

## ⚙️ Tech Stack
- **Python 3** 🐍  
- **spaCy** (`en_core_web_sm`) for NLP  
- **Streamlit** for frontend UI  
- **pdfplumber** → Extract text from PDFs  
- **python-docx** → Extract text from Word files  
- **heapq (nlargest)** → Select top-ranked sentences  

---

## 📊 How It Works (Behind the Scenes)

1. **Tokenization** – Split text into words and sentences using spaCy  
2. **Stopword & Punctuation Removal** – Clean noisy tokens  
3. **Word Frequency Calculation** – Count how often each word occurs  
4. **Normalization** – Scale frequencies between 0 and 1  
5. **Sentence Scoring** – Add up scores of words in each sentence  
6. **Ranking** – Select top sentences based on ratio or min length  
7. **Final Summary** – Output sentences in original order  

---

## 📷 Screenshots

### 1️⃣ Overall App Look
![App Look](Out_1.PNG)

### 2️⃣ Upload File & Generate Summary
![Uploaded File Result](Out_2.PNG)

### 3️⃣ Summary Length = 50%
![Summary 50%](Out_3.PNG)

### 4️⃣ Minimum Sentences = 2
![2 Sentences](Out_4.PNG)

---

## 🚀 Installation & Run

1. Clone this repo:
```bash
   git clone https://github.com/your-username/text-summarizer.git
   cd text-summarizer
```

2. Install dependencies:
```bash
 pip install -r requirements.txt
```

3. Download spaCy model:
```bash
   python -m spacy download en_core_web_sm
```

4. Run the app:
 ```bash
   streamlit run app.py
```
---

## 🌟 Future Enhancements

* Add **Abstractive Summarization** using Transformers (BART, T5)
* Add **Named Entity Recognition (NER)** highlighting in summary
* Export summary as `.txt` or `.pdf`
* Support for **multiple languages**

---

## 🙌 Author

**Akshay Bhujbal**
📌 Project as part of **100 Days of AI/Data**
🎯 Exploring **NLP, spaCy, and Streamlit**


