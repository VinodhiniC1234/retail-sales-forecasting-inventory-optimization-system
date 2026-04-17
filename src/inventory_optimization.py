import pandas as pd
from data_preprocessing import load_data, clean_data

# Load data
df = load_data()
df = clean_data(df)

# -----------------------------
# BASIC INVENTORY LOGIC
# -----------------------------

# Average demand (daily sales)
avg_demand = df["Sales"].mean()

# Demand variability
std_demand = df["Sales"].std()

# Lead time (assume supplier delay in days)
lead_time = 5

# Safety Stock formula
safety_stock = 1.5 * std_demand

# Reorder Point formula
reorder_point = (avg_demand * lead_time) + safety_stock

# -----------------------------
# OUTPUT REPORT
# -----------------------------
print("\n📦 INVENTORY OPTIMIZATION REPORT")
print("----------------------------------")
print(f"Average Daily Demand : {avg_demand:.2f}")
print(f"Safety Stock         : {safety_stock:.2f}")
print(f"Reorder Point        : {reorder_point:.2f}")

# Example recommendation
if avg_demand < reorder_point:
    print("\n⚠️ Recommendation: Reorder Stock Soon")
else:
    print("\n✅ Stock Level is Safe")