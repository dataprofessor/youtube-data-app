# Import the necessary libraries
import streamlit as st
import pandas as pd

# User can upload a JSON file
uploaded_file = st.file_uploader("Choose a JSON file to upload", type="json")

if uploaded_file is not None:
    # Read the uploaded JSON file and generate a Pandas DataFrame from the JSON data
    df = pd.read_json(uploaded_file)

    # Display the DataFrame
    st.dataframe(df)
