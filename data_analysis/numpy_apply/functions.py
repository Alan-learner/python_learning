import numpy as np

"""
    abs、sqrt、square、exp、log、sin、cos、tan，maxinmum、minimum、all、any、inner、clip、
round、trace、ceil、floor

"""


def cal_array():
    arr1 = np.array([1, 4, 8, 9, 16, 25])
    np.sqrt(arr1)  # 开平方
    np.square(arr1)  # 平方
    np.clip(arr1, 2, 16)  # 输出 array([ 2, 4, 8, 9, 16, 16])
    x = np.array([1, 5, 2, 9, 3, 6, 8])
    y = np.array([2, 4, 3, 7, 1, 9, 0])
    np.maximum(x, y)  # 返回两个数组中的比较大的值
    arr2 = np.random.randint(0, 10, size=(5, 5))
    res = np.inner(arr2[0], arr2)  # 返回一维数组向量内积
    print(res)


def where():
    arr1 = np.array([1, 3, 5, 7, 9])
    arr2 = np.array([2, 4, 6, 8, 10])
    cond = np.array([True, False, True, True, False])
    arr = np.where(cond, arr1, arr2)  # True选择arr1，False选择arr2的值
    # 输出 array([ 1, 4, 5, 7, 10])
    print(arr)
    arr3 = np.random.randint(0, 30, size=20)
    res = np.where(arr3 < 15, arr3, -15)  # 小于15还是自身的值，大于15设置成-15
    print(res)


def sort():
    arr = np.array([9, 3, 11, 6, 17, 5, 4, 15, 1])
    # arr.sort()  # 直接改变原数组
    res = np.sort(arr)  # 返回深拷贝排序结果
    arr = np.array([9, 3, 11, 6, 17, 5, 4, 15, 1])
    res2 = arr.argsort()  # 返回从小到大排序索引 array([8, 1, 6, 5, 3, 0, 2, 7, 4])
    print(res, res2)


def calculate_set():
    arr1 = np.array([2, 4, 6, 8, 8])
    arr2 = np.array([3, 4, 5, 6])
    arr3 = np.intersect1d(arr1, arr2)  # 交集 array([4, 6])
    arr4 = np.union1d(arr1, arr2)  # 并集 array([2, 3, 4, 5, 6, 8])
    arr5 = np.setdiff1d(arr1, arr2)  # 差集，A中有，B中没有 array([2, 8])
    print(arr3, arr4, arr5)


def main():
    cal_array()
    where()
    sort()
    calculate_set()


if __name__ == '__main__':
    main()
