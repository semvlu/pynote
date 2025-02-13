import numpy as np
#1D
a=np.array([23,55,24,52])
print(a)
print(a.size) #amount of array
print(a.shape) #for n row m column array, shape will be (n,m)
print(a.ndim) #dimensions of the array
print(a.dtype) #element type e.g. int32, float64
print(a.itemsize) #bits elements occupy, if dtype is float 64, itemsize= 64/8=8
print(np.array([1,2,3,4,5,6]))
print(np.empty(3)) #create an array and input random numbers
print(np.ones(3)) #create an array w/ three elements and all are 1
print(np.arange(5,11,2)) #create an array from 5 to 11 but 11 not included, 2 means increase by 2

#2D
b=np.array([
    [1,4],
    [7,2],
    [3,7]
])
print(b.itemsize)
print(np.empty([3,2]))

#3D
c=np.array([
    [
        [1,2,3], [4,5,6],[7,8,9]
    ],
    [
        [9,8,7],[6,5,4],[3,2,1]
    ]
])
print(c.size)
print(np.empty([4,2,3]))
