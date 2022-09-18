# encoding: utf-8
# author: Alan-learner
import numpy as np
import pandas as pd


class Series:
    l = [0, 1, 7, 9, np.NAN, None, 1024, 512]
    # 无论是numpy中的NAN还是Python中的None在pandas中都以缺失数据NaN对待
    s1 = pd.Series(data=l)  # pandas自动添加索引
    s2 = pd.Series(data=l, index=list('abcdefhi'), dtype='float32')  # 指定行索引
    # 传入字典创建，key行索引
    s3 = pd.Series(data={'a': 99, 'b': 137, 'c': 149}, name='Python_score')


class DataFrame:
    df1 = pd.DataFrame(data={'Python': [99, 107, 122], 'Math': [111, 137, 88], 'En':
        [68, 108, 43]},  # key作为列索引
                       index=['张三', '李四', 'Michael'])  # 行索引
    df2 = pd.DataFrame(data=np.random.randint(0, 151, size=(5, 3)),
                       index=['Danial', 'Brandon', 'softpo', 'Ella', 'Cindy'],  # 行索引
                       columns=['Python', 'Math', 'En'])  # 列索引


def main():
    pass


if __name__ == '__main__':
    main()
