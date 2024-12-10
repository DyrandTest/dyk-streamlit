import streamlit as st
import pandas as pd
import os

# Set the page configuration for the Streamlit app
st.set_page_config(page_title="Dashboard DIY", page_icon="pie", layout="wide")

# Load the dataset
data = pd.read_csv('restaurant.csv')  # Replace 'restaurant.csv' with the correct path to your dataset

# Button widget
st.subheader('Displaying Random 5 Rows')
st.caption('Click on the button below to display 5 random rows from the dataset.')
button = st.button('Display random 5 rows')
if button:
    st.dataframe(data.sample(5))  # Display 5 random rows from the dataset

# Divider line
st.markdown('---')

# Checkbox widget
st.subheader('Checkbox: st.checkbox')
agree = st.checkbox('I agree to terms and conditions')  # Creates a checkbox that returns True or False
st.write('Checkbox status =', agree)  # Display the status of the checkbox
# Multiple checkboxes in a container
with st.container():
    st.info('Select the technologies you are familiar with:')
    python = st.checkbox('Python')
    datascience = st.checkbox('Data Science')
    ai_ml = st.checkbox('AI/ML')
    android = st.checkbox('Android')
    react = st.checkbox('React JS')
    java = st.checkbox('Core Java')
    javascript = st.checkbox('Java Script')

    tech_button = st.button('Submit')
    if tech_button:
        # Create a dictionary to store the selected technologies
        tech_dict = {
            'Python': python,
            'Data Science': datascience,
            'AI/ML': ai_ml,
            'Android': android,
            'React JS': react,
            'Core Java': java,
            'Java Script': javascript,
        }
        st.json(tech_dict)  # Display the selected technologies in JSON format

# Divider line
st.markdown('---')
# Radio button widget
st.subheader('Radio Buttons: st.radio')
radio_button = st.radio(
    "What is your favorite color?",
    ('White', 'Black', 'Pink', 'Red', 'Blue', 'Green')
)
st.write('Your favorite color is', radio_button)

# Selectbox widget
st.markdown('---')
st.subheader('Selectbox: st.selectbox')
select_box = st.selectbox(
    'What skill do you want to learn most?',
    ('Java', 'Python', 'C', 'C++', 'JavaScript', 'HTML', 'Others')
)
st.write('You selected =', select_box)

# Multiselect widget
st.markdown('---')
st.subheader('Multiselect: st.multiselect')
options = st.multiselect(
    'What kinds of movies do you like?',
    ['Comedy', 'Action', 'Sci-fi', 'Drama', 'Romance']
)
st.write('You selected:', options)
# Slider widget
st.markdown('---')
st.subheader('Slider: st.slider')
loan = st.slider(
    'What loan amount are you looking for?', 0, 100000, 1000, 1000
)
# Slider for selecting a loan amount
st.write('Loan amount =', loan)

# Text input, number input, and date input widgets
st.markdown('---')
st.subheader('Text Input, Number Input, and Date Input')
with st.container():
    name = st.text_input('Please enter your name') # Text input field
    age = st.number_input('What is your age?', min_value=0, max_value=150, value=25, step=1) # Number input field
    describe = st.text_area('Description', height=150) # Multi-line text area
    dob = st.date_input('Select your date of birth') # Date input field
submit_button = st.button('Submit Details')  # Submit button
if submit_button:
    # Create a dictionary to display the inputted information
    info = {
        "Name": name,
        "Age": age,
        "Date of Birth": dob,
        "About Yourself": describe
    }
    st.json(info)  # Display the information in JSON format

# File uploader widget
st.markdown('---')
st.subheader('File Uploader: st.file_uploader')
uploaded_file = st.file_uploader('Choose a file to upload', type=["csv"])  # File uploader widget
save_button = st.button('Save File')  # Save button
if save_button:
    if uploaded_file is not None:
        # Save the uploaded file to a folder
        with open(os.path.join("./save_folder", uploaded_file.name), mode='wb') as f:
            f.write(uploaded_file.getbuffer())
        st.success('File uploaded successfully')  # Display success message
    else:
        st.warning('Please select a file to upload')  # Display warning if no file is selected
