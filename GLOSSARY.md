# 📖 Lab01 Glossary — Week 3, Session 1

**The Cozy Bean · M1-W3-Lab01 · Apeiron AI Training Academy**

*Every new word this week, one friendly line each. Alphabetical.*

---

### API
A web service you can ask for data, usually answering in JSON. One of the four places data comes from. *(🚀 bonus in Cluster H.)*

### attribute
A fact a table carries, asked for **without brackets** — `df.shape`, `df.columns`, `df.dtypes`. Compare **method**.

### bins
How many buckets a histogram chops your data into. `bins=50` gives fifty bars. **The number is an editorial decision:** too few hides the tail, too many is noise.

### box plot
A chart showing a column's median, its middle half (the box), most of the rest (the whiskers) and every flagged **outlier** as a dot. `describe()` drawn.

### cardinality
How many *different* values a column holds. One value tells you nothing; a handful means a **category**; thousands means an **identifier**.

### categorical column
A column holding a limited set of labels — `carrier`, `origin`, `channel`. You group by these. Compare **identifier**.

### correlation
A number from **−1 to +1** measuring whether two columns move together. +1 is perfect lockstep, 0 is no relationship, −1 is perfect opposite.

### correlation is not causation
Two columns can move together without either causing the other — often because a third thing causes both. **The number cannot tell you which situation you are in.**

### `.copy()`
Says *"this slice is mine now"* when you take columns off a DataFrame, so pandas knows you are not trying to change the original. Prevents `SettingWithCopyWarning`.

### `describe()`
Eight summary numbers for every numeric column: count, mean, std, min, 25%, 50%, 75%, max. The page you read before forming an opinion.

### duplicate row
A row that is an exact copy of one already in the table. Counted with `df.duplicated().sum()`, removed with `drop_duplicates()`. **Zero is a finding.**

### `.dt`
The doorway to a datetime column's parts — `.dt.hour`, `.dt.day_name()`, `.dt.month`. **Only works once the column is a real datetime**, never on text.

### EDA (Exploratory Data Analysis)
Analysing and visualising data to uncover patterns, trends, anomalies and relationships. **Profiling asks "is this data OK?"; EDA asks "what is it saying?"**

### fence (IQR fence)
The boundary beyond which a value is flagged as an outlier: `Q1 − 1.5×IQR` at the bottom and `Q3 + 1.5×IQR` at the top. **The 1.5 is a convention, not a law.**

### `fig, ax`
The explicit way to make a chart: `fig, ax = plt.subplots()` hands you the figure (the paper) and the axes (the chart on it), so you talk to `ax` by name instead of "whatever chart is current".

### GIGO — Garbage In, Garbage Out
If your input data is flawed, every insight you derive from it is flawed too. **A beautiful chart of wrong numbers is worse than no chart, because people believe charts.**

### heatmap
A grid where colour stands in for value. Used here for **correlation** — read it for bright and dark *patterns*, not individual numbers.

### histogram
A chart chopping a column into buckets and drawing how many values land in each. **The shape of your data.**

### identifier
A column whose values name individual things rather than categories — `tailnum`, `reviewId`. Thousands of unique values. **Do not group by these, and do not one-hot encode them.**

### imputation
The proper word for filling in missing values. *(Covered properly in Lab02.)*

### `info()`
Prints one line per column: name, how many non-empty values, and type. **The single most useful command in pandas** for spotting trouble fast.

### IQR (Interquartile Range)
`Q3 − Q1` — the range covered by the **middle half** of your data. The height of a box plot's box. Robust against extreme values, which is why it beats the z-score on skewed data.

### JSON
The nested format APIs answer in — lists and dictionaries. `pd.json_normalize()` flattens it into a DataFrame.

### median
The **middle** value — half above, half below. On skewed data it describes "typical" far better than the mean, which is why it is the honest fill value.

### method
Something a table *does*, called **with brackets** — `df.head()`, `df.describe()`. Compare **attribute**.

