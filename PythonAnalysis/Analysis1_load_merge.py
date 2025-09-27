# -------------------------------------------------------
# Step 1: Load & Merge Netflix Datasets (Clean Version)
# Save output as merged_clean.csv
# -------------------------------------------------------

import pandas as pd
import os

# Make sure outputs folder exists
os.makedirs("outputs", exist_ok=True)

# File paths
titles_path = r"C:\Users\Aditya Yadav\Desktop\netflix_project\data\netflix_titles.csv"
activity_path = r"C:\Users\Aditya Yadav\Desktop\netflix_project\data\user_activity_dataset.csv"

# ---- Load Netflix Titles ----
titles = pd.read_csv(titles_path, encoding="latin1")   # latin1 worked for you
print(f"Titles dataset loaded. Shape: {titles.shape}")

# ---- Load User Activity ----
activity = pd.read_csv(activity_path, encoding="utf-8")   # utf-8 worked
print(f"Activity dataset loaded. Shape: {activity.shape}")

# ---- Merge on show_id ----
df = activity.merge(titles, on="show_id", how="left")
print(f"Merged dataset created. Shape: {df.shape}")

# ---- Drop junk unnamed columns ----
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
print(f"Cleaned dataset. Shape: {df.shape}")

# ---- Save cleaned dataset ----
output_path = "outputs/merged_clean.csv"
df.to_csv(output_path, index=False)
print(f"Cleaned dataset saved to: {output_path}")

# If column has suffix from merge, fix it
if "country_y" in df.columns:
    df.rename(columns={"country_y": "country"}, inplace=True)
if "country_x" in df.columns:  
    df.drop(columns=["country_x"], inplace=True)  # in case duplicate



# --- Fix multi-country columns ---
# Split rows where 'country' has multiple countries separated by comma
df = df.assign(country=df['country'].str.split(', ')).explode('country')

# Strip spaces
df['country'] = df['country'].str.strip()

print("Fixed multi-country rows. New shape:", df.shape)

# ---- Preview ----
print("\n🔹 Preview of Cleaned Dataset:")
print(df.head())
