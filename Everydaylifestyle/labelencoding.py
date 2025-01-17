# Import necessary libraries
import pandas as pd
import seaborn as sns

# Load the dataset
titanic_df = sns.load_dataset('titanic')

# Print unique categories in 'sex' and 'embark_town' columns
print(titanic_df['sex'].unique())
print(titanic_df['embark_town'].unique())

# Apply Label Encoding to the 'sex' column
titanic_df['sex_encoded'] = pd.factorize(titanic_df['sex'])[0]
print(titanic_df[['sex', 'sex_encoded']].head())
