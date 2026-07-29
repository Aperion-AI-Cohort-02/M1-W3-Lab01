# ============================================================
#  The Cozy Bean -- Script 10: Scout One Competitor
#  Lab STEP 20.
#
#  *** THIS SCRIPT USES THE INTERNET. ***
#  It fetches 100 real, public reviews of a coffee chain's app
#  from the Google Play Store, right now, live.
#
#  Your rows WILL be different from the lab's. That is correct.
#
#  It saves to my_coffee_reviews.csv -- its own filename, so it
#  can never overwrite the shipped copy in data/.
#
#  Run:   python scripts/10_scrape_one_app.py
#         (from M1-W3-Lab01/)
# ============================================================

import pandas as pd
from google_play_scraper import reviews

APP_ID = "com.starbucks.mobilecard"      # Starbucks

print("=== STEP 20: SCOUTING THE COMPETITION ===")
print(f"Asking the Google Play Store for 100 reviews of {APP_ID}")
print()

# ---- the network call, wrapped up warm ----------------------
# Week 2's try/except, finally doing the job it was invented for.
try:
    result, _ = reviews(APP_ID, count=100, lang="en", country="us")
except Exception as error:
    print("The scrape failed. That is not your fault -- networks wobble.")
    print(f"  {type(error).__name__}: {error}")
    print()
    print("Carry on with the shipped copy in data/ -- STEP 21 uses it.")
    raise SystemExit(0)

# A scrape can also come back EMPTY without raising anything at all.
# It happened to me once while building this lab. So we check.
if not result:
    print("The scrape returned no reviews at all -- no error, just nothing.")
    print("Try again in a minute, or carry on with the shipped copy.")
    raise SystemExit(0)

print(f"Got {len(result)} reviews.")
print()

# ---- what the scraper actually hands back -------------------
review_df = pd.DataFrame(result)
print("The scraper gives you far more than you asked for:")
print(list(review_df.columns))
print()

# ---- keep three columns, and make them ours -----------------
# .copy() says "this slice is mine now" -- see the lab's note.
clean = review_df[['content', 'score', 'at']].copy()
clean.columns = ['Review_Text', 'Rating', 'Date']
clean['App_Name'] = APP_ID
clean['Date'] = pd.to_datetime(clean['Date'])

print("Cleaned down to the four columns we care about:")
print(clean.head())
print()
print("Shape:", clean.shape)
print("Ratings run from", clean['Rating'].min(), "to", clean['Rating'].max())
print()

clean.to_csv("my_coffee_reviews.csv", index=False)
print("Saved my_coffee_reviews.csv")
print("(The lab's own copy lives in data/ and is untouched.)")
