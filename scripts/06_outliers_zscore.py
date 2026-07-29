# ============================================================
#  The Cozy Bean -- Script 06: The Strange Ones (Z-score)
#  Lab STEPs 14-15.
#  Shows: one flight's z-score worked out by hand, then scipy
#         doing the same sum 336,776 times, then the two
#         methods compared.
#  Run:   python scripts/06_outliers_zscore.py
#         (from M1-W3-Lab01/)
# ============================================================

import pandas as pd
from scipy.stats import zscore

df = pd.read_csv("data/flights.csv")

# Pick up where STEP 7 left off -- the same two cleaning moves.
# This matters here too: with no gaps left, our hand calculation
# and scipy's are working on exactly the same numbers.
df = df.dropna(axis=1, thresh=0.8 * len(df))
df.fillna(df.median(numeric_only=True), inplace=True)

# ---- Section 1  (STEP 14): ONE flight, by hand --------------
print("=== STEP 14: ONE FLIGHT, WORKED OUT BY HAND ===")
print()

mean = df['dep_delay'].mean()
std = df['dep_delay'].std()

print(f"mean = df['dep_delay'].mean() = {mean:.6f}")
print(f"std  = df['dep_delay'].std()  = {std:.6f}")
print()

value = df.loc[151, 'dep_delay']
z = (value - mean) / std

print(f"Row 151 left {value} minutes late.")
print(f"z = (value - mean) / std")
print(f"z = ({value} - {mean:.6f}) / {std:.6f}")
print(f"z = {z:.6f}")
print()
print("That flight sits 21 standard deviations above the average.")
print("Beyond 3 is already suspicious. This one is off the map.")
print()

# ---- Section 2  (STEP 15): scipy, for every row -------------
print("=== STEP 15: NOW ALL 336,776 OF THEM ===")
df['zscore'] = zscore(df['dep_delay'].fillna(0))
outliers = df[df['zscore'].abs() > 3]

print("Flagged by z-score (rows, columns):", outliers.shape)
print()
print("The same flight, as scipy computed it:")
print(f"  our hand calculation : {z:.6f}")
print(f"  scipy's answer       : {df.loc[151, 'zscore']:.6f}")
print("Near-identical. The last few digits differ because scipy")
print("divides by n and .std() divides by n-1 -- invisible here.")
print()

# ---- Section 3  (STEP 15): the two methods disagree ---------
Q1 = df['dep_delay'].quantile(0.25)
Q3 = df['dep_delay'].quantile(0.75)
IQR = Q3 - Q1
iqr_out = df[(df['dep_delay'] < Q1 - 1.5 * IQR) |
             (df['dep_delay'] > Q3 + 1.5 * IQR)]

print("=== THE TWO METHODS DISAGREE ===")
print(f"  IQR method     flags {iqr_out.shape[0]:,} flights")
print(f"  Z-score method flags {outliers.shape[0]:,} flights")
print("Both are correct. They are asking different questions.")
