import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎓 EduPro Dashboard")

df = pd.read_csv("../data/final_data.csv")

# KPI
st.header("📊 KPI Metrics")

col1, col2 = st.columns(2)
col1.metric("Avg Teacher Rating", round(df["TeacherRating"].mean(), 2))
col2.metric("Avg Course Rating", round(df["CourseRating"].mean(), 2))

# Plot 1
st.subheader("Experience vs Teacher Rating")
fig1, ax1 = plt.subplots()
ax1.scatter(df["Experience"], df["TeacherRating"])
st.pyplot(fig1)

# Plot 2
st.subheader("Teacher vs Course Rating")
fig2, ax2 = plt.subplots()
ax2.scatter(df["TeacherRating"], df["CourseRating"])
st.pyplot(fig2)

# Expertise
st.subheader("Expertise Performance")
exp = df.groupby("Expertise")["CourseRating"].mean()
st.bar_chart(exp)

# Top instructors
st.subheader("Top Instructors")
top = df.sort_values(by="TeacherRating", ascending=False)
st.dataframe(top.head(10))