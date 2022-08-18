import numpy as np

arr1 = np.random.randint(0, 10, size=(3, 4, 5))
print(arr1)


def reshape_array():
    arr2 = arr1.reshape(12, 5)  # 形状改变，返回新数组
    arr3 = arr1.reshape(-1, 12)  # 自动“整形”，自动计算
    print(arr2)
    print(arr3)


def transpose_array():
    print(arr1.T)  # shape(5,3) 转置
    arr2 = np.random.randint(0, 10, size=(3, 6, 4))  # shape(3,6,4)
    print(arr2)
    np.transpose(arr2, axes=(2, 0, 1))  # transpose改变数组维度 shape(4,3,6)
    print(arr2)


def heap_array():
    arr3 = np.array([[1, 2, 3]])
    arr2 = np.array([[4, 5, 6]])
    arr4 = np.concatenate([arr3, arr2], axis=0)
    print(arr4)
    # 串联合并shape(2,3) axis = 0表示第一维串联 输出为
    # array([[1, 2, 3],
    # [4, 5, 6]])
    arr5 = np.concatenate([arr3, arr2], axis=1)
    print(arr5)
    # shape(1,6) axis = 1表示第二维串联 输出为：array([[1, 2, 3, 4, 5, 6]])
    arr6 = np.hstack((arr3, arr2))  # 水平方向堆叠 输出为：array([[1, 2, 3, 4, 5, 6]])
    print(arr6)
    arr7 = np.vstack((arr3, arr2))
    print(arr7)
    # 竖直方向堆叠，输出为：
    # array([[1, 2, 3],
    # [4, 5, 6]])


def split_array():
    arr = np.random.randint(0, 10, size=(6, 5))  # shape(6,5)
    arr_list2 = np.split(arr, indices_or_sections=2, axis=0)  # 在第一维（6）平均分成两份
    arr_list3 = np.split(arr, indices_or_sections=[2, 3], axis=1)  # 在第二维（5）以索引2，3为断点分割成3份
    arr_list4 = np.vsplit(arr, indices_or_sections=3)  # 在竖直方向平均分割成3份
    arr_list5 = np.hsplit(arr, indices_or_sections=[1, 4])  # 在水平方向，以索引1，4为断点分割成3份
    print(arr, arr_list2, arr_list3, arr_list4, arr_list5)


def main():
    reshape_array()
    transpose_array()
    heap_array()
    split_array()


if __name__ == '__main__':
    main()
