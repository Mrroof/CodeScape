# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
flights = sns.load_dataset('flights')

# Pivot the dataset
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

# Create a heatmap where each cell displays the corresponding passenger count for that month and year
heatmap = sns.heatmap(flights_pivot, 
                      cmap='coolwarm', 
                      annot=True, 
                      fmt="d", 
                      linewidths=.5, 
                      cbar=True, 
                      center = flights_pivot.mean().mean()
                     )

# Assign the title
heatmap.set_title("Passenger Count Heatmap of Air Travel Data")

# Display the plot
plt.show()