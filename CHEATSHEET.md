# 📋 Lab01 Cheat Sheet — The Profiling & EDA One-Pager

**The Cozy Bean · M1-W3-Lab01 · Aperion AI Training Academy**

*Print this one. It is the routine you will run on every table for the rest of your career.*

---

## ⭐ THE FIRST TEN MINUTES WITH ANY TABLE

Run these seven lines on anything, ever, before you form a single opinion.

```python
import pandas as pd

df = pd.read_csv("data/whatever.csv")

df.shape                      # (rows, columns) -- how much evidence is there?
df.head()                     # what does the top look like?
df.tail()                     # what does the END look like? (the truth lives here)
df.info()                     # every column: fill count + type
df.describe()                 # eight summary numbers per numeric column
df.isnull().sum()             # how many gaps, per column
df.duplicated().sum()         # has anything been counted twice?
```

**If your terminal truncates a wide table with `...`**, ask for fewer columns:

```python
df[['col_a', 'col_b', 'col_c']].tail()
```

---

## Structure · Content · Quality

| Check | Command | Looking for |
|---|---|---|
| **STRUCTURE** | `df.shape`, `df.info()`, `df.dtypes` | wrong types — especially **dates stored as text** |
| **CONTENT** | `df.describe()`, `df['c'].value_counts()`, `.nunique()` | impossible values, wrong units, mean ≠ median |
| **QUALITY** | `df.isnull().sum()`, `df.duplicated().sum()` | gaps and double-counting |

---

## Missing values

```python
df.isnull().sum()                                  # count per column
(df.isnull().mean() * 100).sort_values(ascending=False)   # percentage, worst first
df.isnull().sum().sum()                            # one number for the whole table
df.isnull().any(axis=1).sum()                      # how many ROWS have any gap
```

**The rule of thumb:**

| Missing | Consider |
|---|---|
| ~20% | **filling** it (impute) |
| ~80% | **dropping** the column |

**Handling:**

```python
df = df.dropna(axis=1, thresh=0.8 * len(df))    # drop COLUMNS >20% empty (axis=1!)
df.fillna(df.median(numeric_only=True), inplace=True)   # fill numerics with median
df = df.dropna(subset=['important_col'])        # drop rows gappy in ONE column
```

> **Median, not mean, on skewed data.** Delays, money, incomes, prices are all skewed. The mean has already been dragged away from typical by the extremes.
>
> **And every filled value afterwards looks exactly like data.** Nothing marks it. Count what you filled.

---

## Duplicates

```python
df.duplicated().sum()                       # count exact-copy rows
df = df.drop_duplicates()                   # remove them
df.duplicated(subset=['a', 'b']).sum()      # "duplicate" = same a AND b
```

**Zero is a finding.** It means your totals are trustworthy.

---

## Profiling text columns

```python
for col in df.select_dtypes(include='str'):     # a Week-1 for loop!
    print(col, df[col].nunique())

df['col'].value_counts()                        # how many of each
df['col'].value_counts(normalize=True) * 100     # as percentages
```

*(Class wrote `include='object'`. Still works on pandas 3, but warns. `'str'` is the modern spelling.)*

**Reading `nunique()`:** 1 value = useless · a handful = **category**, group by it · thousands = **identifier**, do not group by it.

---

## ⭐ THE FOUR EDA CHARTS

Every chart script starts and ends the same way:

```python
import os
os.makedirs("charts", exist_ok=True)     # matplotlib will NOT make the folder

# ... draw ...

plt.savefig("charts/name.png")           # SAVE first...
plt.show()                               # ...THEN show
```

| Chart | Code | Reads |
|---|---|---|
| **Histogram** | `df['c'].hist(bins=50)` | the **shape** — skew, peaks, gaps |
| **Box plot** | `df.boxplot(column='c')` | median, middle half, **outlier dots** |
| **Bar chart** | `df['c'].value_counts().plot(kind='bar')` | counts of a category |
| **Scatter** | `plt.scatter(df['a'], df['b'], s=1, alpha=0.2)` | relationship between two columns |

**On big data, `s=1, alpha=0.2` is the difference between a chart and a black smudge.**

Two charts in one script? `plt.figure()` between them, or the second draws on top of the first.

---

## Reading a distribution

