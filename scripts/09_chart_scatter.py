# ============================================================
#  The Cozy Bean -- Script 09: One Dot Per Flight
#  Lab STEP 18.
#  Shows: a scatter plot of 336,776 points, and what a
#         correlation of almost exactly zero looks like.
#  Run:   python scripts/09_chart_scatter.py
#         (from M1-W3-Lab01/)
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/flights.csv")

# Pick up where STEP 7 left off -- the same two cleaning moves.
df = df.dropna(axis=1, thresh=0.8 * len(df))
df.fillna(df.median(numeric_only=True), inplace=True)

print("=== STEP 18: DISTANCE AGAINST DELAY ===")
print(f"Drawing {df.shape[0]:,} dots. This one takes a moment.")
print()

plt.figure(figsize=(9, 6))
plt.scatter(df['distance'], df['dep_delay'], s=1, alpha=0.2)
plt.xlabel("Distance (miles)")
plt.ylabel("Departure delay (minutes)")
plt.title("Every flight: distance vs departure delay")

plt.tight_layout()
plt.savefig("charts/distance_vs_delay.png")
print("Saved charts/distance_vs_delay.png")
plt.show()

print()
print("Read it: the cloud is a flat band, not a slope.")
print("Long flights are no likelier to leave late than short ones --")
print("which is exactly what the 0.0 in STEP 17 was telling you.")
print("Window closed. Script finished.")
