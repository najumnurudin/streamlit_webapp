import streamlit as st

# Streamlit app
def main():
    st.title("Login Session")

    # Get user input
    st.text_input("Username")
    st.text_input("Password", type="password")

if __name__ == "__main__":
    main()
