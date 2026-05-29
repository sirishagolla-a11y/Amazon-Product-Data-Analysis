import pandas as pd

# Load dataset
df = pd.read_csv("../data/amazon.csv")

# Convert rating column to numeric
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Clean discounted price
df['discounted_price'] = df['discounted_price'].str.replace('₹', '')
df['discounted_price'] = df['discounted_price'].str.replace(',', '')
df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce')

# Clean actual price
df['actual_price'] = df['actual_price'].str.replace('₹', '')
df['actual_price'] = df['actual_price'].str.replace(',', '')
df['actual_price'] = pd.to_numeric(df['actual_price'], errors='coerce')

# Clean discount percentage
df['discount_percentage'] = df['discount_percentage'].str.replace('%', '')
df['discount_percentage'] = pd.to_numeric(df['discount_percentage'], errors='coerce')

# Clean rating count
df['rating_count'] = df['rating_count'].str.replace(',', '')
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

# Dataset shape
print("DATASET SHAPE:")
print(df.shape)

# Column names
print("\nCOLUMN NAMES:")
print(df.columns)

# First 5 rows
print("\nFIRST 5 ROWS:")
print(df.head())

# Data types before and after cleaning
print("\nUPDATED DATA TYPES:")
print(df.dtypes)

# Missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Summary statistics
print("\nSUMMARY STATISTICS:")
print(df.describe())

# Top categories
print("\nTOP PRODUCT CATEGORIES:")
print(df['category'].value_counts().head(10))

# Average rating
print("\nAVERAGE PRODUCT RATING:")
print(df['rating'].mean())