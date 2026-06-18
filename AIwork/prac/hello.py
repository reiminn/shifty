import pandas as pd
df=pd.read_csv('studentsmarks.csv')
print(df)

#1 Display marks in AI
print(df['AI Marks'], '\n')

#2 Find missing values
print(df.isnull(), '\n')

#Fill null values
print(df.fillna(99), '\n')