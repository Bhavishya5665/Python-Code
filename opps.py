# class MyClass :
#     x = 5

# print(MyClass)
# print(MyClass.x)


# class anotherClass:
#     x = 5  # this is an attribute of a class

# p1 = anotherClass() #it is a object.
# print(p1.x)


# class Person:
#     # x , y = "Ayush", 20
#     def __init__(self, name,age):
#         self.age = age
#         self.name = name

#     def myfunc(self):
#         print("Hello my name is " + self.name + " and I am " + str(self.age) + " year old ")

# p1 = Person("Ayush ", 20)
# # del p1
# p1.myfunc()
        

# x = int(input("Enter the Quantity: "))
# # y = str(input("Enter your size: "))
# z = str(input("Enter the Size (Large, Medium, Low):"))

# while z  in  ["Large", "Medium", "Low"]:
#     # print("Invalid size. Please enter a valid size (Large, Medium, Low).")
#     z = str(input("Enter the Size (Large, Medium, Low):"))
    
#     i = i + 
    

    

#     if z == "Large":    
#         print(x*45)

#     elif z == "Medium":
#         print(x*25)

#     elif z== "Low":
#         print(x*15)

#     else:
#         print("Invalid size")



# Larg = 45
# medium = 25
# low = 15
# z = str(input("Enter the Size (Large, Medium, Low):"))
    

# a = int(input("Enter small cup qut: "))
# b = int(input("nter medium cup qut: "))
# c = int(input("nter Larg cup qut: "))


# total = (Larg*a) + (medium*b) + (low*c)

# print(total)

# total = 0

# while True:

#     print("\n----- Tea Menu -----")
#     print("1. Small Tea - ₹15 ")
#     print("2. Medium Tea - ₹30")
#     print("3. Larg Tea - ₹45")


# # Enter the choice of cup

#     choice = input("Enter cup size (small/medium/larg): ").lower()
#     # Enter the quanity of cup
#     qty = int(input("Enter quantity: "))

# #  if else statement

#     if choice == "small":
#         price = 15

#     elif choice == "medium":
#         price = 30

#     elif choice == "larg":
#         price = 45

#     else:
#         print("Invalid choice! Try again")
#         continue

#     amount = price * qty
#     total += amount

#     print("Added ₹", amount, "to total bill.")
#     more = input("Do you want to order more? (yes/no): ").lower()
#     if more != "yes":
#         break
# print("\n-------Final Bill-------")
# print("Total Amount to Pay: ₹", total)
# print("Thank you! visit again")


# class Chai:
#     pass

# class ChaiTime:
#     pass

# print(type(Chai))
# print(type(ChaiTime))


# ginger_tea = Chai()
# p1 = ChaiTime()


# print(type(ginger_tea))

# print(type(ginger_tea) is  Chai)
# print(type(p1) is ChaiTime )


# class Car :
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# car1 = Car("Toyota ", "Camry ", 2020)

# car1.display_info()

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# car1 = Car ("Toyota", "Csmry", 2020)

# print(car1.brand)
# print(car1.model)
# # print(car1.year)

# car1.year = 2021


# print(car1.year)


# # del car1.year
# # print(car1.year)


# car1.colour = "Red"
# print(car1.colour)



# class Person:
#     def __init__(self, name, age, city, country):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.country = country


#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, City: {self.city}, Country: {self.country}"
# p1 = Person("Ayusah", 18 , "Haridwar", "India")

# print(p1)
        



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduc (self):
        print(f"Hello, my name is {self.name} and I am {self.age} year old")

class Ayush(Person):
    pass

x = Ayush("Doreamon", 28)
x.introduc()
        
        

