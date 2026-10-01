import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt




Amazon = pd.read_csv("amazon.csv")

print(Amazon.head())

# Dataset information
print(Amazon.info())

# Missing values
print("\nMissing Values:")
print(Amazon.isnull().sum())

# Check uniqueness
print("\nProduct IDs are unique:", Amazon["product_id"].is_unique)

# Count duplicate Product IDs
print("Duplicate Product IDs:", Amazon["product_id"].duplicated().sum())



    # Remove ₹ and commas
Amazon["discounted_price"] = (
    Amazon["discounted_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
    )

Amazon["actual_price"] = (
    Amazon["actual_price"]
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
    )

# Remove %
Amazon["discount_percentage"] = (
    Amazon["discount_percentage"]
    .str.replace("%", "", regex=False)
    .astype(float)
    )

# Remove commas from rating_count
Amazon["rating_count"] = (
    Amazon["rating_count"]
    .fillna("0")
    .astype(str)
    .str.replace(",", "", regex=False)
    .astype(int)
    )

print("\nData Types After Cleaning:")
print(Amazon.dtypes)


Amazon["rating"] = pd.to_numeric(Amazon["rating"], errors="coerce")

print(Amazon["rating"].unique())

print("Missing ratings:", Amazon["rating"].isnull().sum())

print(Amazon.dtypes)

Amazon.to_csv("amazon_clean.csv", index=False)
print("amazon_clean.csv saved successfully!")

import pandas as pd
import matplotlib.pyplot as plt

Amazon = pd.read_csv("amazon_clean.csv")

#Dataset Overview
print('\nDataset Overview')
print(Amazon.describe())

#Products per Category
print('\nProducts per Category')
category_count = Amazon["category"].value_counts()
print(category_count)

#Average Rating by Category
print('\nAverage Rating by Category')
print(
    Amazon.groupby("category")["rating"]
    .mean()
    .sort_values(ascending=False)
)

Amazon.to_csv("amazon_clean_utf8.csv", index=False, encoding="utf-8-sig")
