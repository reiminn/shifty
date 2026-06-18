import streamlit as st
st.set_page_config(page_title='House Price Prediction App', page_icon="🏡")

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

st.title('House Price Prediction App')
st.write('''
Use the sidebar to navigate:
- Data Analysis
- Data Visualisation
- Prediction
- Evaluation
''')