# ============================================================
#  The Cozy Bean -- Script 07: When Do Delays Happen?
#  Lab STEP 16.
#  Shows: turning text into real dates, pulling the hour out
#         of them, and the first fig/ax style chart.
#  Run:   python scripts/07_chart_delay_by_hour.py
#         (from M1-W3-Lab01/)
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/flights.csv")

# Pick up where STEP 7 left off -- the same two cleaning moves.
# Without the fill, the quietest hour of the night has no delay
# figure at all and the line on our chart breaks in half.
df = df.dropna(axis=1, thresh=0.8 * len(df))
df.fillna(df.median(numeric_only=True), inplace=True)

# ---- Section 1  (STEP 16): text -> real dates ---------------
print("=== STEP 16: THE DATE COLUMN IS NOT A DATE ===")
print("Before:", df['time_hour'].dtype)
print(df['time_hour'].head(3))
print()

df['time_hour'] = pd.to_datetime(df['time_hour'], utc=True)

print("After: ", df['time_hour'].dtype)
print(df['time_hour'].head(3))
print()

# ---- Section 2: pull the hour out ---------------------------
df['hour'] = df['time_hour'].dt.hour
print("Now we can ask for just the hour:")
print(df['hour'].head(3))
print()

# ---- Section 3: average delay per hour ----------------------
hourly_delay = df.groupby('hour')['dep_delay'].mean()
print("Average departure delay, by hour of day (UTC):")
print(hourly_delay)
print()
print("Two things to notice before you draw it:")
print("  * Hours 6, 7 and 8 are MISSING -- nothing takes off from")
print("    New York at 2am local time. No flights, no row.")
print("  * Hour 5 reads exactly -2.00, which is the median we filled")
print("    with in STEP 7. That hour is almost all cancelled flights,")
print("    so what you are seeing is our own fill looking back at us.")
print("    Filling gaps is not free. Sometimes you can see the filler.")
print()

# ---- Section 4: the fig/ax chart ----------------------------
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(hourly_delay.index, hourly_delay.values, marker='o')

ax.set_xlabel("Hour of day (UTC)")
ax.set_ylabel("Average departure delay (minutes)")
ax.set_title("Delay Over the Day")
ax.set_xticks(hourly_delay.index)
ax.set_xticklabels(hourly_delay.index, rotation=45)

plt.tight_layout()
plt.savefig("charts/delay_by_hour.png")
print("Saved charts/delay_by_hour.png")
plt.show()
print("Window closed. Script finished.")
