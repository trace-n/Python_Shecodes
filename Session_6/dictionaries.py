import csv

#-----------------------
# Dictionaries - Exercise 1
#-----------------------

groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Coffee": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
    }

total_cost = 0

# for key, value in groceries.items():
#     qty = int(input(f"Please enter qty for {key}:"))
#     total_cost += qty * value

# print(f"Total cost: ${total_cost}")

#-----------------------
# Dictionaries - Exercise 2
#-----------------------
colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
    "brown": 0,
    "black": 0
    }

# with open("/c/Users/timmi/OneDrive/Documents/she_codes/Python/Python_Shecodes/Session_5/colours_865.csv", mode = "r") as csv_data:
# with open("C:\\Users\\timmi\\OneDrive\\Documents\\she_codes\\Python\\Python_Shecodes\\Session_5\\colours_865.csv", mode = "r") as csv_data:

#     lines = csv.reader(csv_data)
#     # row_count = sum(1 for row in lines)
#     # print(f"total lines: {row_count}")

#     for row in lines:
#         # lower case for string for row to avoid case sensitivity
#         colour_string = row[2].lower()
        
#         for key, value in colour_counts.items():
#             # colour found in row
#             if colour_string.find(key) != -1:
#                 value += 1    
#                 # set the value in the dictionary to updated count
#                 colour_counts[key] = value
#                 # go to next row 
#                 pass   

#     for key, value in colour_counts.items():
#         print(f"{key}: {value}")

#     colour_count_sum = sum(colour_counts.values())
#     print(f"Total count: {colour_count_sum}")

#     csv_data.seek(0)
#     lines = csv.reader(csv_data)
#     row_count = sum(1 for row in lines)
#     print(f"total lines in CSV file: {row_count}")
#     print(f"Lines with no matching colour: {row_count - colour_count_sum}")


#-----------------------
# Dictionaries - Exercise 3
#-----------------------
# with open("C:\\Users\\timmi\\OneDrive\\Documents\\she_codes\\Python\\Python_Shecodes\\Session_5\\data\\colours_20_simple.csv", mode="r") as csv_data:
#     # read file
#     # skip first line
#     next(csv_data)
#     lines = csv.reader(csv_data)
    
#     # create empty dictionary
#     colour_dict = {}

#     # loop and assign values from row to dictionary
#     for row in lines:
#         colour_dict[row[1]] = row[2]
    
#     # print output
#     for keys, values in colour_dict.items():
#         print(f"{keys}: {values}")

 

#-----------------------
# Dictionaries - Exercise 4
#-----------------------
# with open("C:\\Users\\timmi\\OneDrive\\Documents\\she_codes\\Python\\Python_Shecodes\\Session_5\\data\\colours_20_simple.csv", mode="r") as csv_data:
#     # read file
#     # skip first line
#     next(csv_data)
#     lines = csv.reader(csv_data)
    
#     # create empty dictionary
#     colour_dict = {}

#     # loop and assign values from row to dictionary
#     # this time using a list as the value for the dictionary key
#     for row in lines:
#         colour_dict[row[1]] = [row[0], row[2]]
    
#     # print output
#     for keys, values in colour_dict.items():
#         print(f"{keys}: {values}")


#-----------------------
# Dictionaries - Exercise 5
#-----------------------

with open("C:\\Users\\timmi\\OneDrive\\Documents\\she_codes\\Python\\Python_Shecodes\\Session_5\\data\\colours_20_simple.csv", mode="r") as csv_data:
    # read file
    # skip first line
    next(csv_data)
    lines = csv.reader(csv_data)
    
    # create empty dictionary
    colour_dict = {}

    # loop and assign values from row to dictionary
    # this time using a dictionary as the value for the dictionary key
    for row in lines:
        colour_dict[row[1]] = {"RGB": row[0], "English": row[2]}
    
    # print output
    for keys, values in colour_dict.items():
        print(f"{keys}: {values}")