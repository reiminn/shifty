#pip install xgboost
import pandas as pd
import joblib
Data=pd.read_csv("dataproject.csv")
New=Data.drop(['Locality'],axis=1)
y=New.Price
X=New.drop(['Price'], axis=1)
a=(X.dtypes=="object")
cato_cols=list(a[a].index)
#print(cato_cols)
num_cols=X.drop(cato_cols,axis=1)
from sklearn.impute import SimpleImputer
Imputer=SimpleImputer()
imputed_X=pd.DataFrame(Imputer.fit_transform(num_cols))
imputed_X.columns=num_cols.columns
from sklearn.preprocessing import OneHotEncoder
One_hot_Encoder= OneHotEncoder(handle_unknown="ignore", sparse_output=False)
OH_cols_X=pd.DataFrame(One_hot_Encoder.fit_transform(X[cato_cols]))
OH_cols_X.index=X.index

OH_X=pd.concat([num_cols,OH_cols_X],axis=1)
OH_X.columns=OH_X.columns.astype(str)

from xgboost import XGBRegressor
model= XGBRegressor(n_estimators=500, learning_rate=0.1)
from sklearn.model_selection import cross_val_score
scores=-1*cross_val_score(model,OH_X,y,
                          cv=6,
                          scoring="neg_mean_absolute_error")
print("MAE:\n", scores)
w=scores.mean()
print("Mean",scores.mean())
model.fit(OH_X,y)
#joblib.dump(model, 'my_model.pkl')
#joblib.dump(One_hot_Encoder, 'oH.pkl')
joblib.dump(Imputer, 'imputer.pkl')
#joblib.load('my_model.pkl')
