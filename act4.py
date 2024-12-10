import streamlit as st
import pandas as pd
import time

# Set Page Configuration
st.set_page_config(page_title="Dashboard DIY", page_icon="📊", layout="wide")

# Load CSV Data
file_path = 'C:\\Users\\dyran\\Downloads\\UMPSA\\ASSIGNMENT SEM 2\\BTE1522 LAB 2\\DASHBOARD\\restaurant.csv'
df = pd.read_csv(file_path)

# Page Title
st.title("Dashboard Design and Layout with Sample Data")
st.write("Explore different layout components and learn how to organize dashboards effectively.")

# Sidebar Section
st.sidebar.title("Sidebar: Filters and Options")
columns = tuple(df.columns)
selected_option = st.sidebar.selectbox("Select a column to display", options=columns)

# Row 1: Metrics in Three Columns
st.header("Row 1: Metrics Example")
with st.container(border=True):
    coll, col2, col3 = st.columns(3)

    with coll:
        st.metric("Revenue", "$12,000", "-5%")
    with col2:
        st.metric("Orders", "1,240", "-3%")
    with col3:
        st.metric("Customers", "350", "+10%")

# Row 2: Images in Two Columns
st.header("Row 2: Visual Content")
with st.container(border=True):
    coll, col2 = st.columns(2)

    with coll:
        st.image("https://api.met.gov.my/static/images/radar-latest.gif", caption="Latest Radar Image")
    with col2:
        st.image("https://api.met.gov.my/static/images/swirl-latest.gif", caption="Latest Forecast Radar")

# Row 3: Data Table
st.header("Row 3: Sample Data Table")
with st.container():
    st.write("This table displays data from the uploaded CSV file:")
    st.dataframe(df.head(), use_container_width=True)

# Row 4: Dynamic Placeholder Example
st.header("Row 4: Dynamic Updates with Placeholder")
placeholder = st.empty()  # Create a placeholder

# Simulate updating the placeholder dynamically
for i in range(5):
    with placeholder:
        st.write(f"Updating... Step {i + 1} of 5")
        st.progress((i + 1) * 20)
        time.sleep(1)

placeholder.write("Dynamic updates complete! 🎉")

# Row 5: Expander for Additional Details
st.header("Row 5: Expander Example")
with st.expander("Click to Expand: CSV File Details"):
    st.write("Below is a detailed view of the uploaded data:")
    st.dataframe(df)

# Row 6: Tabs for Organized Layout
st.header("Row 6: Tabs Example")
tab1, tab2, tab3 = st.tabs(["Data Overview", "Charts", "Interactive Options"])

with tab1:
    st.write("Overview of the selected column:")
    st.dataframe(df[selected_option].describe())

with tab2:
    st.write("Visualization of the selected column:")
    st.line_chart(df[selected_option])

with tab3:
    st.write("Interactive Input:")
    user_input = st.text_area("Write your observations here:")
    st.write(f"Your input: *{user_input}*")

# Footer
st.success("You've successfully explored different layout components with sample data!")