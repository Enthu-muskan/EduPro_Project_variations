import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/final_data.csv")

print(df.head())

# Plot 1
plt.figure()
sns.scatterplot(x="Experience", y="TeacherRating", data=df)
plt.title("Experience vs Teacher Rating")
plt.savefig("exp_vs_rating.png")

# Plot 2
plt.figure()
sns.scatterplot(x="TeacherRating", y="CourseRating", data=df)
plt.title("Teacher vs Course Rating")
plt.savefig("teacher_vs_course.png")

# Expertise performance
exp = df.groupby("Expertise")["CourseRating"].mean()
print("\nExpertise Performance:\n", exp)

exp.plot(kind="bar", title="Expertise Performance")
plt.savefig("expertise.png")

# Top instructors
top = df.sort_values(by="TeacherRating", ascending=False)
print("\nTop Instructors:\n", top.head())

print("✅ EDA COMPLETED (Graphs saved as images)")