import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the 'flights' dataset
flights_data = sns.load_dataset("flights")

# Pivot the dataset to get yearly passengers sum
flights_pivot = pd.pivot_table(flights_data, values='passengers', index='year', aggfunc='sum').reset_index()

# Prepare data for model fitting
X = np.array(flights_pivot['year']).reshape(-1, 1)
y = flights_pivot['passengers']

# Fit the Linear Regression model
reg = LinearRegression().fit(X, y)

# TODO: Predict the passenger counts for the next decade using the regression model you've just fitted.
new_years = np.array(range(1971, 1981)).reshape(-1, 1)
new_passenger_numbers = reg.predict(new_years)
print(new_passenger_numbers)