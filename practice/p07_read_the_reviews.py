# ============================================================
#  PRACTICE p07 -- Read the Competition's Reviews
#  The Cozy Bean  |  M1-W3 Lab01
#
#  YOUR TASK:
#    No scraping in this one -- the reviews are already in data/.
#    Interrogate them.
#      1. How many reviews, and how many apps?
#      2. How many reviews at each star rating, 1 to 5 in order?
#      3. What is the average rating for each app?
#      4. How many 1-star reviews are there, and what share of
#         everything is that?
#      5. Which app collected the most 1-star reviews?
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Reviews loaded: 300
#    Apps covered: 3
#    Reviews per rating:
#    Rating
#    1     79
#    2     17
#    3     13
#    4     25
#    5    166
#    Name: count, dtype: int64
#    Average rating per app:
#    App_Name
#    com.dunkinbrands.otgo                    3.80
#    com.starbucks.mobilecard                 3.01
#    com.trubeacon.scooters_mobile_android    4.01
#    Name: Rating, dtype: float64
#    One-star reviews: 79
#    That is 26.3% of everything.
#    One-star reviews per app:
#    App_Name
#    com.starbucks.mobilecard                 44
#    com.dunkinbrands.otgo                    19
#    com.trubeacon.scooters_mobile_android    16
#    Name: count, dtype: int64
#
#  HINT: value_counts() sorts by count. Add .sort_index() when you
#        want 1,2,3,4,5 in order instead of biggest-first.
#        groupby('App_Name')['Rating'].mean().round(2) -- Week 2.
#        Filter to the angry ones first, then value_counts them.
#
#  How to run it: python practice/p07_read_the_reviews.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

reviews_df = pd.read_csv("data/coffee_app_reviews_fallback.csv")

# TODO 1: how many reviews, how many apps
print("Reviews loaded: (not counted yet)")
print("Apps covered: (not counted yet)")

# TODO 2: reviews at each star rating, in rating order
print("Reviews per rating:")
print("(not counted yet)")

# TODO 3: average rating per app, rounded to 2 places
print("Average rating per app:")
print("(not worked out yet)")

# TODO 4: how many 1-star reviews, and what share
print("One-star reviews: (not counted yet)")
print("That is ?% of everything.")

# TODO 5: which app collected the most 1-star reviews
print("One-star reviews per app:")
print("(not counted yet)")
