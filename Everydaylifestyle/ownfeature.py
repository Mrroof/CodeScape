# Import the necessary libraries
import seaborn as sns
import pandas as pd

# TODO: Load the Titanic dataset
titanic = sns.load_dataset('titanic')
# TODO: Create a new feature, 'family_size', which is a sum of siblings, plus the number of parents, plus 1
titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1
# TODO: Create a new feature, 'age_group', which groups ages into different bins
bins = [0, 12, 35, 60, 100]
label = ['Child', 'Teen', 'Young adult', 'Adult', 'Senior']
titanic['age_group'] = pd.cut(titanic['age'], bins=bins, labels=labels, include_lowest=True)
# TODO: Print the first few rows of our dataset to check the engineered features
print(titanic['age', 'family_size', 'age_group'].head(10))