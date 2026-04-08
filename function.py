#multiple parameters and arguments

# def name(fname,lname):
#     print(fname + " " +lname)

# name("jk" , "karan")

# Default parameter values


# def greet (name, greeting = "Hello"):
#     print(greeting + " " + name)
# greet("Alice")
# greet ("Bob" , "Hi")





# def newFunction (name, animal ):
#     print(" I have a , " ,animal)
#     print("My" + animal + " name is " + name)

# newFunction ( animal ="dog" , name = "Buddy ")

#passing different data types to a function
# def myFunction (fruits):
#     for fruit in fruits:
#         print(fruit)

# myfruits = ["apple" , "banana", "cherry"]
# myFunction(myfruits)



# Function can pass values using the eturn statement


# def add (a,b):
#     return a + b
# result = add (5, 10)
# print(result)

# def myfunction(a,b):
#     print(a+b)

# def myfunction3(a,b):
#     return a+b

# x = myfunction(56,21)
# print(x)
# x

# y = myfunction3(56,26)
# print(y)
# y

# ==================================Deffrence between print and retrun==================

# def addTwoNumber(a,b):
#     result = a + b

# # addTwoNumber(5,10)
#     print(result)

# x = addTwoNumber(5,10)
# print(x)


# # arge and Kwarge
# def myFunction(*alphabets):
#     print("The first alphabet is " + alphabets)
# myFunction("A","Bhavishaya","C","D")


# def greetFunction(*name):
#     for name in name :
#         print("Hello",name)

# greetFunction("Ram", "Manu", "Simran", "Mennu")


# def myfunction(*numbers):
#     totat = 0
#     for number in numbers:
#         totat += number
#     return totat

# print(myfunction(1,2,3,4,5))
# print(myfunction(10,20,30))
# print(myfunction(5))


# def findMax(*numbers):
#     if len(numbers) ==0:
#         return None
#     maximum_number = numbers[0]
#     for num in numbers:
#         if num > maximum_number:
#             maximum_number = num

#     return maximum_number
# print(findMax(1,5,6,34,2))


# def myFunction(**member):
#     print("His first name is " + member["fname"] + " and last name " + member["lname"])

# myFunction(fname = "John", lname = "Doe")
# myFunction(fname = "Manu", lname = "Sharma")


# def myAnotherFunction(title, *args,**kwargs):
#     print("Title:"+ title)
#     print("Argument:", args)
#     print("Keyword Argument: ", kwargs)

# myAnotherFunction("My Function ", 1,2,3, name = "Alice", age = 30)

# birth_year = int(input("Enter your year:"))

# def ageFunction(birth_year):

#     total = 2026 - birth_year

#     print("Your age is:", total)
#     return total
# ageFunction(birth_year)


# def myfunc(n):
#     return lambda a : a*n

# myvalue = myfunc(3)
# mytripler = myfunc(5)

# print(myvalue(12))
# print(mytripler(23))


# Itreate

# mylist = [1,2,3,4,5]
# double = map(lambda x : x*2, mylist)
# print(list(double))

# mylist = [1,2,3,4,5,6,7,8,9,10 ]
# even_number = filter(lambda x : x%2 == 0, mylist)
# print(list(even_number))
