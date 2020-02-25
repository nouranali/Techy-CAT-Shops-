import numpy as np

#Numpy is the core library for scientific computing in Python. 
# It provides a high-performance multidimensional array object, and tools for working with these arrays

#The most popular data structure in numpy is ndarrays
#unlike python lists
# elements in ndarrays are of the same type, indexed by non -ve integers

arr1=np.array(['a','b','c'])
print(type(arr1))

print(arr1.shape)
print(arr1[1])
arr1[1]='x'
print(arr1)
arr2= np.array([[1,2,3],[4,5,6]])
print(arr2.shape)
print(arr2[0,2],arr2[1,1])

#functions to create arrays

#create array of zeros, pass shape,type, style
z=np.zeros((5,5))
one=np.ones((5,5))
f=np.full((5,5),5)
#I matrix np.eye return 2-d array, pass no of rows
i=np.eye(2)
r=np.random.random((2,2))

#indexing and slicing similar to lists in python
#for ndarray 
a = np.array([
[1,2,3,4], 
[5,6,7,8], 
[9,10,11,12]])

print(a[2,3])
print(a.shape)
#array math
#Basic mathematical functions operate elementwise on arrays
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(np.add(x, y))
print(np.subtract(x, y))
print(np.multiply(x, y))
print(np.divide(x, y))
print(np.sqrt(x))
##dot product
v = np.array([9,10])
w = np.array([11, 12])
print(np.dot(v, w))
#transpose
print(x)
print(x.T)

#numpy also provide so many other functionalities that we won't talk about now
# as our time is limited

