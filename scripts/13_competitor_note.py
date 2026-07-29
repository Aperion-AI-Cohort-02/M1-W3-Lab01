# ============================================================
#  The Cozy Bean -- Script 13: The Competitor Note
#  Lab STEP 23 -- the capstone of this lab.
#  Shows: everything from Cluster I, turned into a written
#         artifact you could actually hand to somebody.
#  Run:   python scripts/13_competitor_note.py
#         (from M1-W3-Lab01/)
# ============================================================

import pandas as pd

CSV_PATH = "data/coffee_app_reviews_fallback.csv"

reviews_df = pd.read_csv(CSV_PATH)

# ---- the four numbers the note is built from ----------------
total = reviews_df.shape[0]
apps = reviews_df['App_Name'].nunique()
overall = reviews_df['Rating'].mean()
unhappy = reviews_df[reviews_df['Rating'] <= 2]
unhappy_share = unhappy.shape[0] / total * 100

per_app = reviews_df.groupby('App_Name').agg(
    reviews=('Rating', 'count'),
    average_rating=('Rating', 'mean'),
).sort_values('average_rating', ascending=False)

best = per_app.index[0]
worst = per_app.index[-1]

# ---- write it out, using Week-1 f-strings and open() --------
lines = []
lines.append("=" * 58)
lines.append("   THE COZY BEAN -- COMPETITOR SCOUTING NOTE")
lines.append("   Before we open branch two")
lines.append("=" * 58)
lines.append("")
lines.append(f"Evidence: {total} public app-store reviews across {apps} coffee chains.")
lines.append(f"Average rating across all of them: {overall:.2f} out of 5")
lines.append(f"Reviews of 2 stars or worse: {unhappy.shape[0]} ({unhappy_share:.1f}%)")
lines.append("")
lines.append("Per chain, best first:")
for app_name, row in per_app.iterrows():
    lines.append(f"  {app_name:42} {row['average_rating']:.2f}  ({int(row['reviews'])} reviews)")
lines.append("")
lines.append(f"FINDING: {best} has the happiest app customers.")
lines.append(f"         {worst} has the most to fix.")
lines.append("")
lines.append("WHAT THIS MEANS FOR US:")
lines.append("  The chains are not being marked down on their coffee.")
lines.append("  They are being marked down on their APPS -- logins,")
lines.append("  payment, and rewards that do not work.")
lines.append("  Branch two does not need an app to beat them.")
lines.append("  It needs the thing an app cannot fake.")
lines.append("")
lines.append("=" * 58)

report = "\n".join(lines)
print(report)

with open("competitor_findings.txt", "w", encoding="utf-8") as f:
    f.write(report + "\n")

print()
print("Saved competitor_findings.txt")
print("That file is the deliverable. Open it -- it is yours.")
