import matplotlib.pyplot as plt
import seaborn as sns
from data_preprocessing import load_data, clean_data

# Load and clean data
df = load_data()
df = clean_data(df)

# Set style
sns.set_style("whitegrid")

# -----------------------------
# 1. SALES TREND OVER TIME
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Sales"])
plt.title("📈 Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 2. CATEGORY WISE SALES
# -----------------------------
plt.figure(figsize=(6,4))
sns.barplot(x="Category", y="Sales", data=df)
plt.title("📊 Category-wise Sales")
plt.show()

# -----------------------------
# 3. PRODUCT DISTRIBUTION
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="Product", data=df)
plt.title("📦 Product Distribution")
plt.show()

print("EDA Completed Successfully!")