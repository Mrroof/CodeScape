# Import necessary libraries
import numpy as np
import seaborn as sns

# TODO: Load the Titanic dataset
titanic = sns.load_dataset('titanic')
# TODO: Clean the dataset to remove rows with missing 'age' data
titanic = titanic.dropna(subset=['age'])
# TODO: Calculate the Z-score for the 'age' column
titanic['age_zscore'] = np.abs((titanic.age - titanic.age.mean()) / titanic.age.std() )
# TODO: Identify and print outliers using the Z-score method (threshold of 3)
outliers_zscore = titanic[(titanic['age_zscore'] > 3)]
# TODO: Handle outliers in the 'age' column detected by the Z-score method by replacing them with a median
titanic_clean = titanic
titanic_clean.loc[titanic_clean['age_zscore'] > 3, 'age'] = titanic['age'].median()
# TODO: Print the cleaned data
print("cleaned data:")
print(titanic_clean)