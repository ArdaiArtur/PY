
import numpy as np

# Create a 1-dimensional array
a = np.array([1, 2, 3, 4, 5])
print(a)
# Output: array([1, 2, 3, 4, 5])

# Create a 2-dimensional array (matrix)
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
# Output: 
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Perform operations on the array
c = a + 2
print(c)
# Output: array([3, 4, 5, 6, 7])

d = b * 3
print(d)
# Output:
# [[ 3  6  9]
#  [12 15 18]
#  [21 24 27]]

# Get the shape of the array
print(a.shape)
# Output: (5,)
print(b.shape)
# Output: (3, 3)

# Access an element in the array
print(b[1, 2])
# Output: 6