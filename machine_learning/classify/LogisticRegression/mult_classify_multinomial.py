# encoding: utf-8

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

np.set_printoptions(suppress=True)
# 1、数据加载
iris = datasets.load_iris()

# 2、数据提取
X = iris['data']
y = iris['target']

# 3、数据拆分
X_train, X_test, y_train, y_test = train_test_split(X, y)
# 4、模型训练
lr = LogisticRegression(multi_class='multinomial')
lr.fit(X_train, y_train)
# 5、模型预测
y_predict = lr.predict(X_test)


# 6、手动计算的概率
def handle():
    w = lr.coef_
    b = lr.intercept_
    z = X_test.dot(w.T) + b

    def softmax(x):
        return np.exp(x) / np.exp(x).sum(axis=1).reshape(-1, 1)

    p = softmax(z)
    return p


handle_pro = handle()


def main():
    print('测试数据保留类别是：', y_test)
    print('测试数据算法预测类别是：', y_predict)
    print('测试数据算法预测概率是：\n', lr.predict_proba(X_test))
    print('手动计算的概率是：\n', handle_pro)


if __name__ == '__main__':
    main()
