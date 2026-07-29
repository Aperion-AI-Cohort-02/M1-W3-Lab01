# ☕ M1-W3-Lab01 — Due Diligence: Learning to Interrogate Data

**Aperion AI Training Academy** · *"Boundless Possibilities, Infinite Potential"*

| | |
|---|---|
| **Module** | M1: AI/ML Fundamentals |
| **Week** | Week 3 |
| **Lab** | Lab01 — Due Diligence: Learning to Interrogate Data |
| **Topic** | Data profiling · EDA · missing values · outliers (IQR and z-score) · correlation · where data comes from · web scraping |
| **Duration** | **≈ 1 hour** of lab work, **plus about 20 minutes of one-time setup** |
| **Difficulty** | ⭐⭐⭐ Beginner, level 3 — you speak pandas now |

Week 2 handed you 244 tidy bills. This week you get **336,776 flights** you have never seen, and the job is not to summarise them — it is to *interrogate* them. Where are the gaps? Which numbers are lies? What is a date pretending to be text? Then you go and get data nobody handed you at all, by scraping real app reviews off the Google Play Store.

**Start here → [`M1-W3-Lab01.md`](M1-W3-Lab01.md)** — the full lab, with quizzes and an answer key.

> ⚠️ **This repo is about 30 MB** because of the flights dataset. The clone takes a moment longer than previous weeks. That is expected.

---

## 1. 📥 Get this repo onto your computer

You reached this repo by clicking the **GitHub Classroom link posted in Google Classroom**. That link made **your own private copy** of the lab — the URL has your GitHub username in it. This is the copy you clone.

### 1.1 Where to put it

Week 3 gets its own folder, alongside Weeks 1 and 2:

```text
AperionAI/
└── Module1/
    ├── Week1/
    │   ├── Lab01/
    │   └── Lab02/
    ├── Week2/
    │   ├── Lab01/
    │   └── Lab02/
    └── Week3/
        ├── Lab01/      ← this repo
        └── Lab02/      ← next repo
```

The link from this lab back to Week 2's cheat sheet is written as `../../Week2/Lab02/…`, so it resolves only when your folders look like this. **Keep `AperionAI` out of OneDrive, iCloud Drive, Google Drive and Dropbox** — this lab writes PNG charts, and a syncing folder can lock a file mid-write.

### 1.2 Copy your repo's address

Click the green **`< > Code`** button on this repo's page, select the **HTTPS** tab, and click the 📋 copy icon. You get something like `https://github.com/AperionAI-2026/M1-W3-Lab01-B02-<your-username>.git`. **Use your own address**, not a classmate's.

### 1.3 Clone it into `Week3/Lab01`

**Windows (PowerShell):**

```text
cd ~
mkdir -Force AperionAI\Module1\Week3
cd AperionAI\Module1\Week3
git clone PASTE-YOUR-REPO-URL-HERE Lab01
cd Lab01
```

**Mac / Linux:**

```text
cd ~
mkdir -p AperionAI/Module1/Week3
cd AperionAI/Module1/Week3
git clone PASTE-YOUR-REPO-URL-HERE Lab01
cd Lab01
```

That last word — `Lab01` — names the folder. Leave it off and git uses the repo name instead, which breaks the layout above.

