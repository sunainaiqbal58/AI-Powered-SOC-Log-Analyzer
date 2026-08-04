import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os

# Import statistics
from log_statistics import ip_counts

# Data
ips = list(ip_counts.keys())
attempts = list(ip_counts.values())

# Create Figure
plt.figure(figsize=(8, 5))

# Horizontal Bar Chart
plt.barh(ips, attempts, color="orange")

# Title
plt.title("Top Attacking IPs")

# Axis Labels
plt.xlabel("Failed Login Attempts")
plt.ylabel("IP Addresses")

# Grid
plt.grid(axis="x", linestyle="--", alpha=0.5)

# Display Values
for i, value in enumerate(attempts):
    plt.text(value + 0.1, i, str(value), va="center")

# Create Folder
os.makedirs("reports_images", exist_ok=True)

# Save Chart
report_path = os.path.join(
    "reports_images",
    "top_attacking_ip_chart.png"
)

plt.savefig(report_path, dpi=300)

print("Chart Saved Successfully!")
print("Location:", report_path)

plt.tight_layout()
plt.show()