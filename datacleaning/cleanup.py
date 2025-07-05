import pandas as pd

# Load the dataset
file_path = "itemIndex_cleaned.csv"  # Update with your correct file path
item_df = pd.read_csv(file_path)

# Standardize column names
item_df.columns = item_df.columns.str.lower().str.replace(" ", "_").str.replace("-", "_")
print("Cleaned column names in item_df:", list(item_df.columns))

# Ensure 'year' is an integer
try:
    item_df['year'] = item_df['year'].astype(int)
except ValueError:
    raise ValueError("The column 'year' contains non-integer values. Check your CSV file!")

# Convert 'month' to integer (if necessary)
item_df['month'] = item_df['month'].astype(str).str.strip()
if not all(item_df['month'].isin([str(i) for i in range(1, 13)])):
    raise ValueError("Some months could not be converted. Check the CSV file for inconsistencies!")
item_df['month'] = item_df['month'].astype(int)

# Save the cleaned dataset
output_file = "itemIndex_final_cleaned.csv"
item_df.to_csv(output_file, index=False)
print(f"Cleaned dataset saved to {output_file}")
