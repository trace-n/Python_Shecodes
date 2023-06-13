import csv

#-----------------------
# CSV I/O - Exercise 1
#-----------------------

with open("colours_20_simple.csv", mode="r", encoding="utf-8") as csv_data:

    # creating a csv.reader object to grab data
    reader = csv.reader(csv_data)

# loop through rows
    for line in reader: 
        print(line)

#-----------------------
# CSV I/O - Exercise 2
#-----------------------

#-----------------------
# CSV I/O - Exercise 3
#-----------------------

#-----------------------
# CSV I/O - Exercise 4
#-----------------------