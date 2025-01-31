# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Remove rows with missing 'age' data for accurate outlier detection
titanic_df = titanic_df.dropna(subset=['age'])

# Calculate the Z-score for the 'age' column
titanic_df['age_zscore'] = np.abs((titanic_df.age - titanic_df.age.mean()) / titanic_df.age.std())

# Identify outliers using the Z-score method (using a threshold of 3)
outliers_zscore = titanic_df[(titanic_df['age_zscore'] > 3)]

# Print the outliers detected by the Z-score method
print("Outliers detected by the Z-score method:")
print(outliers_zscore)

# Handle outliers in the 'age' column detected by the Z-score method by replacing them with median
titanic_clean = titanic_df
titanic_clean.loc[titanic_clean['age_zscore'] > 3, 'age'] = titanic_df['age'].median()

# Print cleaned data
print("\nData after handling outliers detected by Z-score method:")
print(titanic_clean)