# -------------------------------------------------------
# Step 2: Engagement Patterns Analysis
# -------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset from Step 1
df = pd.read_csv("outputs/merged_clean.csv")

print("✅ Cleaned dataset loaded. Shape:", df.shape)

# -------------------------------------------------------
# 1. Average Watch Time by Device
# -------------------------------------------------------
avg_watch_by_device = df.groupby("device_type")["watch_time_minutes"].mean().sort_values(ascending=False)
print("\n📊 Average Watch Time by Device:\n", avg_watch_by_device)

# Plot
plt.figure(figsize=(6,4))
sns.barplot(x=avg_watch_by_device.index, y=avg_watch_by_device.values, palette="viridis")
plt.title("Average Watch Time by Device")
plt.xlabel("Device Type")
plt.ylabel("Avg Watch Time (minutes)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/avg_watch_by_device.png")
plt.close()

# -------------------------------------------------------
# 2. Average Watch Time by Subscription Type
# -------------------------------------------------------
avg_watch_by_sub = df.groupby("subscription_type")["watch_time_minutes"].mean().sort_values(ascending=False)
print("\n📊 Average Watch Time by Subscription Type:\n", avg_watch_by_sub)

# Plot
plt.figure(figsize=(6,4))
sns.barplot(x=avg_watch_by_sub.index, y=avg_watch_by_sub.values, palette="mako")
plt.title("Average Watch Time by Subscription Type")
plt.xlabel("Subscription Type")
plt.ylabel("Avg Watch Time (minutes)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/avg_watch_by_subscription.png")
plt.close()

# -------------------------------------------------------
# 3. Top 10 Most Watched Shows
# -------------------------------------------------------
top_shows = df.groupby("title")["watch_time_minutes"].sum().sort_values(ascending=False).head(10)
print("\n🏆 Top 10 Most Watched Shows:\n", top_shows)

# Plot
plt.figure(figsize=(8,5))
sns.barplot(x=top_shows.values, y=top_shows.index, palette="cubehelix")
plt.title("Top 10 Most Watched Shows")
plt.xlabel("Total Watch Time (minutes)")
plt.ylabel("Show Title")
plt.tight_layout()
plt.savefig("outputs/top_10_shows.png")
plt.close()

# -------------------------------------------------------
# Save Results
# -------------------------------------------------------
avg_watch_by_device.to_csv("outputs/avg_watch_by_device.csv")
avg_watch_by_sub.to_csv("outputs/avg_watch_by_subscription.csv")
top_shows.to_csv("outputs/top_10_shows.csv")

print("\n✅ Step 2 Completed! Results saved in 'outputs/' folder:")
print(" - avg_watch_by_device.csv & .png")
print(" - avg_watch_by_subscription.csv & .png")
print(" - top_10_shows.csv & .png")
