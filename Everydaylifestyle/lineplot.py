# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# TODO: Load the 'flights' dataset from seaborn
flights = sns.load_dataset("flights")
# TODO: Group the data by each month and aggregate passengers' count
month_data = flights.groupby("month")["passengers"].sum().reset_index()
# TODO: Create a line plot with suitable parameters to visualize the distribution of passengers over the months
plt.figure(figsize=(10, 6))
plt.plot(month_data["month"], month_data["passengers"],color="blue", linestyle="--", marker="o", alpha=0.8)
# TODO: Set the plot title, X and Y axis labels with meaningful names
plt.title("Monthly Distribution")
plt.xlabel("Month")
plt.ylabel("Count")
# TODO: Add gridlines to the plot to improve readability
plt.grid(True)
# TODO: Finally, display the plot
plt.show