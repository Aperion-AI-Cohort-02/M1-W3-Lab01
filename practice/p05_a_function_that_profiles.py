# ============================================================
#  PRACTICE p05 -- A Function That Profiles Any Column   (*)
#  The Cozy Bean  |  M1-W3 Lab01
#
#  YOUR TASK:
#    You have now typed "missing, mean, median, max" about six
#    times. Write it ONCE, as a function, and call it four times.
#      1. Write profile_column(df, column_name) that RETURNS a
#         dictionary with five keys: column, missing, mean,
#         median, biggest.
#      2. Round the mean to 2 decimal places inside the function.
#      3. Loop over dep_delay, arr_delay, air_time and distance,
#         calling your function on each and printing one line.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    dep_delay   missing= 8255 mean=    12.64 median=   -2.0 biggest=1301.0
#    arr_delay   missing= 9430 mean=      6.9 median=   -5.0 biggest=1272.0
#    air_time    missing= 9430 mean=   150.69 median=  129.0 biggest=695.0
#    distance    missing=    0 mean=  1039.91 median=  872.0 biggest=4983
#
#  HINT: This is Week 1's def and Week 1's dictionary, pointed at
#        a Week-3 table. The shape is:
#            def profile_column(df, column_name):
#                values = df[column_name]
#                return {'column': column_name, ...}
#        Wrap the counts in int() so they print as 8255 not
#        np.int64(8255).
#        The print line is:
#            print(f"{facts['column']:11} missing={facts['missing']:>5} "
#                  f"mean={facts['mean']:>9} median={facts['median']:>7} "
#                  f"biggest={facts['biggest']}")
#
#  WHY THIS ONE MATTERS: every script in Lab02 starts by repeating
#        the same cleaning block. A function is how you stop doing
#        that. This is the habit that separates a script from a tool.
#
#  How to run it: python practice/p05_a_function_that_profiles.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd


# TODO 1: write profile_column(df, column_name) returning a dict
def profile_column(df, column_name):
    return {'column': column_name, 'missing': 0, 'mean': 0,
            'median': 0, 'biggest': 0}


df = pd.read_csv("data/flights.csv")

# TODO 2: loop over the four columns and print one line each
for name in ['dep_delay', 'arr_delay', 'air_time', 'distance']:
    facts = profile_column(df, name)
    print(f"{facts['column']:11} (not profiled yet)")
