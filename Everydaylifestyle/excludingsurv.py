# Import the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Calculate the correlation matrix
clean_df = titanic_df.drop('survived', axis=1)
corr_matrix = clean_df.corr(numeric_only=True)

# Use a Heatmap to visualize the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm')

# Add a title
plt.title('Correlation Heatmap of Titanic Dataset')

# Display the plot
plt.show()