> **No git?** Install from [git-scm.com/downloads](https://git-scm.com/downloads) and reopen your terminal. Or **`< > Code` → Download ZIP**, unzip, rename to `Lab01`.

Then confirm:

```text
pwd
ls
```

`pwd` must end in **`Week3/Lab01`**. `ls` must show `README.md`, `M1-W3-Lab01.md`, `CHEATSHEET.md`, `GLOSSARY.md`, `data`, `charts`, `scripts`, `practice` and `solutions`.

---

## 2. 🔧 Setup — a refresher, and **one** new install

**Already set up from Week 2?** Then it is genuinely two commands.

Open your `Lab01` folder in VS Code (**File → Open Folder…**), open **Terminal → New Terminal**, and run:

```text
py -m pip install google-play-scraper
py scripts/00_check_setup.py
```

On **Mac**, or if `py` is not recognised, use `python3 -m pip install …` and `python3 scripts/…`.

Everything else — pandas, numpy, matplotlib, seaborn, scipy — is already on your machine from Week 2 and has not changed. **`google-play-scraper`** is the only new library: it fetches app listings and reviews from the Google Play Store, and Cluster I is built on it.

**Six ✅ ticks this week, not five.** Any ❌ and the script prints the exact command to fix that one.

### When setup goes wrong

| What you see | What it means | What to do |
|---|---|---|
| `'pip' is not recognized…` | Windows cannot find pip on its own | `py -m pip install google-play-scraper`. Then use `py` for everything. |
| `SSL: CERTIFICATE_VERIFY_FAILED` or it hangs on "Collecting…" | Your network inspects internet traffic | Try home wifi first — that fixes it most of the time. |
| `SSL` errors **and you have PostgreSQL installed** | A stale `CURL_CA_BUNDLE` variable left behind by a PostgreSQL install points pip at the wrong certificate file | In PowerShell, for this terminal only: `$env:CURL_CA_BUNDLE = $null`, then retry. *(This one bit the person who wrote this lab.)* |
| `Successfully installed`, but still `ModuleNotFoundError` | **You have more than one Python** and pip installed into the other one | Use the same prefix for both: `py -m pip install …` then `py scripts/…` |

---

## 3. 📂 What is in this repo

| Path | What it is |
|---|---|
| [`M1-W3-Lab01.md`](M1-W3-Lab01.md) | **The lab.** Ten clusters, quizzes, answer key. |
| [`CHEATSHEET.md`](CHEATSHEET.md) | Every call from this lab on one page. Print it. |
| [`GLOSSARY.md`](GLOSSARY.md) | Plain-English definitions of the new words. |
| `data/` | Both datasets — see below. |
| `charts/` | **Starts almost empty on purpose.** Your PNGs land here. |
| `scripts/` | `00_check_setup.py` plus thirteen numbered scripts. |
| `practice/` | Nine practice problems, including a capstone. **Your code goes here.** |
| `solutions/` | Worked solutions. Have a real go first. |

### The data

| File | What it holds | Size |
|---|---|---|
| `data/flights.csv` | **336,776 flights × 19 columns** — the teaching dataset | ~30 MB |
| `data/coffee_app_reviews_fallback.csv` | **300 real reviews** of three coffee-chain apps, scraped when this lab was built | small |

**Only two STEPs need the internet** (STEP 20 and the 🚀 CoinGecko bonus). Everything else — including all of Clusters I and J — works offline, because the downstream scripts read the shipped file by default.

> ⏳ **A word about patience.** Some charts take **a few seconds** rather than appearing instantly. Nothing is broken — the Week 2 table was 244 rows and this one is 336,776. Drawing a third of a million dots takes a moment. The slowest thing in the lab takes about four seconds.

> 🛋️ **Aim for one sitting of about an hour**, with the setup done beforehand. If you do need to pause, a natural break is after **Cluster E**, and a second after **Cluster G**, before the scraping starts.

---

## 4. 🌐 A note on scraping live data

Cluster I fetches **real reviews from the live Google Play Store**. Two things follow from that, and both are the point rather than a nuisance:

- **Your numbers will not match this document exactly.** Real apps collect new reviews every day. If your average rating differs in the second decimal place, nothing is wrong — you are simply reading a newer world than the one this lab was written in.
- **The scrape can fail**, because networks and public endpoints are like that. Every scraping script is wrapped in `try`/`except` and falls back to `data/coffee_app_reviews_fallback.csv`, so the lab always continues. A fallback is not a failure; it is what production code does.

Scrape politely: the scripts request modest numbers of reviews and you should not raise those limits or loop them.

---

## 5. 💾 Saving your work back to GitHub

From inside `Lab01`, when you finish, or any time you pause:

```text
git add .
git commit -m "Finished the outliers cluster"
git push
```

Your PNG charts in `charts/` get committed too — deliberately. They are evidence of your own work.

---

## 6. 🆘 If something goes wrong

| What you see | What it means | What to do |
|---|---|---|
| `FileNotFoundError: … 'data/flights.csv'` | 🔙 The Week-1 classic — **wrong folder** | `pwd` must end in `Lab01`. `ls` must show `data`. If not: **File → Open Folder** on your `Lab01` folder, then a fresh terminal. |
| **The terminal froze after a chart appeared** | It has not. It is waiting for you to close the chart window — **which may be hiding behind VS Code** | Find it, admire it, close it. **Your PNG was already saved** before the window opened. |
| A chart takes a few seconds | Normal. You are drawing up to 336,776 points | Wait. See the patience note above. |
| The scrape returned nothing | The network or the endpoint refused | Nothing to fix — the script falls back to the shipped reviews file and the lab continues. |
| **Output did not change after an edit** | **The file was never saved.** | Look for the ● dot on the file tab. **Ctrl+S** / **Cmd+S**. Rerun. |

Still stuck after a genuine try? Post in the course channel with **what you ran**, **what you expected**, and **the last line of the error**.

---

*Aperion AI Training Academy · Module 1, Week 3, Lab 01 · Next up: [Lab02 — The Evidence Pack](https://github.com/AperionAI-2026/M1-W3-Lab02-B02)*
