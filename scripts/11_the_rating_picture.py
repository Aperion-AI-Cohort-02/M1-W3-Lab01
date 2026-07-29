# ============================================================
#  The Cozy Bean -- Script 11: What Are People Actually Saying?
#  Lab STEP 21.
#  Shows: the star-rating distribution of scraped reviews.
#
#  This script reads ONE path, set on the line below. It ships
#  pointing at the copy in data/, so your output matches the
#  lab exactly. Scraped your own in STEP 20? Change the line to
#  "my_coffee_reviews.csv" -- and expect different numbers.
#
#  Run:   python scripts/11_the_rating_picture.py
#         (from M1-W3-Lab01/)
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CSV_PATH = "data/coffee_app_reviews_fallback.csv"

os.makedirs("charts", exist_ok=True)

reviews_df = pd.read_csv(CSV_PATH)

print("=== STEP 21: THE RATING PICTURE ===")
print("Reading:", CSV_PATH)
print("Shape:", reviews_df.shape)
print()

print("How many of each star rating?")
print(reviews_df['Rating'].value_counts().sort_index())
print()

print("Average rating overall:", round(reviews_df['Rating'].mean(), 3))
print()

print("Average rating per app:")
print(reviews_df.groupby('App_Name')['Rating'].mean().round(3))
print()

print("Two shortest 1-star reviews:")
one_star = reviews_df[reviews_df['Rating'] == 1].copy()
one_star['length'] = one_star['Review_Text'].str.len()
for text in one_star.nsmallest(2, 'length')['Review_Text']:
    print(f"  \"{text}\"")
print()

plt.figure(figsize=(8, 6))
sns.countplot(x='Rating', data=reviews_df, hue='Rating',
              legend=False, palette='viridis')
plt.title('Star Ratings -- 300 coffee-chain app reviews')
plt.xlabel('Rating')
plt.ylabel('Number of reviews')

plt.tight_layout()
plt.savefig("charts/rating_distribution.png")
print("Saved charts/rating_distribution.png")
plt.show()
print("Window closed. Script finished.")
