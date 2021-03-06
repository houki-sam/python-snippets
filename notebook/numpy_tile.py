import numpy as np

a = np.array([0, 1, 2, 3])

print(np.tile(a, 2))
# [0 1 2 3 0 1 2 3]

print(np.tile(a, (3, 2)))
# [[0 1 2 3 0 1 2 3]
#  [0 1 2 3 0 1 2 3]
#  [0 1 2 3 0 1 2 3]]

print(np.tile(a, (2, 1)))
# [[0 1 2 3]
#  [0 1 2 3]]

a = np.array([[11, 12], [21, 22]])

print(np.tile(a, 2))
# [[11 12 11 12]
#  [21 22 21 22]]

print(np.tile(a, (3, 2)))
# [[11 12 11 12]
#  [21 22 21 22]
#  [11 12 11 12]
#  [21 22 21 22]
#  [11 12 11 12]
#  [21 22 21 22]]

print(np.tile(a, (2, 1)))
# [[11 12]
#  [21 22]
#  [11 12]
#  [21 22]]
