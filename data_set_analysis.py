import streamlit as st
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

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
   # profile = ProfileReport(df_raw, title="Pandas Profiling Report")
    #profile.to_widgets()
    #if st.button('Generate report and download'):
    #    profile = ProfileReport(df_raw, title="Pandas Profiling Report")
    #    profile.to_file("your_report.html")
    #    b64 = base64.b64encode(profile_html.encode()).decode()  # some strings <-> bytes conversions necessary here
    #    href = f'<a href="data:text/html;base64,{b64}" download="profile.html">Download profile report</a>'
    #    st.markdown(href, unsafe_allow_html=True)
    if st.button('Generate report'):
        profile = ProfileReport(df_raw, title="Pandas Profiling Report")
        profile.to_file("your_report.html")

        with open("your_report.html", "rb") as f:
            st.download_button(label="Download report", data=f, file_name="your_report.html", mime="text/html")       