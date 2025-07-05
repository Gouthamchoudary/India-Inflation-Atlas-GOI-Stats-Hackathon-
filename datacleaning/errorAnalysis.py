import pandas as pd

# Load the dataset
file_path = "itemIndex.csv"  # Update this to the actual path
df = pd.read_csv(file_path)

# Check for duplicates and remove them
df.drop_duplicates(inplace=True)

# Handling missing values in 'combined_index' column
df['combined_index'].fillna(method='ffill', inplace=True)  # Forward fill
df['combined_index'].fillna(df['combined_index'].mean(), inplace=True)  # Fill remaining with mean

# Save the cleaned file
cleaned_file_path = "itemIndex_cleaned_final.csv"
df.to_csv(cleaned_file_path, index=False)

print(f"Data cleaning complete. Cleaned file saved as {cleaned_file_path}")
