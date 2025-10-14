import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Roll-up: Total sales by country
print(df[df["Year"] == 2024].groupby("Country")["Sales"].sum())

# Drill-down: Sales by product category → item
print(df[df["Country"] == "Germany"].groupby(["Category", "Item"])["Sales"].sum())

# Slice: Only 2024 sales
print(df[df["Year"] == 2024])

# Dice: Electronics in Europe during Q1 2024
print(df[(df["Year"] == 2024) & 
         (df["Quarter"] == "Q1") & 
         (df["Category"] == "Electronics") &
         (df["Country"].isin(["Germany", "France", "UK"]))])