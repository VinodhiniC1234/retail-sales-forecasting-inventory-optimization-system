import pandas as pd
import numpy as np

np.random.seed(42)

# Create dates
dates = pd.date_range(start="2023-01-01", periods=365)

# Create dataset
df = pd.DataFrame({
    "Date": dates,
    "Product": np.random.choice(["Laptop", "Phone", "Shoes", "Watch"], 365),
    "Category": np.random.choice(["Electronics", "Fashion", "Accessories"], 365),
    "Sales": np.random.randint(50, 500, 365),
    "Price": np.random.randint(500, 5000, 365),
    "Stock": np.random.randint(20, 200, 365)
})

# Save dataset inside data folder
df.to_csv("data/retail_sales.csv", index=False)

print("✅ Dataset created successfully!")