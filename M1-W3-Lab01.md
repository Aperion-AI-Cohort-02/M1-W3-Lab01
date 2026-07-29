# ☕ M1-W3-Lab01 — Due Diligence: Learning to Interrogate Data

### Data Profiling, EDA, Outliers & Scraping
**Aperion AI Training Academy** · *"Boundless Possibilities, Infinite Potential"*

| | |
|---|---|
| **Module** | M1: AI/ML Fundamentals |
| **Week** | Week 3 |
| **Lab** | Lab01 — Due Diligence: Learning to Interrogate Data |
| **Duration** | **≈ 1 hour** of lab work (**plus ~20 minutes of one-time setup, not counted**) |
| **Difficulty** | ⭐⭐⭐ Beginner, level 3 — **you speak pandas now** |

> 🛋️ **Aim for one sitting of about an hour**, with the setup done beforehand. If you do need to pause, a natural break is after **Cluster E**, when you can profile a table and find its outliers — that is already a real, employable skill. A second natural break is after **Cluster G**, before the scraping starts.

### What you learned in class (and will now make your own)

Data profiling · structure, content, quality · `info()` / `dtypes` / `describe()` · `isnull().sum()` and the percentage view · `dropna(thresh=…)` · `fillna(median)` · `duplicated()` · `select_dtypes` · EDA · histograms · box plots · bar charts · **outliers by IQR** · **outliers by z-score** · time series with `to_datetime` and `.dt` · **correlation** and heatmaps · scatter plots · where data comes from · GIGO · **web scraping with `google-play-scraper`** · ethical data workflows

---

## 1. ☕ The Story

The letter arrived on a Tuesday, and you read it standing up in the middle of the shop.

**In-principle approval.** Mrs Adeyemi's bank will fund the second branch. A **first tranche** has already landed in the account. The unit two streets over — the one with the proper kitchen and room for twelve tables — is as good as yours.

There is a condition, and there is an invitation.

The **condition** is that the full disbursement depends on a deeper evidence pack than the one you handed over last time. Totals are not enough any more. *(That is tomorrow's lab, and it is a big one.)*

The **invitation** is stranger and, it turns out, more valuable. The bank runs a free Saturday workshop for the small businesses it lends to. It is called **"Know Your Numbers"**, it runs for most of a day, and Mrs Adeyemi has already put your name down.

So on Saturday morning — Sara and Ben are covering the shop, and Aisha has promised to text if the muffin tray runs dry — you are sitting in a room above the bank with eleven other people who own small businesses, and the instructor hands out a dataset.

It is not about coffee. It is about **aeroplanes**.

**336,776 flights out of New York.** Nineteen columns. Every departure from JFK, LaGuardia and Newark for a whole year.

Someone at the back asks the obvious question — *what has this got to do with my flower shop?* — and the instructor gives the answer that turns out to be the whole point of the day:

> *"Because a toolkit you can only use on your own data is not a toolkit. It's a habit. I am going to teach you to interrogate a table you have never seen before, about a business you know nothing about. Do that once and you can do it to anything. Including your own books, which is where most of you are going to find something you did not want to know."*

🔙 **Remember from Week 2:** the tips table was **244 rows**. This one is **336,776**. That is **1,380 times bigger**, and you are going to be completely fine.

And then, in the afternoon, you take the toolkit home and point it at something that matters: **before you open branch two, who exactly are you up against?** The big chains have apps. Those apps have thousands of public reviews. And there is a Python library that will fetch them for you.

Every idea in this lab is a physical thing in that Saturday workshop:

- **profiling** is the first ten minutes with any table — *"what have I actually been handed?"*
- **`describe()`** is the summary page the instructor tells you to read before you form a single opinion
- **an outlier** is the one flight that left twenty-one hours late
- **correlation** is *"when this goes up, does that go up too?"*
- **skew** is the shape of almost every real-world number you will ever meet
- and the **scrape** at the end is you, at your own kitchen table, finding out what the giants are getting wrong

### Why this matters in real life (and in AI/ML)

- **This lab is literally the first day of every data job.** Not an exaggeration. You are handed a table, and before you are allowed an opinion you must know its shape, its gaps, its duplicates and its liars. That is Clusters B and C, and professionals do it every single time.
- **"Is this data trustworthy?" is a question models cannot ask.** A model will happily learn from a column that is 40% missing and cheerfully predict nonsense forever. **You** are the part of the system that catches it.
- **Outliers are where the interesting things live.** Fraud, sensor failures, the one customer worth ten others, the bug in the export. Every one shows up as a value that does not belong.
- **Scraping is how modern datasets get built.** Most of the interesting data in the world is on somebody's website, not in a tidy CSV.

### ✅ Success Criteria — what you will be able to produce

- `python scripts/00_check_setup.py` — six ticks, including this week's new library
- `python scripts/01_open_the_big_table.py` — a third of a million rows, profiled
- `python scripts/02_quality_check.py` — gaps measured, gaps handled, duplicates checked
- **eight charts of your own** in `charts/`, made by scripts 03, 04, 07, 08, 09 and 11
- `python scripts/05_outliers_iqr.py` and `06_outliers_zscore.py` — **two** methods, honestly compared
- `python scripts/10_scrape_one_app.py` — 🌐 **you, pulling live data off the internet**
- `python scripts/13_competitor_note.py` — **`competitor_findings.txt`, the deliverable**
- …and eight practice problems, including a capstone note in your own words.

---

## 2. 🎯 Learning Objectives

By the end of this lab you will be able to:

1. Say what **data profiling** is and name the four things it checks.
2. Load and inspect a table far too big to read, using `shape`, `head()`, `tail()`, `info()` and `dtypes`.
3. Read `describe()` out loud, in plain English, for a column you have never seen.
4. **Measure** missing values as counts *and* as percentages, and apply the 20%/80% rule of thumb.
5. Choose between dropping a column and filling it — and say **why median beats mean** on skewed data.
6. Check for duplicate rows, and know what to do when the answer is not zero.
7. Profile the **text** columns of a table with a loop and `value_counts()`.
8. Explain the difference between **profiling** and **EDA** in one sentence each.
9. Read **skew** off a histogram, and read the box, whiskers and outlier cloud off a box plot.
10. Find outliers **two** ways — the **IQR fence** and the **z-score** — and explain why they disagree.
11. Turn a text column into real dates, extract the hour, and draw your first `fig, ax` chart.
12. Read a **correlation** coefficient on the −1…+1 scale, and read a heatmap for patterns.
13. Name the four places data comes from, and state the **GIGO** principle.
14. **Scrape** public app reviews with `google-play-scraper`, wrapped safely in `try`/`except`.
15. Write a findings note to a text file that another human being could act on.

---

## 3. 🔧 Before You Start — a refresher, and **one** new install

> ### ⏱️ About 20 minutes, and much of it you have done before.
>
> **Already set up from Week 2?** Then it is genuinely two commands and you can skip ahead to §3.4.

### 3.1 The two commands

> 📥 **Not cloned this lab yet?** The [README](README.md#1--get-this-repo-onto-your-computer) walks you through it: click the GitHub Classroom link from Google Classroom, copy your own repo address, and clone it into `AperionAI/Module1/Week3/Lab01`.

**File → Open Folder…** on your **`Lab01`** folder, then **Terminal → New Terminal**:

```text
py -m pip install google-play-scraper
py scripts/00_check_setup.py
```

That is it. Everything else — pandas, numpy, matplotlib, seaborn, scipy — is already on your machine from Week 2 and has not changed.

### 3.2 What the new one is for

**`google-play-scraper`** fetches app listings and reviews from the Google Play Store. It is the only new library this week, it is small, and it is what Cluster I is built on.

On **Mac**, or if `py` is not recognised:

```text
python3 -m pip install google-play-scraper
```

### 3.3 Prove it worked

```text
py scripts/00_check_setup.py
```

📺 **Expected output** (your version numbers will differ, and that is fine):

```text
=== THE COZY BEAN -- KITCHEN INSPECTION (WEEK 3) ===

  ✅  pandas               3.0.3
  ✅  numpy                2.4.6
  ✅  matplotlib           3.10.9
  ✅  seaborn              0.13.2
  ✅  scipy                1.17.1
  ✅  google_play_scraper  1.2.7

All six ready. You can start the lab.
```

**Six ticks this week, not five.** If any line has a ❌, the script prints the exact command to fix that one.

### 3.4 "If you see this, do this" — the setup table

| What you see | What it means | What to do |
|---|---|---|
| `'pip' is not recognized…` | Windows cannot find pip on its own | `py -m pip install google-play-scraper`. Then use `py` for everything. |
| `SSL: CERTIFICATE_VERIFY_FAILED` or it hangs on "Collecting…" | Your network inspects internet traffic | Try home wifi first — that fixes it most of the time. |
| `SSL` errors **and you have PostgreSQL installed** | A stale `CURL_CA_BUNDLE` environment variable left behind by a PostgreSQL install can point pip at the wrong certificate file | In PowerShell, for this terminal only: `$env:CURL_CA_BUNDLE = $null`, then retry the install. *(This one bit the person who wrote this lab.)* |
| `Successfully installed`, but still `ModuleNotFoundError` | **You have more than one Python** and pip installed into the other one | Use the same prefix for both: `py -m pip install …` then `py scripts/…` |
| `FileNotFoundError: … 'data/flights.csv'` | 🔙 The Week-1 classic — **wrong folder** | `pwd` must end in `Lab01`. `ls` must show `data`. If not: **File → Open Folder** on your `Lab01` folder, then a fresh terminal. |
| **The terminal froze after a chart appeared** | It has not. It is waiting for you to close the chart window — **which may be hiding behind VS Code** | Find it, admire it, close it. **Your PNG was already saved** before the window opened. |
| A chart takes a few seconds to appear | Normal. You are drawing up to 336,776 points | Wait. See the patience note in §3.6. |

### 3.5 Where the data lives

The `data/` folder ships with **both** files you need:

| File | What it holds | Size |
|---|---|---|
| `data/flights.csv` | **336,776 flights × 19 columns** — the workshop's teaching dataset | ~30 MB |
| `data/coffee_app_reviews_fallback.csv` | **300 real reviews** of three coffee-chain apps, scraped when this lab was built | small |

**Only two STEPs in this lab need the internet** (STEP 20 and the 🚀 CoinGecko bonus). Everything else — including all of Clusters I and J — works on a train, because the downstream scripts read the shipped file by default.

> 📌 **You saw this in class:** your instructor loaded the flights data straight off the web —
>
> ```python
> url = "https://raw.githubusercontent.com/byuidatascience/data4python4ds/master/data-raw/flights/flights.csv"
> df = pd.read_csv(url)
> ```
>
> We ship the identical file locally so a flaky connection can never stop your lab. **Every number in this walkthrough matches your instructor's screen exactly** — we checked all of them, including the famous 46,178.

### 3.6 ⏳ A word about patience

Some charts in this lab take **a few seconds** rather than appearing instantly. That is normal and nothing is broken — the tips table was 244 rows and this one is 336,776. Drawing a third of a million dots takes a moment.

Honestly, though: it is *seconds*, not minutes. The slowest thing in the lab takes about four.

### 3.7 📌 A note about your screen versus your instructor's

pandas changed between the class session and today, in two harmless ways:

- **Text columns** are described as `str` on your screen and `object` on your instructor's. **Same column, different label.**
- **Dates** show as `datetime64[us, UTC]` on yours, `datetime64[ns, UTC]` on theirs. Microseconds versus nanoseconds. No number you care about is affected.

Where the class's exact code now prints a deprecation warning, this lab says so at that STEP and shows you the modern spelling.

---

## 4. 📖 Guided Walkthrough

Twenty-three steps in ten clusters. Same rhythm as always: read the STEP, run the script, compare with the 📺 block, do the 🎤 tweak.

---

## ☕ Cluster A — The Workshop Opens

*Script for this cluster:* **`scripts/01_open_the_big_table.py`** (Section 1)

---

### STEP 1 — What "profiling" actually means

▶ *In your script:* Section 1 of `scripts/01_open_the_big_table.py`

🎯 **Objective:** Know the four things you check before you trust any table.

☕ **Story moment:** The instructor writes one sentence on the whiteboard and leaves it there all day:

> *"Before you trust a number, interrogate the table it came from."*

🧠 **The idea in plain English:** **Data profiling** is the systematic examination of a dataset's **structure**, **content** and **quality**. It is not glamorous and it is not optional. It is the ten minutes that stops you presenting a wrong number to a bank.

In class you were given a list of what profiling should hand you:

| Key output | The question it answers |
|---|---|
| **Data types & distributions** | What kind of thing is in each column, and what shape is it? |
| **Null / missing counts** | How much of this is simply absent? |
| **Duplicate row detection** | Has anything been counted twice? |
| **Basic correlation overview** | Which columns move together? |

**Why it matters:** catching a quality problem now costs you ten minutes. Catching it after you have built an analysis on top of it costs you the analysis — and your credibility. *(This has a name, and it comes back in STEP 19: **GIGO**.)*

📺 **Expected output:**

```text
=== THE PROFILING CHECKLIST ===
Before you trust a number, interrogate the table it came from:
  1. STRUCTURE -- how many rows, how many columns, what type is each
  2. CONTENT   -- what do the numbers look like, what are the categories
  3. QUALITY   -- what is missing, what is duplicated, what is wrong
```

✅ **Verify:** Three numbered lines. No data has been loaded yet — this is the checklist you are about to work through.

🎤 **Try it yourself (30 seconds):** Think of a spreadsheet you actually use. Which of the three would you bet money is wrong in it? Most people's answer is "quality", and most people are right.

---

## ☕ Cluster B — Meet the Workshop Dataset

*Script for this cluster:* **`scripts/01_open_the_big_table.py`**

---

### STEP 2 — A third of a million rows

▶ *In your script:* Section 2 of `scripts/01_open_the_big_table.py`

🎯 **Objective:** Load the biggest table you have ever opened, and measure it.

☕ **Story moment:** The instructor says *"open it"*, and twelve small-business owners open a file with 336,776 rows in it. Somebody's laptop fan comes on. Nothing catches fire.

🧠 **The idea in plain English:** 🔙 Exactly the same two lines as Week 2. `read_csv` reads the file; `.shape` reports `(rows, columns)`. The only thing that has changed is the number.

💻 **The code:**

```python
import pandas as pd

df = pd.read_csv("data/flights.csv")
print("Shape (rows, columns):", df.shape)
print(f"That is {df.shape[0]:,} flights.")
```

📺 **Expected output:**

```text
=== STEP 2: HOW BIG IS THIS THING? ===
Shape (rows, columns): (336776, 19)
That is 336,776 flights.
```

**Sit with that number for a second.** Three weeks ago you had never written a line of Python. You just loaded a third of a million records and it took under a second.

🔙 Note `f"{df.shape[0]:,}"` — Week 1's f-string, with a comma format that inserts thousands separators. `336776` becomes `336,776`.

⚠️ **Common mistake:** `df.shape()` with brackets. `shape` is an **attribute**, not a method. Here is the real error:

```text
Traceback (most recent call last):
  File "your_file.py", line 3, in <module>
    print(df.shape())
          ~~~~~~~~^^
TypeError: 'tuple' object is not callable
```

**Translated:** *"`df.shape` already gave you a tuple. Then you put brackets after it, which means 'call this thing' — and a tuple is not something you can call."*

✅ **Verify:** `(336776, 19)`.

🎤 **Try it yourself (30 seconds):** Print `df.shape[1]`. Nineteen columns. 🔙 Indexed out of a tuple exactly as in Week 1.

> 📌 **You saw this in class:** `print(df.shape)` → `(336776, 19)`, `print(df.columns)` and `print(df.info())`, all on this data.

---

### STEP 3 — Both ends of the book

▶ *In your script:* Section 3 of `scripts/01_open_the_big_table.py`

🎯 **Objective:** Look at the top and bottom of a table — and find your first problem.

☕ **Story moment:** *"Never analyse a table you have not looked at,"* says the instructor. *"And always look at the **end**. The beginning is where the tidy data lives. The end is where the truth is."*

🧠 **The idea in plain English:** 🔙 `head()` is the first five rows, `tail()` the last five. You know these. What is new is **what they reveal on a table this size**.

💻 **The code:**

```python
print(df.head())
print(df.tail())

print(df[['month', 'day', 'carrier', 'dep_time', 'dep_delay',
          'arr_delay', 'tailnum']].tail())
```

📺 **Expected output:**

```text
=== STEP 3: THE FIRST FIVE ===
   year  month  day  dep_time  ...  distance  hour  minute             time_hour
0  2013      1    1     517.0  ...      1400     5      15  2013-01-01T10:00:00Z
1  2013      1    1     533.0  ...      1416     5      29  2013-01-01T10:00:00Z
2  2013      1    1     542.0  ...      1089     5      40  2013-01-01T10:00:00Z
3  2013      1    1     544.0  ...      1576     5      45  2013-01-01T10:00:00Z
4  2013      1    1     554.0  ...       762     6       0  2013-01-01T11:00:00Z

[5 rows x 19 columns]

=== STEP 3: THE LAST FIVE ===
        year  month  day  ...  hour  minute             time_hour
336771  2013      9   30  ...    14      55  2013-09-30T18:00:00Z
336772  2013      9   30  ...    22       0  2013-10-01T02:00:00Z
336773  2013      9   30  ...    12      10  2013-09-30T16:00:00Z
336774  2013      9   30  ...    11      59  2013-09-30T15:00:00Z
336775  2013      9   30  ...     8      40  2013-09-30T12:00:00Z

[5 rows x 19 columns]

Your terminal is too narrow for 19 columns, so pandas hid the
middle with '...'. Ask for just the interesting ones:
        month  day carrier  dep_time  dep_delay  arr_delay tailnum
336771      9   30      9E       NaN        NaN        NaN     NaN
336772      9   30      9E       NaN        NaN        NaN     NaN
336773      9   30      MQ       NaN        NaN        NaN  N535MQ
336774      9   30      MQ       NaN        NaN        NaN  N511MQ
336775      9   30      MQ       NaN        NaN        NaN  N839MQ

THERE they are: NaN. 'Not a Number' -- pandas for 'nothing here'.
These flights never left. They were cancelled.
```

**Two things just happened, and both matter.**

**First**, pandas hid the middle of the table behind `...` because 19 columns will not fit in your terminal. That is not an error, it is politeness — but it *hid the most important thing on the screen*, which is why we asked again for a narrower slice.

**Second**, and this is the real find: **the last rows are full of `NaN`.** Those flights have a scheduled departure time and no actual one. **They were cancelled.** You have been looking at this table for ninety seconds and you have already found a whole category of row that behaves differently from the rest.

🔙 `NaN` is Week 2's missing value, and 🔙 the numbers down the left are the **index**, starting at 0 — so 336,776 rows end at 336,775.

⚠️ **Common mistake:** `print(df)` on a table this size. pandas truncates it, but you still get a screenful of nothing useful. `head()` and `tail()` exist for a reason.

✅ **Verify:** `[5 rows x 19 columns]` twice, then a narrow block with visible `NaN`s.

🎤 **Try it yourself (30 seconds):** Run `df.head(20)`, then `df.tail(3)`. Then predict what `df.head(0)` does before you run it.

> 📌 **You saw this in class:** `df.head()` and `df.tail()`, in exactly this order, on exactly this data — and the cancelled-flight `NaN`s were visible in your instructor's output too.

---

### STEP 4 — The full inventory

▶ *In your script:* Section 4 of `scripts/01_open_the_big_table.py`

🎯 **Objective:** Get every column, its fill rate and its type, in one call.

☕ **Story moment:** *"This is the single most useful command in pandas,"* the instructor says. *"If you only remember one thing from today, remember `info()`."*

🧠 **The idea in plain English:** 🔙 `df.info()` prints one line per column: its name, **how many non-empty values it has**, and what type it holds. On a table this size it is how you spot trouble in five seconds.

💻 **The code:**

```python
df.info()
```

📺 **Expected output:**

```text
=== STEP 4: THE INVENTORY ===
<class 'pandas.DataFrame'>
RangeIndex: 336776 entries, 0 to 336775
Data columns (total 19 columns):
 #   Column          Non-Null Count   Dtype  
---  ------          --------------   -----  
 0   year            336776 non-null  int64  
 1   month           336776 non-null  int64  
 2   day             336776 non-null  int64  
 3   dep_time        328521 non-null  float64
 4   sched_dep_time  336776 non-null  int64  
 5   dep_delay       328521 non-null  float64
 6   arr_time        328063 non-null  float64
 7   sched_arr_time  336776 non-null  int64  
 8   arr_delay       327346 non-null  float64
 9   carrier         336776 non-null  str    
 10  flight          336776 non-null  int64  
 11  tailnum         334264 non-null  str    
 12  origin          336776 non-null  str    
 13  dest            336776 non-null  str    
 14  air_time        327346 non-null  float64
 15  distance        336776 non-null  int64  
 16  hour            336776 non-null  int64  
 17  minute          336776 non-null  int64  
 18  time_hour       336776 non-null  str    
dtypes: float64(5), int64(9), str(5)
memory usage: 59.8 MB
```

**Now read it like a professional.** Scan the `Non-Null Count` column and look for anything that is *not* 336776:

- `dep_time` and `dep_delay`: **328,521** — about 8,255 missing
- `arr_time`: 328,063
- `arr_delay` and `air_time`: **327,346** — about 9,430 missing
- `tailnum`: 334,264

Everything else is complete. **You have just found every gap in a 19-column table in about four seconds**, and you have a theory about all of them already: cancelled flights have no departure, and diverted flights have no arrival.

**One more line worth noticing.** `time_hour` is typed **`str`** — it is *text*. But look at its contents: `2013-01-01T10:00:00Z`. That is obviously a date. This exact point was made in class: **a date column stored as text blocks every time-based analysis you might want to do.** Hold that thought; STEP 16 fixes it.

🔙 `float64` and `int64` are Week 1's `float` and `int` with the bit-count attached.

⚠️ **Common mistake:** Writing `df.info` without brackets. `info` is a **method** — it *does* something — so it needs them. Without them you get a description of the method instead of the inventory.

✅ **Verify:** 19 numbered rows, and `dtypes: float64(5), int64(9), str(5)`.

🎤 **Try it yourself (30 seconds):** Run `df.dtypes` on its own. Same type information, no fill counts, much shorter. Both are useful; `info()` more often.

> 📌 **You saw this in class:** `df.info()` on this data. *(Your instructor's screen said `object` where yours says `str`, and showed a different memory figure — that is the pandas version note from §3.7. All 19 columns and every non-null count are identical.)*

---

### STEP 5 — The summary page

▶ *In your script:* Section 5 of `scripts/01_open_the_big_table.py`

🎯 **Objective:** Read `describe()` in plain English on a column you know nothing about.

☕ **Story moment:** *"Right,"* says the instructor. *"Nobody in this room knows anything about aviation. Let us find out what a departure delay looks like anyway."*

🧠 **The idea in plain English:** 🔙 `describe()` gives eight summary numbers per numeric column. On 19 columns that is a wall of figures, so we ask for three.

💻 **The code:**

```python
print(df[['dep_delay', 'air_time', 'distance']].describe())
```

📺 **Expected output:**

```text
=== STEP 5: THE SUMMARY PAGE (three columns of it) ===
           dep_delay       air_time       distance
count  328521.000000  327346.000000  336776.000000
mean       12.639070     150.686460    1039.912604
std        40.210061      93.688305     733.233033
min       -43.000000      20.000000      17.000000
25%        -5.000000      82.000000     502.000000
50%        -2.000000     129.000000     872.000000
75%        11.000000     192.000000    1389.000000
max      1301.000000     695.000000    4983.000000
```

**Now read the `dep_delay` column out loud, line by line:**

| Row | Means | Here |
|---|---|---|
| `count` | how many values exist | 328,521 — **not** 336,776, because cancelled flights have no delay |
| `mean` | the average | **12.6 minutes late** |
| `std` | how spread out they are | 40.2 — very spread out |
| `min` | the smallest | **−43** — a flight left forty-three minutes *early* |
| `25%` | a quarter are below this | **−5** — a quarter of flights leave 5+ minutes early |
| `50%` | **the middle flight** | **−2** — the typical flight leaves *two minutes early* |
| `75%` | three quarters are below this | 11 minutes late |
| `max` | the largest | **1,301 minutes** — twenty-one and a half hours |

**And here is the finding that should stop you.** The **mean** is +12.6 minutes but the **median** is **−2**. The average flight is late; the *typical* flight is early.

Both numbers are correct. They disagree because a small number of catastrophically late flights drag the average up while barely moving the middle. That gap between mean and median has a name — **skew** — and you will meet it as a picture in STEP 11 and as a *problem* in tomorrow's lab.

**Negative numbers in a delay column are not errors.** They are early departures. The column does not say "lateness", it says "delay", and delay can be negative.

⚠️ **Common mistake:** Reading `describe()` for a column whose units you have not checked. `air_time`'s mean of 150.7 is **minutes**; `distance`'s 1,039.9 is **miles**. The command does not know what your columns mean. **You** supply that.

✅ **Verify:** `mean` for `dep_delay` reading `12.639070`, and `50%` reading `-2.000000`.

🎤 **Try it yourself (30 seconds):** Run `df['dep_delay'].describe()` on its own — the same eight numbers for one column. Then find the flight that left 43 minutes early: `df[df['dep_delay'] == -43]`. 🔙 Week-2 filtering, still working.

> 📌 **You saw this in class:** `df.describe()` — the full 19-column version. We narrowed it to three columns so it fits on your screen and can actually be read; the numbers for these three are identical.

---

### 🧠 Quick Quiz #1 — answer from memory, before peeking

*(Answers are in the **Answer Key** at the end. No scrolling ahead.)*

**Q1.** What does data profiling examine?

- A) Only the number of rows in a table
- B) Only the missing values in a table
- C) A table's structure, content and quality
- D) A table's colours, fonts and layout

