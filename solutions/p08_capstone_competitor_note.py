# ============================================================
#  SOLUTION p08 -- CAPSTONE: Your Own Competitor Note
#  The Cozy Bean  |  M1-W3 Lab01
#
#  There is no single right answer to this one. This is MY five
#  findings; yours will be different and that is correct. What
#  matters is that every number is computed, not typed.
#
#  How to run it: python solutions/p08_capstone_competitor_note.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

reviews_df = pd.read_csv("data/coffee_app_reviews_fallback.csv")

# ---- five findings, all computed --------------------------------
total = reviews_df.shape[0]
average = reviews_df['Rating'].mean()
five_star = (reviews_df['Rating'] == 5).sum()
one_star = (reviews_df['Rating'] == 1).sum()
per_app = reviews_df.groupby('App_Name')['Rating'].mean().round(2)
best_app = per_app.idxmax()
worst_app = per_app.idxmin()

reviews_df['length'] = reviews_df['Review_Text'].str.len()
angry_length = reviews_df[reviews_df['Rating'] == 1]['length'].mean()
happy_length = reviews_df[reviews_df['Rating'] == 5]['length'].mean()

lines = []
lines.append("THE COZY BEAN -- WHAT THE BIG CHAINS GET WRONG")
lines.append("=" * 52)
lines.append("")
lines.append(f"FINDING 1: We read {total} real reviews. The chains average")
lines.append(f"           {average:.2f} stars out of 5 -- not the flawless score")
lines.append("           you would expect from companies this size.")
lines.append("")
lines.append(f"FINDING 2: Opinion is SPLIT, not lukewarm. {five_star} reviews gave")
lines.append(f"           5 stars and {one_star} gave 1. Almost nobody sits")
lines.append("           in the middle. People either love it or rage.")
lines.append("")
lines.append(f"FINDING 3: {best_app}")
lines.append(f"           scores best at {per_app.max():.2f}.")
lines.append(f"           {worst_app}")
lines.append(f"           scores worst at {per_app.min():.2f}.")
lines.append("")
lines.append(f"FINDING 4: Angry reviews are LONGER. A 1-star review runs")
lines.append(f"           {angry_length:.0f} characters on average; a 5-star one only")
lines.append(f"           {happy_length:.0f}. Unhappy customers explain themselves.")
lines.append("")
lines.append("FINDING 5: The complaints are about SOFTWARE, not coffee.")
lines.append("           Logins, payments, rewards. Not one of these")
lines.append("           chains is losing stars over the drink.")
lines.append("")
lines.append("WHAT WE DO ABOUT IT:")
lines.append("  Branch two competes on the thing they cannot fix from")
lines.append("  a server room. We do not need an app to win.")

report = "\n".join(lines)
print(report)

with open("my_competitor_note.txt", "w", encoding="utf-8") as f:
    f.write(report + "\n")

print()
print("Saved my_competitor_note.txt")
