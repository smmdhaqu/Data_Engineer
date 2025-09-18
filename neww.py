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

class Human:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} can speak")

class Man(Human):
    def speak(self):
        print(f"Some {self.name} speak so loudly")

h = Human("Human")
m = Man("men")

h.speak()
m.speak()