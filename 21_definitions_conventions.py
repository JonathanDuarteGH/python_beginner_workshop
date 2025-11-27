# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# In operator = a  membership operator used to test if a sequence contains a value
#            print("pineapple" _in fruits) ## "_in" is used as an emphasis of "in"

# Typecasting = the process of converting a variable from one data type to another 
#            str(), int(), float(), bool()

# if = Do some code only IF some condition is True
#      Else do something else

# logical operators = evaluate multiple conditions (or, and, not)
#                or = at least one condition must be True
#               and = both conditions must be True
#               not = inverts the condition (not False, not True)

# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

# string method = A function that belongs to a string object
#                 string.method()

# string indexing = Each character in a string has a position (index)
#                   [start : end : step]

# format specifiers = {value:flags) format a value based on what
#                     flags are inserted
##
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

# while loop = execute a block of code as long as some condition is True
# print(shopping list, end = " ")

# for loop = execute a block of code for each item in a collection
#            you can iterate over a range, string, sequence, etc
#            similarly applies to a while loop

# nested loop = a loop inside another loop (outer, inner)
#               outer loop:
#                   inner loop:

# collection = single "variable" used to store multiple values
#     List  = [] ordered and changeable. duplicates OK
#     Set   = {} unordered and unchangeable, but Add/Remove OK. NO duplicates
#     Tuple = () ordered and unchangeable. duplicates OK. FASTER
##
# dir() = list all methods and attributes of an object
# help() = display the documentation of an object or method

# dictionary = {key: value} ordered, changeable, indexed. NO duplicates

# random module = generate pseudo-random numbers

# function = block of code which only runs when it is called
#            can pass data, known as parameters, into a function   
#            can use "return" statement as well

# default arguments = value assigned to a parameter if no argument is provided
#                     make your functions more flexable, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

#    *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#            * unpacking operator
#            1. positional, 2. default, 3. keyword, 4. ARBITRARY
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1, 2, 3, 4, 5)) # Output: 15

# Iterables = objects that can be looped over (string, list, set, tuple, dictionary)

# Membership operator = test if a value or variable is in a sequence (in, not in)
#                       applies to string, list , tuple, set, or dictionary

# List comprehension = concise way to create lists
#                      Compact and easier to read than traditional loops
#                      [expression for item/value in iterable if condition == True]
# doubles = [x * 2 for x in range(1, 6) if x % 2 == 0]
# print(doubles)  # Output: [4, 8]

# Match-case statement = Simplified way to handle multiple conditions
#                        Similar to switch-case in other languages
#                        Use 'case _' as a default case

# Module = A file containing Python code (functions, variables, classes)
#          Can be imported and used in other Python files
#          Use 'import module_name' to import a module (OR your own)

# variable scope = The region where a variable is defined and accessible
#                  Local scope = inside a function
#                  Global scope = outside all functions
#                  Use 'global' keyword to modify a global variable inside a function
#                  LEGB rule = Local, Enclosing, Global, Built-in

# if __name__ == "__main__": = Ensures code runs only when the script is executed directly
#                              this script can be imported OR run standalone
#                              Functions and classes in this module can be reused
#                              without executing the main code block
#                              Useful for testing and modular code design
#                              Example: library = Import library for functionality
#                                                 When running llibrary directly, display help page
#                                                 leaves no global variables
# def main():
#     # main code here
# if __name__ == "__main__":
#     main()

