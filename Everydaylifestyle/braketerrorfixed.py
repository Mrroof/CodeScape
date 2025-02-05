# Import necessary libraries
import numpy as np
import seaborn as sns

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Remove rows with missing 'fare' data for accurate outlier detection
titanic_df = titanic_df.dropna(subset=['fare'])

# Calculate the Z-score for the 'fare' column
titanic_df['fare_zscore'] = np.abs((titanic_df.fare - titanic_df.fare.mean()) / titanic_df.fare.std())

# Handle outliers in the 'fare' column by replacing them with mean
titanic_df.loc[titanic_df['fare_zscore'] > 3, 'fare'] = titanic_df['fare'].mean()

# Drop the initial 'fare_zscore' column 
titanic_df = titanic_df.drop(['fare_zscore'], axis=1)

# Recalculate the Z-score for the 'fare' column after outlier handling
titanic_df['fare_zscore'] = np.abs((titanic_df.fare - titanic_df.fare.mean()) / titanic_df.fare.std())

# Print the result
print(titanic_df)