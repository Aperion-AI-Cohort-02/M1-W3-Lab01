# ============================================================
#  SOLUTION p03 -- Fill It, or Drop It?
#  The Cozy Bean  |  M1-W3 Lab01
#
#  How to run it: python solutions/p03_fill_or_drop.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

print("Gaps in arr_delay before:", df['arr_delay'].isna().sum())

mean_delay = df['arr_delay'].mean()
median_delay = df['arr_delay'].median()
print(f"Mean arrival delay:   {mean_delay:.6f}")
print(f"Median arrival delay: {median_delay}")

filled = df.copy()
filled['arr_delay'] = filled['arr_delay'].fillna(median_delay)
print("Gaps in arr_delay after filling:", filled['arr_delay'].isna().sum())

dropped = df.dropna(subset=['arr_delay'])
print(f"Rows kept after dropping instead: {dropped.shape[0]} of {df.shape[0]}")

print("Median, because a handful of enormous delays drag the mean up.")

# The mean is about 6.9 minutes but the median is -5 -- the typical
# flight actually arrives EARLY. Filling 9,430 gaps with +6.9 would
# invent lateness that never happened. The median is the honest fill
# on any skewed column, and money and delays are always skewed.
