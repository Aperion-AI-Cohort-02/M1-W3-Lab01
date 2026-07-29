# ============================================================
#  PRACTICE p01 -- Profile the Table
#  The Cozy Bean  |  M1-W3 Lab01
#
#  YOUR TASK:
#    Mrs Adeyemi's workshop opens with four questions about any
#    table you are handed. Answer all four in code:
#      1. How many rows?
#      2. How many columns?
#      3. What are they called?
#      4. How many are text, and how many are numbers?
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Rows: 336776
#    Columns: 19
#    Column names:
#     - year
#     - month
#     ...one line per column, all 19...
#     - time_hour
#    Text columns: 5
#    Numeric columns: 14
#
#  HINT: df.shape is a tuple -- shape[0] and shape[1].
#        df.columns is a list of names you can loop over.
#        df.select_dtypes(include='str') keeps only text columns;
#        include='number' keeps only numeric ones. len() of
#        .columns on either gives you a count.
#
#  How to run it: python practice/p01_profile_the_table.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

# TODO 1: print the row count and the column count
print("Rows: (not counted yet)")
print("Columns: (not counted yet)")

# TODO 2: print "Column names:" then one " - name" line per column
print("Column names:")
print(" - (not listed yet)")

# TODO 3: print how many columns are text and how many are numeric
print("Text columns: (not counted yet)")
print("Numeric columns: (not counted yet)")
