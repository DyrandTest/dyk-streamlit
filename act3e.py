import streamlit as st
import time  # For simulating dynamic updates

# Title of the app
st.title("Display Metrics on Your Dashboard")

# Section 1: Display Static Metrics
st.header("Static Metric Example")
st.metric(label="Temperature (°C)", value=25, delta="1.5 °C")
st.metric(label="Humidity", value="65%", delta="5%")
st.metric(label="Wind Speed", value="15 km/h", delta="-2 km/h")
st.metric(label="Air Quality Index (AQI)", value=42, delta="3")

# Section 2: Display Dynamic Metrics
st.header("Dynamic Metric Example")

# Create placeholders for updating metrics dynamically
temperature_placeholder = st.empty()
humidity_placeholder = st.empty()

# Initialize dynamic values
temperature = 15.0
humidity = 65

# Simulate updating metrics in real-time
for i in range(50):  # Simulate 50 updates
    temperature += 0.2  # Simulate a gradual temperature increase
    humidity -= 0.5  # Simulate a gradual humidity decrease

    # Update the metrics
    with temperature_placeholder:
        st.metric(label="Temperature (°C)", value=f"{temperature:.1f}", delta=f"{0.2 * (i+1):.1f} °C")
    with humidity_placeholder:
        st.metric(label="Humidity (%)", value=f"{humidity:.1f}%", delta=f"{0.5 * (i+1):.1f}%")
    time.sleep(1)  # Pause for 1 second before the next update
