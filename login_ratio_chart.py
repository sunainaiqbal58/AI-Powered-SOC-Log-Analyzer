# login_ratio_chart.py

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os

# Import statistics
from log_statistics import failed_logins, successful_logins

# Data
labels = ["Failed", "Successful"]
sizes = [failed_logins, successful_logins]
colors = ["red", "green"]

# Create figure
plt.figure(figsize=(6, 6))

# Create pie chart
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90
)

# Chart title
plt.title("Login Success Ratio")

# Make pie chart a perfect circle
plt.axis("equal")

# Create folder if it doesn't exist
os.makedirs("reports_images", exist_ok=True)

# Save chart
report_path = os.path.join(
    "reports_images",
    "login_ratio_chart.png"
)

plt.savefig(report_path, dpi=300)

print("Chart Saved Successfully!")
print("Location:", report_path)

# Show chart
plt.close()