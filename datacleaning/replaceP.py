import pandas as pd

# Load data
df = pd.read_csv("itemIndex.csv")  # Use actual filename

# Remove '.P' from item_code if present
df["item_code"] = df["item_code"].str.replace(r"\.P$", "", regex=True)

# Save cleaned data
df.to_csv("itemwise_final.csv", index=False)

print("✅ Cleaned item_code column. Check saved file: itemwise_final.csv")
