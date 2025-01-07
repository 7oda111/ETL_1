import pandas as pd
import numpy as np

# Generate large dataset with 10,000 rows
data_large = {
    "id": range(1, 10001),
    "name": ["Product_" + str(i) for i in range(1, 10001)],
    "quantity": [np.random.randint(1, 100) if i % 50 != 0 else None for i in range(1, 10001)],  # Nulls every 50 rows
    "price": [round(np.random.uniform(5.0, 100.0), 2) for _ in range(10000)],
    "date": pd.date_range(start="2023-01-01", periods=10000, freq="H").tolist(),  # Hourly timestamps
    "category": ["Category_" + str(np.random.randint(1, 6)) for _ in range(10000)],
}

# Add outliers
data_large["price"][500] = 5000.0  # Extreme outlier
data_large["price"][2000] = -50.0  # Negative outlier

# Convert to DataFrame
df_large = pd.DataFrame(data_large)

# Save locally as CSV
file_path = "large_dummy_sales_data.csv"
df_large.to_csv(file_path, index=False)

print(f"Dataset saved at: {file_path}")
