# import library
import streamlit as st
import eda
import prediction

# select box to select page
page = st.sidebar.selectbox('Select Page', ('Exploratory Data Analysis', 'Prediction'))

# run python file
if page == 'Exploratory Data Analysis':
    eda.run()
else:
    prediction.run()