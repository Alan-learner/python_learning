# encoding: utf-8
# author: Alan-learner

import pandas as pd
import numpy as np

'''
合并
'''

# df1 一班考试成绩
df1 = pd.DataFrame(data=np.random.randint(0, 150, size=[10, 3]),  # 计算机科目的考试成绩
                   index=list('ABCDEFGHIJ'),  # 行标签，用户
                   columns=['Python', 'Tensorflow', 'Keras'])  # 考试科目

# df2 二班考试科目
df2 = pd.DataFrame(data=np.random.randint(0, 150, size=[10, 3]),  # 计算机科目的考试成绩
                   index=list('KLMNOPQRST'),  # 行标签，用户
                   columns=['Python', 'Tensorflow', 'Keras'])  # 考试科目

# df3 增加了两个考试科目（一班）
df3 = pd.DataFrame(data=np.random.randint(0, 150, size=(10, 2)),
                   index=list('ABCDEFGHIJ'),
                   columns=['PyTorch', 'Paddle'])

# 一班和二班成绩合并
pd.concat([df1, df2], axis=0)  # 等价于 np.concatenate()
# axis = 0表示 进行行合并

# 一班科目增加，将原来的科目和增加的科目进行合并
# 合并时，列增加 NaN  == not a number 空数据 404
pd.concat([df1, df3], axis=1)

'''
插入
'''
df = pd.DataFrame(data=np.random.randint(0, 151, size=(10, 3)),
                  index=list('ABCDEFGHIJ'),
                  columns=['Python', 'Keras', 'Tensorflow'])
# 插入第二列
df.insert(loc=2, column='Math', value=150)

# 获取列索引
# 转换成list列表
# 调用index函数，获取列表中特定字段的位置
# + 1表示在后面
index = list(df.columns).index('Python') + 1

# value指定了随机数字
df.insert(loc=index, column='En', value=np.random.randint(0, 151, size=10))

'''
join SQL数据库风格插入合并
'''

# 表一中记录的是name和体重信息
df1 = pd.DataFrame(data={'name': ['softpo', 'Daniel', 'Brandon', 'Ella'], 'weight': [70, 55, 75, 65]})
# 表二中记录的是name和身高信息
df2 = pd.DataFrame(data={'name': ['softpo', 'Daniel', 'Brandon', 'Cindy'], 'height': [172, 170, 170, 166]})
df3 = pd.DataFrame(data={'名字': ['softpo', 'Daniel', 'Brandon', 'Cindy'], 'height': [172, 170, 170, 166]})

pd.merge(df1, df2, )  # 根据共同的属性，进行合并

# 共同的属性是name共同拥有的是：sotfpo、Daniel、Barandon

# 指定了合并时，根据哪一列进行合并
pd.merge(df1, df3, left_on='name', right_on='名字')

# 创建10名学生的考试成绩
df4 = pd.DataFrame(data=np.random.randint(0, 151, size=(10, 3)),
                   index=list('ABCDEFHIJK'),
                   columns=['Python', 'Keras', 'Tensorflow'])

# 每个人的各科平均分，Series
s = df4.mean(axis=1).round(1)

df5 = pd.DataFrame(s, columns=['平均值'])

# 根据某一列，进行合并,df4 和 df5没有共同的一列属性执行，相同
# 共同行索引
# df4 行索引 A ~ K
# df5 行索引 A~ K
pd.merge(df4, df5, left_index=True, right_index=True)
# 等价于以下两种操作
pd.concat([df4, df5], axis=1)
df4.insert(loc=3, column='平均值', value=df5)


def main():
    pass


if __name__ == '__main__':
    main()
