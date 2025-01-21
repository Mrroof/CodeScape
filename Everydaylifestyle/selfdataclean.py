# Import necessary libraries
import pandas as pd
import seaborn as sns

# TODO: Load the Titanic dataset into a variable named titanic_df
titanic_df = sns.load_dataset("titanic")
# TODO: Apply Label Encoding to the 'deck' column and add the result as a new column 'deck_encoded' in the dataset
titanic_df["deck_encoded"] = pd.factorize(titanic_df['deck'])[0]
print(titanic_df["deck", "deck_encoded"])
# TODO: Use One-Hot Encoding on the 'alone' column and concatenate the resultant DataFrame to the main titanic_df
encoded_alone = pd.get_dummies(titanic_df["alone"], prefix="sad")
titanic_df = pd.concat([titanic_df, encoded_alone], axis=1)
print(titanic_df.filter(like="alone").head())