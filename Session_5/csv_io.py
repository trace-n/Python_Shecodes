import csv
import os
# fname = "colours_865.csv"
# fname = "data\colours_20_simple.csv"

# bool = os.path.isfile(fname)

# pwd = os.path.isdir('data')
# # print(os.path.curdir)

# print(bool)
# print(pwd)
 

#-----------------------
# CSV I/O - Exercise 1
#-----------------------

# os.path.exists("galaxies.csv")

# with open("data/colours_20_simple.csv", mode="r") as csv_data:

# #     # creating a csv.reader object to grab data
#     reader = csv.reader(csv_data)

# # # loop through rows
#     for line in reader: 
#         # reset string for each line
#         line_string = ""
#         for item in line:
#             line_string += item + " "

#         print(line_string)

#-----------------------
# CSV I/O - Exercise 2
#-----------------------

with open("data/colours_20_simple.csv", mode="r") as csv_data:
    # Skip first line
    next(csv_data)
    reader = csv.reader(csv_data)
    

    for line in reader:
        print(f"{line[2]}, Hex: {line[1]}, RGB: {line[0]}")

#-----------------------
# CSV I/O - Exercise 3
#-----------------------

# create a set for unique colours



#-----------------------
# CSV I/O - Exercise 4
#-----------------------

# create a list of galaxy and velocity using ordered dictionary?