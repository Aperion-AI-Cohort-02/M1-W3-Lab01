# ============================================================
#  The Cozy Bean -- Script 08: What Moves With What
#  Lab STEP 17.
#  Shows: correlation on four hand-picked columns first, read
#         out loud -- then the whole table as one wall of
#         colour.
#  Run:   python scripts/08_chart_correlation.py
#         (from M1-W3-Lab01/)
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/flights.csv")

# Pick up where STEP 7 left off -- the same two cleaning moves.
df = df.dropna(axis=1, thresh=0.8 * len(df))
df.fillna(df.median(numeric_only=True), inplace=True)

# ---- Section 1  (STEP 17a): four columns, read aloud --------
print("=== STEP 17: FOUR COLUMNS AT A TIME ===")
small = df[['dep_delay', 'arr_delay', 'distance', 'air_time']].corr()
print(small.round(4))
print()
print("Read the two that matter:")
print(f"  dep_delay vs arr_delay: {small.loc['dep_delay', 'arr_delay']:.4f}")
print("     -> very close to +1: leave late, arrive late. No surprise.")
print(f"  distance  vs dep_delay: {small.loc['distance', 'dep_delay']:.4f}")
print("     -> almost exactly 0: long flights are no likelier to")
print("        leave late than short ones. That IS a surprise.")
print()

plt.figure(figsize=(7, 6))
sns.heatmap(small, annot=True, vmin=-1, vmax=1, cmap='coolwarm')
plt.title("Four columns -- how they move together")
plt.tight_layout()
plt.savefig("charts/correlation_small.png")
print("Saved charts/correlation_small.png")
plt.show()

# ---- Section 2  (STEP 17b): the whole table -----------------
plt.figure(figsize=(9, 7))
print()
print("=== STEP 17: NOW THE WHOLE TABLE ===")
corr = df.corr(numeric_only=True)
print("Shape of the correlation matrix:", corr.shape)
print("Too many numbers to read. So don't read numbers -- read PATTERNS.")

sns.heatmap(corr, annot=False)
plt.title("Correlation Matrix -- every numeric column")
plt.tight_layout()
plt.savefig("charts/correlation_full.png")
print("Saved charts/correlation_full.png")
plt.show()
print("Window closed. Script finished.")
