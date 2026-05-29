import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# Safe path setup (NO ERRORS)
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "charts")

# Create folder safely (avoids WinError 183)
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv(os.path.join(BASE_DIR, "data", "amazon.csv"))

# -----------------------------
# Data Cleaning
# -----------------------------
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

df['discounted_price'] = df['discounted_price'].astype(str).str.replace('₹', '')
df['discounted_price'] = df['discounted_price'].str.replace(',', '')
df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce')

df['actual_price'] = df['actual_price'].astype(str).str.replace('₹', '')
df['actual_price'] = df['actual_price'].str.replace(',', '')
df['actual_price'] = pd.to_numeric(df['actual_price'], errors='coerce')

df['discount_percentage'] = df['discount_percentage'].astype(str).str.replace('%', '')
df['discount_percentage'] = pd.to_numeric(df['discount_percentage'], errors='coerce')

df['rating_count'] = df['rating_count'].astype(str).str.replace(',', '')
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

# -----------------------------
# 1. Histogram - Ratings
# -----------------------------
plt.figure(figsize=(8, 5))
plt.hist(df['rating'].dropna(), bins=20)

plt.title("Distribution of Product Ratings")
plt.xlabel("Ratings")
plt.ylabel("Number of Products")

plt.savefig(os.path.join(OUTPUT_DIR, "ratings_histogram.png"))
plt.show()
plt.close()

# -----------------------------
# 2. Bar Chart - Top Categories
# -----------------------------
top_categories = df['category'].value_counts().head(10)

plt.figure(figsize=(12, 6))
top_categories.plot(kind='bar')

plt.title("Top 10 Product Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=90)

plt.savefig(os.path.join(OUTPUT_DIR, "top_categories.png"))
plt.show()
plt.close()

# -----------------------------
# 3. Scatter Plot - Discount vs Rating
# -----------------------------
plt.figure(figsize=(8, 6))
plt.scatter(df['discount_percentage'], df['rating'])

plt.title("Discount Percentage vs Product Rating")
plt.xlabel("Discount Percentage")
plt.ylabel("Product Rating")

plt.savefig(os.path.join(OUTPUT_DIR, "discount_vs_rating.png"))
plt.show()
plt.close()

# -----------------------------
# 4. Correlation Heatmap
# -----------------------------
numeric_data = df[['discounted_price',
                   'actual_price',
                   'discount_percentage',
                   'rating',
                   'rating_count']]

correlation = numeric_data.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True)

plt.title("Correlation Heatmap")

plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
plt.show()
plt.close()