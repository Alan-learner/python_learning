import numpy as np
from numpy.linalg import inv, det, eig, qr, svd

# 矩阵的乘积
A = np.array([[4, 2, 3],
              [1, 3, 1]])  # shape(2,3)
B = np.array([[2, 7],
              [-5, -7],
              [9, 3]])  # shape(3,2)
np.dot(A, B)  # 矩阵运算 A的最后一维和B的第一维必须一致
print(A @ B)  # 符号 @ 表示矩阵乘积运算

A = np.array([[1, 2, 3],
              [2, 4, 7],
              [4, 5, 8]])  # shape(3,3)
A_ = inv(A)  # 逆矩阵
A_det = det(A)  # 计算矩阵行列式
print(A, A_det)