**Q2.** `df.shape` gave `(336776, 19)`. What is the 19?

- A) The number of missing values
- B) The number of columns
- C) The number of airports involved
- D) The number of rows

**Q3.** `tail()` showed `NaN` in the delay columns. What does `NaN` mean?

- A) There was no value recorded here
- B) The value here is zero
- C) The value here is negative
- D) The file failed to load properly

---

## ☕ Cluster C — Is This Table Trustworthy?

*Script for this cluster:* **`scripts/02_quality_check.py`**

---

### STEP 6 — Measure the gaps twice

▶ *In your script:* Section 1 of `scripts/02_quality_check.py`

🎯 **Objective:** Count missing values, then express them as percentages — and know why you need both.

☕ **Story moment:** *"'Some values are missing' is not a sentence I can act on,"* says the instructor. *"'Two point eight per cent of arrival delays are missing' is."*

🧠 **The idea in plain English:** Two views of the same fact:

- `df.isnull().sum()` — **how many** are missing in each column
- `(df.isnull().mean() * 100)` — **what share** of each column is missing

The second one works because `isnull()` gives True/False, and 🔙 Python counts `True` as 1 — so the *mean* of a column of True/False **is** the proportion that are True. Multiply by 100 for a percentage. Sorting it puts the worst offenders on top.

💻 **The code:**

```python
print(df.isnull().sum())
print((df.isnull().mean() * 100).sort_values(ascending=False))
```

📺 **Expected output:**

```text
=== STEP 6: HOW MANY VALUES ARE MISSING? ===
year                 0
month                0
day                  0
dep_time          8255
sched_dep_time       0
dep_delay         8255
arr_time          8713
sched_arr_time       0
arr_delay         9430
carrier              0
flight               0
tailnum           2512
origin               0
dest                 0
air_time          9430
distance             0
hour                 0
minute               0
time_hour            0
dtype: int64

The same thing as a percentage, worst first:
arr_delay         2.800081
air_time          2.800081
arr_time          2.587180
dep_time          2.451184
dep_delay         2.451184
tailnum           0.745896
year              0.000000
day               0.000000
month             0.000000
sched_dep_time    0.000000
sched_arr_time    0.000000
flight            0.000000
carrier           0.000000
origin            0.000000
dest              0.000000
distance          0.000000
hour              0.000000
minute            0.000000
time_hour         0.000000
dtype: float64
```

**Why both views?** Because **8,255** sounds alarming and **2.45%** does not — and the second one is the one that tells you what to do.

