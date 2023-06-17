import csv


# Dictionary
# Keys are unique in a dictionary
# Values in dictionary can be any data type
# Keys can only be immutable data types - cannot be changed
# Immutable - Strings, integers, floats, booleans


student_phonebook = {
    "Cindy":111,
    "Tracey":123,
    "Pauline":444
}
                    

# # add key/value to dictionary
# student_phonebook["Yara"] = 555          
# print(student_phonebook)

# # change dictionary key value
# student_phonebook["Cindy"] = 555
# print(student_phonebook)

# # delete dictionary key/value
# del student_phonebook["Cindy"]
# print(student_phonebook)

## default key
# for element in student_phonebook:
    # print(element)

# for key in student_phonebook:
#     print(key, student_phonebook[key])

# for key in student_phonebook.keys():
#     print(key)

# for value in student_phonebook.values():
#     print(value)

# # returns tuple eg. ('Cindy', 111)
# for items in student_phonebook.items():
#     print(items)

# # can access the tuple values by assigning two vars to split out the tuple returned
# for key, value in student_phonebook.items():
#     print(key, value)

# direct assignment of multiple variables to multiple values
# pack and unpack values
# a,b,c = [1,2,3]
# print(a)
# print(b)
# print(c)


# temp_dict = {
#     "Mon": 3, 
#     "Tue": 15, 
#     "Wed": 15, 
#     "Thu": 15
#     }

# print(temp_dict)

# only returns the first instance of max
# max_temp = max(temp_dict, key=temp_dict.get)
# print(max_temp)

# to find all the instances of max
# ----------------------------------
# max_keys = [key for key, value in temp_dict.items() if value == max(temp_dict.values())]
# print(max_keys, max(temp_dict.values()))



temp_dict = {
    "Mon": {"Min": 30, "Max": 12}, 
    "Tue": {"Min": 7, "Max": 28},  
    "Wed": {"Min": 8, "Max": 28},  
    "Thu": {"Min": 11, "Max": 25},
    "Fri": {"Min": 7, "Max": 25}    
    }

# print(temp_dict)

# for key, value in temp_dict.items():
#     print(key, value)

# for value in temp_dict.values():
    # print(value["Min"])
    # print(value["Max"])
    # print(min(temp_dict.values("Min")))
    # print(f"{value["Min"]}, {min(temp_dict.values("Min"))})

max_temp = {}
# max_temp = {key: max(value.values()) for key, value in temp_dict.items()}

max_temp = {key: value["Max"] for key, value in temp_dict.items()}
# --------------------------------------------------
# This finds the max temperature 
# get max temp list largest max value
max_temp_value = max([value["Max"] for key, value in temp_dict.items()])
max_temp_keys = [key for key, value in temp_dict.items() if value["Max"] == max_temp_value]
# ---------------------------------------------------
# This finds the max temperature 
# get max temp list largest max value
min_temp_value = min([value["Min"] for key, value in temp_dict.items()])
min_temp_keys = [key for key, value in temp_dict.items() if value["Min"] == min_temp_value]
# ---------------------------------------------------

print(max_temp)
print("max temp valu",max_temp_value)
print("max temp keys", max_temp_keys)
print(max(max_temp.values())) # max temperature

print("min temp valu",min_temp_value)
print("min temp keys", min_temp_keys)

# max keys
max_keys = [key for key, value in max_temp.items() if value == max(max_temp.values())]
print(max_keys)

# max_temp_value = [max(value["Max"].values()) for key, value in temp_dict.items()]
# print(max_temp_value)

min_temp = {key: min(value.values()) for key, value in temp_dict.items()}
print(min_temp)

# max_keys = [key for key, value in temp_dict.items() if value == max(temp_dict.values())]

# list comprehension to extract out the min/max and find the max

# max_keys = [key for key, value in temp_dict.items() if value == max(temp_dict.values())]
# print(max_keys, max(temp_dict.values()))

# max_temp = max(temp_dict, key=temp_dict.get)
# print(max_temp)

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

## with open("/c/Users/timmi/OneDrive/Documents/she_codes/Python/Python_Shecodes/Session_5/colours_865.csv", mode = "r") as csv_data:
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

# with open("C:\\Users\\timmi\\OneDrive\\Documents\\she_codes\\Python\\Python_Shecodes\\Session_5\\data\\colours_20_simple.csv", mode="r") as csv_data:
#     # read file
#     # skip first line
#     next(csv_data)
#     lines = csv.reader(csv_data)
    
#     # create empty dictionary
#     colour_dict = {}

#     # loop and assign values from row to dictionary
#     # this time using a dictionary as the value for the dictionary key
#     for row in lines:
#         colour_dict[row[1]] = {"RGB": row[0], "English": row[2]}
    
#     # print output
#     for keys, values in colour_dict.items():
#         print(f"{keys}: {values}")