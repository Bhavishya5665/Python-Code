# import numpy as np

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# newarr = np.add(arr1,arr2)
# print(newarr)



# arr3 = np.array([1,2,3])
# arr4 = np.array([4,5,6])
# newarr1 = np.sum([arr3,arr4])
# print(newarr1)



# CUMULATIVE SUMMATION

# arr = np.array([1,2,3,4,5,6])

# newarr2 = np.cumsum(arr)
# print(newarr2)


# from matplotlib.pylab import f





import pandas as pd

# L = [1,2,3,4,5,6]
# s = pd.Series(L)
# print(s)


# L = [1,2,3,4,5,6]
# s = pd.Series(L, dtype=float)
# print(s)


# data = [1,2,3,4,5,6]
# s = pd.DataFrame(data)
# print(s)


data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'ayush', 'Rohan'],
        'Age': [28, 24, 35, 32, 29, 31],
        'Salary': [50000, 60000, 55000, 70000, 52000, 68000]}

df = pd.DataFrame(data)
# print(df)
# print(df.head())
# print(df.tail())
# print(df)
print(df.rename(columns = {'Salary' : 'Monthly Salary'}, inplace = True))

print(df)       



df.info()