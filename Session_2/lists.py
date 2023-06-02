# Lesson 6 - Lists

# Exercises

# Q1

# foods = [
# "orange",
# "apple",
# "banana",
# "strawberry",
# "grape",
# "blueberry",
# ["carrot", "cauliflower", "pumpkin"],
# "passionfruit",
# "mango",
# "kiwifruit"
# ]
# 
# print(foods[0],foods[2],foods[-1])


# Q2

list2 = [
["Monica", "in my life"],
["Erica", "by my side"],
["Rita's", "all I need"],
["Tina's", "what I see"],
["Sandra", "in the sun"],
["Mary", "having fun"],
["Jessica", "here I am"]
]

# print(len(list2))
# print(list2[0][0])

#--------------------------------------
# simplest solution join space with list with no separator 
# for x in list2:
#     print(f'A little bit of ',' '.join(x),';', sep="")

# print(f"A little bit of you, makes me your man (ah!)")
#--------------------------------------
    # print(f"A little bit of ",x[0]," ", x[1],";",sep="" )


    # print(f"A little bit of {x[0:2]};", sep="")
    # print(list2[x])

# print(f"A little bit of",*list2, sep="\n")
# list1 = ["Monica", "in my life"]
# print(' '.join(list2[0]))
# print(list2[0:-1])

# for x in range(len(list2)):
#  print(f'A little bit of ',' '.join(list2[x]),';', sep="")




# Q3

# name1 = input("Enter name 1")
# name2 = input("Enter name 2")
# name3 = input("Enter name 3")

# list = name1, name2, name3
# list = [name1]
# list.append(name2)
# list.append(name3)


# print(list)


# Q4

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []
f = []

# this is ok, but repetitive
d.append(a)
d.append(b)
d.append(c)

# this is better
for x in a, b, c:
    e.append(x)

# this is ok but repetitive
# for x in a:
#     f.append(x)

# for x in b:
#     f.append(x)    

# for x in c:
#     f.append(x)    

# this is better - create function for reuse
# loop and append the list1 items into list2
def my_append_function(list1, list2):
    for x in list1:
        list2.append(x)

my_append_function(a,f)
my_append_function(b,f)
my_append_function(c,f)

# print(' '.join(str(d[0:])))
print(d)
print(e)
print(f)
