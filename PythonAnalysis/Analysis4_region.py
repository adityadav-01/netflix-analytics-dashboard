# Analysis4_region.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# -----------------------------
# Step 1: Load cleaned dataset
# -----------------------------
file_path = "outputs/merged_clean.csv"
df = pd.read_csv(file_path)
print(f"Cleaned dataset loaded. Shape: {df.shape}")

# Ensure output folder exists
os.makedirs("outputs", exist_ok=True)

# Convert subscription_status if not numeric
if df["subscription_status"].dtype == "object":
    df["subscription_status"] = df["subscription_status"].map({"Active": 0, "Churned": 1})

# -----------------------------
# Step 2: Churn rate by country
# -----------------------------
churn_by_country = df.groupby("country")["subscription_status"].mean() * 100
churn_by_country = churn_by_country.reset_index().sort_values(by="subscription_status", ascending=False)

print("\nTop 10 Countries by Churn Rate (%):")
print(churn_by_country.head(10))

churn_by_country.to_csv("outputs/churn_by_country.csv", index=False)

# Plot top 15 as bar chart
plt.figure(figsize=(10, 6))
sns.barplot(data=churn_by_country.head(15), x="subscription_status", y="country", palette="coolwarm")
plt.title("Top 15 Countries by Churn Rate (%)")
plt.xlabel("Churn Rate (%)")
plt.ylabel("Country")
plt.savefig("outputs/churn_by_country.png")
plt.close()

# -----------------------------
# Step 3: Avg watch time by country
# -----------------------------
watch_by_country = df.groupby("country")["watch_time_minutes"].mean()
watch_by_country = watch_by_country.reset_index().sort_values(by="watch_time_minutes", ascending=False)

print("\nTop 10 Countries by Avg Watch Time (minutes):")
print(watch_by_country.head(10))

watch_by_country.to_csv("outputs/watch_by_country.csv", index=False)

# Plot top 15 as bar chart
plt.figure(figsize=(10, 6))
sns.barplot(data=watch_by_country.head(15), x="watch_time_minutes", y="country", palette="viridis")
plt.title("Top 15 Countries by Avg Watch Time (minutes)")
plt.xlabel("Avg Watch Time (minutes)")
plt.ylabel("Country")
plt.savefig("outputs/watch_by_country.png")
plt.close()

# -----------------------------
# Step 4: Choropleth Maps
# -----------------------------
# Churn Map
fig1 = px.choropleth(
    churn_by_country,
    locations="country",
    locationmode="country names",
    color="subscription_status",
    title="Churn Rate by Country (%)",
    color_continuous_scale="Reds"
)
fig1.write_html("outputs/churn_map.html")

# Watch Time Map
fig2 = px.choropleth(
    watch_by_country,
    locations="country",
    locationmode="country names",
    color="watch_time_minutes",
    title="Avg Watch Time by Country (minutes)",
    color_continuous_scale="Blues"
)
fig2.write_html("outputs/watch_map.html")

print("\nStep 4 Completed! Results saved in 'outputs/' folder:")
print(" - churn_by_country.csv, .png, and churn_map.html")
print(" - watch_by_country.csv, .png, and watch_map.html")
print(df.columns)
