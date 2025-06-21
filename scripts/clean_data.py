import pandas as pd

# Load the raw dataset
df = pd.read_csv('data/raw/Social Media Addiction and Relationships.csv')  # ← Update if filename is different

# Standardize column names: lowercase + underscores
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# Preview first few rows (for manual inspection)
print(df.head())

# Save cleaned data
df.to_csv('data/cleaned/cleaned_addiction.csv', index=False)

print("✅ Cleaned file saved to /data/cleaned/")
