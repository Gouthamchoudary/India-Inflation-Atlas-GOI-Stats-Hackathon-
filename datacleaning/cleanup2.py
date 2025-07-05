import pandas as pd

# Load the dataset
ultimate_df = pd.read_csv("ultimate.csv")

# Standardize column names
ultimate_df.columns = ultimate_df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

# Define a mapping for month names to numbers
month_mapping = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}

# Convert month names to numbers
ultimate_df["month"] = ultimate_df["month"].replace(month_mapping)

# Now convert to integer
ultimate_df["month"] = ultimate_df["month"].astype(int)

# Drop missing values
ultimate_df.dropna(inplace=True)

# Remove duplicates
ultimate_df.drop_duplicates(inplace=True)

# Save cleaned dataset
ultimate_df.to_csv("ultimate_cleaned.csv", index=False)

print("Cleaning completed. Data saved as 'ultimate_cleaned.csv'.")
