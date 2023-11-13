try:
    import os
    import sys
    import streamlit as st
    import pandas as pd
    from io import BytesIO, StringIO
    print("all Modules are loaded")
except Exception as e:
    print("Some modules are missing : {}" .format(e))
    
    
    # css
    
STYLE = """
        <style>
        img {
            max-widt: 100;
        }
        </style>
        """

def main():
    """Run the function to display the Streamlit app"""
    st.info(__doc__)
    st.markdown(STYLE, unsafe_allow_html=True)
    file = st.file_uploader("Upload file", type=["csv", "png", "peg", "gif"])
    show_file = st.empty()
    
    if not file:
        show_file.info("Please Upload a file : {}".format(''.join(["csv", "png","peg", "gif"])))
        return
    content = file.getvalue()
    
    if isinstance(file, BytesIO):
        show_file.image(file)
    else:
        df = pd.read_csv(file)
        st.dataframe(data.head(10))
        
main()
