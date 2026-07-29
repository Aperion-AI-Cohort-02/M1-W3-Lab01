# ============================================================
#  PRACTICE p03 -- Fill It, or Drop It?
#  The Cozy Bean  |  M1-W3 Lab01
#
#  YOUR TASK:
#    arr_delay has 9,430 gaps. You have two honest options and
#    you must choose one, out loud.
#      1. Count the gaps in arr_delay.
#      2. Work out BOTH the mean and the median of the column.
#      3. Fill the gaps with the median, on a COPY, and prove
#         there are none left.
#      4. Separately, drop the gappy rows and report how many
#         rows survived.
#      5. Print one sentence saying which you would choose, and
#         why. (The expected output below has mine.)
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Gaps in arr_delay before: 9430
#    Mean arrival delay:   6.895377
#    Median arrival delay: -5.0
#    Gaps in arr_delay after filling: 0
#    Rows kept after dropping instead: 327346 of 336776
#    Median, because a handful of enormous delays drag the mean up.
#
#  HINT: Work on a copy so you do not clobber the original:
#        filled = df.copy()
#        Use f"{value:.6f}" to print the mean to six places.
#        dropna(subset=['arr_delay']) drops rows gappy in ONE column.
#
#  THINK ABOUT IT: the mean is +6.9 minutes but the median is -5.
#        The typical flight arrives EARLY. What would filling
#        9,430 gaps with +6.9 do to your story?
#
#  How to run it: python practice/p03_fill_or_drop.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

# TODO 1: count the gaps in arr_delay
print("Gaps in arr_delay before: (not counted yet)")

# TODO 2: print the mean (6 decimal places) and the median
print("Mean arrival delay:   (not worked out yet)")
print("Median arrival delay: (not worked out yet)")

# TODO 3: fill the gaps with the median on a copy, then re-count
print("Gaps in arr_delay after filling: (not filled yet)")

# TODO 4: drop the gappy rows instead, and report the survivors
print("Rows kept after dropping instead: ? of", df.shape[0])

# TODO 5: say which you would choose, and why, in one line
print("(your decision goes here)")
