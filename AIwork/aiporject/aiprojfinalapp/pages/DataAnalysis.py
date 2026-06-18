#Importing required modules
import streamlit as st
import pandas as pd


#Custom CSS for background
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
#Main website
st.title('Data Analysis')

st.subheader("The Raw Dataset")
df=pd.read_csv('dataproject.csv')
st.write(df)

st.markdown("Explore the dataset using the options below.")

#functions
def top5sort(data, column='Price', asc=True):
# Sort by a single column in ascending order (default)
    sorted_dfasc = data.sort_values(by=column, ascending=asc)
    return (sorted_dfasc).head()

#selection box
option=st.selectbox("Select an option:", ['Describe', 'Preview', 'Sort Dataset'])

if option == 'Describe':
   st.subheader("Statistical Summary")
   st.dataframe(df.describe())
elif option == 'Preview':
   st.subheader("First 5 rows of the dataset")
   st.dataframe(df.head())
elif option == 'Sort Dataset':
   columns=st.selectbox('Select an option:', ['Price', 'Area', 'BHK'])
   order = st.sidebar.radio("Sort order", ['Ascending', 'Descending'])
   asc=True
   if order=='Descending': asc=False
   st.subheader(f"Top 5 rows of the Dataset sorted by {columns}")
   st.dataframe(top5sort(df, columns, asc))