**A rule of thumb from class, and it is genuinely useful:**

| Roughly how much is missing | What to consider |
|---|---|
| **~20%** | **Fill it** (impute) — there is enough real data to make a fair guess |
| **~80%** | **Drop the column** — there is not enough left to be worth anything |

**Every column here is under 3%.** By that rule, nothing needs dropping and everything can be filled. Which is exactly what STEP 7 does — and it produces a surprise.

Notice too that `arr_delay` and `air_time` are missing *the same* 9,430 values, and `dep_time` and `dep_delay` share 8,255. **Gaps travel in groups**, because one real-world event (a cancellation) empties several columns at once.

⚠️ **Common mistake:** `isnull()` without `.sum()`. You get 336,776 rows of True/False. Always aggregate.

✅ **Verify:** `arr_delay 9430` in the first block, and `arr_delay 2.800081` at the top of the second.

🎤 **Try it yourself (30 seconds):** Run `df.isnull().sum().sum()` — the double sum totals the whole table. You should get **46,595** missing values out of 6.4 million cells.

> 📌 **You saw this in class:** both calls, exactly as written — `df.isnull().sum()` and then `(df.isnull().mean() * 100).sort_values(ascending=False)`.

> ### 🚀 Bonus — beyond class: shares instead of counts
>
> The same trick works on any text column. What share of flights does each airline fly?
>
> ```python
> print((df['carrier'].value_counts(normalize=True).head(3) * 100).round(1))
> ```
>
> ```text
> carrier
> UA    17.4
> B6    16.2
> EV    16.1
> Name: proportion, dtype: float64
> ```
>
> United fly 17.4% of everything out of New York. Practice problem 🚀 p09 uses this.

---

### STEP 7 — Handle the gaps (and meet an honest anticlimax)

▶ *In your script:* Section 2 of `scripts/02_quality_check.py`

🎯 **Objective:** Apply the two standard cleaning moves, and understand why one of them does nothing.

☕ **Story moment:** *"Two moves,"* says the instructor. *"Bin the columns that are beyond saving, then patch the ones that are worth patching."*

🧠 **The idea in plain English:**

**Move 1 — drop the hopeless columns.** `dropna(axis=1, thresh=...)` is a strange-looking call and worth unpacking:

- `axis=1` means **columns**, not rows. *(`axis=0` is rows. This trips up everybody at least once.)*
- `thresh=0.8 * len(df)` means **"keep a column only if it has at least this many real values."** With 336,776 rows, that threshold is 269,420.8.

So: *"delete any column that is more than 20% empty."*

**Move 2 — fill what is left with the middle value.** `fillna(df.median(numeric_only=True))` puts each numeric column's **median** into its own gaps. `numeric_only=True` because you cannot take the median of an airline code.

💻 **The code:**

```python
before = df.shape
df = df.dropna(axis=1, thresh=0.8 * len(df))
print("Shape before:", before)
print("Shape after: ", df.shape)

print("Median departure delay:", df['dep_delay'].median())
print("Mean departure delay:  ", round(df['dep_delay'].mean(), 6))
df.fillna(df.median(numeric_only=True), inplace=True)
print(df.isnull().sum()[df.isnull().sum() > 0])
```

📺 **Expected output:**

```text
=== STEP 7: DROP THE HOPELESS COLUMNS ===
Shape before: (336776, 19)
Shape after:  (336776, 19)
Nothing was dropped -- and that is the correct answer.
No column here is anywhere near 80% empty.

=== STEP 7: FILL THE REST WITH THE MIDDLE VALUE ===
Median departure delay: -2.0
Mean departure delay:   12.63907

Gaps left after filling:
tailnum    2512
dtype: int64
(tailnum is text, so a median cannot fill it. Numbers only.)
```

**Nineteen columns in, nineteen columns out.** The drop did **nothing**.

**And that is the correct outcome, not a failure.** The worst column in this table is 2.8% empty, nowhere near the 80% line. The code ran, considered every column, and correctly decided none deserved deleting.

🔙 **This is Week 2's lesson again.** There, `fillna()` and `dropna()` ran on a spotless till export and changed nothing. Perfectly correct code, invisible effect. **Code that does nothing is not the same as code that is wrong** — and knowing the difference is a real skill. If you had *not* run the check, you would not know your table was in good shape.

**Now the part that genuinely matters: why the median?**

Look at those two numbers again. The **median** delay is **−2.0**. The **mean** is **+12.6**.

There are 8,255 gaps to fill.

- Fill them with the **mean** and you have just invented **8,255 flights that left 12.6 minutes late**.
- Fill them with the **median** and you have added 8,255 flights that behave like the typical flight.

Those gaps are *cancelled flights*. They were never late — they never left. Filling them with +12.6 would manufacture over 28 hours of delay that never happened, and every average you calculate afterwards would be a lie.

> **On any skewed column — delays, money, house prices, incomes — the median is the honest fill.** The mean has already been dragged away from reality by the extremes.

⚠️ **Common mistake:** Forgetting `axis=1`. `dropna(thresh=...)` without it works on **rows**, and would throw away 9,430 flights instead of considering 19 columns.

✅ **Verify:** Both shapes read `(336776, 19)`, median `-2.0`, and only `tailnum` has gaps left.

🎤 **Try it yourself (60 seconds):** Change `0.8` to `0.99` and rerun. Now a column must be 99% complete to survive, so the five gappy columns get deleted and you drop to 14 columns. **The threshold is a judgement, not a law** — and you should be able to defend whichever number you picked.

> 📌 **You saw this in class:**
>
> ```python
> # Drop columns with too many missing values
> df = df.dropna(axis=1, thresh=0.8 * len(df))
>
> # Fill numeric
> df.fillna(df.median(numeric_only=True), inplace=True)
> ```
>
> Identical, including the 0.8. Your instructor's run also dropped nothing — the two `isnull().sum()` outputs either side of it are the same except for the filled columns.

---

### STEP 8 — Has anything been counted twice?

▶ *In your script:* Section 3 of `scripts/02_quality_check.py`

🎯 **Objective:** Check for duplicate rows, and know the fix for when there are some.

☕ **Story moment:** *"Duplicates are the quietest way to be wrong,"* says the instructor. *"Nobody ever notices that their totals are 8% too high."*

🧠 **The idea in plain English:** `df.duplicated()` gives True for any row that is an exact copy of one already seen. `.sum()` counts them.

💻 **The code:**

```python
print("Duplicate rows:", df.duplicated().sum())
```

📺 **Expected output:**

```text
=== STEP 8: HAS ANYTHING BEEN COUNTED TWICE? ===
Duplicate rows: 0
Zero. Say that out loud -- it is a finding, not a non-answer.
If it were not zero, the fix is one call: df.drop_duplicates()
```

**Zero. And zero is a finding.**

It is tempting to feel cheated by a check that comes back clean. Do not. You now *know* that no flight is double-counted, which means every total you produce today is trustworthy. That is worth one line of code.

**And when it is not zero,** the fix is a single call:

```python
df = df.drop_duplicates()
```

You will need it for real. Duplicates were flagged in class as one of the three classic problems in **scraped** data — collect reviews twice and you get the same review twice. Cluster I is exactly where that happens.

⚠️ **Common mistake:** Assuming `drop_duplicates()` needs no thought. By default a row must match on **every** column. Two different customers can share a name; two identical reviews might be two real people typing "great app". `subset=['column']` lets you say what "duplicate" means — and that is your decision, not pandas'.

✅ **Verify:** `0`.

🎤 **Try it yourself (30 seconds):** Try `df.duplicated(subset=['carrier', 'flight']).sum()`. Now "duplicate" means *same airline, same flight number* — and you get a huge number, because flight UA1545 runs every day. **Same data, different definition, completely different answer.**

> 📌 **You saw this in class:** `print(df.duplicated().sum())` → `0`, and the cleaning strategy from class naming `df.drop_duplicates()` as the remedy.

---

### STEP 9 — Profile the text columns

▶ *In your script:* Section 4 of `scripts/02_quality_check.py`

🎯 **Objective:** Loop over a table's text columns and summarise each one.

☕ **Story moment:** *"You have profiled the numbers,"* says the instructor. *"Now the words. And this is where a Week-1 skill you have not used in a fortnight comes back."*

🧠 **The idea in plain English:** `df.select_dtypes(include='str')` hands back only the **text** columns. And a DataFrame can be looped over 🔙 **exactly like a Week-1 list** — each turn of the loop gives you one column name.

`.nunique()` counts how many *different* values a column holds. Low means a category; high means an identifier.

💻 **The code:**

```python
for col in df.select_dtypes(include='str'):
    print(f"  {col:12} {df[col].nunique()}")

print(df['origin'].value_counts())
```

📺 **Expected output:**

```text
=== STEP 9: HOW MANY DIFFERENT VALUES IN EACH TEXT COLUMN? ===
  carrier      16
  tailnum      4043
  origin       3
  dest         105
  time_hour    6936

Where do these flights take off from?
origin
EWR    120835
JFK    111279
LGA    104662
Name: count, dtype: int64
```

**Read those five numbers and you have understood the whole dataset:**

| Column | Different values | What that tells you |
|---|---|---|
| `carrier` | **16** | Sixteen airlines. A **category** — perfect for grouping. |
| `tailnum` | **4,043** | Four thousand physical aeroplanes. An **identifier**. |
| `origin` | **3** | **Three airports** — the whole dataset is "flights out of New York". |
| `dest` | **105** | They fly to 105 places. |
| `time_hour` | 6,936 | a full year at roughly 19 flying hours a day (365 × 19 ≈ 6,935). A **date wearing a text costume**. |

Then `value_counts()` on `origin` gives the actual split: **Newark 120,835 · JFK 111,279 · LaGuardia 104,662.** Newark is the busiest. The point made in class about **cardinality** lands here: a column with one unique value tells you nothing, and a column with 336,776 is an ID, not a feature.

🔙 **This is a Week-1 `for` loop.** Same `for x in thing:` you used on a list of drinks — pointed at a DataFrame's columns.

⚠️ **`include='str'` versus `include='object'`.** Your class notebook wrote `include='object'`, and on pandas 3 that **still works** but prints a deprecation warning:

```text
Pandas4Warning: For backward compatibility, 'str' dtypes are included by
select_dtypes when 'object' dtype is specified. This behavior is
deprecated and will be removed in a future version.
```

**Nothing is broken** — you get all five columns either way. `include='str'` is the modern spelling and is warning-free, which is why this lab uses it.

✅ **Verify:** carrier 16, tailnum 4043, origin 3, dest 105, time_hour 6936, then three airports.

🎤 **Try it yourself (60 seconds):** Print `df['dest'].value_counts().head(5)`. The five most popular destinations. Then `.tail(5)` for the five loneliest routes — some run just once all year.

> 📌 **You saw this in class:**
>
> ```python
> for col in df.select_dtypes(include='object'):
>     print(col, df[col].nunique())
> ```
>
> followed by `df['origin'].value_counts()`. Identical numbers; we swapped `'object'` for `'str'` to silence the warning above.

---

### 🧠 Quick Quiz #2 — answer from memory, before peeking

**Q1.** A column is about 80% empty. What was suggested in class?

- A) Fill it with the column's mean value
- B) Fill it with the column's median value
- C) Fill it with zero and carry on
- D) Consider dropping the column entirely

**Q2.** Why fill `dep_delay`'s gaps with the median (−2) rather than the mean (+12.6)?

- A) Because the median is always smaller than the mean
- B) Because the mean has been dragged up by extreme late flights
- C) Because pandas cannot compute a mean on this column
- D) Because the median is faster to calculate on big tables

**Q3.** `df.duplicated().sum()` returned `0`. What have you learned?

- A) The duplicate check did not run properly
- B) Every row in the table is identical
- C) No row is an exact copy of another row
- D) The table has no missing values anywhere

---

## ☕ Cluster D — So What Is It Saying?

*Scripts for this cluster:* **`scripts/03_chart_histogram.py`**, **`scripts/04_chart_box_and_bar.py`**

> ### 📌 One thing before the charts — where these scripts start
>
> Every script from here on begins with the **same two cleaning lines from STEP 7**:
>
> ```python
> df = df.dropna(axis=1, thresh=0.8 * len(df))
> df.fillna(df.median(numeric_only=True), inplace=True)
> ```
>
> That is deliberate, and it is how real analysis works: **every script re-does its own cleaning**, so it can be run on its own without depending on what you ran an hour ago.
>
> It also means the numbers shift slightly from Cluster B. `dep_delay`'s mean was `12.639070` on the raw data; after the median fill it is `12.280240`, because 8,255 gaps are now −2.0 values. **Both numbers are right for their moment.** Your class notebook worked the same way round, which is why the outlier counts in Cluster E match it exactly.
>
> If typing those two lines eight times starts to annoy you — good. Practice problem **p05** is where that annoyance turns into a function.

---

### STEP 10 — Profiling asks "is it OK?", EDA asks "what is it saying?"

▶ *In your script:* Section 1 of `scripts/03_chart_histogram.py`

🎯 **Objective:** Tell profiling and EDA apart in one sentence each.

☕ **Story moment:** *"Coffee break is over,"* says the instructor. *"This morning you checked whether the data was any good. This afternoon you find out what it knows."*

🧠 **The idea in plain English:**

| | Asks | Produces |
|---|---|---|
| **Profiling** | *Is this data OK?* | counts, types, gaps, duplicates |
| **EDA** | *What is this data saying?* | patterns, trends, anomalies, relationships |

**Exploratory Data Analysis** is where you go looking for what is actually in there — using pictures as much as numbers. You start **univariate** (one column at a time), then move to relationships between columns (STEP 17).

The benefits listed in class are all three real:

