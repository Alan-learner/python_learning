# encoding: utf-8
# author: Alan-learner
import numpy as np
import pandas as pd

# 创建 shape(150,3)的二维标签数组结构DataFrame
df = pd.DataFrame(data=np.random.randint(0, 151, size=(150, 3)),
                  index=None,  # 行索引默认
                  columns=['Python', 'Math', 'En'])  # 列索引


class DataViewer:
    def __init__(self, data):
        self.data = data
        self.shape = data.shape  # 查看形状，行数和列数
        self.dtypes = data.dtypes  # 查看数据类型
        self.index = data.index  # 行索引
        self.columns = data.columns  # 列索引
        self.values = data.values  # 对象值，二维nd array数组
        self.describe = data.describe()  # 查看数值型列的汇总统计,计数、平均值、标准差、最小值、四分位数、最大值
        # 查看其属性、概览和统计信息
        data.head(10)  # 显示头部10行，默认5个
        data.tail(10)  # 显示末尾10行，默认5个

        data.info()  # 查看列索引、数据类型、非空计数和内存信息


def main():
    viewer = DataViewer(data=df)
    dsb = viewer.describe
    print(dsb)


if __name__ == '__main__':
    main()
