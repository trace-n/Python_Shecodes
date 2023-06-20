# Classes - OOP




class Cow():    
    species_name = "Bos Taurus"    
    diet = "grass"
    
    def speak(self):
       print("MOO!")

bessie = Cow()

print(bessie)
print(f"Bessie the cow eats {bessie.diet}")
print("Say something Bessie!") 
bessie.speak()

# --------------------
# Q1
# --------------------

class She_Codes():

    def __init__(self, name, program, year):
        self.name = name
        self.program = program
        self.year = year

# --------------------
# Q2
# --------------------
    def __str__(self):
        return f"<Student: {self.name}, Program: {self.program}, Year: {self.year}>"


student1 = She_Codes("Olivia", "Plus", 2019)
print(student1) #, type(student1))
# print(student1.name, student1.program, student1.year)


# --------------------
# Q3
# --------------------

class Rectangle():
    
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def __str__(self):
        return (f"<Name: {self.name}, L: {self.width}, H: {self.height}>")

    def area(self):
        # area of rectangle
        return self.width * self.height

    def perimeter(self):
        # perimeter of rectangle
        return (self.width * 2) + (self.height * 2)

    def diagonal(self):
        # length of diagonal
        return ((self.width**2) + (self.height**2)) ** (1/2)

    def square(self):
        # return true if square
        if self.width == self.height:
            return True
        else: 
            return False
        
    def solve(self):
        print("--------------")
        print(self)
        print("Area: ", self.area())
        print("Perimiter: ", self.perimeter())
        print("Diagonal: ", self.diagonal())
        print("Is a square: ", self.square())



rectangle1 = Rectangle("Rectangle 1", 5, 10)
print(type(rectangle1))
# print("is square:", rectangle1.square(), "perimeter:", rectangle1.perimeter(), "area:", rectangle1.area())
rectangle2 = Rectangle("Rectangle 2", 5, 5)
# print("is square:",  rectangle2.square(), "perimeter:", rectangle2.perimeter(), "area:", rectangle2.area())
rectangle3 = Rectangle("Rectangle 3", 3, 4)
# print("diagonal:", rectangle3.diagonal())
rectangle1.solve()
rectangle2.solve()
rectangle3.solve()

# print(rectangle1, rectangle2, rectangle3)