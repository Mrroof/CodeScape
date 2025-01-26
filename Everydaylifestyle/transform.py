# Import the necessary libraries
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
import numpy as np

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic').dropna()

# Initialize the scalers
std_scaler = StandardScaler()
min_max_scaler = MinMaxScaler()
robust_scaler = RobustScaler()

# Fit and transform the 'age' column with Standard Scaler
titanic_df['age_std'] = std_scaler.fit_transform(np.array(titanic_df['age']).reshape(-1, 1))

# Fit and transform the 'fare' column with Min-Max Scaler
titanic_df['fare_minmax'] = min_max_scaler.fit_transform(np.array(titanic_df['fare']).reshape(-1, 1))
titanic_df['fare_robust'] = robust_scaler.fit_transform(np.array(titanic_df['fare']).reshape(-1, 1))
# Print the first 5 rows of the modified dataset
print(titanic_df.head())