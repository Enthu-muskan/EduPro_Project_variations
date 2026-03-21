# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------
# Paths
# -------------------
BASE_DIR = r"C:\Users\hp\Desktop\Git-course\EduPro_Project-main (1)\EduPro_Project_variations"
DATA_DIR = os.path.join(BASE_DIR, "data")
FINAL_FILE = os.path.join(DATA_DIR, "final_data.csv")

# Make sure final_data.csv exists
if not os.path.exists(FINAL_FILE):
    raise FileNotFoundError(f"{FINAL_FILE} not found. Run preprocess.py first.")

# -------------------
# Load data
# -------------------
df = pd.read_csv(FINAL_FILE)

print("=== Dataset Info ===")
print(df.info())
print("\n=== Head of Dataset ===")
print(df.head())
print("\n=== Statistical Summary ===")
print(df.describe())

# -------------------
# EDA Visualizations
# -------------------
sns.set(style="whitegrid")

# Function to safely plot and save
def safe_plot(fig, filename):
    path = os.path.join(DATA_DIR, filename)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)
    print(f"Saved plot: {path}")

# 1️⃣ Instructor Rating Distribution
if 'instructor_rating' in df.columns:
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df['instructor_rating'], bins=5, kde=True, color='skyblue', ax=ax)
    ax.set_title('Instructor Rating Distribution')
    ax.set_xlabel('Instructor Rating')
    ax.set_ylabel('Count')
    safe_plot(fig, "instructor_rating_dist.png")

# 2️⃣ Age Distribution
if 'age' in df.columns:
    fig, ax = plt.subplots(figsize=(8,5))
    sns.histplot(df['age'], bins=20, kde=True, color='orange', ax=ax)
    ax.set_title('Age Distribution of Users')
    ax.set_xlabel('Age')
    ax.set_ylabel('Count')
    safe_plot(fig, "age_dist.png")

# 3️⃣ Gender Distribution
if 'gender' in df.columns:
    gender_counts = df['gender'].value_counts()
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=gender_counts.index, y=gender_counts.values, palette="pastel", ax=ax)
    ax.set_title('Gender Distribution')
    ax.set_ylabel('Count')
    safe_plot(fig, "gender_dist.png")

# 4️⃣ Instructor Rating by Age (boxplot) — sampled to avoid freezing
if 'instructor_rating' in df.columns and 'age' in df.columns:
    sample_df = df.sample(min(1000, len(df)))  # sample max 1000 rows
    fig, ax = plt.subplots(figsize=(10,5))
    sns.boxplot(x='age', y='instructor_rating', data=sample_df, palette='coolwarm', ax=ax)
    ax.set_title('Instructor Rating by Age (Sampled)')
    ax.set_xlabel('Age')
    ax.set_ylabel('Instructor Rating')
    safe_plot(fig, "rating_by_age.png")

# 5️⃣ Optional: Top 10 users by rating
if 'instructor_rating' in df.columns and 'username' in df.columns:
    top_users = df[['username', 'instructor_rating']].sort_values(by='instructor_rating', ascending=False).head(10)
    print("\n=== Top 10 Users by Instructor Rating ===")
    print(top_users)

print("\n✅ EDA completed. Plots saved in 'data/' folder.")