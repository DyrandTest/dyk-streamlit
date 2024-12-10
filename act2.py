import streamlit as st

st.write("Hello, welcome to my first dashboard app!")

st.title('This is Title')
st.caption('using st.title(), you can display text in title format')

st.header('This is header')
st.caption('The text inside st.header() is in header formatting')

st.subheader('This is subheader')
st.caption('The text inside st.subheader() is in subheader formatting')

st.markdown('---')
st.divider()

st.subheader('Generate Random Numbers')

body = """
import numpy as np
def generate_random(size):
    rand = np.random(size-size)
    return rand
number = generate_random(10)
"""
st.code(body, language='python')

st.subheader('LaTeX')

formula = """
a + ar + ar^2 + r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} a r^k
"""
st.latex(formula)

st.markdown(
    "<h3 style='text-align: center; color: red; background-color:lightgrey'>"
    "Dashboard Development with Python and Streamlit</h3>",
    unsafe_allow_html=True  # Allows HTML styling for customization
)

# 9. --- Markdown Guide ---
st.markdown(""""
# Markdown Guide
Markdown is an easy way to format text. Below are examples of Markdown formatting you can use in Streamlit apps.

## Headers
- Use `#` for Title (Heading Level 1)
- Use `##` for Heading Level 2
- Use `###` for Heading Level 3
- Use `####` for Heading Level 4

## Lists
### Ordered Lists (Numbered)
1. First item
2. Second item
    1. Sub-item
3. Third item

### Unordered Lists (Bulleted)
- Item 1

### Unordered Lists (Bulleted)
- Item 1
- Item 2
  - Sub-item

## Links
- Create links using `[link text](URL)`.
Example: [Google](https://www.google.com)

## Images
- Use `![alt text](URL)` to add images.
Example:
![UMPSA Logo](https://news.umpsa.edu.my/sites/default/files/gallery-article/UMPSA%20Solar_0.jpg)
""")

# 10 --- Displaying an Image from a URL ---
st.subheader("Displaying an Image from a URL")  # Subheader for the image section
st.image("https://news.umpsa.edu.my/sites/default/files/gallery-article/UMPSA%20Solar_0.jpg")