# Object-oriented programming (OOP) = programming paradigm based on the concept of "objects"
#                                     objects contain a budle of related attributes (variables) and methods (functions)
#                                     Examples: phone, cup, book
#                                     You need a "class" to create many objects
# Class = blueprint used to design the structure and layout of an object
# class Car:
#     def __init__(self, model, year, color, for_sale):                    # constructor method ## "self" parameter refers to the instance of the object
#         self.model = model                                               # attribute
#         self.year = year                                                 # attribute
#         self.color = color                                               # attribute
#         self.for_sale = for_sale                                         # attribute
#     def drive(self):                                                     # method
#         print(f"You drive the {self.color} {self.model}.")               # f"" - f string, {} - placeholder
#     def stop(self):                                                      # method
#         print(f"You stop the {self.color} {self.model}.")
#     def describe(self):                                                  # method
#         print(f"This car is a {self.year} {self.color} {self.model}.")
#
# car1 = Car("Mustang", 2024, "red", False)   # create an object (instance) of the Car class
# car1.describe()                             # call a method of the object
# car1.drive()                                # call another method of the object
# car1.stop()                                 # call another method of the object
# print(car1)                                 # print the object (prints out hash location/memory address)
# print(car1.model)                           # access an attribute of the object ## access attribute operator = .
# print(car1.year)                            # access another attribute of the object
# print(car1.color)                           # access another attribute of the object
# print(car1.for_sale)                        # access another attribute of the object
#
# car2 = Car("Corvette", 2025, "blue, True)   # create another object (instance) of the Car class
# car2.describe()                             # call a method of the object
# car2.drive()                                # call another method of the object
# car2.stop()                                 # call another method of the object
# print(car2.model)                           # access an attribute of the object
# print(car2.year)                            # access another attribute of the object
# print(car2.color)                           # access another attribute of the object
# print(car2.for_sale)                        # access another attribute of the object
#
# car3 = Car("Charger", 2026, "yellow", True) # create another object (instance) of the Car class
# car3.describe()                             # call a method of the object
# car3.drive()                                # call another method of the object
# car3.stop()                                 # call another method of the object
# print(car3.model)                           # access an attribute of the object
# print(car3.year)                            # access another attribute of the object
# print(car3.color)                           # access another attribute of the object
# print(car3.for_sale)                        # access another attribute of the object
#
# CREATE A NEW PYTHON FILE CALLED car.py (the code above is a main.py file)
# TAKE THE Car CLASS AND PUT IT IN car.py
# THEN FROM car IMPORT THE Car MODULE IN main.py

# Class variables = variables that are shared among all instances of a class
#                   defined within the class but outside the constructor method
#                   allows you to share data among all objects created from that class
#                   Good practice to access class variables by the class name itself and not any one instance of this class
# class Student:
#     class_year = 2026             # class variable
#     num_students = 0              # another class variable (if we are going to modify it then we can use it inside the constructor)
#
# def __init__(self, name, age):    # constructor method (will always run when we instantiate an object)
#     self.name = name              # attribute             ## "self" parameter refers to the instance of the object
#     self.age = age                # attribute             ## "self" parameter refers to the instance of the object
#     Student.num_students += 1     # increment class variable
#
# student1 = Student("Alice", 20)   # create an object (instance) of the Student class
# student2 = Student("Bob", 22)     # create another object (instance) of the Student class
# student3 = Student("Charlie", 19) # create another object (instance) of the Student class
# student4 = Student("Diana", 21)   # create another object (instance) of the Student class
#
# print(f"My graduating class is {Student.class_year} has {Student.num_students} students")  # access class variables
# print(f"{student1.name}, {student2.name}, {student3.name} and {student4.name}")"

# Inheritance = allows a class to inherit the attributes and methods of another class
#               promotes code reusability and extensibility
#               class Child(Parent)
# class Animal:                           # parent class (base class)
#     def __init__(self, name):           # constructor method
#         self.name = name                # attribute ## "self" parameter refers to the instance of the object
#         self.is_alive = True            # attribute ## "self" parameter refers to the instance of the object
#
#     def eat(self):                      # method
#         print(f"{self.name} is eating.")
#
#     def sleep(self):                    # method
#         print(f"{self.name} is sleeping.")
#
# class Dog(Animal):                      # child class (derived class)
#    #pass                                # no additional attributes or methods
#    def bark(self):
#        print(f"{self.name} says Woof!")
#
# class Cat(Animal):                      # another child class (derived class)
#     def meow(self):                     # additional method
#         print(f"{self.name} says Meow!")
#
# class Mouse(Animal):                    # another child class (derived class)
#     def squeak(self):                   # additional method
#         print(f"{self.name} says Squeak!")
#
# dog = Dog("Buddy")                    # create an object (instance) of the Dog class
# cat = Cat("Whiskers")                 # create an object (instance) of the Cat class
# mouse = Mouse("Squeaky")              # create an object (instance) of the Mouse class
#
# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()
#
# print(cat.name)
# print(cat.is_alive)
# cat.eat()
# cat.sleep()

