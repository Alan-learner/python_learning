# encoding: utf-8
# author: Alan-learner

import numpy as np
import pandas as pd

df = pd.DataFrame(data={'color': ['red', 'blue', 'red', 'green', 'blue', None, 'red', np.NaN],
                        'price': [10, 20, 10, 15, 20, 0, np.NaN, None]})  # 数字，显示时候都是 NaN

df.isnull()  # 查看空数据

df.dropna()  # 过滤空数据

df.fillna(1024)  # 将空数据填充为1024

'''
指定行或者列过滤
'''
del df['color']  # 直接删除某列,原数据改变

# ！！！ drop删除，返回值，原来的数据没有修改
df.drop(labels=['price'], axis=1)  # 删除指定列
# 没有修改原数据
new_df = df.drop(labels=[0, 1, 5], axis=0)  # 删除指定行

# inplace 替换：替换原来数据，修改原数据
df.drop(labels=[0, 1, 3, 5], axis=0, inplace=True)

'''
异常值按条件过滤
'''
df2 = pd.DataFrame(data=np.random.randn(10000, 3))  # 正态分布数据

# 3σ过滤异常值，σ即是标准差
cond = (df2 > 3 * df2.std()).any(axis=1)
index = df2[cond].index  # 不满足条件的行索引
df2.drop(labels=index, axis=0)  # 根据行索引，进行数据删除

# 比较运算
# 异常值少数
cond = df2.abs() > 3 * df2.std()  # 数据绝对值大于三倍标准差
cond_0 = cond[0]
new_df2 = df2[cond_0]

# 获取所有列异常
cond = df2.abs() > 3 * df2.std()
cond_0 = cond[0]  # 默认[] 只能取列索引
cond_1 = cond[1]
cond_2 = cond[2]

# 逻辑或运算，只要有一个满足，返回True
cond_ = cond_0 | cond_1 | cond_2

new = df2[cond_]

# 上一步操作等价于

cond = df2.abs() > 3 * df2.std()  # 计算异常值

# axis = 1计算每一行：只要一行中有一个TRUE，返回True
# True，表示异常值
cond_ = cond.any(axis=1)  # 只要有一个为真,返回True

df2_new = df2[cond_]


def main():
    pass


if __name__ == '__main__':
    main()
