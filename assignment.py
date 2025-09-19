# ------------------------------------------
# Assignment: Data Analysis with Pandas & Matplotlib
# ------------------------------------------

# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: use the built-in Iris dataset if you don’t have a CSV
from sklearn.datasets import load_iris

try:
    # Load CSV dataset (replace 'your_dataset.csv' with your file)
    # df = pd.read_csv("your_dataset.csv")

    # Alternative: Load the Iris dataset
    iris = load_iris(as_frame=True)
    df = iris.frame  # Iris dataset in DataFrame format

    print("✅ Dataset loaded successfully!")

except FileNotFoundError:
    print("❌ Error: Dataset file not found. Please check the path.")
except Exception as e:
    print("❌ Error:", e)

# Display first few rows
print("\n📌 First 5 rows of the dataset:")
print(df.head())

# Check structure and missing values
print("\n🔍 Dataset Info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Handle missing values (if any)
df = df.dropna()  # or df.fillna(method='ffill')

# ------------------------------------------
# Task 2: Basic Data Analysis
# ------------------------------------------

# Descriptive statistics
print("\n📊 Basic Statistics:")
print(df.describe())

# Group by categorical column (for Iris dataset: 'target')
# Replace 'target' with your categorical column if using another dataset
grouped = df.groupby('target').mean()
print("\n📊 Mean values grouped by target/species:")
print(grouped)

# ------------------------------------------
# Task 3: Data Visualization
# ------------------------------------------

# 1. Line Chart (trend over index)
plt.figure(figsize=(8,5))
plt.plot(df.index, df['sepal length (cm)'], label="Sepal Length")
plt.title("Line Chart: Sepal Length Over Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart (average per species)
plt.figure(figsize=(8,5))
grouped['sepal length (cm)'].plot(kind='bar', color='skyblue')
plt.title("Bar Chart: Avg Sepal Length per Species")
plt.xlabel("Species (Target)")
plt.ylabel("Avg Sepal Length (cm)")
plt.show()

# 3. Histogram (distribution of petal length)
plt.figure(figsize=(8,5))
plt.hist(df['petal length (cm)'], bins=20, color='green', alpha=0.7)
plt.title("Histogram: Petal Length Distribution")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (relationship between sepal length & petal length)
plt.figure(figsize=(8,5))
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], alpha=0.6, c=df['target'])
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.colorbar(label="Species (Target)")
plt.show()

print("\n✅ Analysis and visualization completed!")
