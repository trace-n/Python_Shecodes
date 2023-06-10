# functions we have covered 
# input(), len(), int(), print() 


# name = input("What is your name?")
# age = input("How old are you?")

# if age >= 18:
#     print("Welcome")
# else:
#     print("You cannot enter!")


# task separation

def ask_user_name():
    name = input("What is your name?")
    return name

def ask_user_age():
    age = input("How old are you?")
    return int(age)

def response(user_name, user_age):
    if user_age >= 18:
        print(f"Welcome {user_name}")
    else:
        print(f"You cannot enter! Your age {answer_age} is too young")

# function - "Definition of a job" - series of steps that we set down as a plan
# inputs -> steps -> output

# 1. define the function
# 2. call the function

# answer_name = ask_user_name()
# answer_age = ask_user_age()
# response(answer_name, answer_age)

# Parameters

def add(number1, number2):
    result = number1 + number2
    return result

# num1 = int(input("enter a number:"))
# num2 = int(input("enter another number:"))
# answer = add(num1,num2)
# print(f"Sum of {num1} + {num2} = {answer}")


# Exercises
# Q1

def get_integer(question):
    return int(input(question))


# prompt = "Could I please have an integer?:"

# call function
# user_input = get_integer(prompt)
##print the result 
# print(f"So your integer is {user_input}? Thanks!")


# Q2

# degrees_f = int(input("Input a temperature in Fahrenheit:"))

# def celcius_convert(degrees_fahrenheit):
#      return (degrees_fahrenheit - 32 ) * 5/9


# print(celcius_convert(degrees_f))

# Q3

# number_check = int(input("Input a number: "))

# def check_even(num):
#     check_number = num % 2
#     if check_number == 0:
#         return False #even
#     else:
#         return True #odd

# result = check_even(number_check)

# print(result)

# if result:
#     print(f"Your number {number_check} is odd")
# else:
#     print(f"Your number {number_check} is even")

# Q4

def total_cost(price, qty):
    return price * qty

unit_price = float(input("Enter a unit price: "))
unit_qty = float(input("Enter a quantity: "))

total = total_cost(unit_price, unit_qty)
print(f"Total cost of {unit_price} * {unit_qty} = ${total}")