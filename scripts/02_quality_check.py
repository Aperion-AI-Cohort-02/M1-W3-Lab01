# ============================================================
#  The Cozy Bean -- Script 02: Is This Table Trustworthy?
#  Lab STEPs 6-9.
#  Shows: measuring gaps, handling gaps, checking for
#         duplicates, and profiling the text columns.
#  Run:   python scripts/02_quality_check.py
#         (from M1-W3-Lab01/)
# ============================================================

import pandas as pd

df = pd.read_csv("data/flights.csv")

# ---- Section 1  (STEP 6): measure the gaps ------------------
print("=== STEP 6: HOW MANY VALUES ARE MISSING? ===")
print(df.isnull().sum())
print()
print("The same thing as a percentage, worst first:")
print((df.isnull().mean() * 100).sort_values(ascending=False))
print()

# ---- Section 2  (STEP 7): handle the gaps -------------------
print("=== STEP 7: DROP THE HOPELESS COLUMNS ===")
before = df.shape
df = df.dropna(axis=1, thresh=0.8 * len(df))
print("Shape before:", before)
print("Shape after: ", df.shape)
print("Nothing was dropped -- and that is the correct answer.")
print("No column here is anywhere near 80% empty.")
print()

print("=== STEP 7: FILL THE REST WITH THE MIDDLE VALUE ===")
print("Median departure delay:", df['dep_delay'].median())
print("Mean departure delay:  ", round(df['dep_delay'].mean(), 6))
df.fillna(df.median(numeric_only=True), inplace=True)
print()
print("Gaps left after filling:")
print(df.isnull().sum()[df.isnull().sum() > 0])
print("(tailnum is text, so a median cannot fill it. Numbers only.)")
print()

# ---- Section 3  (STEP 8): duplicates ------------------------
print("=== STEP 8: HAS ANYTHING BEEN COUNTED TWICE? ===")
print("Duplicate rows:", df.duplicated().sum())
print("Zero. Say that out loud -- it is a finding, not a non-answer.")
print("If it were not zero, the fix is one call: df.drop_duplicates()")
print()

# ---- Section 4  (STEP 9): profile the text columns ----------
print("=== STEP 9: HOW MANY DIFFERENT VALUES IN EACH TEXT COLUMN? ===")
for col in df.select_dtypes(include='str'):
    print(f"  {col:12} {df[col].nunique()}")
print()

print("Where do these flights take off from?")
print(df['origin'].value_counts())
