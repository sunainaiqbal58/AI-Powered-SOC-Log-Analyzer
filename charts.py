# charts.py


from ai_summary import generate_ai_report
import matplotlib
matplotlib.use("Agg")

import charts
import os
import matplotlib.pyplot as plt

# Import statistics
from log_statistics import (
    failed_logins,
    successful_logins
)

# Create folder if it doesn't exist
os.makedirs("static/charts", exist_ok=True)

# Data
labels = ["Failed", "Successful"]
values = [failed_logins, successful_logins]

# Create Figure
plt.figure(figsize=(6, 4))

# Create Bar Chart
plt.bar(
    labels,
    values,
    color=["crimson", "seagreen"],
    width=0.5
)

# Title
plt.title(
    "SSH Login Statistics",
    fontsize=15,
    fontweight="bold"
)

# Axis Labels
plt.xlabel(
    "Login Status",
    fontsize=11
)

plt.ylabel(
    "Number of Logins",
    fontsize=11
)

# Horizontal Grid
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.4
)

# Display values on top of bars
for i, value in enumerate(values):

    plt.text(
        i,
        value + 0.1,
        str(value),
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

# Adjust Layout
plt.tight_layout()

# Save Chart
chart_path = "static/charts/login_statistics.png"

plt.savefig(
    chart_path,
    dpi=300
)

# Free Memory
plt.close()

print("Chart Saved Successfully!")
print("Location:", chart_path)