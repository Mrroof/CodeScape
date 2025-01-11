# Importing required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Print out the number of missing values in each column
print('Before imputation:')
print(titanic_df.isnull().sum())

# Impute missing values in the 'age' column with its mean
titanic_df['age'].fillna(titanic_df['age'].mean(),inplace=True)

# Check again the number of missing values
print('\nAfter imputation:')
print(titanic_df.isnull().sum())

# Visualize missing data with a heat map
plt.figure(figsize=(10,6))
sns.heatmap(titanic_df.isnull(), cmap='viridis')
plt.show()