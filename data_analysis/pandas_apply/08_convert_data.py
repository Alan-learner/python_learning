# encoding: utf-8
# author: Alan-learner

import numpy as np
import pandas as pd

'''
轴和元素替换
'''
df = pd.DataFrame(data=np.random.randint(0, 10, size=(10, 3)),
                  index=list('ABCDEFHIJK'),
                  columns=['Python', 'Tensorflow', 'Keras'])
df.iloc[4, 2] = None  # 空数据
# 1、重命名轴索引
df.rename(index={'A': 'AA', 'B': 'BB'}, columns={'Python': '人工智能'})

# 2、替换值
df.replace(5, 1024)  # 将3替换为1024
df.replace([0, 7], 2048)  # 将0和7替换为2048
df.replace({0: 512, np.nan: 998})  # 根据字典键值对进行替换
df.replace({'Python': 1}, -1024)  # 将Python这一列中等于2的，替换为-1024

'''
map series 只支持 Series
'''
df = pd.DataFrame(data=np.random.randint(0, 10, size=(10, 3)),
                  index=list('ABCDEFHIJK'),
                  columns=['Python', 'Tensorflow', 'Keras'])
df.iloc[4, 2] = None  # 空数据

# 1、map批量元素改变，Series专有
df['Keras'].map({9: 'Hello', 5: 'World', np.NaN: 'AI'})  # 字典映射


# 2、等价于用下方函数映射
def convert(x):
    if x == 9:
        return 'Hello'
    elif x == 5:
        return 'World'
    elif x is np.NaN:
        return 'AI'
    else:
        return x


df['Keras'].map(convert)
# 3、隐视函数映射转变
df['Python'].map(lambda x: 100 if x >= 5 else -100)  # 隐式函数映射

'''
apply元素改变 既支持 Series，也支持 DataFrame
'''

# 1、追加单行转换
df = pd.DataFrame(np.random.randint(0, 100, size=(30, 3)), columns=['Python', 'Math', 'En'])


def change(x):
    if x < 60:
        return '不及格'  # 条件满足，直接执行下一个
    elif x < 80:  # 是否小于80，条件满足，60 <= x < 80
        return '中等'
    else:
        return '优秀'


# 根据规则，进行数据转换
result = df['Python'].apply(change)

index = list(df.columns).index('Python') + 1

# 插入
df.insert(loc=index, column='Python' + '等级', value=result)


# 2、多行转换
for col in ['Python', 'Math', 'En']:  # 已经字符换
    # 根据规则，进行数据转换
    result = df[col].apply(change)

    # 插入位置的索引，使用变量表示
    index = list(df.columns).index(col) + 1

    # 插入
    df.insert(loc=index, column=col + '等级', value=result)




def main():
    pass


if __name__ == '__main__':
    main()
