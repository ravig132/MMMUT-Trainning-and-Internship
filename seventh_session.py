import numpy as np 
# where() funtion use case

arr = np.array([10, 15, 20, 25, 50, 10, 75, 83, 99, 17])

# # x = np.where(arr%2 == 0)
# x =  np.where(arr == [25])
# print(x)


# search soted array 


x =  np.searchsorted(arr,[20])

print(x)