import numpy as np
arr1=np.array([[8,7],[3,4]])
arr2=np.array([[5,6],[1,2]])
print("first 2D array")
print(arr1)
print("second 2D array")
print(arr2)
subtract=arr1 - arr2
print("a.subtract 2 matrices")
print(subtract)
x=np.trace(arr1)
y=np.trace(arr2)
print("diagonal sum of first matrix",x)
print("diagonal sum of second matrix",y)


