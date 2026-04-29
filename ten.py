import numpy as np
# # without ufunc


# x = [ 1,2,3,4]
# y=[4,5,6,7]
# z=[]



# for i , j in zip(x,y):
#     z.append(i+j)

# print(z)

# with ufunc

# x = [ 1,2,3,4]
# y=[4,5,6,7]
# z= np.add(x,y)
# print(z)


# Create our own ufunc


# def myadd(x,y)  :

#  return x+y

# xyz = np.frompyfunc(myadd,2, 1 )

# print(xyz([ 1,2,3,4,5], [5,6,7,8,9]))



x = "Jaikaran"
print(type(np.add))



if type(np.subtract) == np.ufunc:
    print("subtract is ufunc")
else:
    print("add is not ufunc")



import numpy as np

