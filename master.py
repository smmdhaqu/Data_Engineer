"""
while True:
    user_input = input("Write the 'Stop' to quite the loop : ")
    
    if user_input == "Stop" or "stop":
        print("Stopping the Loop")
        break
    print(f"You entered the: {user_input} word")
    
"""

"""

value = 0

while True:
    value += 1
    if value > 5:
        print ("Breaking the Loop after 5 times iterations")
        
        break
    
    else:
        print("This will not be printed")
        
"""
"""
try:
    number = int(input("Enter the number: "))
    
    result = 10/ number
    
    print (result)
    print(undefined_variable)
    
except ZeroDivisionError:
    print("You can not divided by zero")

except ValueError:
    print("You can not divided by a variable")

except Exception as e:
    print(f"Something unexpected {e}")
    
finally:
    if number == 2:
        
        print(f"The result is {result}")
        
    """
    
"""
value = int (input("Enter the Number: "))

if (value<5):
    print ("Your given number is less than 5 and the number is: ", value)

elif(value ==5):
    print("the givennumber is exactly", value)
else:
    print("Something else", value)
"""

# num = int(input("Enter the number : "))
# print ("num = ",num)
# if num%2==0:
#    if num%3==0:
#       print ("Divisible by 3 and 2")
#    else:
#       print ("divisible by 2 not divisible by 3")
# else:
#    if num%3==0:
#       print ("divisible by 3 not divisible by 2")
#    else:
#       print ("not Divisible by 2 not divisible by 3")
    

# total = 2 + 3 + 4 + 5 + \
#         6 + 7 + 8
# print(total)

# sum = 2 + 3+ 5+ 6 + \
#     7 +9
    

# my_funk= lambda x: (
#     x + 4+ x*8 
#     +10
# )

# print(my_funk(2))

# x = "Shams"
# y = 4.5555
# z = 19
# a = str (10)
# b = int (10.5)
# c = float (10)

# print (type(x))
# print (type(y))
# print (type(z))

# print ("a = ", a)
# print ("b =", b)
# print ("c =", c)

# a = b = c = 10
# print (a, b, c)
# x, y, z = 10, 20, 30
# print(x, y, z)

# a, b, c = 10, 20, "Shams"
# print(a, b, c)
# print(c)

# a, b = 10, 20

# def sum ():
#     sum = a + b
#     return sum
# print(sum ())
# def my_function():
#     x = 10  # Local variable
#     print("Inside the function, x =", x)
    
# my_function()

# x = 20  # Global variable

# def my_function():
#     print("Inside the function, x =", x)  # Accesses the global variable

# my_function()  # Output: Inside the function, x = 20
# print("Outside the function, x =", x)  # Output: Outside the function, x = 20


# x = 10

# def new_func():
#     x = 20
    
#     print("This is the local value of X: ", x)
    
#     print("This is the global value of X: ", globals() ['x'])

# new_func()

# print("This is a global value of X: ", x)

# str= "Shams Raaju Ahmed"

# print(str)

# print(str[1 : 4])

# print(str + " is learning python and SQL")

# my_list = ["Shams", 18, "Don't", "Have"]

# my_list.append("Hello")

# my_list.insert (2, 55)
# my_list.insert (3, "New mwssages")

# print (my_list)

# my_list.remove()
# remov = my_list.remove(18)
# print(remov)
# print(my_list)
# print(len(my_list))

# print(my_list)
# insert_item = my_list.insert(1, "Data")

# remove_item = my_list.remove ('Have')

# pop_items = my_list.pop(2)

# print(pop_items)
# print(my_list)

# del my_list[0]
# add_item = my_list.append("Hello")
# print(my_list)

# nested_tuple = (1, 2, (3, 4), 5)
# print(nested_tuple[2])  # Output: (3, 4) (Access the nested tuple)
# print(nested_tuple[2][1])  # Output: 4 (Access the second element in the nested tuple)


# x = 6

# match x:
#     case 1:
#         print("The value is One")
#     case 2:
#         print("The value is Two")
#     case 5:
#         print("The value is Five")
#     case _:
#         print("The value does not match")

# color = "Red"

# match color:
#     case "Blue" | "Green":
#         print ("It is true")
#     case "Red" | "Pink":
#         print("It is True because of Red")
#     case _:
#         print("Nothing is correct")

# new_list = ["Shams", 18, "Raaju"]

