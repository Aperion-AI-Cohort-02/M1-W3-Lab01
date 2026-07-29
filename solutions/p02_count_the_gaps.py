# ============================================================
#  SOLUTION p02 -- Count the Gaps, One Column at a Time
#  The Cozy Bean  |  M1-W3 Lab01
#
#  How to run it: python solutions/p02_count_the_gaps.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

# A Week-1 for loop over the columns. df.columns is just a list
# of names, so a for loop walks it exactly like a list of drinks.
print("Columns with gaps in them:")
for name in df.columns:
    gaps = df[name].isna().sum()
    if gaps > 0:
        percent = gaps / len(df) * 100
        print(f"  {name:12} {gaps:>6}  ({percent:.2f}%)")

total_gaps = df.isna().sum().sum()
print("Total missing values in the whole table:", total_gaps)

# isna().sum() gives one number per column. Adding .sum() again
# collapses those into a single number for the whole table.
