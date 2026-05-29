import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/amazon.csv")

# Convert rating to numeric
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

# -----------------------------------
# Histogram of Product Ratings
# -----------------------------------

plt.hist(df['rating'])

plt.title("Distribution of Product Ratings")
plt.xlabel("Ratings")
plt.ylabel("Number of Products")

plt.show()

# -----------------------------------
# Bar Chart of Top Categories
# -----------------------------------

top_categories = df['category'].value_counts().head(10)

plt.figure(figsize=(12, 6))

top_categories.plot(kind='bar')

plt.title("Top 10 Product Categories")
plt.xlabel("Category")
plt.ylabel("Count")

plt.xticks(rotation=90)

plt.show()

# -----------------------------------
# Scatter Plot: Discount vs Rating
# -----------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(df['discount_percentage'], df['rating'])

plt.title("Discount Percentage vs Product Rating")
plt.xlabel("Discount Percentage")
plt.ylabel("Product Rating")

plt.show()

# -----------------------------------
# Correlation Heatmap
# -----------------------------------

numeric_data = df[['discounted_price',
                   'actual_price',
                   'discount_percentage',
                   'rating',
                   'rating_count']]

correlation = numeric_data.corr()

plt.figure(figsize=(8, 6))

sns.heatmap(correlation, annot=True)

plt.title("Correlation Heatmap")

plt.show()