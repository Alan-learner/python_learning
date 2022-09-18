# encoding: utf-8
# author: Alan-learner

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0, 150, size=(1000, 3)),
                  columns=['Python', 'En', 'Math'])
df2 = pd.DataFrame(np.random.randint(0, 150, size=(5, 3)),
                   index=list('ABCDE'),
                   columns=['Python', 'Math', 'En'])


def read_col():
    df['Python']  # Series
    df.Python
    df[['Python', 'Math']]
    df[['En']]


def read_row():
    df2.loc['A']  # 行索引，指定的A~E
    df2.loc[['A', 'D']]


def read_inx():
    df2.iloc[0]  # 自然数索引 0 ~ n
    df2.iloc[[0, 3]]


def read_one():
    df2['Math']['B']  # 分开写，因为[]只支持列索引
    df2['Math', 'B']
    df2.loc['B']['Math']
    # loc 表示，先获取行，再获取列
    df2.loc['B', 'Math']
    # iloc 表示，先获取行，再获取列
    df2.iloc[1, 1]


def read_block():
    df2.loc['A':'C', 'Math':]
    df2.iloc[2:4, [0, -1]]


cond1 = df['Python'] > 130
cond2 = df['Math'] > 130
cod = cond1 & cond2


def read_by_cond(data, cond):
    return data[cond]


def main():
    pass


if __name__ == '__main__':
    main()