# match new_list:
#     case [x, y, z]:
#         print(f"The statement is correct, which are {x}, {y}, {z}.")
#     case _:
#         print("The statemet is not correct")

# x = int(input("Enter the number"))

# print("Your entered number is x = ", x)

# match x:
#     case 0:
#         print("The number is ", x)
#     case n if n > 0:
#         print("The number is greater than O",x)
#     case n if n < 0:
#         print ("The number is less than  Zero", x)

# numbers = [1, 2, 3, 24, 87, 96]
# for number in numbers:
#     if number % 2 == 0:
#         print(f"{number} is even")

# count = 0
# while count < 5:
#     print (count)
#     count += 1
# word = "Shams"
# for words in word:
#     print(words)
    
# for i in range (3, 24, 1):
#     print(i)

# new_dict = {"Name": "Shams", "Age": 25}
# print (new_dict)
# print (new_dict["Name"])

# def data(name, age):
#     print(f"Hello {name}, you are {age}, now!")

# info = data ("Shams", 25)
# def values(numbers):
#     return min(numbers), max(numbers)

# number_list = values([742, 749, 741, 751, 762, 755, 760])
# print(number_list)

# def even_odd(number):
#     if number%2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# result = int(input("Enter the number: "))
# result_2 = even_odd(result)
# print(f"The given number is {result}, which is a {result_2} number")

# def multiply_by(x):
#     def multiplier(n):
#         return n * x
#     return multiplier

# times_three = multiply_by(3)
# result = times_three(5)
# print(result)  # Output: 15

# def outer_function (x):
#     def inner_function(y):
#         return x +y
#     return inner_function

# outer_value = outer_function(5)

# inner_value = outer_value(6)

# print(inner_value)

# def outer(x, y):
#     def inner (a, b):
#         return a +b 
#     calling_outer = inner(x, y)
#     return calling_outer
# calling_outer = outer (10, 20)

# print(calling_outer)
# def new_func (func):
#     def inner_func():
#         print("This will print first")
#         func()
#         print("This will print second")
#     return inner_func

# @new_func
# def calling_dec():
#     print("Hello Shams")
# calling_dec()

# def decorator_function(func):
#     def wrapper(*args, **kwargs):
#         print("Something before the function is called.")
#         func(*args, **kwargs)  # Calling the original function with arguments
#         print("Something after the function is called.")
        
#     return wrapper

# @decorator_function
# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello("Alice")

# main.py
# import math as m

# result =  m.sqrt(16)
# print(result)
# main.py
# test_script.py
# test_script.py
# print(f"__name__ is: {__name__}")

# def greet():
#     print("Hello from the greet function!")

# if __name__ == "__main__":
#     print("This script is being run directly!")
#     greet()


# print(f"_name_ is  : {__name__}")

# def new ():
#     print ("This will print Third")


# if __name__ == "__main__":
#     print ("This will print second")
#     new()

# print (f"__name__ is : {__name__}")

# def new():
#     print ("This will print two")

# if __name__ == "_main_":
#     print ("This wil number one")
#     new()

# print (f"__name__: {__name__}")

# def info(name):
#     print(f"Hello {name}")

# def addding(x, y):
#     return x + y

# if __name__ == "__main__":
#     print("The program is running .....")
#     info("Shams")
#     result = addding(4, 6)
#     print(f"Adding the numbers are {result}")

# my_str = "Shams Haque"
# print("The original string is :", my_str)
# str_list = list(my_str)
# print("String in the List :", str_list)

# str_list[5:5] = ['u', 'l']
# print(str_list)

# my_str = "".join(str_list)
# print(my_str)

# numbers = [10, 20, 30, 40]
# format_number = f"The first number is : {numbers[0]}, second is {numbers[1]}"
# total = f"The list of numbers are {numbers}"
# # print(format_number)
# # print(total)

# print (f"{format_number}\n {total}")

# #Dictonary:

# information = {"name": "Shams", "age": 25}
# format_info = f"Hello {information["name"]}, you are now {information["age"]}"
# print(format_info)
# print (f"{information}")

# number1 = 4.141592653589793
# formatted_number = f"{number1:.2f}"
# print(formatted_number)
# number = 573257235
# format_number = f"{number:,}"
# print(format_number)


# pi = 3.141592653589793
# formatted_pi = f"{pi:.2f}"
# print(formatted_pi)  # Output: 3.14

