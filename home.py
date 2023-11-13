import streamlit as st
import numpy as np
import pandas as pd
import mysql.connector
import altair as alt
from streamlit_option_menu import option_menu
import time

st.title("KIBAHA COLLEGE OF HEALTH AND ALLIED SCIENCES")
st.header("Student Information management System")
selected = option_menu(
        menu_title=None,
        options=["Table Information","Bar Chart display","Line chart", "Total assesment"],
        default_index=0,
        orientation="horizontal",
    )
if selected =="Table Information":
    # Connect to the MySQL database
    cnx = mysql.connector.connect(user='root', password='',host='localhost', database='streamlit')
    cursor = cnx.cursor()
# Execute the query to retrieve all rows
    query = "SELECT * FROM data"
    cursor.execute(query)
    # Fetch all rows
    rows = cursor.fetchall()
    # Convert the rows to a pandas dataframe
    df = pd.DataFrame(rows, columns=[i[0] for i in cursor.description])    
# Display the dataframe using Streamlit
    st.dataframe(df)    
    
if selected =="Bar Chart display":

    # Connect to the MySQL database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="streamlit"
    )

    # Execute the SQL query and fetch the results
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM data")
    myresult = mycursor.fetchall()

    # Convert the results to a Pandas dataframe
    df = pd.DataFrame(myresult, columns=["id", "CAT_1", "CAT_2","SEMESTER_ONE", "SEMESTER_TWO"])

    # Display the bar chart using Streamlit
    st.bar_chart(df)

        
        
        
        
        
if selected =="Line chart":
    # Connect to the MySQL database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="streamlit"
    )

    # Execute the SQL query and fetch the results
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM data")
    myresult = mycursor.fetchall()

    # Convert the results to a Pandas dataframe
    df = pd.DataFrame(myresult, columns=["id", "CAT_1", "CAT_2","SEMESTER_ONE", "SEMESTER_TWO"])

    # Display the line chart using Streamlit
    st.line_chart(df)
     
     
     
     
     
     
     
if selected =="Total assesment":
     st.write("")