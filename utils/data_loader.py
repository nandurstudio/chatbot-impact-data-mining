import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def load_data(file_obj, delim, enc):
    df = pd.read_csv(file_obj, delimiter=delim, encoding=enc, encoding_errors='replace')
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    return df
