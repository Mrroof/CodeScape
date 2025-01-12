# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Print the number of missing values in each column before imputation
print('Before median imputation:')
print(titanic_df.isnull().sum())

# Impute missing values in the 'age' column using the mean method
titanic_df['age'].fillna(titanic_df['age'].median(), inplace=True)

# Print the number of missing values in each column after imputation
print('\nAfter median imputation:')
print(titanic_df.isnull().sum())

# Visualize the missing data with a heatmap
plt.figure(figsize=(10,6))
sns.heatmap(titanic_df.isnull(), cmap='viridis')
plt.show()