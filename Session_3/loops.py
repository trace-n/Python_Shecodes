# Session 3

letters = ['a','b','c']

# print all letter 
# print(letters)

# print(letters one by one)
# print(letters[0])
# print(letters[1])

# ----------------
# loops help execute a task multiple times
# ----------------
# 2 types of loops
# ----------------
# While Loops
# ----------------
# need to set a condition to exit the while loop

# count = 0
# while 5 > count:
#     print(count)
#     count += 1
# --
# name = input("What is your name?")

# while name != 'Ashley':
#     print("I don't know you")
#     name = input("What is your name?")
# --



# ----------------
#  For Loops
# ----------------
# range allows for loop to increment range
# starting number can be ommitted, max range is exclusive
# example below range(0,10) is for the values 0-9

# for loops create the variable for the counter and assign the value of the list based on the index = counter

# letters = ['a','b','c']
# for letter in letters:
#     print(letter)

# list_name[0:9]
# for number in range(0,10):
#     print(number)

# sub list - a list of lists
# students = [
#     ["Cindy","Emily","Eve"],
#     ["Julie","Maddy","Andrea"],
#     ["Jenny","Sarah","Yara"]
#     ]

# for student in students:
#     print(student)
#     for single_student in student:
#         print(single_student)

# if 5 < 3:
#     print("Hello")
# else:
#     if 1 <= 1:
#         print("Hi")
#     if 10 == 10: 
#         print("How are you?")

# How to get tennis ball?
# chilli_wishlist = [
#     ["igloo"],
#     ["donut","tennis ball","other"]
# ]

# print(chilli_wishlist[1][1])


# ----------------
# Q1
# ----------------
# the_number = input("Enter a number:")
# temp_number = 0
# while the_number != "":
#     the_number = int(the_number)
#     temp_number += int(the_number)
#     the_number = input("Enter a number:")


# print(f"Your numbers sum to {temp_number}.")



# ----------------
# Q2
# ----------------
# number = input("Enter a number:")
# for odd_number in range(0,int(number) + 1):
#     if odd_number % 2 != 0:
#         print(odd_number)

# ----------------
# Q3
# ----------------

# number = 12
# print("Guess the random number!")
# random_number = input("Make a guess:")

# while int(random_number) != number:

#     if int(random_number) < number:
#         print("Too low.. ")
#     elif int(random_number) > number:
#         print("Too high")

#     random_number = input("Make a guess:")

# print("You got it right!")

# ----------------
# Q1 - Loops
# ----------------

# number = input("Enter a number:")
# for count in range(0,10):
#     # answer = int(number) * count
#     print(f"{number} * {count+1} = {int(number)*(count+1)}")


# ----------------
# Q1 - Loops
# ----------------

number = input("Enter a number:")
for count in range(1,11):
    # answer = int(number) * count
    print(f"{number} * {count} = {int(number)*(count)}")


# ----------------
# Q2 - Loops
# ----------------
# number = input("Enter a number:")
# sum = 0
# for count in range(0,int(number)+1):
#     sum += count

# print(sum)

# ----------------
# Q3- Loops
# ----------------
# my_numbers = [3,5,9,1]
# my_numbers_a = [-3,-5,9,1]
# my_numbers_empty = []
# sum = 0

# for count in my_numbers_a:
#     sum += count

# print(sum)

# ----------------
# Q4- Loops
# ----------------
# lyrics = [    
#     ["Monica", "in my life"],    
#     ["Erica", "by my side"],    
#     ["Rita's", "all I need"],    
#     ["Tina's", "what I see"],    
#     ["Sandra", "in the sun"],    
#     ["Mary", "having fun"],    
#     ["Jessica", "here I am"]
#     ]

# for count in lyrics:
#     line = "A little bit of"
#     # print(count)
#     for text in count:
#         # print("A little bit of {text}")
#         line += " " + text 

#     print(f"{line};")

# print("A little bit of you makes me your man (ah!)")



# Nested Loops

# iterations = ["first", "second", "third"]
# print("Starting the outer loop!")
# for outer_number in iterations: # outer loop
#     print("Starting the inner loop!") 
    
#     for inner_number in iterations: # inner looppr
#         print(f"The outer loop is on its {outer_number} iteration, while the inner loop is on its {inner_number} iteration.")
              
#     print("Inner loop complete!")
    
# print("Outer loop complete!")


# ----------------
# Q1- Loops Extension
# ----------------

# Groceries = [    
#     ["Baby Spinach", 2.78],    
#     ["Hot Chocolate", 3.70],   
#       ["BBQ Shapes", 9.00],    
#       ["Bread", 2.10],   
#       ["Carrots", 0.56],    
#       ["Oranges", 3.08]
#       ]

# question = "Please enter the quantity for"

# list = []

# # use a list to capture input
# total = 0

# for element in Groceries:
#     # dynamic_variable_name = element[0]
#     qty = input(f"{question} {element[0]}:")
#     # list.append(qty)
#     total += int(qty) * element[1]

# # print(list)
# print(f"Thank you, your total is ${total}.")
 

# ----------------
# Q2 -Extension
# ----------------

# import random

# play = ""

# while play != "no":
#     number = random.randint(1,20) 
#     print(number)
#     print("Guess the random number between 1 - 20!")
#     random_number = input("Make a guess:")

#     while int(random_number) != number:

#         if int(random_number) < number:
#             print("Too low.. ")
#         elif int(random_number) > number:
#             print("Too high")

#         random_number = input("Make a guess:")

#     print("You got it right!")
#     play = input("If you would like to stop playing, type'no'. Otherwise, press enter and we'll play again:")

