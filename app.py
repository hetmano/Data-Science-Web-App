import streamlit as st
import pandas as pd
import numpy as np


DATA_URL = (
r'C:\datafiles\data\Motor_Vehicle_Collisions_-_Crashes.csv'
)

st.title("Motor Vehicle Collisions in New York City Area")
st.markdown("This application is a Streamlit library dashboard used to analyze data about motor vehicle collisions in New York City area 🗽💥🚗")

# Defines function to load data from provided file containing data and performs computations

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data

data = load_data(100000)

st.header("Where are the most injured people in Motor Vehicle Accidents?")
injured_people = st.slider("Number of persons injured in accidents", 0, 19)
st.map(data.query("injured_persons >= @injured_people")[["latitude", "longitude"]].dropna(how="any"))

# Shows raw data by clicking checkbox, unchecked by default

if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(data)


