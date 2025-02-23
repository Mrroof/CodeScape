# Import necessary libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Create a new feature, 'age_x_fare'
titanic['age_x_fare'] = titanic['age']*titanic['fare']

# Check if new feature 'age_x_fare' was added
print("Data with new feature 'age_x_fare':")
print(titanic.head(5))

# Create age groups using bins
bins= [0, 12, 20, 60, np.inf]
labels = ['Child', 'Young Adult', 'Adult']
titanic['AgeGroup'] = pd.cut(titanic['age'], bins=bins, labels=labels, include_lowest=True)

# Display the first 10 rows of the modified DataFrame
print("\nData with new feature 'AgeGroup':")
print(titanic[['age', 'AgeGroup']].head(10))