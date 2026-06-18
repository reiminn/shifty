#Importing required modules
import pandas as pd
import streamlit as st
import numpy as np
import joblib
from xgmodel import w
import time
mymodel= joblib.load('my_model.pkl')
One_Hot_Encoder= joblib.load('oH.pkl')
imputer= joblib.load('imputer.pkl')

# Custom CSS for background
st.markdown(
    """
    <style>
.stApp {
    background: linear-gradient(to bottom right, #ffe5d9, #b2f7ef);
}
[data-testid="stSidebar"] {
    background-color: #ffd6c0;
}
h1, h2, h3 { color: #006d77; }
.stDataFrame div.row_heading, .stDataFrame div.column_heading { background-color: #ffb366; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Price Prediction')
def getval():
    st.subheader('Enter the following:')
    try:
        area = float(st.text_input("Area (sq.ft):",'0') or 0)
        bhk = int(st.text_input("BHK: ", '0') or 0)
        bathroom = int(st.text_input("Bathrooms: ", '0') or 0)
        parking = float(st.text_input("Parking spots (optional):", "NaN") or np.nan)
        per_sqft = float(st.text_input("Per_Sqft (optional):", "NaN") or np.nan)

        furnishing = st.text_input("Furnishing (Furnished/Semi-Furnished): ", "Semi-Furnished ") or "Semi-Furnished"
        status = st.text_input("Status (Ready_to_move/Under_Construction):", "Ready_to_move") or "Ready_to_move"
        transaction = st.text_input("Transaction (New_Property/Resale):", "New_Property") or "New_Property"
        type_ = st.text_input("Type (Apartment/Builder_Floor):", " Apartment") or "Apartment"
    except ValueError:
        st.error("⚠️ Invalid input!")
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
    st.subheader('Your entered values')
    st.dataframe(pd.DataFrame([input_dict]))
    st.markdown('Press this button to predict your results')
    Predbutton=st.button('PREDICT')
    if Predbutton:
        with st.spinner("Imputing values... One Hot Encoding... Predicting...", show_time=True):
            time.sleep(3)
        st.success(predict_hp(pd.DataFrame([input_dict])))
        st.markdown(f'House Price Predictor is subject to errors with an MAE of {w}')
def process_input(data):
    cato_cols = ['Furnishing', 'Status', 'Transaction', 'Type']
    #numerical cols
    num_cols = ['Area', 'BHK', 'Bathroom', 'Parking', 'Per_Sqft']
    X = pd.DataFrame(imputer.transform(data[num_cols]), columns=num_cols)
    #categorical cols
    OH_cols_X = pd.DataFrame(One_Hot_Encoder.transform(data[cato_cols]))
    OH_cols_X.index = data.index
    #join cols
    joined=pd.concat([X, OH_cols_X], axis=1)
    joined.columns=joined.columns.astype(str)
    return joined
def predict_hp(_):
    X_input = process_input(_)
    pred = mymodel.predict(X_input)
    return (f"\n🏡 Predicted House Price: ₹{pred[0]}")

getval()
