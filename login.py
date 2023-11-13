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

# Function to authenticate the user
def authenticate_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()

    # Change the table and column names based on your database structure
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

# Streamlit app
def main():
    st.title("Login Session")

    # Get user input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            user = authenticate_user(username, password)

            if user:
                st.success(f"Logged in as {username}")
                
                
                # Redirect to home.py upon successful login
                redirect_url = "/login.py"
                st.experimental_set_query_params(username=username, password=password)
                st.experimental_rerun()  # Rerun the app to apply the URL changes
            else:
                st.error("Invalid username or password")
        else:
            st.warning("Please enter both username and password.")

if __name__ == "__main__":
    main()
