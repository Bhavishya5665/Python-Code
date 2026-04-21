import numpy  as np
# #  Creation of Array using numpy


# # array = np.array([1,2,3,4,5])
# # print(array)

# array_0D = np.array(4563651)
# print(array_0D)

# array_1D = np.array([1,2,3,4,5])
# print(array_1D)



# array_2D =np.array([[1,2,3],[4,5,6]])
# print(array_2D)


# array_3D =np.array([[1,2,3],[4,5,6], [7,8,9]])

# print(array_3D)


# # array = np.array([1,2,3,4,5])
# # print(array)

# array_0D = np.array(4563651)
# print(array_0D.ndim)

# array_1D = np.array([1,2,3,4,5])
# print(array_1D.ndim)



# array_2D =np.array([[1,2,3],[4,5,6]])
# print(array_2D.ndim)


# array_3D =np.array([[[1,2,3],[4,5,6], [7,8,9]]])

# print(array_3D.ndim)


# arr = np.array([1,2,3,4,5], ndmin = 8)
# print(arr)
# print("The number of dimensions in arr is:", arr.ndim)



# arr = np.array([[1,2,4,5,7], [8,9,10,11,12]])

# print(arr[1,2])
# print(arr[3] + arr[4])    


# arry = np.array([1,2,3,4,5,])
# print(arry[0])


# array_2D = np.array([[1,2,3,4], [4,5,6,7]])
# print(array_2D[0,1])


# array_3D = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(array_3D[0,1,2])


# array = np.array([1,2,3,4,5])
# print(array[1:3])


# array_2D = np.array([[1,2,3],[4,5,6]])
# print(array_2D[0:2,1:3])



# ===================copy and view in numpy======================

# arr = np.array([1,2,3,4,5])

# x = arr.copy()
# arr[0] = 42



# This is the copy of array

# print(arr)
# This is the original array
# print(x)



# arr2 = np.array([1,2,3,4,5])

# y = arr2.view()
# arr2[0] = 42
# print(arr2)
# print(y)


# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

# print(arr.shape)


# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# new = arr.reshape(4,5)
# print(new)



# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# # print(new)
# new = arr.reshape(-1)
                  
# print(new)