- **Improves data quality** — EDA finds problems profiling missed
- **Guides feature selection** — tells you which columns are worth feeding a model *(tomorrow's whole lab)*
- **Enhances stakeholder communication** — nobody has ever been persuaded by a `describe()` table, and everybody has been persuaded by a chart

📺 **Expected output:**

```text
=== STEP 10: FROM PROFILING TO EDA ===
Profiling asked: is this table trustworthy?  (Yes, mostly.)
EDA asks:        so what is it actually telling me?
```

✅ **Verify:** Two lines. This one is a framing STEP; the work is in STEP 11.

🎤 **Try it yourself (30 seconds):** Write down one question you would ask this flight data if you could ask anything. Keep it. See whether the next eight STEPs answer it.

---

### STEP 11 — Skew, as a picture

▶ *In your script:* the rest of `scripts/03_chart_histogram.py`

🎯 **Objective:** Draw a histogram and read skew off it.

☕ **Story moment:** In STEP 5 you noticed the mean and the median disagreed. Now you get to **see why**.

> ### ⚠️ Read this BEFORE you run the script
>
> When the chart appears, **your terminal will stop and appear to freeze.** It has not. It is waiting for you to **close the chart window** — and **the window may open behind VS Code.** Check your taskbar, find it, admire it, close it. The script finishes instantly.
>
> **Your PNG is already saved either way**, because `savefig` runs *before* `show`.

🧠 **The idea in plain English:** A **histogram** chops a column into buckets and draws how many values fall in each. It is the shape of your data.

`bins=50` asks for fifty buckets. More bins = more detail and more noise; fewer bins = smoother and blunter.

💻 **The code:**

```python
import os
os.makedirs("charts", exist_ok=True)

print(df['dep_delay'].describe())

df['dep_delay'].hist(bins=50)
plt.title("Departure Delay Distribution (336,776 flights)")
plt.xlabel("Departure delay (minutes)")
plt.ylabel("Number of flights")

plt.savefig("charts/dep_delay_histogram.png")   # SAVE first...
plt.show()                                       # ...THEN show
```

📺 **Expected output:**

```text
=== STEP 11: THE SHAPE OF DEPARTURE DELAY ===
count    336776.000000
mean         12.280240
std          39.778652
min         -43.000000
25%          -5.000000
50%          -2.000000
75%          10.000000
max        1301.000000
Name: dep_delay, dtype: float64

Saved charts/dep_delay_histogram.png
Window closed. Script finished.
```

…and a chart with one enormous bar near zero and a long, thin tail stretching right.

**Read your chart. This is the most important picture in the lab:**

- **One towering bar just left of zero.** The overwhelming majority of flights leave on time or slightly early.
- **A long, thin tail running right**, all the way to 1,301 minutes, so low it is nearly invisible.
- **Nothing on the left.** Flights cannot leave 500 minutes early.

That shape is called **right-skewed** (or positively skewed), and now the STEP-5 puzzle solves itself: **the tail drags the mean right while the median stays in the tall bar.**

> **This shape is everywhere.** Delays, salaries, house prices, transaction amounts, website visits. Almost nothing in the real world is a tidy bell curve. **Money is always skewed** — and tomorrow's lab meets that head-on.

⚠️ **Common mistake:** `plt.show()` before `plt.savefig()`. On many setups showing a figure clears it, so `savefig` then writes a **blank PNG**. **Save first, show second.** Every time.

✅ **Verify:** **Check the folder, not the window.** `charts/dep_delay_histogram.png` should exist. Also note `count` now reads `336776` — no gaps left after STEP 7 — and the mean has moved to `12.280240`.

🎤 **Try it yourself (60 seconds):** Change `bins=50` to `bins=5`, rerun and look. Then `bins=200`. With 5 bins the tail vanishes into one bar and the chart lies to you by omission. **The number of bins is an editorial decision.**

> 📌 **You saw this in class:**
>
> ```python
> df['dep_delay'].hist(bins=50)
> plt.title("Departure Delay Distribution")
> plt.show()
> ```
>
> Identical, with axis labels and a `savefig` added — because in a notebook the chart stays on screen, but a script's window closes and takes the picture with it.

---

### STEP 12 — The box, the whiskers, and the cloud of dots

▶ *In your script:* the whole of `scripts/04_chart_box_and_bar.py`

🎯 **Objective:** Read a box plot, and draw a bar chart of a text column's counts.

☕ **Story moment:** *"A histogram shows you the shape,"* says the instructor. *"A box plot shows you the **outliers**, and it does it in a way you can put in front of a bank."*

🧠 **The idea in plain English:** A **box plot** is `describe()` drawn:

- the **line inside the box** — the median (50%)
- the **box** — from 25% to 75%: **the middle half of all your data**
- the **whiskers** — most of the rest, reaching out 1.5 × the box's height
- **every dot beyond a whisker** — flagged as an **outlier**

🔙 You drew one of these in Week 2 for tips by day. Same chart, wildly different data.

💻 **The code:**

```python
df.boxplot(column='dep_delay')
plt.title("Departure Delay -- the box and the outlier cloud")
plt.savefig("charts/dep_delay_boxplot.png")
plt.show()

plt.figure()
df['carrier'].value_counts().plot(kind='bar')
plt.title("Flights per Carrier")
plt.tight_layout()
plt.savefig("charts/flights_per_carrier.png")
plt.show()
```

📺 **Expected output:**

```text
=== STEP 12: THE SAME COLUMN, AS A BOX ===
Bottom of the box (25%): -5.0
Line in the box   (50%): -2.0
Top of the box    (75%): 10.0
Everything past the whiskers prints as a dot. There are a lot of dots.

Saved charts/dep_delay_boxplot.png

=== STEP 12: WHICH AIRLINES FLY THE MOST? ===
carrier
UA    58665
B6    54635
EV    54173
DL    48110
AA    32729
Name: count, dtype: int64

Saved charts/flights_per_carrier.png
Window closed. Script finished.
```

**Read the box plot.** The box is *tiny* — from −5 to +10, just fifteen minutes tall — squashed at the bottom of a chart whose axis runs to 1,301. Above it, a dense black column of dots climbing off the top.

**That column of dots is the same long tail from STEP 11**, drawn a different way. The histogram made it look faint; the box plot makes it look *alarming*. Same data. Neither chart is lying — they emphasise different things, and **choosing which to show somebody is an editorial act.**

**And the bar chart** answers a different kind of question: United fly the most (58,665), then JetBlue, then ExpressJet. 🔙 `value_counts()` from Week 2, with `.plot(kind='bar')` stuck on the end — your first chart built from a number *you* computed rather than one seaborn worked out for you.

⚠️ **Common mistake:** Forgetting `plt.figure()` between two charts in one script. Without it the second chart draws **on top of** the first and you save the same muddle twice. And leaving out `tight_layout()` on a bar chart clips the labels off the bottom.

✅ **Verify:** Both PNGs exist in `charts/`. Box quartiles read −5.0, −2.0, 10.0, and `UA 58665` tops the carrier list.

🎤 **Try it yourself (60 seconds):** Change `column='dep_delay'` to `column='air_time'` and rerun. A completely different shape — a fat box with modest whiskers, because flight *durations* are far better behaved than flight *delays*. Not everything is skewed; you have to look.

> 📌 **You saw this in class:**
>
> ```python
> df.boxplot(column='dep_delay')
> plt.show()
> ```
>
> and
>
> ```python
> df['carrier'].value_counts().plot(kind='bar')
> plt.title("Flights per Carrier")
> plt.show()
> ```
>
> Both identical, with `savefig` added per our convention.

---

### 🧠 Quick Quiz #3 — answer from memory, before peeking

**Q1.** Your histogram had one tall bar on the left and a long thin tail to the right. What is that called?

- A) Right-skewed, with a few extreme values pulling the mean up
- B) Left-skewed, with a few extreme values pulling the mean down
- C) A normal distribution, perfectly symmetrical
- D) A flat distribution, with every value equally likely

**Q2.** What does changing `bins=50` to `bins=5` do to a histogram?

- A) It removes the outliers from the data entirely
- B) It converts the chart into a box plot automatically
- C) It makes the chart show more fine detail than before
- D) It smooths the shape and can hide the tail completely

**Q3.** On a box plot, what are the individual dots beyond the whiskers?

- A) Missing values that could not be plotted
- B) Values flagged as outliers by the chart
- C) The median value, drawn once per group
- D) Duplicate rows found in the table

---

## ☕ Cluster E — The Strange Ones

*Scripts for this cluster:* **`scripts/05_outliers_iqr.py`**, **`scripts/06_outliers_zscore.py`**

---

### STEP 13 — The IQR fence

▶ *In your script:* the whole of `scripts/05_outliers_iqr.py`

🎯 **Objective:** Build the interquartile-range fence and count what falls outside it.

☕ **Story moment:** The instructor puts up an example that has nothing to do with flights, and everybody in the room gets it instantly:

> 📌 **Straight from the class session:** *"A transaction of \$1M in a dataset of \$100–\$1000 transactions is likely an outlier."*

*"You did not need a formula for that,"* she says. *"You need a formula for the cases where you cannot eyeball it — which is all of them, once the table has 336,776 rows."*

🧠 **The idea in plain English:** The box plot already drew this; now you compute it.

1. **Q1** = the 25% mark. **Q3** = the 75% mark.
2. **IQR** = Q3 − Q1 — the height of the box, the range of the middle half.
3. Build a **fence** 1.5 × IQR beyond each end of the box.
4. Anything outside the fence is flagged.

Why 1.5? Convention — it flags genuinely unusual values without flagging half your data. It is a **rule of thumb**, not a law of nature.

💻 **The code:**

```python
Q1 = df['dep_delay'].quantile(0.25)
Q3 = df['dep_delay'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df['dep_delay'] < Q1 - 1.5 * IQR) |
    (df['dep_delay'] > Q3 + 1.5 * IQR)
]

print(outliers.shape)
```

🔙 **Look closely at that filter.** It is Week 2's boolean filtering with `|` for OR, every condition in its own brackets — *"below the lower fence **or** above the upper fence"*. Nothing new; you just have not seen it do something this useful before.

📺 **Expected output:**

```text
=== STEP 13: THE IQR FENCE ===

Q1  (a quarter of flights are below this): -5.0
Q3  (three quarters are below this):       10.0
IQR (Q3 - Q1, the width of the box):       15.0

Lower fence (Q1 - 1.5 * IQR): -27.5
Upper fence (Q3 + 1.5 * IQR): 32.5
Anything outside those two numbers is flagged as unusual.

Flagged flights (rows, columns): (46178, 19)
That is 46,178 of 336,776 flights (13.7%).

The worst five:
        month  day carrier origin dest  dep_delay
7072        1    9      HA    JFK  HNL     1301.0
235778      6   15      MQ    JFK  CMH     1137.0
8239        1   10      MQ    EWR  ORD     1126.0
327043      9   20      AA    JFK  SFO     1014.0
270376      7   22      MQ    JFK  CVG     1005.0

A 1,301-minute delay is 21 hours and 41 minutes.
That is not a typo. That is somebody's very bad day.
```

**46,178 flights flagged — 13.7% of everything.**

Two honest observations about that number.

**First: it is a lot.** More than one flight in eight. Anybody who tells you outliers are rare has not looked at real data. If you deleted all of them — which the naive reading of "outlier removal" suggests — you would delete an eighth of your dataset, including every genuinely interesting flight in it.

**Second: the fence is not symmetric.** It runs from −27.5 to +32.5, wider on the late side, because Q1 and Q3 are not symmetric around zero. The method inherits the skew of the data.

**And the worst offender:** a Hawaiian Airlines flight from JFK to Honolulu on 9 January, **1,301 minutes late.** Twenty-one hours and forty-one minutes. That is not a data-entry error; that is a real aeroplane and a real waiting room full of real people.

⚠️ **Common mistake:** Dropping the inner brackets — `df[df['dep_delay'] < Q1 - 1.5 * IQR | df['dep_delay'] > Q3 + 1.5 * IQR]`. `|` binds tighter than `<`, so pandas tries to combine the wrong things and the error is confusing. **Bracket every condition, every time.**

✅ **Verify:** `(46178, 19)` — and this should match your instructor's screen exactly.

🎤 **Try it yourself (60 seconds):** Change `1.5` to `3.0` and rerun. A wider fence flags far fewer flights. **You just moved the definition of "unusual"** — which is exactly what the 1.5 always was: somebody's choice.

> 📌 **You saw this in class:**
>
> ```python
> Q1 = df['dep_delay'].quantile(0.25)
> Q3 = df['dep_delay'].quantile(0.75)
> IQR = Q3 - Q1
>
> outliers = df[
>     (df['dep_delay'] < Q1 - 1.5 * IQR) |
>     (df['dep_delay'] > Q3 + 1.5 * IQR)
> ]
>
> print(outliers.shape)
> ```
>
> **→ `(46178, 19)`.** Line for line, and the same 46,178.

---

### STEP 14 — One flight, worked out by hand

▶ *In your script:* Section 1 of `scripts/06_outliers_zscore.py`

🎯 **Objective:** Compute a single z-score with arithmetic you already know.

☕ **Story moment:** *"Before I show you the library that does this,"* says the instructor, *"you are going to do one by hand. Because if you do not, the library will always feel like magic — and you cannot debug magic."*

🧠 **The idea in plain English:** A **z-score** answers one question:

> **How many standard deviations does this value sit from the average?**

That is the entire concept. The formula is one line of Week-1 arithmetic:

```text
z = (value - mean) / std
```

- z = 0 → exactly average
- z = 1 → one standard deviation above
- **|z| > 3 → far enough out to be suspicious** *(the threshold from class)*

🔙 **You already know both ingredients.** `mean` and `std` are **two rows of `describe()`** — you read them in STEP 5. The `std` of 39.78 is just "how spread out delays are, in minutes".

💻 **The code:**

```python
mean = df['dep_delay'].mean()
std = df['dep_delay'].std()

value = df.loc[151, 'dep_delay']
z = (value - mean) / std
```

📺 **Expected output:**

```text
=== STEP 14: ONE FLIGHT, WORKED OUT BY HAND ===

mean = df['dep_delay'].mean() = 12.280240
std  = df['dep_delay'].std()  = 39.778652

Row 151 left 853.0 minutes late.
z = (value - mean) / std
z = (853.0 - 12.280240) / 39.778652
z = 21.134949

That flight sits 21 standard deviations above the average.
Beyond 3 is already suspicious. This one is off the map.
```

**You just did statistics with a subtraction and a division.**

Row 151 left **853 minutes late** — over fourteen hours. Subtract the average (12.28), divide by the spread (39.78), and you get **21.13**. The threshold for "suspicious" is 3. This flight is seven times past it.

⚠️ **Common mistake:** Mixing up `std` and `var`. Variance is the standard deviation squared, so it is in *squared minutes* — a unit nobody can picture. The z-score formula wants `std`.

