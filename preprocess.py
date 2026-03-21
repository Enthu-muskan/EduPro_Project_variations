import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("C:/Users/hp/Downloads/EduPro Online Platform.xlsx - Users.csv")

# Create new columns
np.random.seed(42)

df["Experience"] = np.random.randint(1, 11, len(df))

df["Expertise"] = np.random.choice(
    ["Data Science", "Web Dev", "Machine Learning", "Cyber Security"],
    len(df)
)

df["TeacherRating"] = np.round(np.random.uniform(3.5, 5.0, len(df)), 2)

df["CourseRating"] = np.round(
    df["TeacherRating"] - np.random.uniform(0, 0.5, len(df)), 2
)

# Save new file
df.to_csv("data/final_data.csv", index=False)

print("✅ Preprocessing Done!")