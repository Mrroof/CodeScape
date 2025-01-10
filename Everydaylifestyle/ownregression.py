# Import necessary libraries
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# TODO: Load the 'flights' dataset
flight = sns.load_dataset("flights")
# TODO: Pivot the dataset to get the yearly passenger count
flight_pivot= flight.pivot_table(flight, index="year", value="passengers", aggfunc="sum").rest_index()
# TODO: Prepare data for model fitting
X = np.array(flight_pivot["year"]).reshape(-1, 1)
y = flight_pivot["passengers"]
# TODO: Fit the Linear Regression model
reg = LinearRegression().fit(X, y)
# TODO: Predict the passenger counts for the next decade
new_years = np.array(range(1960, 1971)).reshape(-1, 1)
new_years_passengers = reg.predict(new_years)
# TODO: Plot the original data and the regression line
plt.scatter(X, y, color="red", s=30)
plt.plot(X, reg.predict(X), color="blue")
plt.scatter(new_years, new_years_passengers, color="green", s=30)
plt.plot(new_years, new_years_passengers, color="orange")
# TODO: Set labels and title of the plot
plt.xlabel("Years")
plt.ylabel("Total passengers")
plt.title("Historical Airline Data")
# TODO: Show the plot
plt.show()