✅ **Verify:** `z = 21.134949`.

🎤 **Try it yourself (60 seconds):** Compute the z-score for a *normal* flight — try row 0, which left 2 minutes late. You should get about **−0.26**: a quarter of a standard deviation *below* average, because average is +12.28 and this flight was better than that. **A negative z-score is not a negative delay.**

---

### STEP 15 — Now all 336,776 of them

▶ *In your script:* Sections 2–3 of `scripts/06_outliers_zscore.py`

🎯 **Objective:** Let scipy do your hand calculation for every row, then compare the two methods honestly.

☕ **Story moment:** *"Right,"* says the instructor. *"You have done one. There are 336,775 to go. Shall we?"*

🧠 **The idea in plain English:** `scipy.stats.zscore` does **exactly** the subtraction and division you just did, to every value at once, and hands back a whole column of z-scores. Then 🔙 Week-2 filtering picks out the extreme ones.

`.abs()` gives the absolute value — so `abs(z) > 3` catches both suspiciously high *and* suspiciously low.

💻 **The code:**

```python
from scipy.stats import zscore

df['zscore'] = zscore(df['dep_delay'].fillna(0))
outliers = df[df['zscore'].abs() > 3]
```

📺 **Expected output:**

```text
=== STEP 15: NOW ALL 336,776 OF THEM ===
Flagged by z-score (rows, columns): (8183, 20)

The same flight, as scipy computed it:
  our hand calculation : 21.134949
  scipy's answer       : 21.134980
Near-identical. The last few digits differ because scipy
divides by n and .std() divides by n-1 -- invisible here.

=== THE TWO METHODS DISAGREE ===
  IQR method     flags 46,178 flights
  Z-score method flags 8,183 flights
Both are correct. They are asking different questions.
```

**Your hand calculation: 21.134949. scipy: 21.134980.** Identical to four decimal places. *(The tiny difference is real and harmless: scipy divides by n, pandas' `.std()` divides by n−1. On 336,776 rows that distinction vanishes.)*

**Notice the shape is `(8183, 20)`, not 19 columns.** You added a `zscore` column, so the table got wider. Easy to miss, worth catching.

**And now the honest bit — the two methods disagree, badly:**

| Method | Flags | Share |
|---|---|---|
| **IQR** | 46,178 | 13.7% |
| **Z-score** | 8,183 | 2.4% |

**Nearly six times more from IQR. Both are right.**

The reason is worth understanding, because it is the difference between the two methods:

- **IQR** builds its fence from **quartiles** — positions in the sorted data. The extreme values barely affect where the fence goes.
- **Z-score** builds its threshold from the **mean and standard deviation** — and *both of those are themselves inflated by the extreme values*. The 1,301-minute flight pushes the std up to 39.78, which makes the 3-std threshold enormous (about +131 minutes), which lets a lot of very late flights through.

> **The outliers defend each other.** That is the single most useful thing to understand about z-scores: on badly skewed data, the method's own inputs are corrupted by the thing it is looking for. **On skewed data, prefer IQR.**

⚠️ **Common mistake:** Treating "flagged as an outlier" as "delete this row". Neither of these methods says *delete*. They say *look*. Tomorrow's lab has a case where the biggest outlier in the file is the single most important row in it — and deleting it would destroy the whole point.

✅ **Verify:** `(8183, 20)` and the two counts 46,178 vs 8,183.

🎤 **Try it yourself (60 seconds):** Change `> 3` to `> 2` and rerun. Far more flights. Then `> 4`. **The threshold is a dial**, and 3 is a convention rather than a discovery.

> 📌 **You saw this in class:**
>
> ```python
> from scipy.stats import zscore
>
> df['zscore'] = zscore(df['dep_delay'].fillna(0))
> outliers = df[df['zscore'].abs() > 3]
> ```
>
> **→ `outliers.shape` = `(8183, 20)`.** Identical, including the 8,183.

---

### 🧠 Quick Quiz #4 — answer from memory, before peeking

**Q1.** How do you build the upper IQR fence?

- A) The mean of the column plus three standard deviations
- B) The median of the column plus the standard deviation
- C) Q3 plus one and a half times the IQR
- D) Q1 minus one and a half times the IQR

**Q2.** In one sentence, what does a z-score of 21 mean?

- A) This value sits 21 standard deviations from the average
- B) This value is 21 times bigger than the average value
- C) This value is 21 minutes later than it was scheduled
- D) This value appeared 21 times in the whole column

**Q3.** IQR flagged 46,178 flights; z-score flagged 8,183. Why?

- A) One of the two methods was written incorrectly
- B) The z-score method only looks at the highest values
- C) The IQR method ignores three quarters of the data
- D) Extreme values inflate the std, so the z threshold widens

---

## ☕ Cluster F — When Do Delays Happen?

*Script for this cluster:* **`scripts/07_chart_delay_by_hour.py`**

---

### STEP 16 — Text into time, and your first `fig, ax` chart

▶ *In your script:* the whole of `scripts/07_chart_delay_by_hour.py`

🎯 **Objective:** Convert a text column into real dates, extract a part of them, and draw a line chart the grown-up way.

☕ **Story moment:** Somebody asks the question the whole room has been waiting for: *"Is it worse at certain times of day?"* And the instructor says: *"Excellent. And you cannot answer it yet, because your date column is a lump of text. Watch."*

🧠 **The idea in plain English:** Three moves, then a chart.

**Move 1 — make the dates real.** `pd.to_datetime(df['time_hour'], utc=True)` turns text into genuine timestamps. `utc=True` says "these are UTC" and stops pandas guessing.

**Move 2 — take the hour out.** Once it is a real datetime, `.dt` unlocks its parts: `.dt.hour`, `.dt.day_name()`, `.dt.month`. **You cannot do any of that to a string.** This is exactly what was meant in class by *"a date column stored as object will prevent time-based analysis"*.

**Move 3 — 🔙 group and average.** Week-2 `groupby`, one pile per hour.

💻 **The code:**

```python
df['time_hour'] = pd.to_datetime(df['time_hour'], utc=True)
df['hour'] = df['time_hour'].dt.hour
hourly_delay = df.groupby('hour')['dep_delay'].mean()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(hourly_delay.index, hourly_delay.values, marker='o')

ax.set_xlabel("Hour of day (UTC)")
ax.set_ylabel("Average departure delay (minutes)")
ax.set_title("Delay Over the Day")
ax.set_xticks(hourly_delay.index)
ax.set_xticklabels(hourly_delay.index, rotation=45)

plt.tight_layout()
plt.savefig("charts/delay_by_hour.png")
plt.show()
```

**Two friendly lines on why `fig, ax` exists.** Until now you have used `plt.something()` — which draws on "whatever chart is current". That is fine for one chart. `fig, ax = plt.subplots()` instead hands you two named objects: the **figure** (the sheet of paper) and the **axes** (the chart on it). You then talk to `ax` directly. It is slightly more typing and *much* less ambiguous, and it is what you will see in every professional codebase — because as soon as you want two charts side by side, "whatever is current" stops being good enough.

📺 **Expected output:**

```text
=== STEP 16: THE DATE COLUMN IS NOT A DATE ===
Before: str
0    2013-01-01T10:00:00Z
1    2013-01-01T10:00:00Z
2    2013-01-01T10:00:00Z
Name: time_hour, dtype: str

After:  datetime64[us, UTC]
0   2013-01-01 10:00:00+00:00
1   2013-01-01 10:00:00+00:00
2   2013-01-01 10:00:00+00:00
Name: time_hour, dtype: datetime64[us, UTC]

Now we can ask for just the hour:
0    10
1    10
2    10
Name: hour, dtype: int32

Average departure delay, by hour of day (UTC):
hour
0     22.999346
1     22.841669
2     18.575575
3     16.810312
4      6.217507
5     -2.000000
9      0.056240
10     1.347059
11     1.644013
12     2.867305
13     4.588789
14     6.175975
15     6.802156
16     7.972361
17    10.613853
18    13.231135
19    15.810225
20    17.595900
21    19.865095
22    20.529325
23    22.488696
Name: dep_delay, dtype: float64

Two things to notice before you draw it:
  * Hours 6, 7 and 8 are MISSING -- nothing takes off from
    New York at 2am local time. No flights, no row.
  * Hour 5 reads exactly -2.00, which is the median we filled
    with in STEP 7. That hour is almost all cancelled flights,
    so what you are seeing is our own fill looking back at us.
    Filling gaps is not free. Sometimes you can see the filler.

Saved charts/delay_by_hour.png
Window closed. Script finished.
```

**Look at the `Before:` and `After:` blocks.** `str` became `datetime64[us, UTC]`, and `2013-01-01T10:00:00Z` became a real timestamp. **That one word changing is what unlocked everything else.**

**Now read the pattern, because it is a genuinely lovely finding.** Follow the numbers from hour 9 to hour 23:

**0.06 → 1.35 → 1.64 → 2.87 → 4.59 → 6.18 → 6.80 → 7.97 → 10.61 → 13.23 → 15.81 → 17.60 → 19.87 → 20.53 → 22.49**

**Delay climbs relentlessly all day long.** The first flights of the morning leave essentially on time. By late evening the average flight is 22 minutes late. Then the small hours (0–3) stay high, because those are the *previous* day's delays still unwinding.

**Nothing is being rescheduled. Delay accumulates.** One late aircraft in the morning makes its next three flights late, and the whole system slides. That is a real insight about how airlines work, and you got it from a table you had never seen ninety minutes ago.

**And two honest wrinkles in that output**, both worth more than the chart itself:

- **Hours 6, 7 and 8 are absent entirely** — not zero, *absent*. Those are 2–4am in New York and nothing takes off. `groupby` cannot make a row for a group with no members. If you had assumed 24 rows, your code would have broken.
- **Hour 5 reads exactly `-2.000000`** — which is precisely the median you filled with in STEP 7. That hour is almost entirely cancelled flights, so what you are looking at is **your own imputation staring back at you.** Filling gaps is not free. You put a number in, and later it came out and pretended to be a finding.

