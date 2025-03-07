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

# Predict the passenger counts for the next decade
new_years = np.array(range(1961, 1971)).reshape(-1, 1)
new_passenger_numbers = reg.predict(new_years)

# Plot the original data and the predictions
plt.scatter(X, y, color='blue', s=30)
plt.plot(X, reg.predict(X), color='orange')
plt.scatter(new_years, new_passenger_numbers, color='red', s=30)
plt.plot(new_years, new_passenger_numbers, color='green')

# Set labels and title 
plt.xlabel("Year")
plt.ylabel("Total Passengers")
plt.title("Historical and Predicted Airline Passengers Over Time")

# Show the plot
plt.show()