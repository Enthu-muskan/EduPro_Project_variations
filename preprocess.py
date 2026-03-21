import pandas as pd
import os

print("🚀 Starting preprocessing...")

# Correct path (FIXED)
input_path = r"C:\Users\hp\Downloads\EduPro Online Platform.xlsx - Users.csv"

# Check file exists
if not os.path.exists(input_path):
    print("❌ Input file NOT found:", input_path)
else:
    print("✅ Input file found")

    # Load data
    df = pd.read_csv(input_path)

    print("✅ Data loaded")

    # Basic cleaning
    df.dropna(inplace=True)

    # Create data folder
    os.makedirs("data", exist_ok=True)

    # Save cleaned file
    output_path = os.path.join("data", "final_data.csv")
    df.to_csv(output_path, index=False)

    print("✅ File saved at:", os.path.abspath(output_path))