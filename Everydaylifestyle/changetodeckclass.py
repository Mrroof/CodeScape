# Import necessary libraries
import pandas as pd
import seaborn as sns

# Load dataset
titanic_df = sns.load_dataset('titanic')

# Display unique categories in 'who' and 'embark_town'
print(titanic_df['class'].unique())
print(titanic_df['deck'].unique())

# Label Encoding for 'who'
titanic_df['class_encoded'] = pd.factorize(titanic_df['class'])[0]
print(titanic_df[['class', 'class_encoded']].head())

# One-Hot Encoding for 'embark_town'
encoded_deck = pd.get_dummies(titanic_df['deck'], prefix='decks')
titanic_df = pd.concat([titanic_df, encoded_deck], axis=1)
print(titanic_df.filter(like="deck").head())