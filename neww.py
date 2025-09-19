# x = 10
# y = 20.5
# z =1j

# #Conversion

# a = float(x)
# b = int(y)
# c = complex(z)


# print(a, b, c)


# import random
# print(random.randrange(1,10))

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def badhuman(self):
#         print(f"{self.name, self.age} is not so friendly")
    
#     def goodhuman(self):
#         print(f"{self.name} is a good person")
        
# human1 = Human("Aline", 55)
# human2 = Human("Aieda", 45)

# human1.badhuman()
# human2.goodhuman()

# class BankAccount:
#     def __init__(self, name, age, balance= 0):
#         self.name = name
#         self.age = age
#         self.balance = balance
        
    
#     def deposit(self, amount):
#         if amount <= 0:
#             print(f"Hello {self.name}, deposit amount must be more than 0")
#             return False, self.balance
#         self.balance += amount #self.balance = self.balance + amount
#         print(f"Hello {self.name}, successfully diposited {amount}")
#         return True, self.balance
    
    
#     def withdraw(self, amount):
#         if amount <=0:
#             print(f"Hello {self.name}, deposit amount must be more than 0")
#             return False, self.balance
#         if amount > self.balance:
#             print(f"Hello {self.name}, you do not have sufficient balance")
#             return False, self.balance
#         self.balance -= amount
#         print(f"Hello {self.name}, successfully withdraw the {amount}")
#         return True, self.balance

# account1 = BankAccount("Shams", 1000)
# account2 = BankAccount("Ahmed", 2000)

# success, new_balance = account1.deposit(500)
# success, new_balance = account1.withdraw(200)

# success, new_balance = account2.deposit(500)
# success, new_balance = account2.withdraw(100)

# #print(f"New balance: {new_balance}")

# print(f"{account1.name} has {account1.balance} Euros")
# print(f"{account2.name} has {account2.balance} Euros")

################################################################
################################################################

# class Human:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} can speak")

# class Man(Human):
#     def speak(self):
#         print(f"Some {self.name} speak so loudly")

# h = Human("Human")
# m = Man("men")

# h.speak()
# m.speak()

#################################################################

# class Vehicle:
#     def __init__(self, brand, wheels):
#         self.brand = brand
#         self.wheels = wheels
    
#     def info(self):
#         print(f"Every {self.brand} has at least {self.wheels} wheel.")


# class Car(Vehicle):
#     def __init__(self, brand, doors):
#         super().__init__(brand, 4)  #super() is used to call the Parent's constructror
#         self.doors = doors
    
#     def info(self):
#         print(f"{self.brand} is car with at least {self.doors} doors.")


# class Bike(Vehicle):
#     def __init__(self, brand, light):
#         super().__init__(brand, 2)
#         self.light = light
    
#     def info(self):
#         print(f"{self.brand} is a bike name with {self.light} lights.")

# v = Vehicle("vehicle", 1)
# c = Car("Marcedes Benz", 4)
# b = Bike("Hero Honda", 2)

# v.info()
# c.info()
# b.info()

###########################################################

# class Animal:
#     def foods(self):
#         print("Every animal needs foods")
    
# class Elephant(Animal):
#     def foods(self):
#         print("Elephants need more foods than others")

# a = Animal()
# e = Elephant()
# e.foods()
############################################################

# class Animal:
#     def foods(self):
#         print("Every animal needs foods")
        
# class Elephant(Animal):
#     def foods(self):
#         super().foods()
#         print("Elephants eat more than any other animals")
        
# e = Elephant()
# e.foods()
#############################################################

# class Father:
#     def work(self):
#         print("Earning Money")


# class Mother:
#     def work(self):
#         print("Cooking Foods at home")
        

# class Child(Father, Mother):
#     def work(self):
#         print("I take money and eat outside")
#         Father.work(self)
#         Mother.work(self)
        
        

# c = Child()
# c.work()


class Base:
    def info(self):
        pass

class Father(Base):
    def info(self):
        print("I am a Doctor")
        super().info()    #super() to call the next method in the MRO chain

class Mother(Base):
    def info(self):
        print("I am a nurse")
        super().info()

class Child(Father, Mother): #Child → Father → Mother → Base → object

    def info(self):
        print("I am a Student")
        super().info()     #Method Resolution Order or MRO.

child = Child()
child.info()
    

        