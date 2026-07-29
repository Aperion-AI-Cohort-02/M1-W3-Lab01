# ============================================================
#  PRACTICE p08 -- CAPSTONE: Your Own Competitor Note   (*)
#  The Cozy Bean  |  M1-W3 Lab01
#
#  THIS IS THE ONE TO BE PROUD OF.
#
#  YOUR TASK:
#    Write the note YOU would take into a meeting about branch two.
#    Not a copy of script 13 -- your own five findings, in your
#    own words, with every number computed rather than typed.
#
#      1. Load the reviews from data/.
#      2. Work out FIVE findings. At least three must be numbers
#         you calculated. Ideas, if you want them:
#           - the overall average rating
#           - the 5-star count against the 1-star count
#           - best and worst app by average rating
#           - whether angry reviews are LONGER than happy ones
#             (hint: .str.len() gives you the length of each
#             review, and you already know how to filter and mean)
#           - what share of all reviews are 2 stars or worse
#      3. Print the note.
#      4. Write it to my_competitor_note.txt with open().
#
#  THERE IS NO SINGLE CORRECT OUTPUT. The solution file has my
#  five findings so you can compare approach, not answers. Yours
#  will look different and that is the point.
#
#  YOU ARE DONE WHEN:
#    - the note prints, and reads like something a person wrote
#    - my_competitor_note.txt exists and contains the same text
#    - every number in it came from the data, not from your memory
#    - you would not be embarrassed to show it to Mrs Adeyemi
#
#  HINT: Build a list of lines, then "\n".join(lines) at the end.
#        It is far easier to get right than one enormous string.
#        Week-1 f-strings do all the number formatting:
#          f"{average:.2f}"   two decimal places
#          f"{count}"         a plain whole number
#        And Week-1 file writing does the saving:
#          with open("my_competitor_note.txt", "w",
#                    encoding="utf-8") as f:
#              f.write(report + "\n")
#
#  How to run it: python practice/p08_capstone_competitor_note.py
#                 (run it from inside the M1-W3-Lab01 folder)
# ============================================================

import pandas as pd

reviews_df = pd.read_csv("data/coffee_app_reviews_fallback.csv")

# TODO 1: work out your five findings

# TODO 2: build the note, line by line
lines = []
lines.append("THE COZY BEAN -- WHAT THE BIG CHAINS GET WRONG")
lines.append("=" * 52)
lines.append("")
lines.append("(your five findings go here)")

report = "\n".join(lines)
print(report)

# TODO 3: write the note to my_competitor_note.txt
print()
print("(not saved yet)")
