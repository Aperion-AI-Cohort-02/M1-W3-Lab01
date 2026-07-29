# ============================================================
#  PRACTICE p09 -- BONUS: Buckets and Shares
#  The Cozy Bean  |  M1-W3 Lab01
#
#  *** BONUS -- beyond the class session. Nothing depends on
#  *** this file. Do it because it is genuinely useful, or skip it.
#
#  YOUR TASK:
#    Two new tools, both one-liners.
#      1. pd.cut turns a continuous column into labelled buckets.
#         Cut 'distance' into short (0-500), medium (500-1500)
#         and long (1500-5000), in a new column 'trip_length'.
#      2. Count the flights in each bucket, in bucket order.
#      3. Print the same thing as a PERCENTAGE, using
#         value_counts(normalize=True).
#      4. Average departure delay per bucket.
#      5. Top three carriers by share of all flights.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Flights in each bucket:
#    trip_length
#    short      80327
#    medium    183736
#    long       72713
#    Name: count, dtype: int64
#    Same thing as a share of all flights:
#    trip_length
#    short     23.9
#    medium    54.6
#    long      21.6
#    Name: proportion, dtype: float64
#    Average departure delay per bucket:
#    trip_length
#    short     13.40
#    medium    12.85
#    long      11.31
#    Name: dep_delay, dtype: float64
#    Top three carriers by share of all flights:
#    carrier
#    UA    17.4
#    B6    16.2
#    EV    16.1
#    Name: proportion, dtype: float64
#
#  HINT: pd.cut(df['distance'], bins=[0, 500, 1500, 5000],
#               labels=['short', 'medium', 'long'])
#        .sort_index() puts the buckets in bucket order rather
#        than count order.
#        normalize=True gives a share; multiply by 100 and .round(1).
#        On a bucketed column groupby needs observed=True, or
#        pandas warns you about categories nobody used.
#
#  WHY THIS IS INTERESTING: you just invented a column that did
#        not exist. "Long-haul" is a sentence a person can say;
#        "distance > 1500" is a filter. That is what tomorrow's
#        lab means by feature engineering.
#
#  How to run it: python practice/p09_bonus_bins_and_shares.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

# TODO 1: make the 'trip_length' column with pd.cut

# TODO 2: count the flights in each bucket, in bucket order
print("Flights in each bucket:")
print("(not counted yet)")

# TODO 3: the same as a percentage
print("Same thing as a share of all flights:")
print("(not worked out yet)")

# TODO 4: average departure delay per bucket
print("Average departure delay per bucket:")
print("(not worked out yet)")

# TODO 5: top three carriers by share
print("Top three carriers by share of all flights:")
print("(not worked out yet)")
