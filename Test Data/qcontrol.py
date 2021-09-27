import pandas as pd
import sys

#Prints a welcome message to the user
print("Welcome to the Quality Index assesment") , sys.argv[0]

#Imports the csv_file in a readable way
csv_file = pd.read_csv(testdata1.csv)
df = pd.DataFrame(csv_file)

# Creates a series from the CSV test data displaying the first column
#s = df["Insulin"]
se = pd.Series(df)

#Prints out the column data
se

#Appends the content of the test file to a "Results" file

dr = pd.DataFrame(results)

dr["New Data"] = csv_file

#Calculates the quality index of the experiment

df["Insulin"].describe()
quality = min(csv_file/max(csv_file))

print (min(csv_file))
print (max(csv_file))

def qresult(quality):
    if quality > 3:
        print ("Good job!")
    else:
        print ("Try again :(")

print ("The quality index is" , quality , qresult )

#Finally, we plot the data

import matplotlib.pyplot as plt

fig, axs = plt.subplots( figsize=(16, 5))
df.plot (ax=axs)
axs.set_ylabel("Insulin in ng/min")
fig.savefig("Insulin secretion.png")
