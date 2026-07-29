# ============================================================
#  The Cozy Bean -- Script 04: The Box and the Bars
#  Lab STEP 12.
#  Shows: the same delay column as a boxplot, then a bar chart
#         of a text column's counts. Two charts, one script.
#  Run:   python scripts/04_chart_box_and_bar.py
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

# ---- Section 1  (STEP 12a): the boxplot ---------------------
print("=== STEP 12: THE SAME COLUMN, AS A BOX ===")
q1 = df['dep_delay'].quantile(0.25)
q2 = df['dep_delay'].quantile(0.50)
q3 = df['dep_delay'].quantile(0.75)
print(f"Bottom of the box (25%): {q1}")
print(f"Line in the box   (50%): {q2}")
print(f"Top of the box    (75%): {q3}")
print("Everything past the whiskers prints as a dot. There are a lot of dots.")
print()

df.boxplot(column='dep_delay')
plt.title("Departure Delay -- the box and the outlier cloud")
plt.ylabel("Departure delay (minutes)")
plt.savefig("charts/dep_delay_boxplot.png")
print("Saved charts/dep_delay_boxplot.png")
plt.show()

# ---- Section 2  (STEP 12b): the bar chart -------------------
plt.figure()
print()
print("=== STEP 12: WHICH AIRLINES FLY THE MOST? ===")
print(df['carrier'].value_counts().head())
print()

df['carrier'].value_counts().plot(kind='bar')
plt.title("Flights per Carrier")
plt.xlabel("Carrier code")
plt.ylabel("Number of flights")
plt.tight_layout()
plt.savefig("charts/flights_per_carrier.png")
print("Saved charts/flights_per_carrier.png")
plt.show()
print("Window closed. Script finished.")
