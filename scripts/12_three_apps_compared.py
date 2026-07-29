# ============================================================
#  The Cozy Bean -- Script 12: Three Chains, Side by Side
#  Lab STEP 22.
#  Shows: one table holding three apps' reviews, and what
#         happens when you group it by app.
#
#  RUN_LIVE is False, so this reads the shipped copy in data/
#  and your numbers match the lab exactly. Flip it to True to
#  scrape all three yourself -- the loop below is the real
#  thing, and it is the same loop your instructor ran.
#
#  Run:   python scripts/12_three_apps_compared.py
#         (from M1-W3-Lab01/)
# ============================================================

import pandas as pd

RUN_LIVE = False
CSV_PATH = "data/coffee_app_reviews_fallback.csv"

APP_IDS = [
    'com.starbucks.mobilecard',                 # Starbucks
    'com.dunkinbrands.otgo',                    # Dunkin'
    'com.trubeacon.scooters_mobile_android',    # Scooter's Coffee
]

if RUN_LIVE:
    from google_play_scraper import reviews
    all_reviews = pd.DataFrame()
    for app_id in APP_IDS:
        result, _ = reviews(app_id, count=100, lang="en", country="us")
        app_reviews = pd.DataFrame(result)
        app_reviews['App_Name'] = app_id
        all_reviews = pd.concat([all_reviews, app_reviews], ignore_index=True)
    reviews_df = all_reviews[['content', 'score', 'at', 'App_Name']].copy()
    reviews_df.columns = ['Review_Text', 'Rating', 'Date', 'App_Name']
    reviews_df['Date'] = pd.to_datetime(reviews_df['Date'])
else:
    reviews_df = pd.read_csv(CSV_PATH)

print("=== STEP 22: THREE CHAINS IN ONE TABLE ===")
print("Reading:", "live scrape" if RUN_LIVE else CSV_PATH)
print("Shape:", reviews_df.shape)
print()

print("How many reviews from each app?")
print(reviews_df['App_Name'].value_counts())
print()

# ---- one row per app, three numbers each --------------------
print("=== THE COMPARISON THAT MATTERS ===")
summary = reviews_df.groupby('App_Name').agg(
    reviews=('Rating', 'count'),
    average_rating=('Rating', 'mean'),
)
summary['average_rating'] = summary['average_rating'].round(3)

# How many 1-star reviews did each app collect? Filter, then count.
unhappy = reviews_df[reviews_df['Rating'] == 1]
summary['one_star'] = unhappy['App_Name'].value_counts()

print(summary)
print()

worst = summary['average_rating'].idxmin()
best = summary['average_rating'].idxmax()
print(f"Happiest customers: {best}")
print(f"Grumpiest customers: {worst}")
print()
print("Scooter's Coffee is a fraction of Starbucks' size --")
print("and that is exactly why it is the useful comparison for you.")
