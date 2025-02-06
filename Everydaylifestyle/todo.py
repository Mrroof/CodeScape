# Import necessary libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# TODO: Calculate the Z-score for the 'fare' column
titanic_df['fare_zscore'] = np.abs((titanic_df.fare - titanic_df.fare.mean()) / titanic_df.fare.std())
# TODO: Identify outliers using the Z-score method (using a threshold of 3)

# Replace the outliers with the mean of the 'fare' column
titanic_df.loc[titanic_df['fare_zscore'] > 3, 'fare'] = titanic_df['fare'].mean()

# Print the dataframe
print(titanic_df)
