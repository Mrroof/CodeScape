# import necessary libraries
from sklearn.datasets import fetch_california_housing
import pandas as pd

# Fetch the dataset
dataset = fetch_california_housing()

# Create a dataframe for dataset
df = pd.DataFrame(data = dataset.data, columns = dataset.feature_names)

# Add the target values to the dataframe
df["MedHouseValue"] = dataset.target

# Print the size of dataframe
print("Size of the dataframe: ", df.shape)

# Get the statistical summary for the dataset
print("\nStatistical Summary for the dataset:")
print(df.describe())

# Check for missing values
print("\nChecking for missing values in the dataset:")
print(df.isnull().sum())

# Print the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(df.head())