⚠️ **Common mistake:** Expecting these hours to be New York time. `utc=True` means UTC, and New York in summer is UTC−4 — so "hour 0" here is 8pm in New York. The chart is honest; its label just has to say `UTC` so nobody misreads it. *(The class notebook overwrote the dataset's own local-time `hour` column with the UTC one at this point, exactly as we do — worth knowing if you compare.)*

✅ **Verify:** `charts/delay_by_hour.png` exists. 21 hours listed (not 24), hour 5 reading `-2.000000`.

🎤 **Try it yourself (60 seconds):** Swap `'dep_delay'` for `'arr_delay'` and rerun. Arrival delays climb the same way — the pattern is real, not an artefact of one column. Then try `df['time_hour'].dt.day_name()` and group by that instead. Which weekday is worst?

> 📌 **You saw this in class:** all of it, line for line — `pd.to_datetime(df['time_hour'], utc=True)`, `.dt.hour`, `groupby('hour')['dep_delay'].mean()`, and the `fig, ax = plt.subplots(figsize=(10,5))` block with `set_xticks`, `set_xticklabels(rotation=45)` and `tight_layout()`. Your instructor then ran the same chart for `arr_delay`, which is the 🎤 above.

---

## ☕ Cluster G — What Moves With What

*Scripts for this cluster:* **`scripts/08_chart_correlation.py`**, **`scripts/09_chart_scatter.py`**

---

### STEP 17 — Correlation, four columns at a time

▶ *In your script:* the whole of `scripts/08_chart_correlation.py`

🎯 **Objective:** Read a correlation coefficient in plain English, then read a heatmap for patterns.

☕ **Story moment:** *"Last big idea of the day,"* says the instructor. *"Everything so far has been one column at a time. Now: when this goes up, does that go up too?"*

🧠 **The idea in plain English:** **Correlation** measures whether two columns move together. It is always between **−1 and +1**:

| Value | Means |
|---|---|
| **+1** | perfect lockstep — when one goes up, the other always goes up |
| **+0.9** | very strong positive relationship |
| **0** | **no relationship at all** — knowing one tells you nothing about the other |
| **−0.9** | very strong *opposite* relationship |
| **−1** | perfect opposite |

🔙 **Week 2 gave you a heatmap of `isna()`** — a picture of *where the gaps were*. This is a heatmap of *numbers*, which is a new thing to read, so we start with **four columns** rather than all nineteen.

💻 **The code:**

```python
small = df[['dep_delay', 'arr_delay', 'distance', 'air_time']].corr()
print(small.round(4))

sns.heatmap(small, annot=True, vmin=-1, vmax=1, cmap='coolwarm')
```

`annot=True` writes the number in each square. `vmin=-1, vmax=1` **pins the colour scale to the full range** — without it, seaborn scales colours to whatever it found, and a meaningless 0.05 can look dramatically red.

📺 **Expected output:**

```text
=== STEP 17: FOUR COLUMNS AT A TIME ===
           dep_delay  arr_delay  distance  air_time
dep_delay     1.0000     0.9093   -0.0172   -0.0207
arr_delay     0.9093     1.0000   -0.0581   -0.0335
distance     -0.0172    -0.0581    1.0000    0.9821
air_time     -0.0207    -0.0335    0.9821    1.0000

Read the two that matter:
  dep_delay vs arr_delay: 0.9093
     -> very close to +1: leave late, arrive late. No surprise.
  distance  vs dep_delay: -0.0172
     -> almost exactly 0: long flights are no likelier to
        leave late than short ones. That IS a surprise.

Saved charts/correlation_small.png

=== STEP 17: NOW THE WHOLE TABLE ===
Shape of the correlation matrix: (14, 14)
Too many numbers to read. So don't read numbers -- read PATTERNS.
Saved charts/correlation_full.png
Window closed. Script finished.
```

**Read the four numbers that matter, out loud:**

- **`dep_delay` vs `arr_delay` = 0.9093.** Very strong. Leave late, arrive late. Obvious once said, and reassuring — if this came out near zero you would suspect the data.
- **`distance` vs `air_time` = 0.9821.** Almost perfect. Longer flights take longer. Also obvious. **These two columns are nearly the same fact twice**, which matters enormously tomorrow: feeding a model two columns that say the same thing is waste at best.
- **`distance` vs `dep_delay` = −0.0172.** **Essentially zero.** Long-haul flights are *no more likely* to leave late than short hops. Most people guess wrong on this one.
- **The diagonal is all 1.0000**, because every column correlates perfectly with itself. That is a sanity check, not a finding — if your diagonal is not 1, something is broken.

**Then the whole table**, all 14 numeric columns as one wall of colour. **Do not read the numbers** — there are 196 of them. Read the *patterns*: bright blocks where groups of columns move together, and the bright diagonal line running corner to corner.

> ⚠️ **The sentence that keeps people out of trouble: correlation is not causation.** Delay and arrival delay correlate at 0.91, and one genuinely does cause the other. `distance` and `air_time` correlate at 0.98 and *neither* causes the other — they are both caused by the route. The number cannot tell you which situation you are in. **You** have to know that.

⚠️ **Common mistake:** Leaving out `vmin=-1, vmax=1`. seaborn then stretches its colours over whatever range it found, and correlations of 0.02 and 0.05 render as dramatically different shades. Pin the scale.

✅ **Verify:** `0.9093`, `0.9821`, `-0.0172` — and both PNGs in `charts/`.

🎤 **Try it yourself (60 seconds):** Add `'hour'` to the four columns and rerun. `hour` vs `dep_delay` comes out clearly positive — the same climbing pattern you charted in STEP 16, expressed as a single number. **Two completely different tools, same finding.** That is what "validate your findings" means.

> 📌 **You saw this in class:**
>
> ```python
> corr = df.corr(numeric_only=True)
> sns.heatmap(corr, annot=False)
> plt.title("Correlation Matrix")
> plt.show()
> ```
>
> That is the second half of this STEP. We put the small four-column version *first*, with the numbers written on, because a 14×14 grid is a poor place to meet an idea for the first time.

> ### 🚀 Bonus — beyond class: every pair at once, with `pairplot`
>
> `sns.pairplot` draws a scatter plot for **every pair** of columns, with each column's histogram down the diagonal. It is a lot of information for one line of code.
>
> On 336,776 rows it produces an unreadable black smear, so take a **random sample** first — which is a genuinely useful habit in its own right:
>
> ```python
> sample = df.sample(3000, random_state=42)
> sns.pairplot(sample[['dep_delay', 'arr_delay', 'distance']])
> plt.savefig("charts/bonus_pairplot.png")
> plt.show()
> ```
>
> `random_state=42` makes the "random" sample **the same random sample every time**, so your chart is reproducible. Any number works; 42 is a very old joke.
>
> `df.sample(5)` on its own is worth knowing too: **five random rows instead of the first five.** `head()` shows you the top of the file, which is often the tidiest part. `sample()` shows you what the data is actually like.
>
> **PCA** was also named alongside pair plots as a multivariate tool. PCA is a Module-2 conversation; the pair plot you can have today.

---

### STEP 18 — One dot per flight

▶ *In your script:* the whole of `scripts/09_chart_scatter.py`

🎯 **Objective:** See what a correlation of zero looks like.

☕ **Story moment:** *"You have the number,"* says the instructor. *"−0.017. Now look at what it looks like, because the number and the picture teach different things."*

🧠 **The idea in plain English:** A **scatter plot** puts one dot per row: one column across, another up. If they move together the dots form a slope; if not, a shapeless cloud.

With 336,776 dots we need two tricks: `s=1` makes each dot tiny, `alpha=0.2` makes it mostly transparent so you can see where they pile up.

💻 **The code:**

```python
plt.scatter(df['distance'], df['dep_delay'], s=1, alpha=0.2)
plt.xlabel("Distance (miles)")
plt.ylabel("Departure delay (minutes)")
```

📺 **Expected output:**

```text
=== STEP 18: DISTANCE AGAINST DELAY ===
Drawing 336,776 dots. This one takes a moment.

Saved charts/distance_vs_delay.png

Read it: the cloud is a flat band, not a slope.
Long flights are no likelier to leave late than short ones --
which is exactly what the 0.0 in STEP 17 was telling you.
Window closed. Script finished.
```

**Read your chart.** A dense horizontal band hugging the bottom, with a scatter of dots flung upward at every distance. **Flat, not sloped.** The dots reach just as high at 500 miles as at 4,000.

**That flatness is `−0.0172` made visible.** And notice the *vertical* stripes — dots cluster at particular distances, because there are only 105 destinations and every JFK–Honolulu flight is exactly 4,983 miles.

⚠️ **Common mistake:** Plotting 336,776 solid dots at default size. You get a black rectangle. `s=1, alpha=0.2` is the difference between a chart and a smudge — and on big data those two arguments are not decoration, they are the whole difference between seeing your data and not.

✅ **Verify:** `charts/distance_vs_delay.png` exists and shows a flat band, not a slope.

🎤 **Try it yourself (60 seconds):** Plot `distance` against `air_time` instead — the 0.98 pair. A tight diagonal line, the exact opposite picture. Now you have seen both ends of the scale.

> 📌 **You saw this in class:**
>
> ```python
> plt.scatter(df['distance'], df['dep_delay'])
> plt.xlabel("Distance")
> plt.ylabel("Delay")
> plt.show()
> ```
>
> Identical, plus `s=1, alpha=0.2` so a third of a million dots stay readable.

---

### 🧠 Quick Quiz #5 — answer from memory, before peeking

**Q1.** Correlation always falls between which two values?

- A) 0 and 100
- B) −1 and +1
- C) 0 and 1
- D) −100 and +100

**Q2.** `distance` vs `dep_delay` came out at −0.0172. What does that mean?

- A) Longer flights are much more likely to leave late
- B) Longer flights are much more likely to leave early
- C) Flight distance tells you essentially nothing about delay
- D) The correlation could not be calculated for these columns

**Q3.** Why convert `time_hour` with `pd.to_datetime()` before analysing it?

- A) Because `.dt` parts like `.dt.hour` only work on real datetimes
- B) Because the column contained missing values that needed filling
- C) Because text columns cannot be saved to a CSV file
- D) Because it makes the DataFrame use less memory overall

---

## ☕ Cluster H — Where Data Actually Comes From

*No script for this cluster — read it, then go straight into Cluster I.*

---

### STEP 19 — The four taps, and the principle that governs all of them

▶ *In your script:* nothing to run. This one is a briefing.

🎯 **Objective:** Name the four places data comes from, and state the GIGO principle.

☕ **Story moment:** Last session of the workshop. The instructor puts up four words and says: *"Everything you will ever analyse arrived through one of these."*

🧠 **The four taps:**

**1. Files.** CSV, Excel, JSON. What you have used all day — `pd.read_csv("data/flights.csv")`. Most common starting point in the world, and the easiest.

**2. Databases, via SQL.** Most companies keep their real data in a database, and you get it out with a query.

> ### 📖 Story box: what your instructor's screen actually showed
>
> Before the flights data, your instructor showed the class something rather different: a **live query against a real bank's loan database**. It looked, in outline, like this:
>
> ```text
> SELECT customer_id, approved_amount, disbursed_amount, repayment_status
> FROM "CustomerLoan"
> LEFT JOIN "Customer" ON ...
> WHERE loan_product_code IN (...)
> LIMIT 10000
> ```
>
> **Three plain-English lines on what SQL is:** it is a language for asking a database questions. You describe *what you want* — which columns, from which tables, matching which conditions — and the database works out how to fetch it. `pd.read_sql_query(query, engine)` then drops the answer straight into a DataFrame, and from that moment on it is a table like any other and everything you learned today applies.
>
> **Why you are not running it.** That query needed a password, and it returned real customers' names, phone numbers and incomes. Credentials do not belong in a lab, and neither does anybody's personal data. So this one is a **story, not an exercise** — and that is itself a professional lesson: *real projects often start with a SQL query to a company database, and the first rule of that database is that what comes out of it is somebody's private life.*
>
> Your instructor also loaded a file from **Google Drive** inside Colab (`drive.mount('/content/drive')`) and a **California housing** sample. Both are Colab conveniences rather than skills; we mention them so nothing on your instructor's screen is left unexplained.

**3. APIs.** A web service you ask politely for data, usually getting JSON back. See the 🚀 bonus below.

**4. Scraping.** When there is no file, no database and no API — but the data is sitting on a web page. **That is Cluster I**, and it is the headline skill of this session.

### 🗑️ And the principle that governs all four: GIGO

> ## **Garbage In, Garbage Out.**

It was put plainly in class: *if your input data is flawed, any analysis or insight you derive from it will also be flawed and unreliable. You'll make bad decisions based on bad data.*

This is why Clusters B and C came **first**. Not because profiling is fun, but because **every clever thing you do afterwards inherits the quality of what you started with.** A beautiful chart of wrong numbers is worse than no chart, because people believe charts.

Class also previewed the three cleaning strategies you are about to need on scraped data:

| Problem | Strategy |
|---|---|
| **Duplicate entries** | `df.drop_duplicates()` — 🔙 STEP 8 |
| **Missing information** | `df.dropna()` or `df.fillna()` — 🔙 STEPs 6–7 |
| **Inconsistent date formats** | `pd.to_datetime()` — 🔙 STEP 16 |

**You already know all three.** That is not a coincidence — the workshop was building to this.

✅ **Verify:** Nothing to run. If you can name the four taps and say what GIGO means, this STEP worked.

🎤 **Try it yourself (60 seconds):** Which of the four taps does your own business data come out of? Most small businesses: a file, exported by hand from something else. Which is exactly why "check it before you trust it" matters most to *you*.

