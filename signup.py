import streamlit as st
import mysql.connector

# Function to create a MySQL connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="streamlit"
    )

# Function to insert a new user into the database
def insert_user(username, level, phone, address, email, password):
    conn = create_connection()
    cursor = conn.cursor()

    # Change the table and column names based on your database structure
    query = "INSERT INTO users (username, level, phone, address, email, password) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (username, level, phone, address, email, password)

    cursor.execute(query, values)

    conn.commit()
    cursor.close()
    conn.close()

# Streamlit app
def main():
    st.title("Signup Form with MySQL")

    # Get user input
    username = st.text_input("Username")    
        # Options for the user to choose from
    main_options = ["NMT", "CMT"]

    # Create a selectbox for the user to choose a main option
    level = st.selectbox("Select Your course:", main_options)

    # Define sub-options based on the selected main option
    if level == "Main Option 1":
        sub_options = ["Sub-Option 1A", "Sub-Option 1B"]
    elif level == "Main Option 2":
        sub_options = ["Sub-Option 2A", "Sub-Option 2B"]
    else:
        sub_options = ["LEVEL 4", "LEVEL 5", "LEVEL 6"]

    # Create a selectbox for the user to choose a sub-option
    selected_sub_option = st.selectbox("Select your Level:", sub_options)


    
    phone = st.number_input("Phone", value=+255)
    address = st.text_input("Address")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if username and level and phone and address and email and password:
            insert_user(username, level, phone, address, email, password)
            st.success("User registered successfully!")
        else:
            st.warning("Please fill in all fields.")

if __name__ == "__main__":
    main()