# Formatting numbers with commas
# large_number = 1234567
# formatted_number = f"{large_number:,}"
# print(formatted_number)  # Output: 1,234,567

# square_set = {x**2 for x in range (1, 6)}
# print(square_set)

# even_set= {x for x in range(1, 11) if x%2 == 0}
# print(even_set)

# new_set= {i for i in range(1, 21) if i % 2 == 0}
# print ("The even numbers are: ", new_set)
# Creating a single set for both even and odd numbers
# number_set = {f"Even-{i}" if i % 2 == 0 else f"Odd{i}" for i in range(1, 21)}

# # Printing the set
# print("The numbers (even and odd) are:", number_set)

# Creating a set for both even and odd numbers

# number_set = {f"Even-{x}" if x % 2 == 0 else f"Odd-{x}" for x in range (0, 21)}

# sorted_number_set = sorted(number_set, key= lambda x: (x.startswith("Odd"), int(x.split('-')[1])))

# print("The sorted Even and Odd numbers are: ", sorted_number_set)

# numbers_set = {"Python", 18, "Data Engineer", 55}
# for x in numbers_set:
#     print (x) 
# number_as_list= [x for x in numbers_set]
# print(number_as_list)

# import itertools
# my_set = {1, 2, 3, 4, 5, 6}

# combine_set = [set(subset) for subset in itertools.combinations(my_set, 2)]
# print(combine_set)

# is_set = {1, 2}.issubset(my_set)
# print("{1,2} is in the set: ", my_set)
# my_set = {1,2,3}
# print(my_set)
# my_set.update([4])
# print("The set is: ",my_set)
# my_set1 = {1, 2, "Python", 4, "Data", 5}
# my_set2 = {2, "SQL", 3 , "Science", 5}
# my_set1.update(my_set2)
# print(my_set1)

# both_set= my_set1.union(my_set2)
# print(both_set)

# uniq_set= my_set1 | my_set2
# print(uniq_set)
# number_list = [1, 2, 3, 4]
# numbers_set = {x**2 for x in number_list}
# numbers_set2 = [x**2 for x in number_list]
# print("The numbers are: {}, {}, {}".format(number_list, numbers_set, numbers_set2))
# print(numbers_set)
# my_set= {1, 2, 3, 4, "Shams", "Raaju"}
# print(my_set)
# my_set.discard(3)
# print(my_set)
# new_set = my_set.pop()
# print(new_set)
# print("Upadted set is: ", my_set)
# s1 = {1, 2, 3, 4, 5}
# new_set = list (s1)
# my_set = {25, 12, 10, 21, 10, 100}
# s2 = {7, 8, 2, 9, 10, 3}
# print("S1: ", s1, "S2: ", s2)

# s3= s1.intersection(s2)
# s4= s1.symmetric_difference(s2)
# print(s3)
# print(s4)
# for i in s1:
#     print(s1)
# square_s1= {x**2 for x in s1 if x % 2 == 0}
# print(square_s1)
# for index, x in enumerate(new_set):
#     print(new_set)
# my_set = {1, 2, 3, 4, 5, 6}
# #my_list = list(my_set)

# for index, x in enumerate(my_set):
#     print("Index: ", index, "Item->", x)
    
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}

# joining_set= set()

# for x in s1:
#     joining_set.add(x)
# for x in s2:
#     joining_set.add(x)
# print(joining_set)

# s3 = s1.union(s2)
# print(s3)

# numbers = [1, 2, 3, 4, 5]

# numbers.append(6)
# print(numbers)

# numbers.remove(5)
# print(numbers)

# numbers.pop(3)
# print(numbers)
# import array
# arr = array.array("i", [12, 18, 8, 1972])
# print(arr)
# arr = [x** 2 for x in arr]

# print(arr)
    
# print(arr[0])
# print(arr[1])

# numbers = [1, 2, 3, 4]
# for x in numbers:
#     print(x)

# import array
# new_array = array.array("i", [1, 2, 3, 4, 5])

# #new_array = array.array("i", (f*3 for f in new_array))
# for x in new_array:
#     print(x)
# import array as arr
# a = arr.array("i", [10,5,15,4,6,20,9])
# b = arr.array('i')

# for i in range(len(a)-1, -1, -1):
#     b.append(a[i])
    
# print("The original array is: ", a)
# print("The Inverse array is: ", b)

