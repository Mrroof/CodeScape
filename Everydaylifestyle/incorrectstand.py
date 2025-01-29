# Import the necessary libraries
import numpy as np
import seaborn as sns
from sklearn.preprocessing import RobustScaler

# Load the Titanic dataset6
titanic_df = sns.load_dataset('titanic').dropna()

# Initialize the RobustScaler
robust_scaler = RobustScaler()

# Incorrectly applying the fit_transform function to the 'age' column
titanic_df['age'] = robust_scaler.fit_transform(np.array(titanic_df['age']).reshape(-1, 1))

# Print the first 5 rows of the modified dataset
print(titanic_df.head())