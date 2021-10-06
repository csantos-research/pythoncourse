# Quality Control script

### This script takes Insulin secretion data and checks if the experiment was successful. A successful experiment will see a step increase in Insulin secretion over 5 times from basal concentration (i.e. the lowest insulin secretion value)

## Before running

### Change the qcontrol.py script to include the right directory of the test data

## How to run
        
    pip qcontrol.py
    
## What does the script do?

1. The script takes the test data and calculates the quality of the experiment.
2. The script appends the test data to a new file.
3. The script plots the test data results and prints the plot as a png file.
