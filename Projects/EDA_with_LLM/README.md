
# 📊 AI-Powered Exploratory Data Analysis (EDA) with Python, Mistral LLM & Gradio

📅 **Project Date:** June 27, 2025  
📁 **Project Name:** Day29_EDA_WITH_LLM

---

## 🎯 Objective

This project demonstrates a smart and scalable approach to **exploratory data analysis (EDA)** using:
- Manual visualizations and pandas summaries
- AI-powered insights using **Mistral LLM** via **Ollama**
- Interactive web-based EDA app using **Gradio**

---

## 🧠 What You Will Learn

- How to explore and clean tabular data using pandas
- How to build charts using seaborn and matplotlib
- How to connect a **Large Language Model (LLM)** like Mistral to generate automatic insights
- How to build a **Gradio-based web app** for automated EDA

---

## 🛠️ Technologies Used

- `Python`
- `Pandas`, `NumPy` for data wrangling
- `Matplotlib`, `Seaborn` for visualizations
- `Gradio` for web interface
- `Ollama` for connecting to **Mistral LLM**

---

## 📦 Dataset Used

- Titanic Dataset (CSV format)
- Contains 891 rows × 12 columns
- Features include: Passenger ID, Class, Age, Sex, Fare, Survival status, etc.

---

## 📌 Key Features & Flow

### 🔍 Step 1: Manual EDA
- Load dataset with pandas
- View summary statistics (`.describe()`)
- Identify missing values
- Generate bar plots, histograms, and heatmaps

### 🤖 Step 2: AI-Powered Insights
- Pass dataset summary to Mistral LLM using `ollama`
- Get back human-like insights in seconds
- Example insight:
  > "The average age of passengers is ~29.7 with a wide range... Most traveled in 3rd class..."

### 🌐 Step 3: Web Apps with Gradio
- ✅ **Simple App**:
  - Upload any `.csv` file
  - View AI-generated insights

- 📊 **Advanced App**:
  - Upload `.csv`
  - Get:
    - Summary stats
    - Missing value report
    - AI insights
    - Auto-generated histograms
    - Correlation matrix

---

## 🚀 How to Run This Project

### 🧪 Setup Instructions

1. Install the required libraries:
   ```bash
   pip install pandas seaborn matplotlib gradio ollama

2. Start Ollama in your terminal (to use Mistral LLM):

   ```bash
   ollama run mistral
   

3. Run the Python script or notebook with Gradio:

   ```bash
   python eda_with_llm.py
   

4. Access the web app on:

   ```
   http://127.0.0.1:7860
   ```

---

## 📊 Sample Outputs

* ✅ AI-generated insights from dataset summary
* 📉 Visualizations:

  * Histogram for numerical columns
  * Correlation matrix heatmap

---

## ✅ Conclusion

* Successfully created an **AI-powered EDA tool** using Mistral LLM
* Built 2 levels of **Gradio apps**: basic and full-featured
* Makes EDA fast, interactive, and beginner-friendly

---

> 🚀 This project demonstrates how LLMs can assist in real-world data analysis and automation. Perfect for data professionals and AI beginners alike.



---

