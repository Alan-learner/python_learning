import numpy as np


def calculate_array():
    arr1 = np.array([1, 7, 2, 19, 23, 0, 88, 11, 6, 11])
    arr1.min()  # 计算最小值 0
    arr1.argmax()  # 计算最大值的索引 返回 6
    np.argwhere(arr1 > 20)  # 返回大于20的元素的索引
    np.cumsum(arr1)  # 计算累加和
    arr2 = np.random.randint(0, 10, size=(4, 5))
    arr2.mean(axis=0)  # 计算列的平均值
    arr2.mean(axis=1)  # 计算行的平均值
    np.cov(arr2, rowvar=True)  # 协方差矩阵
    np.corrcoef(arr2, rowvar=True)  # 相关性系数


def apply():
    data = np.loadtxt(r"D:\AIot\files\作业\iris.csv", delimiter=',')  # 读取数据文件，data是二维的数组
    data.sort(axis=-1)  # 简单排序
    print('简单排序后：', data)
    print('数据去重后：', np.unique(data))  # 去除重复数据
    print('数据求和：', np.sum(data))  # 数组求和
    print('元素求累加和', np.cumsum(data))  # 元素求累加和
    print('数据的均值：', np.mean(data))  # 均值
    print('数据的标准差：', np.std(data))  # 标准差
    print('数据的方差：', np.var(data))  # 方差
    print('数据的最小值：', np.min(data))  # 最小值
    print('数据的最大值：', np.max(data))  # 最大值


def main():
    calculate_array()
    apply()


if __name__ == '__main__':
    main()
