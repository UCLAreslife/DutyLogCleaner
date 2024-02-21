import streamlit as st
import functions as f
import pandas as pd

st.title("Duty Log Cleaner")

st.subheader("File Upload")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    file = f.location_categorizer(
    f.incident_categorizer(pd.read_csv(uploaded_file),
        pd.read_csv('reslifekeywords.csv'),
        'dutylog_labeled.csv'
        ),
    pd.read_csv('uclalocations.csv'),
    pd.read_csv('uclazones.csv'),
    'dutylog_labeled.csv'
    )
    dropped = ['Token', 'Token Used']
    file = file.drop(dropped, axis=1)
    file = f.duration_cleaner(file)
    btn = st.download_button(
        label="Download csv",
        data=file.to_csv(),
        file_name='Duty Log Cleaned.csv',
        mime="text/csv"
    )
