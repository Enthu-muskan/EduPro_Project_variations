import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("EduPro Dashboard")

file_path = os.path.join(os.getcwd(), "data", "final_data.csv")

st.write("Loading from:", file_path)

df = pd.read_csv(file_path)

st.write(df.head())