import numpy as np 
# listArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
# # print(listArray)
# # print(listArray.dtype)
# # print(listArray.shape)
# # print(listArray.size)
# objectArr = np.array({2,3,4})
# print(objectArr.dtype)

# zeroes = np.zeros((2,5))
# print(zeroes) 

# rng = np.arange(15)
# print(rng)

# lspace = np.linspace(1,10,4)
# print(lspace)
# print(lspace.dtype) 

# emp = np.empty((4,5))
# print(emp)

# ide = np.identity(3)
# print(ide)

x = [[1,2,3],[4,5,6],[7,1,0]]
arr = np.array(x)
print(arr)

# print(arr.sum(axis = 0))
# print(arr.sum(axis = 1))

# print(arr.T)


for item in arr.flat:
    print(item)

