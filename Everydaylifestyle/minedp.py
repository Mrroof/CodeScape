# Import required libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# TODO: Detect and print the number of missing values in the dataset before imputation.
print("data before imputation")
print(titanic_df.isnull().sum())
# TODO: Fill in missing values in the 'age' column with the mean
titanic_df["age"].fillna(titanic_df["age"].mean(), inplace=True)
# TODO: Detect and print the number of missing values in the dataset after imputation.
print("after imputation")
print(titanic_df.isnull().sum())
# Visualize missing data with a heatmap
plt.figure(figsize=(10,7))
sns.heatmap(titanic_df.isnull(), cmap='viridis')
plt.show()