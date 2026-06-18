#1. Importing required modules
import pandas as pd
#No preprocessing required at this stage

# Sort by a single column in descending order
#sorted_df_age_desc = df.sort_values(by='Age', ascending=False)
#print("\nSorted by Age (Descending):\n", sorted_df_age_desc)
#top 5 houses according to price

#After sorting, the index labels from the original data are kept by default.
#use iloc[0]['Price] instead
#print(data.sort_values(by='Price', ascending=False).iloc[2]['Price'])
def top5sort(data, column='Price'):
# Sort by a single column in ascending order (default)
    sorted_dfasc = data.sort_values(by=column)
    return (sorted_dfasc.head())
def invalid(data):
    print("INVALID")

def ana(df):
    actions={
    #'0' : QUIT,
    '1': lambda df: print(df.describe()),
    '2': lambda df: print(df.info()),
    '3': lambda df: print(df.head()),
    '4': lambda df :print(top5sort(df))
    }
    while True:
        print('\n','DATA ANALYSIS')
        print('1 describe')
        print('2 info')
        print('3 head')
        print('4 top5sort')
        print('0 - quit submenu')
        choice = input('choose an option:')
        if choice == '0':
            print("Quiting \'Data Analysis\' menu")
            break
        actions.get(choice, invalid)(df)


#main
#data=pd.read_csv('dataproject.csv')
#ana(data)