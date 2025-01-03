# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load flights dataset
flights = sns.load_dataset('flights')

# Pivot the dataset
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

# TODO: Define a colormap to visualize the passenger count and annotate each cell with the actual passenger count.
# On top of that, configure line widths, heatmap color bar, and centralize the heatmap
heatmap = sns.heatmap(flights_pivot,
annot=True,
cbar=True,
cmap="viridis",
center=flights_pivot.mean().mean(),
linewidths=.5,
)

# Set the heatmap title
heatmap.set_title("Heatmap of Monthly Airline Passengers Count From 1949 to 1960")

# Display the plot
plt.show()