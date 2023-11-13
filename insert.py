import mysql.connector
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time



# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost', database='streamlit')
cursor = cnx.cursor()

# Create a form for user input
with st.form(key='my_form'):
    CAT_1 = st.number_input(max_value=100, min_value=0,label='Enter  CAT_1 results')
    CAT_2 = st.number_input(max_value=100, min_value=0,label='Enter  CAT_2 results')
    SEMESTER_ONE = st.number_input(max_value=100, min_value=0,label='Enter  SEMESTER_ONE results')
    SEMESTER_TWO = st.number_input(max_value=100, min_value=0,label='Enter SEMESTER_TWO results')
    submit_button = st.form_submit_button(label='Submit')

# Insert the data into the MySQL database
if submit_button:
    query = f"INSERT INTO data (CAT_1, CAT_2, SEMESTER_ONE, SEMESTER_TWO) VALUES ('{CAT_1}', '{CAT_2}','{SEMESTER_ONE}', '{SEMESTER_TWO}')"
    cursor.execute(query)
    cnx.commit()
    st.success('Data inserted successfully!')

# Close the database connection
cursor.close()
cnx.close()
