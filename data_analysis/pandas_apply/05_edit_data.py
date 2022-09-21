# encoding: utf-8
# author: Alan-learner

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0, 50, size=(20, 3)), columns=['Python', 'Math', 'En'])
df['物理'] = np.random.randint(0, 50, size=20)  # 增加一列
df['Python'] += 10  # 将Python列的数值增加10

# 将Math，索引是2的这个人变成100分
df['Math'][2] = 100  # 修改成功
df['Math'][[2, 3]] = 100  # 修改成功
df[['Math', 'En']][[2, 3]] = 100  # 修改成功

# 选行列组合，批量修改多个数据
df.loc[[2, 3], ['Python', 'En']] = 1024

# 按条件值过滤
cond = df['物理'] < 10

# 特别说明，表示从原来数据中，复制！！！
# 根据条件从原数据取出来的数据，分家了！！！
# 两者没有关系，一顿操作，修改，原数据不变
new_data = df[cond] * 100

df.loc[cond] -= 100  # 对原数据进行修改


def main():
    pass


if __name__ == '__main__':
    main()
