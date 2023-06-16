import csv
# import os



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

# with open("data/colours_20_simple.csv", mode="r") as csv_data:
#     # Skip first line
#     next(csv_data)
#     reader = csv.reader(csv_data)
    

#     for line in reader:
#         print(f"{line[2]}, Hex: {line[1]}, RGB: {line[0]}")

#-----------------------
# CSV I/O - Exercise 3

# create a set for unique colours?
def colour_count(file_name):

    with open(file_name, mode="r") as csv_data:
    # with open("data/colours_20_simple.csv", mode="r") as csv_data:

        # read all lines
        lines = csv_data.readlines()
        
        # csv_reader = csv.reader(csv_data)

        #  list has count for red, green, blue, yellow
        colour_list = ["red","green","blue","yellow"]
        count_list = [0,0,0,0]
        for row in lines:
            # lower case to compare to avoid case sensitivity
            row = row.lower()

            for i in range(len(colour_list)):
                if row.find(colour_list[i]) != -1:
                    count_list[i] += 1   

        for count in range(len(count_list)):

            print(f"{colour_list[count]}: {count_list[count]}")


print(f"File results: data/colours_20_simple.csv")
colour_count("data/colours_20_simple.csv")

print("-------------------")
print(f"File results: colours_865.csv")
colour_count("colours_865.csv")
print("-------------------")

#-----------------------
# CSV I/O - Exercise 4
#-----------------------

# create a list of galaxy and velocity using ordered dictionary?

with open("galaxies.csv", mode="r") as galaxy_data:
    csv_reader = csv.reader(galaxy_data)

    # print(max([lines[-1] for lines in csv_reader]))
        # print(lines)
        # print(max([lines[-1]]) )
    galaxy_number = []
    galaxy_velocity = []

    for line in csv_reader:
        galaxy_number.append(int(line[0]))
        galaxy_velocity.append(int(line[1]))

    # print(galaxy_velocity)
    # print(galaxy_number)

    min_val = min(galaxy_velocity)
    max_val = max(galaxy_velocity)
    index_min = galaxy_velocity.index(min_val)
    index_max = galaxy_velocity.index(max_val)

    print(f"Galaxy {galaxy_number[index_min]} has the min velocity of {min_val}km/sec.")
    print(f"Galaxy {galaxy_number[index_max]} has the max velocity of {max_val}km/sec.")

