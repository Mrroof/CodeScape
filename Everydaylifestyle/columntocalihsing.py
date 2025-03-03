# Import required libraries
from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np

# Load the California Housing dataset
data = fetch_california_housing()

# Create a DataFrame
df = pd.DataFrame(data=np.c_[data['data'], data['target']],
                  columns=data['feature_names'] + ['MedHouseValue'])

# TODO: Add a new column 'PopHouseValue' describing 'Population' divided by 'MedHouseValue'
df['PopHouseValue'] = df['Population'] / df['MedHouseValue']

print(df.head())