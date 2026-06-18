import pandas as pd
#1 Creating a dataframe
Result_sheet={'Rajat':[90, 91, 97], 'Amrita':[82, 90, 99], 'Fathima':[76, 99, 92]}
result=pd.DataFrame(Result_sheet, index=['Math', 'Science', 'Punjabi'])
print(result, '\n')

#2 Adding new columns
result['Meenakshi']=[93, 87, 77]
print(result, '\n')

#Adding new rows
result.loc['English']= [98, 76, 93, 82]
result.loc['AI']= [87, 96, 93, 92]
result.loc['Social Science']= [99, 79, 95, 89]
print(result, '\n')

#Display first 5 records
print(result.head(5), '\n')

#Display last 3 records
print(result.tail(3), '\n')

print(result.isnull().sum())