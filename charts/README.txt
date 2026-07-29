This folder is where your charts land.

It ships almost empty on purpose -- every PNG in here is one YOU
made by running a script. Nothing in this folder is shipped with
the lab except this note.

By the end of the walkthrough you should have eight of them:

  dep_delay_histogram.png    STEP 11  -- the shape of lateness
  dep_delay_boxplot.png      STEP 12  -- the box and the outlier cloud
  flights_per_carrier.png    STEP 12  -- flights per airline
  delay_by_hour.png          STEP 16  -- delay climbing through the day
  correlation_small.png      STEP 17  -- four columns, numbers written on
  correlation_full.png       STEP 17  -- every numeric column, as patterns
  distance_vs_delay.png      STEP 18  -- 336,776 dots, and a flat band
  rating_distribution.png    STEP 21  -- the U-shape of app reviews

Plus whatever you make in practice problem p06, and a pairplot if
you do the bonus box in Cluster G.

Two rules for every chart script in this lab:

  1. os.makedirs("charts", exist_ok=True) FIRST -- matplotlib will
     not create this folder for you, and savefig into a folder that
     does not exist raises FileNotFoundError.

  2. plt.savefig(...) BEFORE plt.show() -- on many setups, showing
     a figure clears it, and then you save a blank PNG.

If the terminal seems frozen after a chart appears, it is waiting
for you to close the chart window -- which may be hiding behind
VS Code. Your PNG was already saved before the window opened.
