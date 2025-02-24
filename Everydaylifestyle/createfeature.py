# Required libraries
import seaborn as sns
import pandas as pd

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Create new feature 'family_size'
titanic_df['family_size'] = titanic_df['sibsp'] + titanic_df['parch'] + 1

# Create age groups
bins = [0, 12, 18, 35, 60, 100]
labels = ['Child', 'Teen', 'Young Adult', 'Middle Age', 'Senior']
titanic_df['age_group'] = pd.cut(titanic_df['age'], bins=bins, labels=labels, include_lowest=True)

# Print the first 10 rows of the dataset to check the engineered features
print(titanic_df[['age', 'age_group', 'family_size']].head(10))