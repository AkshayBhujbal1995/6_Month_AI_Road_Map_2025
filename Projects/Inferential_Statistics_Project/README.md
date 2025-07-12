
# 📊 Descriptive & Inferential Statistics on Sales Dataset

📅 **Project Date:** July 4, 2025  
📁 **Project Name:** Day36_Inferential_Stat_Project

---

## 🎯 Objective

This project demonstrates how to apply both **descriptive** and **inferential statistics** to a **simulated sales dataset**. You’ll explore statistical measures like mean, standard deviation, confidence intervals, and hypothesis testing to uncover business insights.

---

## 🧠 What You Will Learn

- Generate synthetic business data using NumPy
- Perform summary statistics (mean, median, mode, std, variance)
- Calculate group-wise statistics by product category
- Build confidence intervals using `scipy.stats`
- Run hypothesis tests (1-sample t-test)
- Visualize data distribution using histograms, boxplots, and bar charts

---

## 🛠️ Technologies Used

- `Python`
- `NumPy` and `Pandas` for data generation and manipulation
- `Matplotlib` and `Seaborn` for visualizations
- `Scipy.stats` for inferential statistics

---

## 📁 Dataset Overview

- **Synthetic dataset** with 20 products
- Columns include:
  - `product_id`
  - `product_name`
  - `category` (Electronics, Clothing, Home, Sports)
  - `units_sold` (generated using Poisson distribution)
  - `sale_date` (daily from Jan 1, 2023)

---

## 🔍 Key Analysis Steps

### ✅ Descriptive Statistics
- Calculated:
  - Mean: `18.8`
  - Median: `18.5`
  - Mode: `17`
  - Variance: `10.91`
  - Standard Deviation: `3.30`
- Group-wise stats by category (Total, Average, Std Dev)

### 📏 Inferential Statistics

#### ✅ Confidence Intervals:
- **95% CI:** (17.25, 20.34)
- **99% CI:** (16.69, 20.91)

#### ✅ One-Sample t-test:
- Null Hypothesis (H₀): Mean = 20  
- Result: **Fail to Reject** H₀ (p = 0.12)

---

## 📊 Visualizations

- ✅ Histogram with KDE and vertical lines for mean/median/mode
- ✅ Boxplot of units sold per category
- ✅ Bar plot of total sales per category

---

## ✅ Conclusion

- The average units sold per product ≈ `18.8`, close to 20.
- Confidence intervals show the true mean lies within a reasonable range.
- Based on p-value > 0.05, we **do not have strong evidence** to reject the assumption that mean units sold is 20.
- Highest variation in sales observed in the **Clothing** category.
- Distribution appears slightly skewed but mostly consistent.

---

## 🚀 How to Run This Project

1. Clone the repository or open the `.ipynb` file.
2. Make sure you have the following libraries:
   ```bash
   pip install numpy pandas matplotlib seaborn scipy


3. Run the notebook cells sequentially to view results and visualizations.

---

> 📈 This project simulates a real-world sales analysis workflow using core statistical techniques and visual analytics.



---

