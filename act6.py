import streamlit as st  # Streamlit for creating the interactive app
import pandas as pd  # Pandas for data manipulation
import numpy as np  # NumPy for numerical operations
import matplotlib.pyplot as plt  # Matplotlib for plotting
import seaborn as sns  # Seaborn for advanced statistical plots

# Setting the page title and layout
st.set_page_config(page_title="Dashboard DIY: Data Visualization", layout="centered")
st.header('Data Visualization using Matplotlib and Seaborn in Streamlit')

# Load the data
df = pd.read_csv('./restaurant.csv')
st.subheader("Dataset Overview")
st.dataframe(df.head())

# Question 1: Male and Female Distribution (Pie and Bar Charts)
st.subheader('1. Distribution of Male and Female')
st.write("### 1.1 Gender Distribution (Pie and Bar Charts)")

value_counts = df['sex'].value_counts()

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### Pie Chart")
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct='%0.2f%%', labels=value_counts.index)
        st.pyplot(fig)

    with col2:
        st.write("#### Bar Chart")
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts, color=['blue', 'pink'])
        ax.set_title('Gender Distribution')
        st.pyplot(fig)

with st.expander('Show Gender Counts'):
    st.dataframe(value_counts)

st.write("### 1.2 Distribution Based on Selected Feature")

cat_cols = df.select_dtypes(include='object').columns
selected_feature = st.selectbox('Choose a feature:', cat_cols)

value_counts = df[selected_feature].value_counts()

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### Pie Chart")
        fig, ax = plt.subplots()
        ax.pie(value_counts, autopct='%0.2f%%', labels=value_counts.index)
        st.pyplot(fig)

    with col2:
        st.write("#### Bar Chart")
        fig, ax = plt.subplots()
        ax.bar(value_counts.index, value_counts, color='skyblue')
        st.pyplot(fig)

with st.expander('Show Value Counts'):
    st.dataframe(value_counts)

# Question 2: Spending Distribution by Gender
st.subheader('2. Distribution of Spending by Gender')

chart_types = ['Box Plot', 'Violin Plot', 'KDE Plot', 'Histogram']
chart_choice = st.selectbox('Choose a Chart Type:', chart_types)

with st.container():
    fig, ax = plt.subplots()
    if chart_choice == 'Box Plot':
        sns.boxplot(x='sex', y='total_bill', data=df, ax=ax)
    elif chart_choice == 'Violin Plot':
        sns.violinplot(x='sex', y='total_bill', data=df, ax=ax)
    elif chart_choice == 'KDE Plot':
        sns.kdeplot(x=df['total_bill'], hue=df['sex'], ax=ax, shade=True)
    else:
        sns.histplot(x='total_bill', hue='sex', data=df, ax=ax, kde=True)
    st.pyplot(fig)

# Question 3: Average Total Bill by Day and Gender
st.subheader('3. Average Total Bill by Day and Gender')

avg_total_bill = df.groupby(['day', 'sex'])['total_bill'].mean().unstack()

fig, ax = plt.subplots()
avg_total_bill.plot(kind='bar', ax=ax, colormap='viridis', edgecolor='black')
ax.set_ylabel('Average Total Bill')
ax.set_title('Average Total Bill by Day and Gender')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
st.pyplot(fig)

st.dataframe(avg_total_bill)

# Question 4: Relationship Between Total Bill and Tip
st.subheader('4. Relationship Between Total Bill and Tip')

hue_feature = st.selectbox('Choose a Feature for Coloring:', cat_cols)

fig, ax = plt.subplots()
sns.scatterplot(x='total_bill', y='tip', hue=hue_feature, data=df, ax=ax)
ax.set_title('Total Bill vs Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')
st.pyplot(fig)
