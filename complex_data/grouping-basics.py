import pandas as pd

# Mock data
df_complex = pd.DataFrame(
    {
        "City": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai"],
        "Price": [5000, 8000, 4500, 6000, 8500],
        "SqFt": [1200, 1500, 1100, 1400, 1600],
        "Views": [100, 500, 150, 300, 600],
    }
)

# 1. Group by City
# 2. Select the 'Price' column
# 3. Apply the mean() function
avg_prices = df_complex.groupby("City")["Price"].mean()

print(avg_prices)

# Calculate mean, max, and min simultaneously in one pass
metrics = df_complex.groupby("City")["Price"].agg(["mean", "max", "min", "count"])

print(metrics)


# The Enterprise Pattern
# We tell Pandas EXACTLY what to do with each specific column
final_report = df_complex.groupby("City").agg(
    {
        "Price": ["mean", "min"],  # Get average and lowest price
        "SqFt": "max",  # Get only the largest square footage
        "Views": "sum",  # Get the total number of views combined
    }
)

print(final_report)