> ### 🚀 Bonus — beyond class: pulling live data from an API
>
> Your instructor demonstrated this in class, and it is six lines. **CoinGecko** publishes cryptocurrency prices for free, no signup:
>
> ```python
> import requests
> import pandas as pd
>
> url = "https://api.coingecko.com/api/v3/coins/markets"
> params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10, "page": 1}
>
> try:
>     res = requests.get(url, params=params, timeout=10)
>     data = res.json()
>     df_api = pd.json_normalize(data)
>     print(df_api[["name", "current_price", "market_cap"]])
> except Exception as error:
>     print("The API did not answer:", error)
> ```
>
> **🌐 Live data — your rows WILL look different from anybody else's, including five minutes from now.** Check instead: you got a table, it has those three columns, and the prices are numbers.
>
> `pd.json_normalize` is the interesting part: APIs answer in **JSON** (nested lists and dictionaries — 🔙 Week 1's containers, arriving from the internet), and `json_normalize` flattens that nest into a rectangular DataFrame. From there it is a table like any other.
>
> **Needs the internet.** Nothing else in the lab depends on it.

---

## ☕ Cluster I — Scouting the Competition

*Scripts for this cluster:* **`scripts/10_scrape_one_app.py`**, **`scripts/11_the_rating_picture.py`**, **`scripts/12_three_apps_compared.py`**

---

### STEP 20 — 🌐 Your first scrape

▶ *In your script:* the whole of `scripts/10_scrape_one_app.py`

🎯 **Objective:** Fetch real, live reviews off the internet, safely.

☕ **Story moment:** Saturday evening. You are home, the shop is shut, and you are thinking about the unit two streets over.

You know your coffee is better than Starbucks'. That is not the question. The question is what the big chains are actually *bad* at — because that is the gap branch two has to live in.

And here is the thing you did not appreciate before this morning: **every one of those chains has an app, and every one of those apps has thousands of public reviews written by people who were annoyed enough to type.**

It was put better in class than we can put it:

> 📌 *"Imagine having access to thousands of direct, unsolicited opinions from your app users. That's the power of online reviews! Manually collecting this much feedback is impossible. That's where web scraping comes in."*

And the part that should make you smile:

> 📌 *"Why this library? It's user-friendly and handles many complexities for us, making it ideal for beginners. **You don't need to be an HTML expert!**"*

### 🤝 First, three lines on doing this decently

Before you point a script at somebody else's website:

1. **Public data only.** These reviews are published for anybody to read. That is what makes this fair game — and it is the whole difference between this and the loan database in STEP 19.
2. **Gentle volumes.** We ask for **100 reviews per app**, not 100,000. You are one small business doing research, not a denial-of-service attack. *(The person who built this lab asked for five at a time while testing.)*
3. **Respect the terms of service, and use a real question.** Scraping to understand a market is research. Scraping to copy somebody's content wholesale is theft. **If you would not be comfortable explaining your scrape to the company, do not run it.**

That is your session's "ethical data workflows" objective, and it fits on a napkin.

🧠 **The idea in plain English:** `reviews(app_id, count=100)` hands back **two** things: the reviews, and a token for fetching the next page. We want the first and ignore the second — which is what `result, _ = ...` means. 🔙 Week 1's tuple unpacking; `_` is a conventional name for *"something arrives here and I do not need it"*.

Every app has an **ID** — the string in its Play Store URL. Starbucks is `com.starbucks.mobilecard`.

**And this call goes over the internet, which means it can fail.** So 🔙 **Week 2's `try`/`except` finally does the job it was invented for:**

💻 **The code:**

```python
from google_play_scraper import reviews

APP_ID = "com.starbucks.mobilecard"

try:
    result, _ = reviews(APP_ID, count=100, lang="en", country="us")
except Exception as error:
    print("The scrape failed. That is not your fault -- networks wobble.")
    print(f"  {type(error).__name__}: {error}")
    raise SystemExit(0)

if not result:
    print("The scrape returned no reviews at all -- no error, just nothing.")
    raise SystemExit(0)

review_df = pd.DataFrame(result)

clean = review_df[['content', 'score', 'at']].copy()
clean.columns = ['Review_Text', 'Rating', 'Date']
clean['App_Name'] = APP_ID
clean['Date'] = pd.to_datetime(clean['Date'])

clean.to_csv("my_coffee_reviews.csv", index=False)
```

> ### ⚠️ Two guards, not one — and the second one is the interesting one
>
> `try`/`except` catches the scrape **raising an error**. But a scrape can also come back **completely empty without raising anything at all** — no error, no reviews, just an empty list.
>
> **This genuinely happened while this lab was being built.** One of the three apps returned nothing on the first attempt and worked perfectly a minute later. If the script had assumed success, it would have crashed three lines later with a confusing message about an empty DataFrame.
>
> `if not result:` is the whole fix. **Check that you got something, not just that nothing went wrong.** Those are different questions, and the second one catches bugs the first never will.

📺 **Expected output — 🌐 LIVE DATA:**

> ### 🌐 Live data — your rows WILL look different
>
> These are real reviews written by real people, fetched at the moment you run the script. **Your text, names, dates and ratings will not match the block below and are not supposed to.**
>
> **Check instead:** the shape is `(100, 4)`, the columns are `Review_Text, Rating, Date, App_Name`, and `Rating` runs somewhere in 1–5.

```text
=== STEP 20: SCOUTING THE COMPETITION ===
Asking the Google Play Store for 100 reviews of com.starbucks.mobilecard

Got 100 reviews.

The scraper gives you far more than you asked for:
['reviewId', 'userName', 'userImage', 'content', 'score', 'thumbsUpCount', 'reviewCreatedVersion', 'at', 'replyContent', 'repliedAt', 'appVersion']

Cleaned down to the four columns we care about:
                                         Review_Text  ...                  App_Name
0  The app used to work great. But the past month...  ...  com.starbucks.mobilecard
1    love it! very EZ full of color, EZ to navigate.  ...  com.starbucks.mobilecard
2                                  Excellent amazing  ...  com.starbucks.mobilecard
3                            Great app! Fast pick up  ...  com.starbucks.mobilecard
4  Super Convenient...a little expensive though, ...  ...  com.starbucks.mobilecard

[5 rows x 4 columns]

Shape: (100, 4)
Ratings run from 1 to 5

Saved my_coffee_reviews.csv
(The lab's own copy lives in data/ and is untouched.)
```

**You just pulled a hundred real opinions off the live internet with one function call.** Take a moment on that.

**Now the three cleaning moves, and why each one is there:**

- **`[['content', 'score', 'at']]`** — the scraper returned **eleven** columns including everybody's username and profile-photo URL. You want three. 🔙 Week 2's double-bracket column selection.
- **`.copy()`** — and this one deserves a proper explanation, below.
- **`.columns = [...]`** — renaming so the columns say what they mean. `content` and `score` are the scraper's words; `Review_Text` and `Rating` are yours.
- **`pd.to_datetime()`** — 🔙 STEP 16, on real data, doing real work.

> ### 🧠 Why `.copy()`, and what happens without it
>
> When you write `review_df[['content', 'score', 'at']]`, pandas may hand you a **view** — a window onto the original table rather than a new table of your own. Then you change it, and pandas cannot always tell whether you meant to change the original too. So it warns you:
>
> ```text
> SettingWithCopyWarning: A value is trying to be set on a copy of a
> slice from a DataFrame. Try using .loc[row_indexer,col_indexer] = value
> ```
>
> **`.copy()` says "this slice is mine now"** and removes all doubt. It costs one method call and it prevents the single most confusing warning in pandas.
>
> Your instructor's single-app cell used `.copy()`, exactly as above. The three-app cell did not — and that warning duly appeared in class. **Make `.copy()` a habit** and you will never have to think about it again.

**And where the file goes.** The script saves to **`my_coffee_reviews.csv`** — its own filename, in the lab folder. The lab's shipped copy in `data/` is a *different file with a different name*, so your scrape can never overwrite it. If your scrape fails, nothing is lost.

⚠️ **Common mistake:** Writing `result = reviews(...)` instead of `result, _ = reviews(...)`. The function returns two things; catch one and `result` becomes a tuple containing your reviews rather than the reviews themselves, and the next line fails oddly.

✅ **Verify — structure, not content:** `Shape: (100, 4)`, the four column names, ratings within 1–5, and `my_coffee_reviews.csv` in your lab folder. **Do not** expect the review text to match.

🎤 **Try it yourself (60 seconds):** Change `count=100` to `count=10` and rerun. Ten reviews, same shape. Then check: is `my_coffee_reviews.csv` now shorter? **You just overwrote your own scrape** — which is worth knowing before it surprises you.

> 📌 **You saw this in class:**
>
> ```python
> # Scrape reviews for Instagram (you can replace with any app ID)
> result, _ = reviews('com.instagram.android', count=100)  # Fetch 100 reviews
>
> review_df = pd.DataFrame(result)
> print(review_df.head())
> ```
>
> then
>
> ```python
> review_df_cleaned = review_df[['content', 'score', 'at']].copy()
> review_df_cleaned.columns = ['Review_Text', 'Rating', 'Date']
> review_df_cleaned['App_Name'] = 'com.instagram.android'
> review_df_cleaned['Date'] = pd.to_datetime(review_df_cleaned['Date'])
> review_df_cleaned.to_csv("instagram_reviews.csv", index=False)
> ```
>
> **Identical, move for move.** Your instructor pointed it at **Instagram** because the session's example was social apps; we point it at a **coffee chain** because you are about to open a coffee shop. Same code, and we added the `try`/`except` and the `if not result:` guard, because a notebook cell you can re-run by hand is more forgiving than a script.
>
> *(In class this technique was aimed at **bank** apps, collecting 400+ reviews each. Same method, and we keep to the gentler 100.)*

---

### STEP 21 — What are people actually saying?

▶ *In your script:* the whole of `scripts/11_the_rating_picture.py`

🎯 **Objective:** Summarise scraped reviews, and draw the rating distribution.

☕ **Story moment:** You have 300 reviews of three coffee chains sitting on your kitchen table. Time to find out what is in them.

> ### 🌐 The one line that makes this lab work offline
>
> Look at the top of the script:
>
> ```python
> CSV_PATH = "data/coffee_app_reviews_fallback.csv"
> ```
>
> That file ships with the lab: **300 real reviews of three coffee-chain apps**, genuinely scraped when this lab was built. Because this script reads *that* file, **every number below will match your screen exactly** — and the whole cluster works with no internet at all.
>
> **Scraped your own in STEP 20?** Change that one line to `"my_coffee_reviews.csv"` and rerun. Everything still works, and **your numbers will differ from the doc's** — because they are your reviews, from today.

🧠 **The idea in plain English:** Nothing new. 🔙 `value_counts()`, `groupby().mean()`, boolean filtering, and a seaborn count plot. All Week-2 tools — pointed at data you collected yourself.

💻 **The code:**

```python
CSV_PATH = "data/coffee_app_reviews_fallback.csv"
reviews_df = pd.read_csv(CSV_PATH)

print(reviews_df['Rating'].value_counts().sort_index())
print(reviews_df.groupby('App_Name')['Rating'].mean().round(3))

sns.countplot(x='Rating', data=reviews_df, hue='Rating',
              legend=False, palette='viridis')
```

📺 **Expected output:**

```text
=== STEP 21: THE RATING PICTURE ===
Reading: data/coffee_app_reviews_fallback.csv
Shape: (300, 4)

How many of each star rating?
Rating
1     79
2     17
3     13
4     25
5    166
Name: count, dtype: int64

Average rating overall: 3.607

Average rating per app:
App_Name
com.dunkinbrands.otgo                    3.80
com.starbucks.mobilecard                 3.01
com.trubeacon.scooters_mobile_android    4.01
Name: Rating, dtype: float64

Two shortest 1-star reviews:
  "Breaks constantly"
  "this app is unworkable"

Saved charts/rating_distribution.png
Window closed. Script finished.
```

**Read that rating distribution, because it is a genuinely interesting shape:**

| Rating | Count |
|---|---|
| ⭐ | **79** |
| ⭐⭐ | 17 |
| ⭐⭐⭐ | 13 |
| ⭐⭐⭐⭐ | 25 |
| ⭐⭐⭐⭐⭐ | **166** |

**Look at the middle. It is empty.** 166 people gave five stars, 79 gave one, and only 13 could be bothered with three.

That is a **U-shape**, and it is what almost all review data looks like. People do not write reviews when a thing is *fine*. They write when they are delighted or furious. **The middle of the market does not review; it just gets on with its day.**

**And two shortest one-star reviews, in full:** *"Breaks constantly"* and *"this app is unworkable"*. Nobody is complaining about the coffee.

⚠️ **`palette` without `hue`.** Your class notebook wrote `sns.countplot(x='Rating', data=..., palette='viridis')`, which works but prints:

```text
FutureWarning: Passing `palette` without assigning `hue` is deprecated
and will be removed in v0.14.0.
```

The fix is to assign `hue='Rating'` and `legend=False` — same chart, no warning. That is what this script does.

✅ **Verify:** `Shape: (300, 4)`, the five rating counts, average `3.607`, and `charts/rating_distribution.png` on disk.

🎤 **Try it yourself (60 seconds):** Find the *longest* review: `reviews_df.loc[reviews_df['Review_Text'].str.len().idxmax(), 'Review_Text']`. Read it. Somebody was **furious** — and `.str.len()` is your first hint that text columns have their own toolkit.

---

### STEP 22 — Three chains, side by side

▶ *In your script:* the whole of `scripts/12_three_apps_compared.py`

🎯 **Objective:** Compare several apps in one table, and see the class's multi-app loop.

☕ **Story moment:** One chain is an anecdote. Three is a pattern.

🧠 **The idea in plain English:** Scraping several apps is a 🔙 **Week-1 `for` loop** with `pd.concat` to stack the results:

```python
all_reviews = pd.DataFrame()

for app_id in APP_IDS:
    result, _ = reviews(app_id, count=100)
    app_reviews = pd.DataFrame(result)
    app_reviews['App_Name'] = app_id
    all_reviews = pd.concat([all_reviews, app_reviews], ignore_index=True)
```

**`pd.concat([a, b])` stacks tables on top of each other**, and `ignore_index=True` renumbers the rows 0…299 rather than 0…99 three times.

**The script ships with `RUN_LIVE = False`**, so it reads the shipped 300-row file and your numbers match the doc exactly. **Flip it to `True`** and the loop above runs for real, live, on all three apps. Both paths work; the toggle is there so you can choose.

💻 **The comparison:**

```python
summary = reviews_df.groupby('App_Name').agg(
    reviews=('Rating', 'count'),
    average_rating=('Rating', 'mean'),
)

unhappy = reviews_df[reviews_df['Rating'] == 1]
summary['one_star'] = unhappy['App_Name'].value_counts()
```

🔙 That `agg(reviews=('Rating', 'count'), ...)` form is a **named aggregation** — you name the column you want and say how to build it. It is tomorrow's main tool, arriving a day early.

📺 **Expected output:**

```text
=== STEP 22: THREE CHAINS IN ONE TABLE ===
Reading: data/coffee_app_reviews_fallback.csv
Shape: (300, 4)

How many reviews from each app?
App_Name
com.starbucks.mobilecard                 100
com.dunkinbrands.otgo                    100
com.trubeacon.scooters_mobile_android    100
Name: count, dtype: int64

=== THE COMPARISON THAT MATTERS ===
                                       reviews  average_rating  one_star
App_Name                                                                
com.dunkinbrands.otgo                      100            3.80        19
com.starbucks.mobilecard                   100            3.01        44
com.trubeacon.scooters_mobile_android      100            4.01        16

Happiest customers: com.trubeacon.scooters_mobile_android
Grumpiest customers: com.starbucks.mobilecard

Scooter's Coffee is a fraction of Starbucks' size --
and that is exactly why it is the useful comparison for you.
```

**Now this is a finding you can act on.**

| Chain | Average | 1-star reviews |
|---|---|---|
| **Scooter's Coffee** (small chain) | **4.01** | 16 |
| Dunkin' | 3.80 | 19 |
| **Starbucks** (the giant) | **3.01** | **44** |

**Starbucks — the biggest coffee company on earth — has the angriest app customers of the three.** Forty-four of its hundred reviewers gave one star. And **Scooter's Coffee**, a chain most people outside the American Midwest have never heard of, has the happiest.

**Read that as a business owner, not an analyst.** Scale is not winning here. The small operator is beating the giant on the thing customers actually rate. That is not a consolation prize — that is your entire strategy for branch two, and you found it in a table you built yourself.

⚠️ **Common mistake:** Assuming `pd.concat` lines up columns by position. It matches on **column names**. If one app's DataFrame comes back with slightly different columns you get NaN-filled gaps rather than an error — so 🔙 STEP 6's `isnull().sum()` after a concat is never wasted.

✅ **Verify:** `(300, 4)`, 100 per app, and the three averages 3.80 / 3.01 / 4.01.

🎤 **Try it yourself (2 minutes):** Set `RUN_LIVE = True` and run it for real. Three live scrapes, about ten seconds. **Your averages will differ from the table above** — the reviews are newer than this lab. Then set it back to `False` and watch the numbers snap back to the doc's.

> 📌 **You saw this in class:**
>
> ```python
> app_ids = ['com.instagram.android', 'com.whatsapp', 'com.facebook.katana']
> all_reviews = pd.DataFrame()
>
> for app_id in app_ids:
>     result, _ = reviews(app_id, count=100)
>     app_reviews = pd.DataFrame(result)
>     app_reviews['App_Name'] = app_id
>     all_reviews = pd.concat([all_reviews, app_reviews], ignore_index=True)
>
> all_reviews_cleaned = all_reviews[['content', 'score', 'at', 'App_Name']]
> all_reviews_cleaned.columns = ['Review_Text', 'Rating', 'Date', 'App_Name']
> ```
>
> **Same loop, exactly.** Two differences worth naming: your instructor scraped **Instagram, WhatsApp and Facebook** (the session's social-app example) where we scrape three **coffee chains**; and that fourth line has no `.copy()`, which is precisely why `SettingWithCopyWarning` appeared on the class screen. Ours has it.

> ### 🚀 Bonus — beyond class: scout a fourth chain yourself
>
> Pick your own competitor. Change `APP_ID` in script 10 and rerun:
>
> | Chain | App ID |
> |---|---|
> | Pret A Manger | `cloud.cofe.pret` |
> | Costa Coffee Club ME | `com.alghanim.costakuwait` |
> | Panera Bread Canada | `com.tacitinnovations.panerabreadcanada` |
>
> All three were live when this lab was built. **To find any app's ID**, open its Play Store page and look at the URL: `play.google.com/store/apps/details?id=`**`com.starbucks.mobilecard`**.
>
> 🌐 Live, so your numbers are yours. Gentle volumes, please — the ethics note applies to your curiosity too.

---

## ☕ Cluster J — The Findings Note

*Script for this cluster:* **`scripts/13_competitor_note.py`**

---

### STEP 23 — Write it down, or it did not happen

▶ *In your script:* the whole of `scripts/13_competitor_note.py`

🎯 **Objective:** Turn the whole afternoon into a written artifact somebody else could act on.

☕ **Story moment:** Sunday morning. You have 300 reviews, three averages and one genuinely useful insight. In a week you will have forgotten the numbers.

So you write it down. **This is the deliverable** — not the charts, not the DataFrame. The page.

🧠 **The idea in plain English:** Four best practices were given in class, and the fourth is the one people skip:

| Practice | What it means | Where you did it |
|---|---|---|
| **Iterate** | EDA is never finished — new questions arrive | you re-ran with new thresholds all day |
| **Visualise** | pictures alongside numbers | eight charts in `charts/` |
| **Document** | **record findings for other people** | ⬅ **this STEP** |
| **Validate** | cross-check against domain knowledge | STEP 17's 🎤: two tools, same answer |

🔙 And the tools are Week-1's: **f-strings** for the sentences, **`open()`** with `"w"` for the file.

💻 **The code** (the heart of it):

```python
lines = []
lines.append("=" * 58)
lines.append("   THE COZY BEAN -- COMPETITOR SCOUTING NOTE")
lines.append(f"Average rating across all of them: {overall:.2f} out of 5")

for app_name, row in per_app.iterrows():
    lines.append(f"  {app_name:42} {row['average_rating']:.2f}  ({int(row['reviews'])} reviews)")

report = "\n".join(lines)
print(report)

with open("competitor_findings.txt", "w", encoding="utf-8") as f:
    f.write(report + "\n")
```

**Building a list of lines and joining it at the end** is far easier to get right than one enormous string. And `"\n".join(lines)` glues them with a newline between each.

📺 **Expected output:**

```text
==========================================================
   THE COZY BEAN -- COMPETITOR SCOUTING NOTE
   Before we open branch two
==========================================================

Evidence: 300 public app-store reviews across 3 coffee chains.
Average rating across all of them: 3.61 out of 5
Reviews of 2 stars or worse: 96 (32.0%)

Per chain, best first:
  com.trubeacon.scooters_mobile_android      4.01  (100 reviews)
  com.dunkinbrands.otgo                      3.80  (100 reviews)
  com.starbucks.mobilecard                   3.01  (100 reviews)

FINDING: com.trubeacon.scooters_mobile_android has the happiest app customers.
         com.starbucks.mobilecard has the most to fix.

WHAT THIS MEANS FOR US:
  The chains are not being marked down on their coffee.
  They are being marked down on their APPS -- logins,
  payment, and rewards that do not work.
  Branch two does not need an app to beat them.
  It needs the thing an app cannot fake.

==========================================================

Saved competitor_findings.txt
That file is the deliverable. Open it -- it is yours.
```

**Read the last four lines again.** Every number above them was computed from evidence you gathered yourself. **96 of 300 reviews — nearly a third — are two stars or worse**, and not one of them is about the drink.

That is a real finding, defensible in a real meeting, and you produced it from nothing in an afternoon.

🔙 Note `{overall:.2f}` turning `3.607` into `3.61`, and `{app_name:42}` padding names to 42 characters so the column lines up. Week-1 f-strings, earning their keep.

⚠️ **Common mistake:** Opening a file without `encoding="utf-8"`. On Windows the default encoding chokes on characters outside its small set, and a review containing an emoji will crash your script at the very last line. **Always name the encoding when writing text.**

✅ **Verify:** `competitor_findings.txt` exists in your lab folder. **Open it.** It should be identical to what printed.

🎤 **Try it yourself (2 minutes):** Add a line to the note giving the **shortest** one-star review verbatim, as evidence. *(Hint: 🔙 STEP 21 already found it.)* A quote from a real customer is worth three averages in a meeting.

---

### 🧠 Quick Quiz #6 — answer from memory, before peeking

**Q1.** What does GIGO stand for, and what is the point of it?

- A) Get In, Get Out — analyse quickly before the data changes
- B) Group In, Group Out — always aggregate before charting
- C) Guess In, Guess Out — estimates are fine if consistent
- D) Garbage In, Garbage Out — bad input guarantees bad conclusions

