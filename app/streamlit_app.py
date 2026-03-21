# app/streamlit_app.py
import streamlit as st
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------
# Paths
# -------------------
BASE_DIR = r"C:\Users\hp\Desktop\Git-course\EduPro_Project-main (1)\EduPro_Project_variations"
DATA_DIR = os.path.join(BASE_DIR, "data")
FINAL_FILE = os.path.join(DATA_DIR, "final_data.csv")

# -------------------
# Load Data
# -------------------
@st.cache_data
def load_data():
    if os.path.exists(FINAL_FILE):
        return pd.read_csv(FINAL_FILE)
    else:
        st.error(f"File not found: {FINAL_FILE}")
        return pd.DataFrame()

df = load_data()

# -------------------
# Check for instructor column
# -------------------
instructor_col = 'instructor_name' if 'instructor_name' in df.columns else 'username'

# -------------------
# Dashboard Title
# -------------------
st.set_page_config(page_title="EduPro Instructor Dashboard", layout="wide")
st.title("EduPro Instructor Performance Dashboard")

# -------------------
# KPIs
# -------------------
total_instructors = df[instructor_col].nunique()
total_users = df['userid'].nunique() if 'userid' in df.columns else 0
average_rating = df['instructor_rating'].mean() if 'instructor_rating' in df.columns else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Instructors", total_instructors)
col2.metric("Total Users", total_users)
col3.metric("Average Rating", round(average_rating, 2))

st.markdown("---")

# -------------------
# EDA Graphs
# -------------------
sns.set(style="whitegrid")

def plot_hist(column, title, color='skyblue', bins=10):
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df[column], bins=bins, kde=True, color=color, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    st.pyplot(fig)

def plot_bar(column, title, color_palette="pastel"):
    counts = df[column].value_counts()
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=counts.index, y=counts.values, palette=color_palette, ax=ax)
    ax.set_title(title)
    ax.set_ylabel("Count")
    st.pyplot(fig)

def plot_box(x_col, y_col, title):
    sample_df = df.sample(min(1000, len(df)))  # sample max 1000 rows to avoid freezing
    fig, ax = plt.subplots(figsize=(10,5))
    sns.boxplot(x=x_col, y=y_col, data=sample_df, palette='coolwarm', ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

# -------------------
# Show EDA Charts
# -------------------
st.subheader("Instructor Rating Distribution")
if 'instructor_rating' in df.columns:
    plot_hist('instructor_rating', "Instructor Rating Distribution", color='skyblue', bins=5)

st.subheader("Age Distribution")
if 'age' in df.columns:
    plot_hist('age', "Age Distribution of Users", color='orange', bins=20)

st.subheader("Gender Distribution")
if 'gender' in df.columns:
    plot_bar('gender', "Gender Distribution")

st.subheader("Instructor Rating by Age (Sampled)")
if 'instructor_rating' in df.columns and 'age' in df.columns:
    plot_box('age', 'instructor_rating', "Instructor Rating by Age")

# -------------------
# Optional: Top 10 Users by Rating
# -------------------
st.subheader("Top 10 Users by Instructor Rating")
if 'instructor_rating' in df.columns and 'username' in df.columns:
    top_users = df[['username', 'instructor_rating']].sort_values(by='instructor_rating', ascending=False).head(10)
    st.dataframe(top_users)