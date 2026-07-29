# ============================================================
#  SOLUTION p06 -- A Chart of Your Own
#  The Cozy Bean  |  M1-W3 Lab01
#
#  How to run it: python solutions/p06_your_own_chart.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/flights.csv")

df['air_time'].hist(bins=40)
plt.title("How Long Are These Flights?")
plt.xlabel("Air time (minutes)")
plt.ylabel("Number of flights")

plt.savefig("charts/my_air_time_chart.png")     # save BEFORE show
print("Saved charts/my_air_time_chart.png")

plt.show()
print("Done.")

# Any of these would also have been a correct answer:
#   df.boxplot(column='air_time')
#   df['dest'].value_counts().head(10).plot(kind='bar')
#   plt.scatter(df['air_time'], df['distance'], s=1)
# The only two rules: os.makedirs first, and savefig BEFORE show.
