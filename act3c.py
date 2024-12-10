import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Fetch and Display Data from Google Sheets")

conn = st.connection("gsheets", type=GSheetsConnection)
google_sheet_data = conn.read()

st.subheader("Display Data from Local CSV File")
st.dataframe(google_sheet_data, use_container_width=True)
st.caption("Displaying data retrieved from Google Sheets")

