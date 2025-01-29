# Import the necessary libraries
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Load data
titanic_df = sns.load_dataset("titanic").dropna()

# Initialize the scalers
std_scaler = StandardScaler()
min_max_scaler = MinMaxScaler()
robust_scaler = RobustScaler()

# Transform 'age' with Standard Scaler
titanic_df['age_std'] = robust_scaler.fit_transform(np.array(titanic_df['age']).reshape(-1, 1))
# TODO: Apply the appropriate scaling techniques to the 'fare' column.
titanic_df[fare_min] = min_max_scaler.fit_transform(np.array(titanic_df['fare']).reshape(-1, 1))
# Print the summary statistics of the transformed dataset
print(titanic_df.describe())