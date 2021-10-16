import numpy as np

matrix = np.array([[21, 11, 13, 3],
                   [4, 1, 22, 30],
                   [41, 50, 8, 91],
                   [10, 7, 34, 17]])

for index in matrix:
    max = np.max(index, axis=1)  # axis=1 => row
    min = np.min(index, axis=0)  # axis=0 => column
    print(max)
    print(min)
