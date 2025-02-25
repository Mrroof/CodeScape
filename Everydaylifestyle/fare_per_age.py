# Import required libraries
import seaborn as sns
import pandas as pd
import numpy as np

# Load Titanic dataset
titanic = sns.load_dataset('titanic')

# TODO: divide the fare by the age to create a feature 'fare_per_age'. Use DataFrame operations. Any non-number should be replaced with 0.
titanic['age'] = titanic['age'].replace(np.nan, 0)
titanic['fare_per_age'] = titanic['fare'] / titanic['age']
# Print the first 10 rows of the titanic dataframe
print(titanic.head(10))