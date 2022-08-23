import numpy as np

# 一维
arr1 = np.sort(np.array([0, 1, 2, 3] * 3)).reshape(4, 3)  # shape(4,3)
arr2 = np.array([1, 2, 3])  # shape(3,)
arr3 = arr1 + arr2  # arr2进行广播复制4份 shape(4,3)
print(arr3)

# 二维
arr1 = np.sort(np.array([0, 1, 2, 3] * 3)).reshape(4, 3)  # shape(4,3)
arr2 = np.array([[1], [2], [3], [4]])  # shape(4,1)
arr3 = arr1 + arr2  # arr2 进行广播复制3份 shape(4,3)
print(arr3)

# 三维
arr1 = np.array([0, 1, 2, 3, 4, 5, 6, 7] * 3).reshape(3, 4, 2)  # shape(3,4,2)
arr2 = np.array([0, 1, 2, 3, 4, 5, 6, 7]).reshape(4, 2)  # shape(4,2)
arr3 = arr1 + arr2  # arr2数组在0维上复制3份 shape(3,4,2)
print(arr3)