# multiple inheritance   = a class can inherit from more than one parent class
#                          class Child(Parent1, Parent2) OR C(A, B)
# multilevel inheritance = a class can inherit from a child class, creating a hierarchy
#                          class Grandchild(Child) OR C(B) <- C(A) <- C
#
# class Animal:                            # Grandparent Class
#     def __init__(self, name):            # contructor method
#         self.name = name                 # attribute ## "self" parameter refers to the instance of the object
#
#     def eat(self):                       # method
#         print(f"{self.name} is eating.")
#
#     def sleep(self):                     # method
#         print(f"{self.name} is sleeping.")
#
# class Prey(Animal):                      # Parent Classes
#     def flee(self):
#         print(f"{self.name} is fleeing.")
#
# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting.")
#
# class Rabbit(Prey):                      # Children Classes
#     pass                                 # no additional attributes or methods
#
# class Hawk(Predator):
#     pass                                 # no additional attributes or methods
#
# class Fish(Prey, Predator):              ## Multiple Inheritance
#     pass                                 # no additional attributes or methods                      
#
# rabbit = Rabbit("Bugs")                  # create an object (instance) of the Rabbit class
# hawk = Hawk("Tony")                      # create an object (instance) of the Hawk class
# fish = Fish("Nemo")                      # create an object (instance) of the Fish class
# 
# rabbit.flee()
# hawk.hunt()
# fish.flee()
#
# rabbit.eat()
# hawk.sleep()
# fish.eat()

# super() = function used in a child class to call methods and attributes from a parent class (super class)
#           useful when overriding methods in a child class
#           allows you to extend the functionality of the inherited methods
# 
# class Shape:                                                        # parent class
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
#
#     def describe(self):
#         print(f"This shape is {self.color} and {'filled' if self.is_filled else 'not filled'}.")  # ternary operator
#
# class Circle(Shape):                                                                        # child class
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)                                                  # call parent constructor
#         self.radius = radius
#     
#     def describe(self):
#         super().describe()                                                                  # call parent method
#         print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")     # override parent method
#
# class Square(Shape):                                                                        # child class
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)                                                  # call parent constructor
#         self.width = width
#
#     def describe(self):
#         super().describe()                                                                  # call parent method
#         print(f"It is a square with an area of {self.width * self.width}cm^2")              # override parent method
#
# class Triangle(Shape):                                                                      # child class
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)                                                  # call parent constructor
#         self.width = width
#         self.height = height
#
#     def describe(self):
#         super().describe()                                                                  # call parent method
#         print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")              # override parent method
#
# circle = Circle(color="red", is_filled=True, radius=5)                                      # create an object (instance) of the Circle class
# square = Square(color="blue", is_filled=False, width=6)                                     # create an object (instance) of the Circle class
# triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)                      # create an object (instance) of the Circle class
# 
# print(circle.color)                                                                         # access inherited attribute
# print(circle.is_filled)                                                                     # access inherited attribute
# print(f"{circle.radius}cm")                                                                 # access child attribute
#
# print(square.color)                                                                         # access inherited attribute
# print(square.is_filled)                                                                     # access inherited attribute
# print(f"{square.width}cm")                                                                  # access child attribute
#
# print(triangle.color)                                                                       # access inherited attribute
# print(triangle.is_filled)                                                                   # access inherited attribute
# print(f"{triangle.width}cm")                                                                # access child attribute
# print(f"{triangle.height}cm")                                                               # access child attribute
#
# cirlce.describe()                                                                           # call inherited method
# square.describe()                                                                           # call inherited method
# triangle.describe()                                                                         # call inherited method

