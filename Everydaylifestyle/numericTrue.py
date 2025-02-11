import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
titanic_df = sns.load_dataset('titanic')

# Calculate correlation matrix
correlation_matrix = titanic_df.corr(numeric_only=True)

# Check the correlation between 'fare' and 'pclass' and print it
correlation = correlation_matrix['fare']['pclass']
print('Correlation between fare and pclass: ', correlation)

# Visualize the correlation matrix using seaborn heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')

# Add title and labels
plt.title('Heatmap of Correlation Matrix for Titanic dataset')
plt.xlabel('Features')
plt.ylabel('Features')

# Display the plot
plt.show()

# If 'pclass' and 'fare' are highly correlated, drop one of these columns
if abs(correlation) > 0.5:
    titanic_df = titanic_df.drop('fare', axis=1)

# Print the first 5 rows of the cleaned dataframe
print(titanic_df.head())