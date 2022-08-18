import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([2, 3, 1, 5, 9])


def numerical_calculate():
    arr1 - arr2  # 减法
    arr1 * arr2  # 乘法
    arr1 / arr2  # 除法
    arr1 ** arr2  # 两个星号表示幂运算


def main():
    numerical_calculate()


if __name__ == '__main__':
    main()
