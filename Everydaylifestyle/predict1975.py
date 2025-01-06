# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Load the 'flights' dataset
flights_data = sns.load_dataset("flights")

# Pivot the dataset to get yearly passengers sum
flights_pivot = pd.pivot_table(data=flights_data, values='passengers', index ='year', aggfunc='sum').reset_index()

# Prepare data for model fitting 
X = np.array(flights_pivot['year']).reshape(-1,1)
y = flights_pivot['passengers']

# Fit the Linear Regression model
reg = LinearRegression().fit(X, y)

# Predict the passenger count for the year 1961
new_year = np.array([1975]).reshape(-1,1)
new_passenger_number = reg.predict(new_year)
print(f"Predicted number of passengers for 1975: {int(new_passenger_number)}")