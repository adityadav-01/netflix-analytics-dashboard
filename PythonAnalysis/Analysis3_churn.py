# Analysis3_churn.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# Step 1: Load cleaned dataset
# -----------------------------
file_path = "outputs/merged_clean.csv"
df = pd.read_csv(file_path)
print(f" Cleaned dataset loaded. Shape: {df.shape}")

# Ensure output folder exists
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# Step 2: Convert subscription_status to numeric
# -----------------------------
# Map: Active = 0, Churned = 1
df["subscription_status"] = df["subscription_status"].map({"Active": 0, "Churned": 1})

# Safety check
print("\n Unique values in subscription_status after conversion:", df["subscription_status"].unique())

# -----------------------------
# Step 3: Overall churn rate
# -----------------------------
churn_rate = df["subscription_status"].value_counts(normalize=True) * 100
print("\n Overall Churn Rate (%):")
print(churn_rate)

churn_rate.to_csv("outputs/churn_overall.csv")

plt.figure(figsize=(6, 6))
sns.barplot(x=churn_rate.index, y=churn_rate.values, palette="Set2")
plt.title("Overall Churn Rate (%)")
plt.xlabel("Subscription Status (0 = Active, 1 = Churned)")
plt.ylabel("Percentage")
plt.savefig("outputs/churn_overall.png")
plt.close()

# -----------------------------
# Step 4: Churn by Subscription Type
# -----------------------------
churn_by_sub = df.groupby("subscription_type")["subscription_status"].mean() * 100
print("\n Churn Rate by Subscription Type (%):")
print(churn_by_sub)

churn_by_sub.to_csv("outputs/churn_by_subscription.csv")

plt.figure(figsize=(7, 5))
sns.barplot(x=churn_by_sub.index, y=churn_by_sub.values, palette="mako")
plt.title("Churn Rate by Subscription Type (%)")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Subscription Type")
plt.savefig("outputs/churn_by_subscription.png")
plt.close()

# -----------------------------
# Step 5: Churn by Device Type
# -----------------------------
churn_by_device = df.groupby("device_type")["subscription_status"].mean() * 100
print("\n Churn Rate by Device Type (%):")
print(churn_by_device)

churn_by_device.to_csv("outputs/churn_by_device.csv")

plt.figure(figsize=(7, 5))
sns.barplot(x=churn_by_device.index, y=churn_by_device.values, palette="coolwarm")
plt.title("Churn Rate by Device Type (%)")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Device Type")
plt.savefig("outputs/churn_by_device.png")
plt.close()

print("\n Step 3 Completed! Results saved in 'outputs/' folder:")
print(" - churn_overall.csv & .png")
print(" - churn_by_subscription.csv & .png")
print(" - churn_by_device.csv & .png")
