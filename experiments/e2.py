import numpy as np

arr = np.array([[-1, 2, 0, 4], 
                [4, -0.5, 6, 0], 
                [2.6, 0, 7, 8], 
                [3, -7, 4, 2.0]])
                # Integer array indexing example 
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]] 
print ( temp) 