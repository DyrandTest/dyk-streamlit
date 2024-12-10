import streamlit as st
import requests
import pandas as pd

st.title("Fetch and Display Data from an API")

# Fetch data
# Replace with a valid API endpoint
api_url = "https://api.met.gov.my/v2.1/locations?locationcategoryid=TOWN"
headers = {"Authorization": "METToken f443c1375933a9bb4abde6bc06aecd57f94830df"}

try:
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        api_data = response.json()  # Raw JSON response
        st.subheader("Raw API Data")
        st.json(api_data, expanded=False)  # Display raw JSON

        # Process data if applicable (example: convert JSON to DataFrame)
        results = api_data["results"]  # Adjust based on API response structure
        df = pd.DataFrame(results)

        # Display processed data
        st.subheader("Processed API Data")
        st.dataframe(df, use_container_width=True)
    else:
        st.error(f"Failed to fetch API data: {response.status_code}")
except Exception as e:
    st.error(f"Error fetching data: {e}")
