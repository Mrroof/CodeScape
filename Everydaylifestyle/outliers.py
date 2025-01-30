# using mean
titanic_df.loc[titanic_df['age_zscore'] > 3, 'age'] = titanic_df['age'].mean()

# using median
titanic_df.loc[(titanic_df['age'] < lower_bound) | (titanic_df['age'] > upper_bound), 'age'] = titanic_df['age'].median()