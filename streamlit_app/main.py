import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO


st.set_page_config('Homepage', page_icon="🏡")

with st.sidebar:
    st.markdown("# Hello 👋")
    st.markdown("## Welcome to this app on visualizing and forecasting the sales of the Favorita Grocery Stores in Ecuador from 2013 to 2017!")

''''''
# Attach the 'store_sales_raw.csv'
st.title('Favorita Store Sales Source Data')
st.subheader('Sales data from 2013-01-01 to 2017-08-15')
st.markdown('Raw data can be downloaded from the download button below')

# Function to convert DataFrame into stringIO for download
def convert_df_to_csv_string(df):
    # Convert DataFrame to CSV and then encode it to string using StringIO
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    return csv_buffer.getvalue()

# Load the 'store_sales_raw.csv' file into a DataFrame
store_sales_df = pd.read_csv(r'../data/store_sales_raw.csv')

#  Load the 'holidays_events.csv' file into a DataFrame
holidays_df = pd.read_csv(r'../data/holidays_events.csv')

# Load the 'store_df' file into a DataFrame
store_df = pd.read_csv(r'../data/stores.csv')

# Convert DataFrames to CSV for download
store_sales_csv_string = convert_df_to_csv_string(store_sales_df)
holidays_csv_string = convert_df_to_csv_string(holidays_df)
store_df_csv_string = convert_df_to_csv_string(store_df)

# Create download button for 'store_sales_raw.csv'
st.download_button(
    label="Download the raw sales data",
    data=store_sales_csv_string,
    file_name=r'../data/store_sales_raw.csv',
    mime='text/csv',
)

# Create download button for 'holidays_events.csv'
st.download_button(
    label="Download the holidays & events data",
    data=holidays_csv_string,
    file_name=r'../data/holidays_events.csv',
    mime='text/csv',
)

# Create download button for 'holidays_events.csv'
st.download_button(
    label="Download the stores data",
    data=store_df_csv_string,
    file_name=r'../data/holidays_events.csv',
    mime='text/csv',
)

