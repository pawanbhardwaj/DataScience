import numpy as np

arr = np.array([[10, 20, 30, 45, 34], [12, 34, 54, 65, 75]])
arr1 = np.array([[33, 43, 56, 98, 99], [123, 45, 65, 76, 90]])
arr2 = np.array([[33, 43, 56, 98, 99], [123, 45, 65, 76, 90]])
# print(np.sum([arr, arr1]))
# print()
# print(np.sum([arr, arr1], axis=0))
# print()
# print(np.sum([arr, arr1], axis=1))
# print()
# print(np.sum([arr, arr1], axis=2))
# print()
# print(np.shape(arr1))
# print()
print(np.vstack([arr]))
print()
print(np.hstack([arr, arr1, arr2]))
print()
print(np.column_stack([arr, arr1, arr2]))
