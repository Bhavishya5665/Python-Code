# Declare a set  using curly braces
# myset = {1, 2, 3, 4, 5}
# print(myset)


# set can not declare duplicate values it will automatically remove the duplicate values
# myset = {"apple", "banana", "cherry", "apple"}
# print(myset)

# true and 1 are considered the same value in a set
# myset = {True, 1, "apple", "banana", "cherry"}
# print(myset)

# myset = {True, 1, 2, 3}
# print(myset)

# myset = {False,0, True, 1, False, 0,True, 1, False, 0,True, 1, False, 0,True, 1, False, 0}
# print(myset)


# x = {"apple", "banana", "cherry"}
# print("The length of x set is: ", len(x))

# myset = {"apple", "banana", "cherry"}
# print(type(myset))

# myset2 = set(("apple", "banana", "cherry"))
# print(myset2)

# iterating through a set using for loop

# x= {"apple", "banana", "cherry"}
# for i in x:
#     print(i)
# myset = {"apple", "banana", "cherry"}
# if "apple" in myset:
#     print("Yes, 'apple' is in the set")
# else: print("No, 'apple' is not in the set")




# myset2 = {"apple", "banana", "cherry"}
# print("Vedansh" in myset2)




# thisset = {"apple", "banana", "cherry"}
# thisset.add("Haridwar")
# print(thisset)




# anotherset = {"apple", "banana", "cherry"}
# main = {"dog", "cat", "mouse"}
# main.update(anotherset)
# print(main)




# thisset = {"apple", "banana", "cherry"}
# thislist =["dog", "cat", "mouse"]
# thisset.update(thislist)
# print(thisset)




# ======================REMOVE ITEMS FROM A SET====================
# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thiset)

# set1 ={"a","b","c"}

# set2 = {1,2,3}
# set3 = set1.union(set2)
# print(set3)


# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = {"cat","dog","mouse"}
# x =set1.union(set2,set3)
# print(x)


# set1 = {"a","b","c"}
# set2 = {1,2,3}
# set3 = {"cat","dog","mouse"}

# x = set1 | set2 | set3

# print(x)


# mearg sets and tupples using union() method

# set1 = {"a","b","c"}
# tuple = (1,2,3)
# x = set1.union(tuple)
# print(x)

# set1 = {"a","b","c"}
# set2 = {1,2,3}

# set1.update(set2)
# print(set1)


# ======================INTERSECTION OF SETS====================================

# set1 = {"apple", "banana","cherry","c"}
# set2 = {"Google", "Microsof","Apple","c"}
# x = set1.intersection(set2)
# print(x)

# set1 = {1,False,"apple","c"}
# set2 = {0,True,3,"c"}
# set3 = set2.intersection(set1)
# print(set3)

# ====================symmetric diffrence of set===================

# set1 = {"apple", "banana","mango"}
# set2 = {"dod","cat","c","mango"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1 = {"apple","mango","banana","a"}
# set2 = {"a","b","c"}
# set1.symmetric_difference_update(set2)
# print(set1)

# Creating a frozen set using the Frozenset()constructor

# myset = frozenset(["apple","mango","banana"])
# print(myset)

# name = input("enter my name :")
# print(name)

# x = int(input("Enter the first number:"))

# y = int(input("Enter the Seconed number:"))

# x= 25

# y =5

# z =(x//y)

# print(z)