**Q2.** Why is the scrape wrapped in `try`/`except`?

- A) Because the Play Store requires an API key to be handled
- B) Because a network call can fail for reasons that are not your fault
- C) Because `reviews()` always raises an error on its first call
- D) Because pandas cannot build a DataFrame without it

**Q3.** Which of these makes a scrape reasonable rather than rude?

- A) Requesting as much data as the server will physically send
- B) Scraping private user profiles rather than public pages
- C) Public data, gentle volumes, and respect for the terms of service
- D) Removing your name from the request so it cannot be traced

---

### 🧠 Quick Quiz #7 — answer from memory, before peeking

**Q1.** Why does script 11 read `CSV_PATH` from a variable at the top?

- A) So one edit switches between the shipped file and your own scrape
- B) So the script runs faster on very large review files
- C) So pandas can detect the file's encoding automatically
- D) So the scraped reviews are never written to disk at all

**Q2.** What does `.copy()` prevent when you slice columns off a DataFrame?

- A) It prevents the original file on disk from being modified
- B) It prevents the new table from using too much memory
- C) It prevents duplicate rows from appearing in the slice
- D) It prevents the `SettingWithCopyWarning` about views

---

## 5. 🏋️ Practice Problems

Reading pandas feels easy. Writing it is where it sticks.

**How practice works here:** one problem per file in `practice/`; run just the one you want with `python practice/p01_profile_the_table.py`. Every file's header repeats the task **and the exact expected output**. Every file runs as-is before you touch it — it just prints the wrong things. Answers are in `solutions/` — **open them only after a genuine attempt.**

| # | File | Story task | You will practise |
|---|---|---|---|
| p01 | `p01_profile_the_table.py` | The workshop's four opening questions about any table. | `shape`, `columns`, `select_dtypes` |
| p02 | `p02_count_the_gaps.py` | Count the gaps **the long way** — one column at a time. | 🔙 **a Week-1 `for` loop**, `isna()` |
| p03 | `p03_fill_or_drop.py` | Fill `arr_delay` or drop it — and defend your choice out loud. | `fillna`, `dropna`, mean vs median |
| **p04** | `p04_find_the_outliers.py` | **The whole IQR fence again, on a different column, from scratch.** | ⭐ `quantile`, the fence, filtering |
| **p05** | `p05_a_function_that_profiles.py` | You have typed "missing, mean, median, max" six times. Write it **once**. | ⭐ 🔙 **Week-1 `def` returning a dict** |
| p06 | `p06_your_own_chart.py` | One chart, your choice, saved to `charts/`. | seaborn/matplotlib + `savefig` |
| p07 | `p07_read_the_reviews.py` | Interrogate the 300 scraped reviews. No internet needed. | `value_counts`, `groupby`, filtering |
| **p08** | `p08_capstone_competitor_note.py` | **CAPSTONE — your own five findings, your own note, your own words.** | ⭐ the whole lab |
| 🚀 p09 | `p09_bonus_bins_and_shares.py` | **Bonus:** `pd.cut` into buckets, and `value_counts(normalize=True)`. | bonus material only |

> 🚀 **p09 is a bonus** and uses `pd.cut` and `normalize=True`, neither of which was in your class session. **Nothing depends on it.**

### 🏔️ About the capstone

**p08 — Your Own Competitor Note** is the one to be proud of. Every piece of it is something you did between p01 and p07. What is hard — and what makes it worth doing — is that **nobody tells you which piece to use where.** That is exactly what real data work feels like.

Your note will not match mine, and it should not. Mine looked at averages and review lengths; yours might look at dates, or at which app improved recently, or at something I did not think of.

### 🔗 And one that sets up tomorrow

**p05** asks you to write a function because you have typed the same thing six times. **Hold on to that feeling.** Tomorrow's lab repeats a nine-line cleaning block in eight separate scripts, and its p07 asks you to do exactly the same thing on a bigger scale. **Irritation is how you learn to spot a missing function.**

---

## 6. 📚 Cheat Sheet & Glossary

- **[CHEATSHEET.md](CHEATSHEET.md)** — ⭐ **the profiling & EDA checklist.** The first-ten-minutes-with-any-table routine, the outlier formulas, and the scraping recipe. **This is the page you will still be using in a year.**
- **[GLOSSARY.md](GLOSSARY.md)** — every new word this week in one friendly line: profiling, EDA, skew, IQR, z-score, correlation, GIGO, scraping and the rest.

*(Week 2's [cheat sheet](../../Week2/Lab02/CHEATSHEET.md) still applies in full — `read_csv`, filtering, `groupby`, `agg`, `savefig`. This week builds on it and replaces none of it.)*

---

## 7. 🤔 Reflection (2 minutes — please actually do this)

1. **What did the flights data tell you that surprised you?** There is at least one thing. For most people it is that long flights are no likelier to leave late — or that delay climbs all day.
2. **What is still fuzzy?** Name the one thing you would ask an instructor sitting beside you. Write it down; it is your first question next session.
3. **Which of your own numbers do you now distrust?** You have spent a day learning that tables lie. Is there a spreadsheet in your life you would now check before quoting from it?
4. **Now go and scrape something you actually care about.** Any app. Your bank's, your gym's, a competitor's. You have the tool, you have the ethics note, and it is four lines. That is not homework — that is the moment this becomes yours.

---

## 8. ✅ Answer Key

*No peeking until you have answered. Twenty questions in total.*

### Quiz #1

| Q | Answer | Why |
|---|---|---|
| 1 | **C** — structure, content and quality | Those are the three things profiling systematically examines. Rows and missing values are *part* of it, not the whole. |
| 2 | **B** — the number of columns | `shape` is always `(rows, columns)`. 336,776 flights, 19 columns. |
| 3 | **A** — no value was recorded here | `NaN` is "Not a Number" — pandas for "nothing here". Not zero, which is a real value. |

### Quiz #2

| Q | Answer | Why |
|---|---|---|
| 1 | **D** — consider dropping the column | The rule of thumb from class: ~20% missing → consider filling; ~80% → consider dropping. There is not enough left to be useful. |
| 2 | **B** — the mean has been dragged up by extreme late flights | Median −2, mean +12.6. The gaps are cancelled flights; filling with +12.6 would invent lateness that never happened. |
| 3 | **C** — no row is an exact copy of another | Which means no flight is double-counted, so your totals are trustworthy. Zero is a finding. |

### Quiz #3

| Q | Answer | Why |
|---|---|---|
| 1 | **A** — right-skewed, extremes pulling the mean up | One tall bar and a long right tail. It is why mean (+12.6) and median (−2) disagree. |
| 2 | **D** — it smooths the shape and can hide the tail | Five buckets swallow the entire outlier tail into one bar. Bin count is an editorial decision. |
| 3 | **B** — values flagged as outliers | Anything beyond the whiskers, which reach 1.5 × IQR past the box. |

### Quiz #4

| Q | Answer | Why |
|---|---|---|
| 1 | **C** — Q3 + 1.5 × IQR | And the lower fence is Q1 − 1.5 × IQR. D describes the *lower* fence. A describes the z-score method. |
| 2 | **A** — 21 standard deviations from the average | That is the definition. Beyond 3 is already suspicious; 21 is extraordinary. |
| 3 | **D** — extreme values inflate the std, widening the z threshold | The outliers defend each other: they push up the std that defines the threshold. On skewed data, prefer IQR. |

### Quiz #5

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — −1 and +1 | +1 perfect lockstep, 0 no relationship, −1 perfect opposite. |
| 2 | **C** — distance tells you essentially nothing about delay | −0.0172 is as close to zero as real data gets, and the scatter plot in STEP 18 shows it as a flat band. |
| 3 | **A** — `.dt` parts only work on real datetimes | While `time_hour` was text you could not ask for its hour. That is the class's "a date stored as object prevents time-based analysis". |

### Quiz #6

| Q | Answer | Why |
|---|---|---|
| 1 | **D** — Garbage In, Garbage Out | Flawed input guarantees flawed conclusions, however good your analysis. It is why profiling comes first. |
| 2 | **B** — a network call can fail for reasons that are not your fault | Networks wobble, servers rate-limit. `try`/`except` means one bad moment does not lose your work — and `if not result:` catches the silent version. |
| 3 | **C** — public data, gentle volumes, respect the terms of service | The three-line rule. A is a denial-of-service attack, B is a privacy violation, D is evasion. |

### Quiz #7

| Q | Answer | Why |
|---|---|---|
| 1 | **A** — one edit switches between the shipped file and your own scrape | Which is what keeps every downstream number exact-match *and* lets the lab work offline. |
| 2 | **D** — the `SettingWithCopyWarning` about views | A slice may be a view onto the original. `.copy()` says "this is mine now" and removes the ambiguity. |

---

## 9. ➡️ What's Next

Stop and look at what you did today.

You opened a table with **336,776 rows** in it — a table you had never seen, about a business you know nothing about — and you found out that it had 46,595 gaps in six columns, no duplicates, three origin airports and sixteen airlines. You discovered that its central column is **right-skewed**, that the typical flight leaves **two minutes early** while the average flight leaves **twelve minutes late**, and that **delay accumulates through the day** like interest. You found the same outliers **two different ways** and understood why the two answers disagreed. You read a **correlation matrix**. You worked out a **z-score by hand**.

Then you went to the live internet, **scraped 300 real opinions** off it, and discovered that the biggest coffee company in the world has worse app reviews than a chain you had never heard of.

**Three weeks ago you had never written a line of Python.**

**Next session** the ground shifts under you in a way you will enjoy. Everything today was about *understanding* data. Tomorrow is about **building** it — taking the Cozy Bean's own bank statement, in a state so bad that the money columns arrive as *text with commas in them*, and turning it into a tidy feature table plus a one-page note for Mrs Adeyemi.

Everything you did today is a tool you will pick up again tomorrow. The IQR fence comes back — and this time the outlier it flags is the loan tranche itself, and deleting it would be a catastrophe. `describe()` comes back. `to_datetime` comes back. Skew comes back, and this time you do something about it.

And that z-score formula you worked out by hand for one late Hawaiian Airlines flight? **Tomorrow it turns out to be a machine-learning preprocessing step.** Same arithmetic. Completely different job.

The evidence pack is due on Mrs Adeyemi's desk. The second branch opens in the spring. ☕

---

*Aperion AI Training Academy · Module 1: AI/ML Fundamentals · Week 3 · Lab01*
*"Boundless Possibilities, Infinite Potential"*