# Polymorphism = the ability of different classes to be treated as instances of the same class through a common interface
#                 typically achieved through inheritance
#                 allows methods to do different things based on the object it is acting upon
#                 TWO WAYS TO ACHIEVE POLYMORPHISM: "INHERITANCE" AND "DUCK TYPING"
#                 1. Inheritance = method overriding in child classes. An object could be treated of the same type as a parent class
#                 2. Duck Typing = different classes have methods with the same name. Objects must have necessry attributes/methods
# 
# from abc import ABC, abstractmethod         # abstract base class
#
# class Shape:
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius **2
#
# class Square(Shape):
#     def __init__(self, width):
#         self.width = width
#
#     def area(self):
#         return self.width * self.width
#
# class Triangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height / 2
#
# class Pizza(Circle):                                                     # Duck Typing example
#     def __init__(self, topping, radius):
#         super().__init__(radius)
#         self.topping = topping
#
# shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]  # list of different shape objects
#
# for shape in shapes:
#     print(f"The area is: {shape.area()}cm²")                             # polymorphic behavior

# "Duck Typing" = Another way to achieve polymorphism besides inheritance
#                 different classes have methods with the same name
#                 objects must have necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it's a duck"
# 
# class Animal:
#     alive = True
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof!")
#
# class Cat(Animal):
#     def speak(self):
#         print("Meow!")
#
# class Car:
#     alive = False                                       # Car class does not inherit from Animal. Change to ture to demonstrate attribute access
#     def speak(self):                                    
#         print("Beep!")
#
# animals = [Dog(), Cat(), Car()]                         # list of different animal objects
#
# for animal in animals:
#     animal.speak()                                      # polymorphic behavior
#     print(animal.alive)                                 # access inherited attribute. # Note: Car class does not have speak() method, will raise AttributeError

# Staic modules = A method that belong to a class rather than any object from that class (instance)
#                 does not require an instance of the class to be called
#                 usually used for general utility functions
#
# Instance method = a method that belongs t o the class itself rather than any object from that class
#
# class Employee:
#
#     def __init__(self, name, position):    # constructor method
#         self.name = name                   # attribute ## "self" parameter refers to the instance of the object
#         self.position = position           # attribute ## "self" parameter refers to the instance of the object
#
#     def get_info(self):                    # instance method
#         return f"{self.name} = {self.position}."
#
#     @staticmethod
#     def is_valid_position(position):       # static method. belongs ot the class itself not any instance of the class
#         valid_positions = ["Manager", "Developer", "Designer", "Intern"]
#         return position in valid_positions # membership operator. checks whether position is in valid_positions list
#
# emp1 = Employee("Alice", "Manager")        # create an object (instance) of the Employee class
# emp2 = Employee("Bob", "Developer")        # create another object (instance) of the Employee class
# emp3 = Employee("Charlie", "Chef")         # create another object (instance) of the Employee class
#
# print(Employee.is_valid_position("Developer"))     # call static method without creating an instance
# print(emp1.get_info())                             # call instance method
# print(emp2.get_info())                             # call instance method
# print(emp3.get_info())                             # call instance method

