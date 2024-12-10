import streamlit as st
import pandas as pd

st.title("Fetch and Display Data from Local Storage")

file_path = 'C:\\Users\\dyran\\Downloads\\UMPSA\\ASSIGNMENT SEM 2\\BTE1522 LAB 2\\DASHBOARD\\restaurant.csv'

local_data = pd.read_csv(file_path)

st.subheader("Display Data from Local CSV File")
st.dataframe(local_data, use_container_width=True)
st.caption("Displaying data using st.dataframe")