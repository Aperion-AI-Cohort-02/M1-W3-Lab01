# ============================================================
#  The Cozy Bean -- Script 03: The Shape of Lateness
#  Lab STEPs 10-11.
#  Shows: a histogram, and how to read skew off it.
#  Run:   python scripts/03_chart_histogram.py
#         (from M1-W3-Lab01/)
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/flights.csv")

# Pick up where STEP 7 left off -- the same two cleaning moves.
# Every real analysis re-does its cleaning before it starts, which
# is why cleaning always lives at the top of the file.
df = df.dropna(axis=1, thresh=0.8 * len(df))
df.fillna(df.median(numeric_only=True), inplace=True)

# ---- Section 1  (STEP 10): profiling asks "is it OK?",
#      EDA asks "what is it saying?" ------------------------
print("=== STEP 10: FROM PROFILING TO EDA ===")
print("Profiling asked: is this table trustworthy?  (Yes, mostly.)")
print("EDA asks:        so what is it actually telling me?")
print()

# ---- Section 2  (STEP 11): the histogram --------------------
print("=== STEP 11: THE SHAPE OF DEPARTURE DELAY ===")
print(df['dep_delay'].describe())
print()

df['dep_delay'].hist(bins=50)
plt.title("Departure Delay Distribution (336,776 flights)")
plt.xlabel("Departure delay (minutes)")
plt.ylabel("Number of flights")

plt.savefig("charts/dep_delay_histogram.png")   # SAVE first...
print("Saved charts/dep_delay_histogram.png")
plt.show()                                       # ...THEN show
print("Window closed. Script finished.")
