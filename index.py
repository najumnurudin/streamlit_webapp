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




st.image("data:image/jpeg;base64,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", caption="A beautiful image")
