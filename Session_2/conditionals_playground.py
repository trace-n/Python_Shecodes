# Python session 2 - lesson 5

is_raining = False
is_cold = True
is_warm = False
is_dry = True

# print(type(is_raining))
# print(type(is_cold))

just_the_string_true = "True"
# print(type(just_the_string_true))

# print(is_raining or is_warm)
# print(is_raining or is_cold)
# print(is_cold or is_dry)


# print(is_raining and is_warm)
# print(is_raining and is_cold)
# print(is_cold and is_dry)

# print(5 ==3)
# print(5 == "five")
# print(5 == "5")
# print(5 == 2+3)
# print(5 == 5.0)
# print("five" == f"{'fi'}{'ve'}")

# print(5 !=3)
# print(5 != "five")
# print(5 != "5")
# print(5 != 2+3)
# print(5 != 5.0)
# print("five" != f"{'fi'}{'ve'}")

# print(3 < 3)
# print(4 < 3)
# print(3 < 3.0)
# print(3 < 99)
# print(3 < 2+2)
# print(3 < 4.0)

# Lesson 5 Exercises
# Q1 / Q2

# sara_has_helmet = input("Does Sarah have a helmet?")
# rei_has_rope = input("Does Rei have a rope?")

# if sara_has_helmet and rei_has_rope:
#     print(f"Let's send it!")
# elif sara_has_helmet != True and rei_has_rope:
#     print(f"No way, my brains is my moneymaker")
# elif sara_has_helmet and rei_has_rope != True:
#     print(f"Who's unprepared now, Rei??")
# elif sara_has_helmet != True and rei_has_rope != True:
#     print(f"I guess let's just go hiking?")

# Q3

# light_colour = input("Light colour")
# car_detected = input("Is a car driving?")

# if car_detected:
#     if light_colour == "Red":
#         print(f"Flash!")
#     elif light_colour != "Red":
#         print(f"Do nothing!")
# else:    
#     print(f"Do nothing")

# Q4

# height = input("How tall are you in cms? Enough to enjoy the ride?")

# if int(height) >= 120:
#     print(f"Hop on!")
# else: 
#     print(f"Sorry, not today.")

# Q5

# username = input("Enter username:")
# password = input("Enter password:")

# if username == "lucyq":
#     if password == "quartzgleam?1":
#         print(f"Logged in successfully")
#     else:
#         print(f"Access is denied")
# else:
#     print(f"Access denied")    

# Q6

# email = input("Enter email:")

# if email.count('@')  != 0 and email.count('.') != 0:
#         print(f"Email valid")
# else:
#     print(f"Invalid email detected!")        

# Q7 - will print to terminal as string = true if it is not empty

str_false = "False"

if str_false:
    print("A strange game. The only winning move is not to play.")
    print(type("False"))
else:
    print("String was not false")


    