# Class Methods = A method that belongs to the class itself rather than any object from that class
#                 Take (self) as first parameter, which refers to the class itself
#                 usually used for factory methods that create instances of the class
# 
# class Student:
#     count = 0
#     total_gpa = 0.0
#
#     def __init__(self, name, gpa):                      # constructor method
#         self.name = name                                # attribute ## "self" parameter refers to the instance of the object
#         self.gpa = gpa                                  # attribute ## "self" parameter refers to the instance of the object
#         Student.count += 1                              # increment class variable
#         Student.total_gpa += gpa                        # accumulate total GPA
#
#     #INSTANCE METHOD
#     def get_info(self):                                 # instance method
#         return f"{self.name} has a GPA of {self.gpa}."
#
#     #CLASS METHOD
#     @classmethod
#     def get_count(cls):                                 # class method
#         return f"There are {cls.count} students."       # access class variable via cls parameter
#
#     @classmethod
#     def get_average_gpa(cls):                           # class method
#         if cls.count == 0:
#             return 0
#         else:
#             return f"Average GPA: {cls.total_gpa / cls.count:.2f}"       # calculate average GPA
#
# student1 = Student("Alice", 3.8)                        # create an object (instance) of the Student class
# student2 = Student("Bob", 3.5)                          # create another object (instance) of the Student class
# student3 = Student("Charlie", 3.9)                      # create another object (instance) of the Student class
#
# print(Student.get_count())                              # call class method without creating an instance
# print(Student.get_average_gpa())                        # call class method without creating an instance

# Magin Methods = special methods that start and end with double underscores. also known as dunder methods (double underscore methods)
#                 allow you to define how objects of a class behave with built-in operations
#                 __init__, __str__, __add__, __len__, etc.
#
# class Book:
#     def __init__(self, title, author, num_pages):                   # constructor method
#         self.title = title                                          # attribute ## "self" parameter refers to the instance of the object
#         self.author = author                                        # attribute ## "self" parameter refers to the instance of the object
#         self.num_pages = num_pages                                  # attribute ## "self" parameter refers to the instance of the object
#
#     def __str__(self):                                              # string representation method
#         return f"'{self.title}' by {self.author}, {self.num_pages} pages."
#
#     def __eq__(self, other):                                        # equality method
#         return self.title == other.title and self.author == other.author and self.num_pages == other.num_pages
#
#     def __lt__(self, other):                                        # less than method
#         return self.num_pages < other.num_pages
#
#     def __gt__(self, other):                                        # greater than method
#         return self.num_pages > other.num_pages
#
#     def __add__(self, other):                                       # addition method
#         return f"{self.num_pages + other.num_pages} pages"
#
#     def __contains__(self, keyword):                                   # membership method
#         return keyword in self.title or keyword in self.author
#
#     def __getitem__(self, key):                                     # indexing method
#         if key == 'title':
#             return self.title
#         elif key == 'author':
#             return self.author
#         elif key == 'num_pages':
#             return self.num_pages
#         else:
#             return f"{key} is not a valid key. Use 'title', 'author', or 'num_pages'."
#
# book1 = Book("The Hobbit", "J.R.R. Tolhien", 310)                           # create an object (instance) of the Book class
# book2 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 223)  # create another object (instance) of the Book class
# book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 208)     # create another object (instance) of the Book class
#
# print(book1)                                                        # default string representation (memory address)
# print(book1 == book2)                                               # comparison using default behavior (memory address)
# print(book2 < book3)                                                # comparison using default behavior (memory address)
# print(book2 + book3)                                                # addition using default behavior (memory address)
# print("Lion" in book3)                                               # membership test using default behavior (memory address) / True
# print("Lion" in book2)                                               # membership test using default behavior (memory address) / False
# print(book1['title'])                                               # TypeError: 'Book' object is not subscriptable
# print(book2['author'])                                              # TypeError: 'Book' object is not subscriptable
# print(book3['num_pages'])                                          # TypeError: 'Book' object is not subscriptable

