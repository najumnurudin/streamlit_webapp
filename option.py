import streamlit as st


# Options for the user to choose from
main_options = ["Main Option 1", "Main Option 2"]

# Create a selectbox for the user to choose a main option
selected_main_option = st.selectbox("Select a main option:", main_options)

# Define sub-options based on the selected main option
if selected_main_option == "Main Option 1":
    sub_options = ["Sub-Option 1A", "Sub-Option 1B"]
elif selected_main_option == "Main Option 2":
    sub_options = ["Sub-Option 2A", "Sub-Option 2B"]
else:
    sub_options = []

# Create a selectbox for the user to choose a sub-option
selected_sub_option = st.selectbox("Select a sub-option:", sub_options)

# Display the selected options
st.write(f"You selected: {selected_main_option}, {selected_sub_option}")

