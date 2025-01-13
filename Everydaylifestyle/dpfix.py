# Import required libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Display the count of missing values for each column
print("Number of missing values before imputation:")
print(titanic.isnull().sum())

# Use the backward fill method to fill missing values in the 'age' column
titanic['age'].fillna(titanic['age'].mean(), inplace=True)

# After filling, display the count of missing values for each column again
print("\nNumber of missing values after imputation:")
print(titanic.isnull().sum())

# Visualize missing data using a heatmap
plt.figure(figsize=(10,6))
sns.heatmap(titanic.isnull(), cmap='viridis')
plt.show()