# Import required libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# TODO: Load the Titanic dataset
titanic = sns.load_dataset("titanic")
# TODO: Detect any missing values in the 'age' column and print the count
print("before impute")
print(titanic["age"].isnull().sum())
# TODO: Impute missing data in the 'age' column using backward fill
titanic["age"].fillna(titanic["age"].bfill().sum(), inplace=True)
# TODO: After imputing, confirm whether there are still any missing values in the 'age' column and print the count
print("after impute")
print(titanic["age"].isnull().sum())
# TODO: Create a visualization of the missing data using seaborn's heatmap functionality
plt.figure(figsize=(10, 7))
sns.heatmap(titanic.isnull(), cmap= "viridis")
plt.show()