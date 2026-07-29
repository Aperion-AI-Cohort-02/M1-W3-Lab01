# ============================================================
#  SOLUTION p05 -- A Function That Profiles Any Column
#  The Cozy Bean  |  M1-W3 Lab01
#
#  How to run it: python solutions/p05_a_function_that_profiles.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd


def profile_column(df, column_name):
    """Return the five profiling facts about one numeric column."""
    values = df[column_name]
    return {
        'column': column_name,
        'missing': int(values.isna().sum()),
        'mean': round(values.mean(), 2),
        'median': values.median(),
        'biggest': values.max(),
    }


df = pd.read_csv("data/flights.csv")

for name in ['dep_delay', 'arr_delay', 'air_time', 'distance']:
    facts = profile_column(df, name)
    print(f"{facts['column']:11} missing={facts['missing']:>5} "
          f"mean={facts['mean']:>9} median={facts['median']:>7} "
          f"biggest={facts['biggest']}")

# Week 1's def, Week 1's dictionary, Week 3's data. The function does
# not care which column you hand it -- which is the whole point of
# writing it once instead of copying four blocks of print statements.
