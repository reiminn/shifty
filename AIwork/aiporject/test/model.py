import pandas as pd
#pip install scikit-learn
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
import matplotlib.pyplot as pl
#pip install joblib
import joblib
data=pd.read_csv('dataproject.csv')
#print(data.columns)
l=['Locality', 'Furnishing','Status','Transaction', 'Type' ,'Per_Sqft']
data=data.drop(l, axis=1)
Y=data.Price
X=data.drop('Price', axis=1)
#model = DecisionTreeRegressor(random_state=1)
#model.fit(X,Y)
#model.predict(X):for predictions!
from sklearn.metrics import mean_absolute_error
"""
predicted_home_prices = model.predict(X)
print(mean_absolute_error(Y, predicted_home_prices))"""
#validation stuff need to continute from model validation tomorrow
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, Y, random_state = 0)
# Define model
model = DecisionTreeRegressor(random_state=1)
# Fit model
model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
#print(val_predictions[0])
#how to predict something
#print(model.predict(pd.DataFrame({'Area':[1300] , "BHK":[4] , "Bathroom":[3], "Parking":[1]}))) #how to predict a value
#joblib.dump(model, 'my_model.pkl')
print("Model saved!")
mymodel= joblib.load('my_model.pkl')
print(mymodel.predict(pd.DataFrame({'Area':[1300] , "BHK":[4] , "Bathroom":[3], "Parking":[1]})))

