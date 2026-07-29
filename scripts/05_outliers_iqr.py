# ============================================================
#  The Cozy Bean -- Script 05: The Strange Ones (IQR method)
#  Lab STEP 13.
#  Shows: the interquartile-range fence, and how many flights
#         fall outside it.
#  Run:   python scripts/05_outliers_iqr.py
#         (from M1-W3-Lab01/)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

# Pick up where STEP 7 left off -- the same two cleaning moves.
# This matters: outlier counts depend on what you cleaned first.
df = df.dropna(axis=1, thresh=0.8 * len(df))
df.fillna(df.median(numeric_only=True), inplace=True)

print("=== STEP 13: THE IQR FENCE ===")
print()

# ---- the three numbers everything is built from -------------
Q1 = df['dep_delay'].quantile(0.25)
Q3 = df['dep_delay'].quantile(0.75)
IQR = Q3 - Q1

print(f"Q1  (a quarter of flights are below this): {Q1}")
print(f"Q3  (three quarters are below this):       {Q3}")
print(f"IQR (Q3 - Q1, the width of the box):       {IQR}")
print()

# ---- the fence ----------------------------------------------
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print(f"Lower fence (Q1 - 1.5 * IQR): {lower}")
print(f"Upper fence (Q3 + 1.5 * IQR): {upper}")
print("Anything outside those two numbers is flagged as unusual.")
print()

# ---- who is outside it? -------------------------------------
outliers = df[
    (df['dep_delay'] < Q1 - 1.5 * IQR) |
    (df['dep_delay'] > Q3 + 1.5 * IQR)
]

print("Flagged flights (rows, columns):", outliers.shape)
print(f"That is {outliers.shape[0]:,} of {df.shape[0]:,} flights "
      f"({outliers.shape[0] / df.shape[0] * 100:.1f}%).")
print()

print("The worst five:")
print(outliers.nlargest(5, 'dep_delay')[
    ['month', 'day', 'carrier', 'origin', 'dest', 'dep_delay']])
print()
print("A 1,301-minute delay is 21 hours and 41 minutes.")
print("That is not a typo. That is somebody's very bad day.")
