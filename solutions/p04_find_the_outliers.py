# ============================================================
#  SOLUTION p04 -- Find the Outliers in a Different Column
#  The Cozy Bean  |  M1-W3 Lab01
#
#  How to run it: python solutions/p04_find_the_outliers.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

# Same two cleaning moves as the walkthrough, so the numbers line up.
df = df.dropna(axis=1, thresh=0.8 * len(df))
df.fillna(df.median(numeric_only=True), inplace=True)

Q1 = df['arr_delay'].quantile(0.25)
Q3 = df['arr_delay'].quantile(0.75)
IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower fence:", Q1 - 1.5 * IQR)
print("Upper fence:", Q3 + 1.5 * IQR)

outliers = df[
    (df['arr_delay'] < Q1 - 1.5 * IQR) |
    (df['arr_delay'] > Q3 + 1.5 * IQR)
]

print("Flagged flights:", outliers.shape[0])
print(f"Share of all flights: {outliers.shape[0] / df.shape[0] * 100:.1f}%")

print("Worst three arrivals:")
print(outliers.nlargest(3, 'arr_delay')[['month', 'day', 'carrier', 'arr_delay']]
      .to_string(index=False))

# Note the fence is NOT symmetric around zero, because Q1 and Q3
# are not. Arrivals have a long late tail and a short early one.
