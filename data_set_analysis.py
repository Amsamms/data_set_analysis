import streamlit as st
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

# Add a title
st.title("Data Analysis Simplified")

# Add a catchy subtitle
st.markdown("## Unleash the power of data with a single click!")

# Add a section on how to use the app
st.markdown("""
### How to use this app:
1. Upload your dataset (Make sure the first row contains column names).
2. Click on 'Generate report' and wait for a while.
3. Click 'Download' to download the generated report.
""")

data= st.file_uploader("Choose excel or csv file to upload",type=['csv','xls','xlsx'],key='1')
if data is not None:
    try:
        df_raw = pd.read_csv(data,encoding_errors='ignore')
    except:
        pass
    try:
        df_raw = pd.read_csv(data)
    except:
        pass
    try:
        df_raw = pd.read_excel(data)
    except:
        pass
    try:
        df_raw = pd.read_excel(data, engine='openpyxl')
    except:
        pass
else:
    st.write('*Kindly upload a data set for quick analysis')
    
if data is not None:
    if st.button('Generate report'):
        profile = ProfileReport(df_raw, title="Pandas Profiling Report")
        profile.to_file("your_report.html")

        with open("your_report.html", "rb") as f:
            st.download_button(label="Download report", data=f, file_name="your_report.html", mime="text/html")       
