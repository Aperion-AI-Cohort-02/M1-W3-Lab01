# ============================================================
#  SOLUTION p07 -- Read the Competition's Reviews
#  The Cozy Bean  |  M1-W3 Lab01
#
#  How to run it: python solutions/p07_read_the_reviews.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

reviews_df = pd.read_csv("data/coffee_app_reviews_fallback.csv")

print("Reviews loaded:", reviews_df.shape[0])
print("Apps covered:", reviews_df['App_Name'].nunique())

print("Reviews per rating:")
print(reviews_df['Rating'].value_counts().sort_index())

print("Average rating per app:")
print(reviews_df.groupby('App_Name')['Rating'].mean().round(2))

angry = reviews_df[reviews_df['Rating'] == 1]
print("One-star reviews:", angry.shape[0])
print(f"That is {angry.shape[0] / reviews_df.shape[0] * 100:.1f}% of everything.")

print("One-star reviews per app:")
print(angry['App_Name'].value_counts())

# value_counts() sorts by count, biggest first. .sort_index() sorts
# by the rating itself -- which is what you want when the labels are
# 1 to 5 and you are reading a distribution rather than a ranking.
