import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([2, 3, 1, 5, 9])


def numerical_calculate():
    arr1 - arr2  # 减法
    arr1 * arr2  # 乘法
    arr1 / arr2  # 除法
    arr1 ** arr2  # 两个星号表示幂运算


def logic_calculate():
    cond1 = (arr1 < 5)
    cond2 = (arr1 >= 5)
    cond3 = (arr1 == 5)
    cond4 = (arr1 == arr2)
    cond5 = (arr1 > arr2)
    print(cond1, cond2, cond3, cond4, cond5)


def num_calculate():
    print(arr1)
    print(arr1 + 5)
    print(1 / arr1)
    print(arr1 * 2)


def point_array():
    a = np.random.randint(0, 100, size=(4, 5))
    b = a
    print(a is b)  # 返回True a和b是两个不同名字对应同一个内存对象
    b[0, 0] = 1024  # 命运共同体
    print(a, b)


def view_array():
    a = np.random.randint(0, 100, size=(4, 5))
    b = a.view()  # 使用a中的数据创建一个新数组对象
    var1 = (a is b)  # 返回False a和b是两个不同名字对应同一个内存对象
    var2 = b.base is a  # 返回True，b视图的根数据和a一样
    var3 = b.flags.owndata  # 返回False b中的数据不是其自己的
    var4 = a.flags.owndata  # 返回True a中的数据是其自己的
    print(var1, var2, var3, var4)
    b[0, 0] = 1024  # a和b的数据都发生改变
    print(a, b)


def copy_array():
    a = np.random.randint(0, 100, size=(4, 5))
    b = a.copy()
    var1 = b is a  # 返回False
    var2 = b.base is a  # 返回False
    var3 = b.flags.owndata  # 返回True
    var4 = a.flags.owndata  # 返回True
    print(var1, var2, var3, var4)
    b[0, 0] = 1024  # b改变，a不变，分道扬镳
    print(a, b)


def main():
    numerical_calculate()
    logic_calculate()
    num_calculate()
    point_array()
    view_array()
    copy_array()


if __name__ == '__main__':
    main()
