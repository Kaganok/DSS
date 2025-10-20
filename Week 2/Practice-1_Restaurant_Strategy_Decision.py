import pandas as pd

# --- Phase 1: Intelligence ---
print("Phase 1: Intelligence - Problem Definition")
print("A restaurant chain must decide on an expansion strategy.\n")


df = pd.read_csv("restaurant_decision_matrix.csv")
print("CSV 'restaurant_decision_matrix.csv' was read successfully.\n")

# --- Phase 2: Design ---
print("Phase 2: Design - Criteria and Weights")

# Define weights (sum to 1.0)
weights = {
    "FinancialInvestment": 0.2,
    "ControlQuality": 0.15,
    "SpeedOfGrowth": 0.25,
    "RiskLevel": 0.15,
    "Scalability": 0.15,
    "ProfitPotential": 0.10
}

print("Weights:", weights, "\n")

# --- Phase 3: Choice ---
print("Phase 3: Choice - Scoring Alternatives")

# Normalize and compute weighted score
for col in list(weights.keys()):
    df[col + "_Norm"] = df[col] / df[col].max()

df["WeightedScore"] = sum(df[col + "_Norm"] * w for col, w in weights.items())
df_sorted = df.sort_values(by="WeightedScore", ascending=False)

print(df_sorted[["Alternative", "WeightedScore"]], "\n")

# --- Phase 4: Implementation ---
best_choice = df_sorted.iloc[0]["Alternative"]
print("Phase 4: Implementation - Selected Alternative")
print(f"✅ Recommended Decision: {best_choice}")