| Sign | Means |
|---|---|
| mean **>** median | **right-skewed** — a few big values pull the mean up |
| mean **<** median | left-skewed |
| mean ≈ median | roughly symmetrical |
| one tall bar + long thin tail | classic skew. Money and delays always look like this |

**Bin count is an editorial decision.** Too few hides the tail; too many is noise.

---

## ⭐ OUTLIERS — BOTH METHODS

### IQR fence (prefer this on skewed data)

```python
Q1 = df['c'].quantile(0.25)
Q3 = df['c'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df['c'] < Q1 - 1.5 * IQR) | (df['c'] > Q3 + 1.5 * IQR)]
print(outliers.shape)
```

### Z-score

```python
# By hand, for one value:
z = (value - df['c'].mean()) / df['c'].std()

# For every row:
from scipy.stats import zscore
df['zscore'] = zscore(df['c'].fillna(0))
outliers = df[df['zscore'].abs() > 3]
```

**A z-score is how many standard deviations a value sits from the mean. Beyond 3 is suspicious.**

### Why they disagree

| Method | Built from | On skewed data |
|---|---|---|
| **IQR** | quartiles — **positions** | robust; extremes barely move the fence |
| **Z-score** | mean and std — **both inflated by the outliers** | flags fewer; the outliers defend each other |

> ## An outlier is a **question**, not a verdict.
>
> The question is *"why is this here?"* Sometimes: a typo — fix it. Sometimes: a broken sensor — drop it. Sometimes: **the most important thing that happened all year** — flag it, explain it, **keep it**.

**Flag, don't delete:**

```python
df['flagged'] = False
df.loc[outliers.index, 'flagged'] = True
df['flag_reason'] = ""
df.loc[outliers.index, 'flag_reason'] = "large credit - expected, loan tranche"
```

---

## Dates and time

```python
df['when'] = pd.to_datetime(df['when'], utc=True)        # text -> real dates
df['when'] = pd.to_datetime(df['when'], errors='coerce') # unreadable -> NaT, no crash

df['when'].dt.hour        # .dt unlocks the parts -- ONLY on real datetimes
df['when'].dt.day_name()  # 'Monday'
df['when'].dt.month
df['when'].dt.to_period('M').astype(str)   # '2026-10'

df.groupby(df['when'].dt.hour)['value'].mean()
```

**A date stored as text blocks every time-based analysis.** Convert first, always.

**After any `coerce`, count what it ate:** `df['when'].isna().sum()`.

**Careful:** `groupby` creates no row for a group with no members. Do not assume 24 hours or 12 months.

---

## The `fig, ax` chart form

```python
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_values, y_values, marker='o')
ax.set_xlabel("...")
ax.set_ylabel("...")
ax.set_title("...")
ax.set_xticks(x_values)
ax.set_xticklabels(x_values, rotation=45)
plt.tight_layout()
```

`plt.something()` draws on "whatever chart is current". `fig, ax` names things explicitly — and is what you need the moment you want two charts side by side.

---

## Correlation

```python
small = df[['a', 'b', 'c', 'd']].corr()          # start SMALL
print(small.round(4))

sns.heatmap(small, annot=True, vmin=-1, vmax=1, cmap='coolwarm')
sns.heatmap(df.corr(numeric_only=True), annot=False)     # the whole wall
```

| Value | Means |
|---|---|
| **+1** | perfect lockstep |
| +0.9 | very strong positive |
| **0** | **no relationship at all** |
| −0.9 | very strong opposite |
| **−1** | perfect opposite |

**Always pass `vmin=-1, vmax=1`** or seaborn stretches its colours over whatever it found and a meaningless 0.05 looks dramatic.

**The diagonal is always 1.0** — every column correlates perfectly with itself. If it is not, something is broken.

> ⚠️ **Correlation is not causation.** Two columns correlating at 0.98 may both be caused by a third thing. The number cannot tell you which situation you are in. You have to know.

**Two columns correlating near 1.0 are nearly the same fact twice** — which matters when you feed a model.

---

## Where data comes from

| Source | How | Note |
|---|---|---|
| **Files** | `pd.read_csv(path)` | most common by far |
| **Databases** | `pd.read_sql_query(query, engine)` | SQL asks a database for what you want |
| **APIs** | `requests.get(url)` → `pd.json_normalize(data)` | JSON in, DataFrame out |
| **Scraping** | a library like `google-play-scraper` | when there is no file, database or API |