# @property = decorator that allows you to define methods in a class that can be accessed like attributes
#             used to encapsulate private attributes and provide controlled access to them
#             Benefit: add additional logic when getting or setting a value without changing the class interface
#             Gives you getter, setter, and deleter methods
# 
#  class Rectangle:
#     def __init__(self, width, height):                     # constructor method
#         self._width = width                                # private attribute ## "self" parameter refers to the
#         self._height = height                              # private attribute ## "self" parameter refers to the instance of the object
#
#     @property
#     def width(self):                                       # getter method
#         return f"{self._width:.1f}cm"
#
#     @property
#     def height(self):                                      # getter method
#         return f"{self._height:.1f}cm"
#
#     @width.setter
#     def width(self, new_width):                            # setter method
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be positive.")
#
#     @height.setter
#     def width(self, new_height):                           # setter method
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height must be positive.")
#
#     @width.deleter
#     def width(self):                                       # deleter method
#         del self._width
#         print("Width deleted.")
#
#     @height.deleter
#     def height(self):                                      # deleter method
#         del self._height
#         print("Height deleted.")
#
# rectangle = Rectangle(10, 5)                               # create an object (instance) of the Rectangle class
#
# rectangle.width = 5                                        # set width using setter method
# rectangle.height = 12                                      # set height using setter method
#
# del rectangle.width                                        # delete width using deleter method
# del rectangle.height                                       # delete height using deleter method
#
# print(rectangle.width)                                     # get width using getter method
# print(rectangle.height)                                    # get height using getter method

# Decorators = functions that modify the behavior of other functions or methods
#              w/o modifying the base function
#              Pass the base function as an argument to the decorator function
#
# def add_sprinkles(func):                                    # decorator function
#     def wrapper(*args, **kwargs):                           # inner function (wrapper)
#         print("Adding sprinkles...🍬")                     # additional behavior
#         func(*args, **kwargs)
#     return wrapper
#
# def add_fudge(func):                                        # another decorator function
#     def wrapper(*args, **kwargs):                           # inner function (wrapper)
#         print("Adding fudge...🍫")                         # additional behavior
#         func(*args, **kwargs)
#     return wrapper
#
# @add_sprinkles                                              # apply decorator to the base function
# @add_fudge                                                  # apply another decorator to the base function
# def get_ice_cream(flavor):
#      print(f"Here is your {flavor} ice cream! 🍦")
#
# get_ice_cream("vanilla")                                    # call the base function
# get_ice_cream("chocolate")                                  # call the base function

# Exceptions = events that occur during the execution of a program that disrupt the normal flow of instructions
#              (ZeroDivisionError, FileNotFoundError, ValueError, TypeError, etc.) more specific errors in Python documentation
#              1. try, 2. except, 3. finally
#
# try:                                                      # try block
#     number = int(input("Enter a number: "))
#     print(1 / number)  # may cause ZeroDivisionError if number is 0
# except ZeroDivisionError:                                 # except block for ZeroDivisionError
#     print("Error: Cannot divide by zero.")
# except ValueError:                                        # except block for ValueError
#     print("Error: Invalid input. Please enter a valid number.")
# except Exception:                                         # generic except block for any other exceptions
#     print("An unexpected error occurred.")
# finally:                                                  # finally block
#     print("Do some cleanup here.")                        # always executes regardless of exceptions

# Python file detection
# 
# import os
# # WITHIN THE PROJECT FOLDER, CREATE A NEW FILE CALLED test.txt
# # WITHIN THE test.txt FILE, ADD THE TEXT: "I like pizza." THEN CLOSE THE FILE
#
# file_path = "test.txt"                                    # relative file path 
# #file_path = "C:\\Users\\HP\\Desktop\\text.txt"           # absolute file path
# if os.path.exists(file_path):                             # check if file exists
#     print(f"The location {file_path} exists")
#
#     if os.path.isfile(file_path):                         # check if it's a file
#         print(f"It is a file.")
#     elif os.path.isdir(file_path):                        # check if it's a directory
#         print(f"It is a directory.")
#
# else:
#     print(f"The location does not exist")

