import mysql.connector
import streamlit as st
import pandas as pd

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost', database='streamlit')
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