# import array as arr
# Original_array = arr.array("i", [10,5,15,4,6,20,9])

# print("The original array is: ", Original_array)

# array_as_list = Original_array.tolist()

# array_as_list.sort()

# sorted_array = arr.array("i", array_as_list)

# print("The Sorthed array is: ", sorted_array)

# print(sorted_array)

# import array as arr
# Original_array = arr.array("i", [10,5,15,4,6,20,9])

# import array as arr
# a = arr.array('i', [88, 99, 77, 66, 44, 22])
# b = arr.array('i', [12, 17, 18, 11, 13, 10])
# a.extend(b)
# print (a)  

# class Student:
#     roll = ""
#     gpa = ""
    

# shams = Student()
# shams.roll = 1
# shams.gpa = 2.7
# print(f"Hello Shams, your roll number is {shams.roll} and you GPA is {shams.gpa }")

# class Student:
#     def __init__(self, name, roll, gpa):
#         self.name = name
#         self.roll = roll
#         self.gpa = gpa
#         self.display()
    
#     def display(self):
#         print(f"Hello {self.name}, your roll number is {self.roll} and your GPA is {self.gpa}\n")

# # Create student objects with name, roll, and gpa
# shams = Student("Shams", 10, 2.7)

# Raaju = Student("Raaju", 20, 2.8)

# class Car:
#     def __init__(self, model, year, miles):
#         self.model= model
#         self.year= year
#         self.miles= miles
#         self.display()
        
#     def display(self):
#         print(f"The model {self.model} was built in {self.year} and already ran around {self.miles} miles")

# bmw = Car("V77", 2025, 2000)

# marcedes = Car("i37", 2022, 5000)

# class Human:
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#         #print(f"Hello {self.name}, you are {self.age} years old and your height is {self.height}")
#         self.dislay_infor()
    
#     def dislay_infor(self):
#         print(f"Hello {self.name}, you are {self.age} years old and your height is {self.height}")
    
# man = Human("Shams", 25, 5.8)
# women = Human("Hridi", 13, 5)

# class Human():
#     def walk(self):
#         print("Human can walk")
    
    
# class Man(Human):
#     def walk(self):
#         print("So a Man can walk too")
#     def speak(self):
#         print("Man can also speak")

# human = Human()
# man = Man()
# human.walk()
# man.walk()
# man.speak()

# class Human():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f"As a Human your name is {self.name} and you are {self.age} years old.")

# class Man(Human):
#     def __init__(self, name, age, gender):
#         self.name = name 
#         self.gender= gender
#         super().__init__(name, age)
    
#     def info(self):
#         super().info()
#         print(f"You are an {self.gender}")

# class Women(Man):
#     def __init__(self, name, age, gender, weight):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.weight = weight
#         super().__init__(name, age, gender)
        
#     def info(self):
#         super().info()
#         print(f"Your weight is {self.weight}")
        
        
    
# man = Man ("Shams", 25, "Male")
# man.info()
# women = Women("Putul", 21, "Female", 50)
# women.info()

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return Number(self.value + other.value)

#     def display(self):
#         print(self.value)

# num1 = Number(5)
# num2 = Number(10)
# num3 = num1 + num2  # Uses __add__ method
# num3.display()      # 15

# class Human:
#     def walk(self):
#         print("Human can walk")

# class Man(Human):
#     def walk(self):
#         print("Man can walk too")
        
# class Woman(Human):
#     def walk(self):
#         print("Woman can also walk")

# def display(human):
#     human.walk()

# human = Human()
# man = Man()
# woman = Woman()

# display(human)
# display(man)
# display(woman)
# class Number():
#     def __init__(self, numb1):
#         self.numb1 = numb1
    
#     def __add__(self, numb2):
#         return Number (self.numb1 + numb2.numb1)
    
#     def display(self):
#         print(self.numb1)
    
# number1 = Number(20)
# number2 = Number(10)
# number3 = number1 + number2
# number3.display()

from abc import ABC, abstractmethod

class Vichel(ABC):
    @abstractmethod
    
    def start_engine(self):
        pass
class Bus(Vichel):
    def start_engine(self):
        print("Bus uses the Key to start")

class Bike(Vichel):
    def start_engine(self):
        print("Bike can start automatically")

def vichel_start_system(vichel : Vichel):
    vichel.start_engine()

bus = Bus()
bike = Bike()
vichel_start_system(bus)
vichel_start_system(bike)


        