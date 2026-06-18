print('hello')
import pandas as pd
data=pd.read_csv('dataproject.csv')
#print(data.head())
#print(data.describe())
#data analysis, data vis, data pred, evaluation
"""
Enter the corresponding number or letter to select:
(1) Data Analysis
(2) Data Visualisation
(3) Prediction
(4) Evaluation
(Q) Exit
"""
'''DATA ANALYSIS SELECTED
(1) Display the prices of house areawise
(2) Display top 10 costliest houses
(3) Display top 4 affordable houses
'''

'''
# Sort by a single column in ascending order (default)
sorted_df_age_asc = df.sort_values(by='Age')
print("Sorted by Age (Ascending):\n", sorted_df_age_asc)

# Sort by a single column in descending order
sorted_df_age_desc = df.sort_values(by='Age', ascending=False)
print("\nSorted by Age (Descending):\n", sorted_df_age_desc)
'''
#SORT ACC TO SOME COLUMN
#MEAN MODE MEDIAN
#brief description of data: data.describe()
#top 5 houses according to price
#print(data.sort_values(by='Price', ascending=False).loc[0,'Price'])
#print(df.loc['row2', 'col1'])
#After sorting, the index labels from the original data are kept by default.
#use iloc[0]['Price] instead
#print(data.sort_values(by='Price', ascending=False).iloc[2]['Price'])
#Count missing values per column (data.isna().sum())
#print(data.info())