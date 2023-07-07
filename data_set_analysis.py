import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components
from ydata_profiling import ProfileReport

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Data quick Analysis and visualization",
    layout="wide"
)

# Add a title
st.title("Data Analysis and visualization")

# Add a catchy subtitle
st.markdown("## Unleash the power of data with a few clicks!")

# Add a section on how to use the app
st.markdown("""
### How to use this app:
1. Upload your dataset (Make sure the first row contains column names).
2. Click on 'Generate report' to generate a data analysis report, then click download bottom to have offline report. It might take a while.
3. Or Click 'Online Analysis' to activate Pygwalker visualization on the spot.
""")

# Upload data for data analysis
data = st.file_uploader("Choose excel or csv file to upload", type=['csv', 'xls', 'xlsx'], key='1')
if data is not None:
    try:
        df_raw = pd.read_csv(data, encoding_errors='ignore')
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
    st.write('*Kindly upload a data set for quick analysis and visualization')
    
if data is not None:
    col1,col2 = st.columns([0.7,0.3], gap="large")  # create two columns
    

    with col1:  # use the first column for the 'Generate report' button
        if st.button('Generate report'):
            with st.spinner('Generating report...'):
                profile = ProfileReport(df_raw, title="Pandas Profiling Report")
                profile.to_file("your_report.html")

            with open("your_report.html", "rb") as f:
                st.download_button(label="Download report", data=f, file_name="your_report.html", mime="text/html")

    online_analysis = False
    with col2:  # use the second column for the 'Online Analysis' button
        if st.button('Online Analysis'):
            online_analysis = True

    if online_analysis:
        st.subheader('Pygwalker Visualization')
        pyg_html = pyg.walk(df_raw, return_html=True)
        components.html(pyg_html, height=1000, scrolling=True)