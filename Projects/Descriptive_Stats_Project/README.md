
# 📊 Descriptive Statistics Project – Household Income & Expense Analysis

📅 **Project Date:** June 30, 2025  
📁 **Project Name:** Day32_Descriptive_Stats_Project

---

## 📌 Objective

This project demonstrates the application of **descriptive statistical analysis** on a **household income-expense** dataset. The aim is to understand the data distribution, central tendency, spread, and relationships between variables.

---

## 🧠 What You Will Learn

- How to perform **basic descriptive statistics**: mean, median, mode, std, IQR, etc.
- Visualization of **categorical** and **numerical** variables using plots
- Use of **group-by** and **correlation matrix** to gain insights
- Real-life use case: **Coefficient of Variation (CV)** for stock risk comparison

---

## 📦 Technologies Used

- `Python`
- `Pandas`, `NumPy` for data analysis
- `Matplotlib`, `Seaborn` for data visualization
- `SciPy` for skewness and kurtosis

---

## 📂 Dataset Overview

- **Source**: Local CSV file
- **Features**:
  - Monthly and Annual Household Income
  - Expenses and EMI/Rent
  - Number of Family and Earning Members
  - Highest Qualification in Household

---

## 📈 Key Analysis Performed

1. **Central Tendency**
   - Mean monthly expense: ₹18,818
   - Median: ₹15,500
   - Mode: ₹25,000

2. **Spread**
   - Standard Deviation and Variance
   - Interquartile Range (IQR)
   - Boxplot for outliers

3. **Distributions**
   - Skewness: 1.16 (Right-skewed)
   - Kurtosis: 0.73 (Slightly peaked)

4. **Visual Insights**
   - Bar plots for qualification-wise income
   - Correlation matrix heatmap
   - Boxplots to detect outliers

5. **Group Analysis**
   - Average income based on qualification levels

6. **Real-world Application**
   - CV of two stocks (Stock A: 0.67, Stock B: 0.50)
   - Stock B has less risk and more consistent returns

---

## 📌 How to Run

1. Clone this project or open the notebook directly in Jupyter or Google Colab
2. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn scipy
3. Update the CSV path inside the notebook:

   ```python
   income_df = pd.read_csv("your_path/Inc_Exp_Data.csv")
   ```
4. Run the cells step-by-step to explore insights

---

## ✅ Conclusion

* Most households have a **single earning member**
* Expense data is **right-skewed** with a few high outliers
* Qualification has a clear impact on household income
* CV method is effective for comparing investment risk

---

> 📍 This project builds a strong foundation in descriptive statistics and its application to real-life data for analysis and decision-making.


---
