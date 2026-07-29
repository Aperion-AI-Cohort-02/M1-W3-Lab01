# ============================================================
#  PRACTICE p06 -- A Chart of Your Own
#  The Cozy Bean  |  M1-W3 Lab01
#
#  YOUR TASK:
#    One chart, your choice of column, saved to charts/.
#      1. Make the charts/ folder if it is not there.
#      2. Draw ANY chart you like from this table. A histogram of
#         air_time is the obvious one, but a boxplot, a bar chart
#         of the top ten destinations, or a scatter plot all count.
#      3. Give it a title and axis labels.
#      4. Save it BEFORE you show it.
#
#  WHEN YOU ARE DONE, running this file should print something
#  like:
#    Saved charts/my_air_time_chart.png
#    Done.
#
#  ...and charts/ should contain a PNG you made. THE FILE IS THE
#  DELIVERABLE, not the printout. Open it and look at it.
#
#  HINT: os.makedirs("charts", exist_ok=True) first -- matplotlib
#        will not create the folder for you.
#        plt.savefig(path) BEFORE plt.show(), every time. Showing
#        a figure can clear it, and then you save a blank PNG.
#
#  How to run it: python practice/p06_your_own_chart.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/flights.csv")

# TODO 1: make sure charts/ exists

# TODO 2: draw a chart of your choosing

# TODO 3: title and axis labels

# TODO 4: save it, then show it
print("(no chart made yet)")
