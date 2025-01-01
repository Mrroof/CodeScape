# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
flights = sns.load_dataset('flights')

# Pivot the dataset
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

# Create a customized heatmap
heatmap = sns.heatmap(flights_pivot, 
                      cmap='YlGnBu', 
                      annot=True, 
                      fmt="d", 
                      linewidths=.5, 
                      cbar=True, 
                      center = flights_pivot.loc["Jan", 1955]
                      )

# Assign the title
heatmap.set_title("Customized Heatmap of Monthly Air Travel Data")

# Display the plot
plt.show()