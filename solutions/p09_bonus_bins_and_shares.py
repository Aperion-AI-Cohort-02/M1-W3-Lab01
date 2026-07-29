# ============================================================
#  SOLUTION p09 -- BONUS: Buckets and Shares
#  The Cozy Bean  |  M1-W3 Lab01
#
#  BONUS material -- beyond the class session. Nothing depends
#  on this file.
#
#  How to run it: python solutions/p09_bonus_bins_and_shares.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

# ---- pd.cut: turn a continuous column into labelled buckets ----
df['trip_length'] = pd.cut(
    df['distance'],
    bins=[0, 500, 1500, 5000],
    labels=['short', 'medium', 'long'],
)

print("Flights in each bucket:")
print(df['trip_length'].value_counts().sort_index())

print("Same thing as a share of all flights:")
print((df['trip_length'].value_counts(normalize=True).sort_index() * 100).round(1))

print("Average departure delay per bucket:")
print(df.groupby('trip_length', observed=True)['dep_delay'].mean().round(2))

# ---- and shares of a text column -------------------------------
print("Top three carriers by share of all flights:")
print((df['carrier'].value_counts(normalize=True).head(3) * 100).round(1))

# pd.cut is feature engineering, which is Lab02's whole subject:
# one continuous column becomes one categorical column that a human
# can actually talk about. "Long-haul flights" is a sentence;
# "distance > 1500" is a filter.
