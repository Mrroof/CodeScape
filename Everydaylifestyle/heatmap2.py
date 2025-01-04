# TODO: Load the dataset
flights = sns.load_dataset("flights")
# TODO: Pivot the dataset
flight_pivot=flights.pivot(index="month", columns="year", values="passengers")
# TODO: Create a heatmap enhanced for better readability
heatmap = sns.heatmap(
    flight_pivot,
    annot=True,
    cbar=True,
    cmap="coolwarm",
    center=flight_pivot.mean().mean(),
    linewidth=.5,
    fmt="d"
    
)
# TODO: Add a title
plt.title("Heatmap monthly passenger Distribution")
# TODO: Display the plot
plt.show()