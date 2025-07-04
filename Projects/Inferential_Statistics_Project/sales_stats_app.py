import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

st.set_page_config(layout="wide")

# Create synthetic dataset
np.random.seed(42)
data = {
    'product_id': range(1, 21),
    'product_name': [f'Product {i}' for i in range(1, 21)],
    'category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports'], 20),
    'units_sold': np.random.poisson(lam=20, size=20),
    'sale_date': pd.date_range(start='2023-01-01', periods=20, freq='D')
}
df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.title("Filter Options")
category_filter = st.sidebar.multiselect("Select Categories", options=df['category'].unique(), default=df['category'].unique())
filtered_df = df[df['category'].isin(category_filter)]

# App title
st.title("Sales Data: Descriptive and Inferential Statistics")

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(filtered_df)

# Descriptive statistics
st.subheader("Descriptive Statistics")
st.write(filtered_df['units_sold'].describe())

# Additional statistics
mean_val = filtered_df['units_sold'].mean()
median_val = filtered_df['units_sold'].median()
mode_val = filtered_df['units_sold'].mode()[0]
std_val = filtered_df['units_sold'].std()
var_val = filtered_df['units_sold'].var()

st.markdown(f"""
- Mean: {mean_val:.2f}
- Median: {median_val:.2f}
- Mode: {mode_val}
- Standard Deviation: {std_val:.2f}
- Variance: {var_val:.2f}
""")

# Confidence Interval (95%)
st.subheader("95% Confidence Interval for Mean")
n = len(filtered_df)
dfree = n - 1
se = std_val / np.sqrt(n)
t_score = stats.t.ppf(0.975, dfree)
margin_error = t_score * se
ci_low = mean_val - margin_error
ci_high = mean_val + margin_error
st.write(f"95% Confidence Interval: ({ci_low:.2f}, {ci_high:.2f})")

# Hypothesis Test
st.subheader("Hypothesis Testing (Is mean = 20?)")
t_stat, p_val = stats.ttest_1samp(filtered_df['units_sold'], 20)
st.write(f"T-statistic: {t_stat:.3f}")
st.write(f"P-value: {p_val:.4f}")
if p_val < 0.05:
    st.error("Reject the null hypothesis: Mean is significantly different from 20.")
else:
    st.success("Fail to reject the null hypothesis: Mean is not significantly different from 20.")

# Visualizations
st.subheader("Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Histogram with KDE")

    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df['units_sold'], bins=10, kde=True, ax=ax1)
    plt.axvline(mean_val, color='red', linestyle='--', label='Mean')
    plt.axvline(median_val, color='blue', linestyle='--', label='Median')
    plt.axvline(mode_val, color='green', linestyle='--', label='Mode')
    plt.legend()
    st.pyplot(fig1)

with col2:
    st.markdown("Boxplot by Category")
    fig2, ax2 = plt.subplots()
    sns.boxplot(x='category', y='units_sold', data=filtered_df, ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

st.markdown("Bar Plot – Total Units Sold per Category")
total_sales = filtered_df.groupby("category")['units_sold'].sum().reset_index()
fig3, ax3 = plt.subplots()
sns.barplot(x='category', y='units_sold', data=total_sales, ax=ax3)
st.pyplot(fig3)
