# Import the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Calculate the correlation matrix
corr_matrix = titanic_df.corr(numeric_only=True)

# TODO: Visualize the correlation matrix with a heatmap.
plt.figure(figsize(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')
# TODO: Print the correlation between 'age' and 'parch'.
correlation = corr_matrix['age']['parch']
print(correlation)

# Handle redundant or correlated feature
# Choose 'age' and 'parch' as they are highly correlated
# Drop the 'age' column
titanic_df = titanic_df.drop('age', axis=1)

# Print the first 5 rows of the cleaned dataframe
print(titanic_df.head())