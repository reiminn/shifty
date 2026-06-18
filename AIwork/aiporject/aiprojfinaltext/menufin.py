#1. Importing required modules
import analysisfin
import visfin
import pandas as pd
import numpy as np
import joblib
from xgmodel import w
mymodel= joblib.load('my_model.pkl')
One_Hot_Encoder= joblib.load('oH.pkl')
imputer= joblib.load('imputer.pkl')
#OH_cols_X=pd.DataFrame(One_hot_Encoder.fit_transform(X[cato_cols]), columns=One_hot_Encoder.get_feature_names_out(cato_cols))
#print(mymodel.predict(pd.DataFrame({'Area':[1300] , "BHK":[4] , "Bathroom":[3], "Parking":[1]})))
#leaving prediction and evaluation for later

def getval():
    print('Enter the following:')
    try:
        area = float(input("Area (sq.ft): ") or 0)
        bhk = int(input("BHK: ") or 0)
        bathroom = int(input("Bathrooms: ") or 0)
        parking = float(input("Parking spots (optional): ") or np.nan)
        per_sqft = float(input("Per_Sqft (optional): ") or np.nan)

        furnishing = input("Furnishing (Furnished/Semi-Furnished): ") or "Semi-Furnished"
        status = input("Status (Ready_to_move/Under_Construction): ") or "Ready_to_move"
        transaction = input("Transaction (New_Property/Resale): ") or "New_Property"
        type_ = input("Type (Apartment/Builder_Floor): ") or "Apartment"
    except ValueError:
        print("⚠️ Invalid input!")
        return None

    input_dict = {
        'Area': area,
        'BHK': bhk,
        'Bathroom': bathroom,
        'Parking': parking,
        'Per_Sqft': per_sqft,
        'Furnishing': furnishing,
        'Status': status,
        'Transaction': transaction,
        'Type': type_
    }

    return pd.DataFrame([input_dict])
def process_input(data):
    cato_cols = ['Furnishing', 'Status', 'Transaction', 'Type']
    # Numeric columns
    num_cols = ['Area', 'BHK', 'Bathroom', 'Parking', 'Per_Sqft']
    X = pd.DataFrame(imputer.transform(data[num_cols]), columns=num_cols)

    # Categorical columns
    OH_cols_X = pd.DataFrame(One_Hot_Encoder.transform(data[cato_cols]))
    OH_cols_X.index = data.index

    # Combine numeric + categorical
    joined=pd.concat([X, OH_cols_X], axis=1)
    joined.columns=joined.columns.astype(str)
    # Match training column order
    #joined = joined.reindex(columns=mymodel.get_booster().feature_names, fill_value=0)

    return joined
def predict_hp(_):
    df_input = getval()
    X_input = process_input(df_input)
    print(X_input)
    pred = mymodel.predict(X_input)
    print(f"\n🏡 Predicted House Price: ₹{pred[0]}")


def invalid(data):
    print("INVALID")

def menu(df):
    actions={
    #'0' : QUIT,
    '1': analysisfin.ana,
    '2': visfin.vis,
    '3': predict_hp,
    '4': lambda df :print('Evaluation\n', f'MAE is {w}'),
    }
    while True:
        print('\n','Menu')
        print('1 analysis')
        print('2 vis')
        print('3 model')
        print('4 eval')
        print('0 - quit menu')
        choice = input('choose an option:')
        if choice == '0':
            print("Quiting menu")
            break
        actions.get(choice, invalid)(df)

data=pd.read_csv('dataproject.csv')
try:
    menu(data)
except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting...")