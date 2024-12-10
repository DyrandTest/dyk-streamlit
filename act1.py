import streamlit as st

st.title("My First Dashboard App")

st.write("Hello, welcome to my first Dashboard App")

user_input = st.text_input("Enter Your Name:")

st.write(f"Hello, {user_input}!")