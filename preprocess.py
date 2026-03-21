# preprocess.py
import pandas as pd
import numpy as np
import os
import sys

# -------------------
# Step 1: Path Setup
# -------------------
# Path to your raw dataset (update this to your actual file)
RAW_FILE = r"C:\Users\hp\Downloads\EduPro Online Platform.xlsx - Users.csv"

# Path to save processed file
BASE_DIR = r"C:\Users\hp\Desktop\Git-course\EduPro_Project-main (1)\EduPro_Project_variations"
DATA_DIR = os.path.join(BASE_DIR, "data")
FINAL_FILE = os.path.join(DATA_DIR, "final_data.csv")

# Make sure data folder exists
os.makedirs(DATA_DIR, exist_ok=True)

# -------------------
# Step 2: Preprocess Function
# -------------------
def preprocess_data():
    # Check if raw dataset exists
    if not os.path.exists(RAW_FILE):
        print("ERROR: Raw dataset not found!")
        print(f"Expected file at: {RAW_FILE}")
        sys.exit(1)

    # Load dataset based on file extension
    if RAW_FILE.lower().endswith(".xlsx"):
        print("Loading Excel file...")
        df = pd.read_excel(RAW_FILE)
    elif RAW_FILE.lower().endswith(".csv"):
        print("Loading CSV file...")
        df = pd.read_csv(RAW_FILE)
    else:
        print("ERROR: Unsupported file type. Use .csv or .xlsx")
        sys.exit(1)

    # -------------------
    # Step 3: Cleaning
    # -------------------
    df.drop_duplicates(inplace=True)
    df.fillna(0, inplace=True)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # -------------------
    # Step 4: Add instructor_rating if missing (1-5 scale)
    # -------------------
    if 'instructor_rating' not in df.columns:
        np.random.seed(42)
        df['instructor_rating'] = np.random.randint(1, 6, size=len(df))

    # -------------------
    # Step 5: Save processed data
    # -------------------
    df.to_csv(FINAL_FILE, index=False)
    print(f"Processed data saved at: {FINAL_FILE}")

# -------------------
# Step 6: Run
# -------------------
if __name__ == "__main__":
    preprocess_data()