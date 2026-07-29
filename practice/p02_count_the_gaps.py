# ============================================================
#  PRACTICE p02 -- Count the Gaps, One Column at a Time
#  The Cozy Bean  |  M1-W3 Lab01
#
#  YOUR TASK:
#    The walkthrough used df.isnull().sum() to get every column
#    at once. Do it the long way instead, with a Week-1 for loop
#    -- and print ONLY the columns that actually have gaps.
#      1. Loop over the column names.
#      2. For each one, count the missing values.
#      3. If the count is above zero, print the name, the count,
#         and the percentage.
#      4. Finish with the total for the whole table.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Columns with gaps in them:
#      dep_time       8255  (2.45%)
#      dep_delay      8255  (2.45%)
#      arr_time       8713  (2.59%)
#      arr_delay      9430  (2.80%)
#      tailnum        2512  (0.75%)
#      air_time       9430  (2.80%)
#    Total missing values in the whole table: 46595
#
#  HINT: for name in df.columns:  walks the names one at a time.
#        df[name].isna().sum() counts the gaps in one column.
#        The alignment above is f"  {name:12} {gaps:>6}" and the
#        percentage is f"({percent:.2f}%)".
#        df.isna().sum().sum() -- yes, twice -- totals the lot.
#
#  How to run it: python practice/p02_count_the_gaps.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

# TODO 1: loop over the columns and print the ones with gaps
print("Columns with gaps in them:")
print("  (not counted yet)")

# TODO 2: print the total number of missing values in the table
print("Total missing values in the whole table: (not counted yet)")
