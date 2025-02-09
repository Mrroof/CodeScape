# Import the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Calculate the correlation matrix
corr_matrix = titanic_df.corr(numeric_only=True)

# Let's visualize this correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)

# Add a title
plt.title('Heatmap of the Correlation Matrix')

# Show the plot
plt.show()

# Now, let's remove a redundant feature
# Choose age and parch, as they are highly correlated
clean_df = titanic_df.drop('age', axis=1)

# Print the first 5 rows of the cleaned dataframe
print(clean_df.head())