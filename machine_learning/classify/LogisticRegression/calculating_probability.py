# encoding: utf-8

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1、数据加载
iris = datasets.load_iris()

# 2、数据提取与筛选
X = iris['data']
y = iris['target']
cond = y != 2
X = X[cond]
y = y[cond]

# 3、数据拆分
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 4、模型训练
lr = LogisticRegression()
lr.fit(X_train, y_train)

# 5、模型预测
y_predict = lr.predict(X_test)


# 6、手动计算的概率
def handle():
    b = lr.intercept_
    w = lr.coef_

    # 逻辑回归函数
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    # y = 1 概率
    z = X_test.dot(w.T) + b
    p_1 = sigmoid(z)

    # y = 0 概率
    p_0 = 1 - p_1

    # 最终结果
    p = np.concatenate([p_0, p_1], axis=1)
    return p


handle_pro = handle()


def main():
    print('测试数据保留类别是：', y_test)
    print('测试数据算法预测类别是：', y_predict)
    print('测试数据算法预测概率是：\n', lr.predict_proba(X_test))
    print('手动计算的概率是：\n', handle_pro)


if __name__ == '__main__':
    main()
