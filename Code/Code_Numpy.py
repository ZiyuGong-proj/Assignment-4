import numpy as np
# NumPy’s main object is the homogeneous multidimensional array. 
# It is a table of elements (usually numbers), all of the same 
# type, indexed by a tuple of non-negative integers. 

# 1-d numpy array
a_1 = np.array([1,2,3])
b_1 = np.zeros((3,1)) 
a_1.size  # => 3 
a_1.shape # => (3,)
b_1.shape # => (3,1), this is different from the shape of a_1

# reshape a_1 to have shape (3,1)
a_1 = a_1.reshape(-1,1)  # -1 means "whatever is needed"
a_1.shape # => (3,1)

# 2-d numpy array 
a_2 = np.array([[1,2,3],[4,5,6]])
b_2 = np.zeros((3,2))
a_2.size # => 6
a_2.shape # => (2,3)
b_2.size # => 6
b_2.shape # => (3,2)

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
# Indexing, Slicing and Filtering
a[0,1] # => 2, first index represents row, second col 
a[0,:] # => [1 2 3]
a[a>4] # => [5 6]

# Arithmetic operators on arrays apply elementwise
a**2 # => [[ 1,  4,  9],
       #  [16, 25, 36]]
       
a + 1 # => [[2, 3, 4],
       #   [5, 6, 7]]
       
# Arithmetic operators can be be applied on two
# arraies if they share common length in all axises that
# are not of length 1
b = np.arange(1,4).reshape(1,-1) # => [[1,2,3]]
a - b # => [[0, 0, 0],
           #[3, 3, 3]]
# The shape of b is (1,3), and the shape of a is (2,3),
# so a and b share common length 3 in y-axis.
# Although they have differnt lengths in x-axis, it works
# as long as one of them has length 1 in the x-axis.
# You can now see the importance of "reshape".

A = np.array( [[1,1],
               [0,1]] )
B = np.array( [[2,0],
              [3,4]] )
A * B         # elementwise product
# => [[2, 0],
    #[0, 4]]
A @ B         # matrix product
# => [[5, 4],
    #[3, 4]]
A.dot(B)      # another matrix product
#  => [[5, 4],
   #  [3, 4]]
A.transpose() # transpose a matrix
#  => [[1, 0],
    # [1, 1]]






