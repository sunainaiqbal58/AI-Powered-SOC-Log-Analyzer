import matplotlib
matplotlib.use("Agg")


import matplotlib.pyplot as plt
import os

from parser import parsed_logs

# Store failed logins by time
timeline = {}

for log in parsed_logs:

    if log["status"] == "Failed":

        time = log["time"]

        timeline[time] = timeline.get(time, 0) + 1

# Data
times = list(timeline.keys())
failed_attempts = list(timeline.values())

# Figure
plt.figure(figsize=(10,5))

# Line Chart
plt.plot(
    times,
    failed_attempts,
    marker="o",
    linewidth=2
)

# Title
plt.title("Attack Timeline")

# Labels
plt.xlabel("Time")
plt.ylabel("Failed Login Attempts")

# Grid
plt.grid(True, linestyle="--", alpha=0.5)

# Display values
for i, value in enumerate(failed_attempts):
    plt.text(times[i], value + 0.05, str(value), ha="center")

# Rotate X-axis labels
plt.xticks(rotation=45)

# Create folder
os.makedirs("reports_images", exist_ok=True)

# Save
report_path = os.path.join(
    "reports_images",
    "attack_timeline_chart.png"
)

plt.savefig(report_path, dpi=300)

print("Chart Saved Successfully!")
print("Location:", report_path)

plt.tight_layout()

plt.close()