import numpy as np


def index_array():
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(arr)
    print(arr[5])  # 索引 输出 5
    print(arr[5:8])  # 切片输出：array([5, 6, 7])
    print(arr[2::2])  # 从索引2开始每两个中取一个 输出 array([2, 4, 6, 8])
    print(arr[::3])  # 不写索引默认从0开始，每3个中取一个 输出为 array([0, 3, 6, 9])
    print(arr[1:7:2])  # 从索引1开始到索引7结束，左闭右开，每2个数中取一个 输出 array([1, 3, 5])
    print(arr[::-1])  # 倒序 输出 array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    print(arr[::-2])  # 倒序 每两个取一个 输出 array([9, 7, 5, 3, 1])
    arr[5:8] = 12  # 切片赋值会赋值到每个元素上，与列表操作不同
    temp = arr[5:8]
    temp[1] = 1024
    print(arr)  # 输出：array([ 0, 1, 2, 3, 4, 12, 1024, 12, 8, 9])
    arr2d = np.array([[1, 3, 5], [2, 4, 6], [-2, -7, -9], [6, 6, 6]])  # 二维数组 shape(3,4)
    print(arr2d)
    print(arr2d[0, -1])  # 索引 等于arr2d[0][-1] 输出 5
    print(arr2d[0, 2])  # 索引 等于arr2d[0][2] == arr2d[0][-1] 输出 5
    print(arr2d[:2, -2:])  # 切片 第一维和第二维都进行切片 等于arr2d[:2][:,1:]
    print(arr2d[:2, 1:])  # 切片 1 == -2 一个是正序，另个一是倒序，对应相同的位置
    # 输出：
    # array([[3, 5],
    # [4, 6]])


def index_array_advanced():
    # 一维
    arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    arr2 = arr1[[1, 3, 3, 5, 7, 7, 7]]  # 输出 array([2, 4, 4, 6, 8, 8, 8])
    arr2[-1] = 1024  # 修改值，不影响arr1
    # 二维
    arr2d = np.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [12, 18, 22, 23, 37], [123, 55, 17, 88, 103]])
    # shape(4,5)
    print(arr2d[[1, 3]])  # 获取第二行和第四行，索引从0开始的所以1对应第二行
    # 输出 array([[ 2, 4, 6, 8, 10],
    # [123, 55, 17, 88, 103]])
    print(arr2d[([1, 3], [2, 4])])  # 相当于arr2d[1,2]获取一个元素,arr2d[3,4]获取另一个元素
    # 输出为 array([ 6, 103])
    print("选择一个区域")
    print(arr2d[np.ix_([1, 3, 3, 3], [2, 4, 4])])  # 相当于 arr2d[[1,3,3,3]][:,[2,4,4]]
    print(arr2d[[1, 3, 3, 3]][:, [2, 4, 4]])
    # ix_()函数可用于组合不同的向量
    # 第一个列表存的是待提取元素的行标，第二个列表存的是待提取元素的列标
    # 输出为
    # array([[ 6, 10, 10],
    # [ 17, 103, 103],
    # [ 17, 103, 103],
    # [ 17, 103, 103]])


def boolean_index_array():
    names = np.array(['softpo', 'Brandon', 'Will', 'Michael', 'Will', 'Ella', 'Daniel', 'softpo', 'Will', 'Brandon'])
    cond1 = names == 'Will'
    print(cond1)
    # 输出array([False, False, True, False, True, False, False, False, True,False])
    print(names[cond1])  # array(['Will', 'Will', 'Will'], dtype='<U7')
    arr = np.random.randint(0, 100, size=(10, 8))  # 0~100 随机数
    cond2 = arr > 90
    print(arr[cond2])
    # 找到所有大于90的索引，返回boolean类型


def main():
    index_array()
    index_array_advanced()
    boolean_index_array()


if __name__ == '__main__':
    main()
