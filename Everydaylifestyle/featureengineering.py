# Required Libraries
import pandas as pd
import seaborn as sns

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# Create new features 'family_size' and 'is_alone'
titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1
titanic['is_alone'] = 1
titanic.loc[titanic['family_size'] > 1, 'is_alone'] = 0

# Print the first 5 rows of the dataset
print(titanic[['sibsp', 'parch', 'family_size', 'is_alone']].head())