# Python writing files (.txt, .json, .csv)
#
# import json
# import csv
# 
# txt_data = "I like pizza!"
#
# file_path = "C:\\Users\\HP\\Desktop\\text.txt"                         # absolute file path
#
# try:
#     with open(file_path, 'w') as file:                                  # open file in write mode ## If mode = x and the file already exists, it will raise a FileExistsError
#         for employee in employees_list:
#             file.write("txt_data")                                      # write data to file      ## If mode = a and the file already exists, it will append data to the end of the file. Inside paraentheses, write "\n" + txt_data
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print(f"Error: The file '{file_path}' already exists.")
#
##
# employees_list = ["Alice", Bob", "Charlie", "Diana"]
#
# file_path = "C:\\Users\\HP\\Desktop\\text.txt"                          # absolute file path
#
# try:
#     with open(file_path, mode='w') as file:                             # open file in write mode ## If mode = x and the file already exists, it will raise a FileExistsError
#         for employee in employees:
#             file.write(employee + " ")                                  # write data to file      ## If mode = a and the file already exists, it will append data to the end of the file
#         json.dump(employees_dictionary, file, indent=4)                 # write JSON data to file
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print(f"Error: The file '{file_path}' already exists.")
#
# employees= {"name": "Alice", 
#                     "age": 20, 
#                     "job": "Developer"}
# 
# file_path = "C:\\Users\\HP\\Desktop\\output.json"                       # absolute file path
#
# try:
#     with open(file_path, mode='w') as file:                             # open file in write mode ## If mode = x and the file already exists, it will raise a FileExistsError
#         for employee in employees_list:
#             file.write(employee + " ")                                  # write data to file      ## If mode = a and the file already exists, it will append data to the end of the file
#         json.dump(employee, file, indent=4)                             # write JSON data to file
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print(f"Error: The file '{file_path}' already exists.")
#
##
# employees = [["Name", "Age", "Job"], 
#                       ["Alice", 20, "Developer"], 
#                       ["Bob", 22, "Designer"], 
#                       ["Charlie", 19, "Intern"], 
#                       ["Diana", 21, "Manager"]]
# 
# file_path_csv = "C:\\Users\\HP\\Desktop\\output.csv"                     # absolute file path for csv
#
# try:
#     with open(file_path, 'w', newline="") as file:            # open file in write mode ## If mode = x and the file already exists, it will raise a FileExistsError
#         writer = csv.writer(file)                                       # create a CSV writer object
#         for row in employees_list_csv:
#             writer.writerow(row)                                        # write CSV data to file
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print(f"Error: The file '{file_path}' already exists.")

# Python reading files (.txt, .json, .csv)
#
# import json
# import csv
#
# file_path = "C:\\Users\\HP\\Desktop\\input.txt"                              # absolute file path
#
# try:
#     with open(file=file_path, mode='r') as file:                             # open file in read mode
#         content = file.read()                                                # read the entire file
#         print(content)                                                       # print the content of the file 
# except FileNotFoundError:
#     print(f"Error: The file '{file_path}' was not found.")
# expect PermissionError:
#     print(f"Error: You do not have permission to read the file '{file_path}'.")
#
# file_path = "C:\\Users\\HP\\Desktop\\input.json"                             # absolute file path
# 
# try:
#     with open(file=file_path, mode='r') as file:                             # open file in read mode
#         content = json.load(file)                                            # read the entire file
#         print(content["name"])                                               # print the content of the file 
# except FileNotFoundError:
#     print(f"Error: The file '{file_path}' was not found.")
# expect PermissionError:
#     print(f"Error: You do not have permission to read the file '{file_path}'.")
#
# file_path = "C:\\Users\\HP\\Desktop\\input.csv"                              # absolute file path
# 
# try:
#     with open(file=file_path, mode='r') as file:                             # open file in read mode
#         content = csv.reader(file)                                           # read the entire file
#         for line in content:
#             print(line)                                                      # print the content of the file 
# except FileNotFoundError:
#     print(f"Error: The file '{file_path}' was not found.")
# expect PermissionError:
#     print(f"Error: You do not have permission to read the file '{file_path}'.")

# Dates and Times in Python
#
# import datetime