> ## 🗑️ GIGO — Garbage In, Garbage Out
>
> If your input is flawed, every insight you derive from it is flawed. **A beautiful chart of wrong numbers is worse than no chart, because people believe charts.** This is why profiling comes first.

**Never put credentials in a script, and never put anybody's personal data in a lab file.**

---

## ⭐ SCRAPING RECIPE

```python
from google_play_scraper import reviews

try:
    result, _ = reviews('com.starbucks.mobilecard', count=100,
                        lang="en", country="us")
except Exception as error:
    print("Scrape failed:", error)
    raise SystemExit(0)

if not result:                      # it can return EMPTY without raising!
    print("No reviews came back.")
    raise SystemExit(0)

df = pd.DataFrame(result)
clean = df[['content', 'score', 'at']].copy()      # .copy() -- see below
clean.columns = ['Review_Text', 'Rating', 'Date']
clean['App_Name'] = 'com.starbucks.mobilecard'
clean['Date'] = pd.to_datetime(clean['Date'])
clean.to_csv("my_reviews.csv", index=False)
```

**Several apps:**

```python
all_reviews = pd.DataFrame()
for app_id in APP_IDS:
    result, _ = reviews(app_id, count=100)
    part = pd.DataFrame(result)
    part['App_Name'] = app_id
    all_reviews = pd.concat([all_reviews, part], ignore_index=True)
```

**Two guards, not one.** `try`/`except` catches an error being *raised*. `if not result:` catches the scrape coming back **empty with no error at all** — which happens, and is much harder to debug.

**`result, _ = reviews(...)`** — the function returns two things (reviews, next-page token). `_` means "arrives here, not needed".

**`.copy()`** — a column slice may be a *view* onto the original. `.copy()` says "this is mine now" and prevents `SettingWithCopyWarning`.

**Find any app's ID** in its Play Store URL: `...details?id=`**`com.starbucks.mobilecard`**

### 🤝 The three-line ethics rule

1. **Public data only.**
2. **Gentle volumes** — 100, not 100,000.
3. **Respect the terms of service.** If you would not be comfortable explaining your scrape to the company, do not run it.

---

## Best practices (the four from class)

| | |
|---|---|
| **Iterate** | EDA is never finished — new questions keep arriving |
| **Visualise** | pictures alongside numbers, always |
| **Document** | **write findings down** — the one people skip |
| **Validate** | cross-check with a second method or with domain knowledge |

---

## Writing the findings note

```python
lines = []
lines.append("=" * 58)
lines.append("   THE COZY BEAN -- FINDINGS")
lines.append(f"Average rating: {overall:.2f} out of 5")
lines.append(f"  {name:42} {value:.2f}")       # :42 pads to line up columns

report = "\n".join(lines)
print(report)

with open("findings.txt", "w", encoding="utf-8") as f:
    f.write(report + "\n")
```

**Build a list of lines and join at the end** — far easier than one giant string.
**Always pass `encoding="utf-8"`** when writing text, or one emoji crashes your script.

---

## Errors you will actually meet

| Error | Cause | Fix |
|---|---|---|
| `TypeError: 'tuple' object is not callable` | `df.shape()` with brackets | `shape` is an attribute — drop them |
| `ValueError: The truth value of a Series is ambiguous` | `and` inside `df[...]` | use `&`, and bracket every condition |
| `AttributeError: Can only use .str accessor with string values` | `.str` on a numeric column | `.astype(str)` first |
| `FileNotFoundError: 'data/x.csv'` | wrong working folder | `pwd` must end in the lab folder |
| `FileNotFoundError` from `savefig` | `charts/` does not exist | `os.makedirs("charts", exist_ok=True)` |
| A blank PNG | `show()` before `savefig()` | **save first, show second** |
| `Pandas4Warning` on `select_dtypes` | `include='object'` on pandas 3 | use `include='str'` |
| `FutureWarning` on `countplot` | `palette` without `hue` | add `hue='Rating', legend=False` |

---

## Attributes vs methods — the brackets rule

| No brackets (facts) | Brackets (actions) |
|---|---|
| `df.shape`, `df.columns`, `df.dtypes`, `df.index` | `df.head()`, `df.describe()`, `df.info()` |

`dir(df)` lists everything a DataFrame has, when you cannot remember.

---

*Aperion AI Training Academy · M1-W3-Lab01 · "Boundless Possibilities, Infinite Potential"*

