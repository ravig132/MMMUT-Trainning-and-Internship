import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100],np.int16)

# to access the element

# print(arr[0])

# for 2d array 

twoDarray = np.array([[3,4,5,6]])

# print(twoDarray[0,1])

# to know the shape of the array

# print(twoDarray.shape)

# to know the type of the data present in arrray

# print(arr.dtype)

# to change the element at specific iteration 

arr[5] = 45

# print(arr)

# to create array in numpy

# creating array with python object created above 

# listArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(listArray,listArray.dtype,listArray.shape,listArray.size)

# using object
print(np.array({23,34,65}))








