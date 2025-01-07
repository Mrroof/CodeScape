# Import necessary libraries
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

# Predict the passenger counts for the years from 1966 to 1970
new_years = np.array(range(1966, 1971)).reshape(-1, 1)
new_passenger_numbers = reg.predict(new_years)

# Print the predicted passenger counts for the next 5 years
print("Year, Predicted Passengers")
for year, passengers in zip(new_years, new_passenger_numbers):
    print(f"{year[0]}, {int(passengers)}")