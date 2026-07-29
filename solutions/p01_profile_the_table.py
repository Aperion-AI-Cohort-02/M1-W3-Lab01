# ============================================================
#  SOLUTION p01 -- Profile the Table
#  The Cozy Bean  |  M1-W3 Lab01
#
#  How to run it: python solutions/p01_profile_the_table.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("Column names:")
for name in df.columns:
    print(" -", name)

print("Text columns:", len(df.select_dtypes(include='str').columns))
print("Numeric columns:", len(df.select_dtypes(include='number').columns))

# shape is an ATTRIBUTE (no brackets); select_dtypes is a METHOD.
# Getting that wrong is the single commonest pandas error there is.
