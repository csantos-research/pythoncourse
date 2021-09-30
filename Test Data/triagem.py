import pandas as pd
import sys

#Prints a welcome message to the user
print("Welcome to the Quality Index assesment") , sys.argv[0]

#Imports the csv_file in a readable way
csv_file = pd.read_csv("/home/cake/github/pythoncourse/Test Data/testdata1.csv")
df = pd.DataFrame(csv_file)

# Creates a series from the CSV test data displaying the first column
s = df["Insulin"]
se = pd.Series(s)

#Prints out the column data
print(se)

#Appends the content of the test file to a "Results" file

results_csv = pd.read_csv("/home/cake/github/pythoncourse/Test Data/results.csv")
dr = pd.DataFrame(results_csv)

dr["New Data"] = s

#Calculates the quality index of the experiment

df["Insulin"].describe()

p = df["Insulin"].max()
b = df["Insulin"].min()
quality = p / b

print ("The peak is" , p)
print ("The minimum is" , b)

def qresult(quality):
    if quality > 3:
        print ("Good job!")
    else:
        print ("Try again :(")

print (qresult(quality))