### `NaN` (Not a Number)
pandas' way of writing *"there was nothing here"*. **Not zero** — zero is a real value.

### `NaT` (Not a Time)
The date version of `NaN`. What `pd.to_datetime(errors='coerce')` writes when it cannot read a date.

### `.nunique()`
How many **different** values a column holds. See **cardinality**.

### outlier
A value far enough from the rest to be worth questioning. Found by the **IQR fence** or the **z-score**.

> **An outlier is a question, not a verdict.** The question is *"why is this here?"* — and the answer is sometimes "the most important thing that happened all year".

### pair plot
A grid of scatter plots showing every pair of columns at once, with each column's histogram down the diagonal. `sns.pairplot`. *(🚀 bonus.)*

### profiling (data profiling)
The systematic examination of a dataset's **structure, content and quality** before you trust anything in it. Types, distributions, null counts, duplicates, correlation overview.

### quantile
The value below which a given share of your data falls. `.quantile(0.25)` is the point a quarter of your data sits below — also called Q1.

### `random_state`
A number that makes a "random" operation reproducible. `df.sample(3000, random_state=42)` gives the **same** random 3,000 rows every time.

### `.sample()`
Random rows instead of the first rows. `df.sample(5)` shows you what your data is *actually* like; `head()` shows you the tidiest part of the file.

### scatter plot
One dot per row, one column across and another up. A slope means the columns are related; a shapeless cloud means they are not.

### scraping (web scraping)
Automating the collection of data from websites. Here: `google-play-scraper` fetching public app reviews. **Public data, gentle volumes, respect the terms of service.**

### `select_dtypes`
Picks columns by type. `include='str'` for text, `include='number'` for numbers. *(The class wrote `include='object'`; it still works but warns on pandas 3.)*

### Series
A single column of a DataFrame — 🔙 a labelled list. Compare **DataFrame**, which is the whole table.

### `SettingWithCopyWarning`
pandas telling you it cannot be sure whether you meant to change a slice or the original table it came from. Fixed by `.copy()`.

### skew (right-skewed)
When one tail of a distribution stretches much further than the other. **Right-skewed** — one tall bar and a long tail to the right — pulls the **mean above the median**. Delays, money, incomes and prices are all skewed.

### SQL
The language for asking a database for data. You describe *what you want*; the database works out how to fetch it. **Narrative only in this lab** — never put credentials or real personal data in a script.

### standard deviation (`std`)
How spread out a column's values are. Small means the values are alike; large means they vary a lot. One of the two ingredients of a z-score.

### `thresh`
In `dropna(axis=1, thresh=N)`, the **minimum number of real values a column must have to survive**. `thresh=0.8 * len(df)` keeps columns that are at least 80% full.

### `to_datetime`
Turns text into real dates. `utc=True` fixes the timezone; `errors='coerce'` writes `NaT` instead of crashing on the unreadable ones.

### `value_counts()`
How many of each value are in a column, biggest first. Add `.sort_index()` for label order instead, or `normalize=True` for shares rather than counts.

### z-score
**How many standard deviations a value sits from the mean.** `(value − mean) / std`. Beyond ±3 is far enough out to be suspicious.

> On badly skewed data the z-score is **weaker** than IQR, because the outliers inflate the very `std` used to define the threshold. **The outliers defend each other.**

---

## The two outlier methods, side by side

| | IQR fence | Z-score |
|---|---|---|
| **Built from** | quartiles (positions) | mean and standard deviation |
| **Formula** | outside `Q1 − 1.5×IQR` … `Q3 + 1.5×IQR` | `abs((x − mean) / std) > 3` |
| **On skewed data** | **robust** — prefer this | flags fewer; inputs corrupted by the outliers |
| **Flagged in this lab** | 46,178 flights | 8,183 flights |

**Both are correct. They ask different questions.**

---

*Apeiron AI Training Academy · M1-W3-Lab01 · "Boundless Possibilities, Infinite Potential"*
