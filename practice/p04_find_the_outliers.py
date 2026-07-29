# ============================================================
#  PRACTICE p04 -- Find the Outliers in a Different Column
#  The Cozy Bean  |  M1-W3 Lab01
#
#  YOUR TASK:
#    The walkthrough put the IQR fence around dep_delay (leaving
#    late). Do the whole thing again for arr_delay (arriving
#    late) -- from scratch, without peeking at script 05.
#      1. Clean the table the same way STEP 7 did, so your
#         numbers line up with everyone else's.
#      2. Work out Q1, Q3 and IQR for arr_delay.
#      3. Print both fences.
#      4. Count the flights outside them, and the share.
#      5. Show the three worst arrivals.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Q1: -16.0
#    Q3: 13.0
#    IQR: 29.0
#    Lower fence: -59.5
#    Upper fence: 56.5
#    Flagged flights: 30203
#    Share of all flights: 9.0%
#    Worst three arrivals:
#     month  day carrier  arr_delay
#         1    9      HA     1272.0
#         6   15      MQ     1127.0
#         1   10      MQ     1109.0
#
#  HINT: The two cleaning lines are:
#          df = df.dropna(axis=1, thresh=0.8 * len(df))
#          df.fillna(df.median(numeric_only=True), inplace=True)
#        Then .quantile(0.25) and .quantile(0.75).
#        The fence is Q1 - 1.5 * IQR and Q3 + 1.5 * IQR.
#        df.nlargest(3, 'arr_delay') gets the worst three, and
#        .to_string(index=False) hides the row numbers.
#
#  NOTICE: the fence is NOT symmetric around zero. Why not?
#
#  How to run it: python practice/p04_find_the_outliers.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

# TODO 1: the same two cleaning moves as STEP 7

# TODO 2: Q1, Q3 and IQR for arr_delay
print("Q1: (not worked out yet)")
print("Q3: (not worked out yet)")
print("IQR: (not worked out yet)")

# TODO 3: the two fences
print("Lower fence: (not worked out yet)")
print("Upper fence: (not worked out yet)")

# TODO 4: how many flights fall outside, and what share
print("Flagged flights: (not counted yet)")
print("Share of all flights: (not worked out yet)")

# TODO 5: the three worst arrivals
print("Worst three arrivals:")
print("(not found yet)")
