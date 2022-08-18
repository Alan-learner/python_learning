import os

import numpy as np


class Arrays:
    def __init__(self):
        lis = [4, 5, 6, 9]
        self.arr1 = np.array(lis)
        self.arr2 = np.ones([3, 5], dtype=float)
        self.arr3 = np.zeros([2, 3], dtype=int, order=None)
        self.arr4 = np.full(shape=[2, 2, 2], fill_value=3)
        self.arr5 = np.arange(start=2, stop=10, step=2)
        self.arr6 = np.linspace(start=2, stop=10, num=5)
        self.arr7 = np.random.randint(0, 100, [2, 3])
        self.arr8 = np.random.randn(5)  # 正态分布
        self.arr9 = np.random.random(7)
        self.arr10 = self.arr1.view()  # 浅copy
        self.arr11 = self.arr1.copy()  # 深copy


def read_one(array):
    print(f"array_info: dim:{array.ndim},size:{array.size},nums:{array.shape},data_type:{array.dtype}")
    print(array)


def read_array():
    arr = Arrays()
    for k in range(1, 10):
        array_name = "arr" + str(k)
        array = arr.__getattribute__(array_name)
        print(array_name)
        read_one(array)
        path = r"D:\Repository\python_learning\data_analysis\output\numpy"
        save_array(array, file_name=f"{array_name}.txt", file_path=path)
        read_from_file(path=rf"D:\Repository\python_learning\data_analysis\output\numpy\{array_name}.npy")


def save_array(array, file_name: str, file_path: str):
    path = os.path.join(file_path, file_name)
    np.save(path, array)


def read_from_file(path):
    array = np.loadtxt(path)
    read_one(array)


if __name__ == '__main__':
    read_array()
