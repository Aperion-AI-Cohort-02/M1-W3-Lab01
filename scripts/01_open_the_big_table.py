# ============================================================
#  The Cozy Bean -- Script 01: Open the Big Table
#  Lab STEPs 1-5.
#  Shows: what profiling is, then the four calls that answer
#         "what have I actually got here?"
#  Run:   python scripts/01_open_the_big_table.py
#         (from M1-W3-Lab01/)
# ============================================================

import pandas as pd

# ---- Section 1  (STEP 1): what profiling actually checks ----
print("=== THE PROFILING CHECKLIST ===")
print("Before you trust a number, interrogate the table it came from:")
print("  1. STRUCTURE -- how many rows, how many columns, what type is each")
print("  2. CONTENT   -- what do the numbers look like, what are the categories")
print("  3. QUALITY   -- what is missing, what is duplicated, what is wrong")
print()

# ---- Section 2  (STEP 2): open it ---------------------------
df = pd.read_csv("data/flights.csv")

print("=== STEP 2: HOW BIG IS THIS THING? ===")
print("Shape (rows, columns):", df.shape)
print(f"That is {df.shape[0]:,} flights.")
print()

# ---- Section 3  (STEP 3): look at both ends -----------------
print("=== STEP 3: THE FIRST FIVE ===")
print(df.head())
print()
print("=== STEP 3: THE LAST FIVE ===")
print(df.tail())
print()
print("Your terminal is too narrow for 19 columns, so pandas hid the")
print("middle with '...'. Ask for just the interesting ones:")
print(df[['month', 'day', 'carrier', 'dep_time', 'dep_delay',
          'arr_delay', 'tailnum']].tail())
print()
print("THERE they are: NaN. 'Not a Number' -- pandas for 'nothing here'.")
print("These flights never left. They were cancelled.")
print()

# ---- Section 4  (STEP 4): the full inventory ----------------
print("=== STEP 4: THE INVENTORY ===")
df.info()
print()

# ---- Section 5  (STEP 5): the summary page ------------------
print("=== STEP 5: THE SUMMARY PAGE (three columns of it) ===")
print(df[['dep_delay', 'air_time', 'distance']].describe())
