#importing all reqd modules-DONE
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as pl

data=pd.read_csv('dataproject.csv')
#print(data.columns) #11 #Area,BHK,Bathroom(8),Furnishing(4, nan incl),Locality,Parking(10 including nan and 144 (baaki range between 1 se 33)),Price,Status(2),Transaction(2),Type(3, nan incl),Per_Sqft
#list of stuff to be dropped
l=['Locality']
data=data.drop(l, axis=1)
#


#heatmap, furnishing, status, transaction, type removed
#In a correlation heatmap, each cell's color represents the strength of the correlation between two variables (BAthroom, area, bhk)
def heatmap(data):
    dataplot = sb.heatmap(data.corr(numeric_only=True), cmap='coolwarm', annot=True)
    pl.show()
#heatmap(data)



#def scatterplot(data, X,Y,COLOURED)
#dataplot=sb.scatterplot(x=data['Area'], y=data['Price'], hue=data['Bathroom']) #Status and transaction


#dataplot=sb.lmplot(x='Area', y='Price', hue='Bathroom', data=data)
#df['category'] = df['category'].fillna('NaN_Category') to show nan values too
pl.figure(figsize=(12,7))
#pl.show()

print(data['Type'].unique())

pl.plot(data['Area'], data['Price'])
pl.show()
#plt.plot(x1, y1, x2, y2)
#pie/histogram based on frequency of data