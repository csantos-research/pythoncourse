# Quality Control script

This script takes Insulin secretion data and checks if the experiment was successful. A successful experiment will see a step increase in Insulin secretion over 5 times from basal concentration (i.e. the lowest insulin secretion value).

## Before running

Change the qcontrol.py script to include the right directory of the test data.

## Requirements - Packages needed

1. Pandas
2. Matplotlib.pyplot

More information on the Pandas package is available on https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html
For a full explanation on the Matplotlib.pyplot functions please read https://matplotlib.org/stable/api/pyplot_summary.html#

## How to run
        
    python3 qcontrol.py
    
## What does the script do?

1. The script takes the test data and calculates the quality of the experiment.
2. The script appends the test data to a new file.
3. The script plots the test data results and prints the plot as a png file.
