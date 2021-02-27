import numpy as np

# how to create arrays
a = np.zeros(3)
print('np.zeros(3)', a) # [0. 0. 0.]

# type of an item
print(type(a[0])) # <class 'numpy.float64'>

# shape of the array
z = np.zeros(10)
print('shape', z.shape) # (10,)

# change the shape
z.shape = (10, 1)
print('z.shape = (10, 1)', z) # [[0.]
                              #  [0.]
                              #  [0.]
                              #  [0.]
                              #  [0.]
                              #  [0.]
                              #  [0.]
                              #  [0.]
                              #  [0.]
                              #  [0.]]

# populate with ones
z = np.ones(10)
print('np.ones(10)', z) # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

# an empty array
z = np.empty(3)
print('np.empty(3)', z) # [0. 0. 0.]

# a range with a starting point and end point and then the number of elements
# from 2 to 10, with 5 elements
z = np.linspace(2, 10, 5)
print('np.linspace(2, 10, 5)', z) # [ 2.  4.  6.  8. 10.]

# create an array from a list
a_list = [1, 2, 3, 4, 5, 6, 7]
z = np.array(a_list)
print('type(a_list)', type(a_list)) # <class 'list'>
print('type(z)', type(z)) # <class 'numpy.ndarray'>
print('np.array(a_list)', z) # [1 2 3 4 5 6 7]

# random arrays
z1 = np.random.randint(10, size = 6)
print('np.random.randint(10, size = 6)', z1) # [8 1 6 3 6 1]

# get a range
a = z1[0:2]
print('z1[0:2]', a) # [8 1]

# lower than a value
z = np.array([1, 2, 3, 4, 5])
print('z < 3', z < 3) # [ True  True False False False]

# greater than a value
z = np.array([1, 2, 3, 4, 5])
print('z < 3', z > 3) # [False False False  True  True]

# operations
a_array = np.array([1, 2, 3, 4, 5])
b_array = np.array([6, 7, 8, 9, 10])

print('a_array + b_array', a_array + b_array) # [ 7  9 11 13 15]

print('a_array + 30', a_array + 30) # [31 32 33 34 35]

print('a_array * b_array', a_array * b_array) # [ 6 14 24 36 50]

print('a_array * 10', a_array * 10) # [10 20 30 40 50]

# sort
z = np.array([2, 1, 4, 5, 6])
print('np.sort(z)', np.sort(z)) # [1 2 4 5 6]
























