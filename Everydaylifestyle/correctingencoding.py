# Importing necessary libraries
import pandas as pd
import seaborn as sns
from sklearn import preprocessing

# Loading Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Misinterpreting the output of pd.factorize
titanic_df['alive_encoded'] = pd.factorize(titanic_df['alive'])[0]
print(titanic_df[['alive', 'alive_encoded']])

# Print the 'alive' and 'alive_encoded' columns
print(titanic_df[['alive', 'alive_encoded']].head())