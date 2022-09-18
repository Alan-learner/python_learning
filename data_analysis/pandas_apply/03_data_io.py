# encoding: utf-8
# author: Alan-learner

import numpy as np
import pandas as pd

# SQLAlchemy是Python编程语言下的一款开源软件。提供了SQL工具包及对象关系映射（ORM）工具
from sqlalchemy import create_engine

PATH = './data_source/salary.csv'
df = pd.DataFrame(data=np.random.randint(0, 50, size=[5, 5]),  # 薪资情况
                  columns=['IT', '化工', '生物', '教师', '士兵'], index=list('ABCDE'))

df1 = pd.DataFrame(data=np.random.randint(0, 50, size=[50, 5]),  # 薪资情况
                   columns=['IT', '化工', '生物', '教师', '士兵'])
df2 = pd.DataFrame(data=np.random.randint(0, 50, size=[150, 3]),  # 计算机科目的考试成绩
                   columns=['Python', 'Tensorflow', 'Keras'])
# 连接数据库
conn = create_engine('mysql+pymysql://root:root@localhost/pandas?charset=UTF8MB4')


def save_csv(data, path):
    # 保存到当前路径下，文件命名是：salary.csv。csv逗号分割值文件格式
    data.to_csv(path,
                sep=',',  # 文本分隔符，默认是逗号
                header=True,  # 是否保存列索引
                index=False)  # 是否保存行索引，保存行索引，文件被加载时，默认行索引会作为一列


def read_csv(path):
    # 加载
    data = pd.read_csv(path,
                       sep=',',  # 默认是逗号
                       header=[0],  # 指定列索引
                       index_col=0)  # 指定行索引
    return data


def save_xlsx(data, path, double=False):
    # 保存到当前路径下，文件命名是：salary.xls
    if not double:
        data.to_excel(path,
                      sheet_name='salary',  # Excel中工作表的名字
                      header=True,  # 是否保存列索引
                      index=False)  # 是否保存行索引，保存行索引
    else:
        # 一个Excel文件中保存多个工作表
        with pd.ExcelWriter('./data.xlsx') as writer:
            df1.to_excel(writer, sheet_name='salary', index=False)
            df2.to_excel(writer, sheet_name='score', index=False)
        pd.read_excel('./data.xlsx',
                      sheet_name='score')  # 读取Excel中指定名字的工作表


def read_xlsx(path):
    pd.read_excel(path,
                  sheet_name='salary',  # 读取哪一个Excel中工作表，默认第一个
                  header=0,  # 使用第一行数据作为列索引
                  names=list('ABCDE'),  # 替换列索引
                  index_col=3)  # 指定行索引，B作为行索引


def save_sql(data, sql_con):
    # 数据库连接
    # 保存到数据库
    data.to_sql('data',  # 数据库中表名
                sql_con, index=False, if_exists='append')  # 数据库连接


def read_aql():
    # 从数据库中加载
    data = pd.read_sql('select * from score limit 10',  # sql查询语句
                       conn,  # 数据库连接
                       index_col='Python')  # 指定行索引名
    return data


def main():
    pass


if __name__ == '__main__':
    main()
