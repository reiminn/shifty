#Setup: Importing required modules
import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as pl

df=pd.read_csv('dataproject.csv')

#Preprocessing the data
def processed_data(df,l):
    df_vis=df.copy()
    #processing
    df_vis=df_vis.drop(l, axis=1)
    return df_vis
data=processed_data(df, ['Locality'])

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

#Main website
st.title('Data Visualization')
st.markdown("Explore the dataset visually using the options below.")

#3. the functions
def heatmap(pre_df): #input=preprocessed data, output=fig
    fig, ax = pl.subplots()
    sb.heatmap(pre_df.corr(numeric_only=True), cmap='coolwarm', annot=True, ax=ax)
    ax.set_title("Heatmap")
    st.pyplot(fig)


def scatterplot(pre_df):
    fig, ax = pl.subplots()
    sb.scatterplot(x=pre_df['Area'], y=pre_df['Price'], hue=pre_df['Bathroom'], ax=ax)
    ax.set_title("Variation of Area with Price")
    st.pyplot(fig)

def lmplot(pre_df):
    fig = sb.lmplot(x='Area', y='Price', hue='Bathroom', data=pre_df)
    st.pyplot(fig)

def hist(pre_df):
    fig, ax= pl.subplots()
    ax.hist(pre_df['Bathroom'].dropna(), bins=6, color='#69b3a2', edgecolor='black')
    ax.set_title("Distribution of houses according to Bathrooms")
    st.pyplot(fig)

#selection box
option=st.selectbox("Select an option:", ['Histogram', 'Scatterplot', 'lmplot','Heatmap'])

if option == 'Histogram':
   st.subheader("Histogram")
   hist(data)
elif option == 'lmplot':
   st.subheader("lmplot")
   lmplot(data)
elif option == 'Heatmap':
   st.subheader("Heatmap")
   heatmap(data)
elif option == 'Scatterplot':
   st.subheader("Scatterplot")
   scatterplot(data)
