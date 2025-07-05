import pandas as pd

# Load the dataset
file_path = "itemIndex.csv"  # Update with correct path if needed
df = pd.read_csv(file_path)

# 1️⃣ Check for missing values
missing_values = df.isnull().sum()
print("Missing Values:\n", missing_values)

# 2️⃣ Check for duplicates
duplicate_rows = df[df.duplicated()]
print(f"\nNumber of duplicate rows: {duplicate_rows.shape[0]}")

# 3️⃣ Check for outliers in 'combined_index'
desc_stats = df['combined_index'].describe()
print("\nCombined Index Statistics:\n", desc_stats)

# Identify potential outliers using IQR method
Q1 = df['combined_index'].quantile(0.25)
Q3 = df['combined_index'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['combined_index'] < (Q1 - 1.5 * IQR)) | (df['combined_index'] > (Q3 + 1.5 * IQR))]
print(f"\nNumber of outliers in 'combined_index': {outliers.shape[0]}")

# 4️⃣ Validate item codes format
invalid_codes = df[~df['item_code'].str.match(r'^\d+\.\d+\.\d+\.\d+\.\d+\.\w+$', na=False)]
print(f"\nNumber of invalid item codes: {invalid_codes.shape[0]}")
