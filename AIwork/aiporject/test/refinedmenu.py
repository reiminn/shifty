import streamlit as st
st.title("Gimme that title title")
#st.header("This is a header")
#st.subheader("This is a subheader")
st.write('hello world')
st.text("Hello GeeksForGeeks!!!")
#streamlit run refinedmenu.py
#st.success("Success")

#st.info("Information")

#st.warning("Warning")

#st.error("Error")

#exp = ZeroDivisionError("Trying to divide by Zero")
#st.exception(exp)
import pandas as pd
data=pd.read_csv('dataproject.csv')
st.write(data)
# Create a dropdown menu for selecting a hobby
hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])

# Display the selected hobby
st.write("Your hobby is:", hobby)
# Create a multiselect box for choosing hobbies
hobbies = st.multiselect("Select Your Hobbies:", ['Dancing', 'Reading', 'Sports'])

# Display the number of selected hobbies
st.write("You selected", len(hobbies), "hobbies")# A simple button that does nothing
st.button("Click Me")

# A button that displays text when clicked
if st.button("About"):
    st.text("Welcome to GeeksForGeeks!")
    # Create a text input box with a default placeholder
name = st.text_input("Enter your name", "Type here...")

# Display the name after clicking the Submit button
if st.button("Submit"):
    result = name.title()  # Capitalize the first letter of each word
    st.success(result)
    # Create a slider to select a level between 1 and 5
level = st.slider("Choose a level", min_value=1, max_value=5)

# Display the selected level
st.write(f"Selected level: {level}")
import matplotlib.pyplot as plt
import streamlit as st
from numpy.random import default_rng as rng

arr = rng(0).normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

st.toast('Mr Stay-Puftt')
import time

with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)
st.success("Done!")
st.button("Rerun")