# encoding: utf-8

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale  # 数据标准化Z-score
import warnings

warnings.filterwarnings("ignore")

# 1、加载乳腺癌数据
data = datasets.load_breast_cancer()
X, y = scale(data['data'][:, :2]), data['target']

# 2、求出两个维度对应的数据在逻辑回归算法下的最优解
lr = LogisticRegression()
lr.fit(X, y)

# 3、分别把两个维度所对应的参数W1和W2取出来
w1 = lr.coef_[0, 0]
w2 = lr.coef_[0, 1]
print(w1, w2)


# 4、已知w1和w2的情况下，传进来数据的X，返回数据的y_predict
def sigmoid(X, w1, w2):
    z = w1 * X[0] + w2 * X[1]
    return 1 / (1 + np.exp(-z))


# 5、传入一份已知数据的X，y，如果已知w1和w2的情况下，计算对应这份数据的Loss损失
def loss_function(X, y, w1, w2):
    loss = 0
    # 遍历数据集中的每一条样本，并且计算每条样本的损失，加到loss身上得到整体的数据集损失
    for x_i, y_i in zip(X, y):
        # 这是计算一条样本的y_predict，即概率
        p = sigmoid(x_i, w1, w2)
        loss += -1 * y_i * np.log(p) - (1 - y_i) * np.log(1 - p)
    return loss


# 6、参数w1和w2取值空间
w1_space = np.linspace(w1 - 2, w1 + 2, 100)
w2_space = np.linspace(w2 - 2, w2 + 2, 100)
loss1_ = np.array([loss_function(X, y, i, w2) for i in w1_space])
loss2_ = np.array([loss_function(X, y, w1, i) for i in w2_space])
w1_grid, w2_grid = np.meshgrid(w1_space, w2_space)  # 网格线
loss_grid = loss_function(X, y, w1_grid, w2_grid)


def visualize():
    # 7、数据可视化
    fig1 = plt.figure(figsize=(12, 9))
    plt.subplot(2, 2, 1)
    plt.plot(w1_space, loss1_)

    plt.subplot(2, 2, 2)
    plt.plot(w2_space, loss2_)

    plt.subplot(2, 2, 3)
    plt.contour(w1_grid, w2_grid, loss_grid, 20)  # 等值线

    plt.subplot(2, 2, 4)
    plt.contourf(w1_grid, w2_grid, loss_grid, 20)  # 等值圈
    plt.savefig('D:/Files/Output/figures/4-损失函数可视化.png', dpi=200)


# 8、3D立体可视化
def visualize_3d():
    fig2 = plt.figure(figsize=(12, 6))
    ax = Axes3D(fig2)
    ax.plot_surface(w1_grid, w2_grid, loss_grid, cmap='viridis')  # 等值面
    plt.xlabel('w1', fontsize=20)
    plt.ylabel('w2', fontsize=20)
    ax.view_init(30, -30)
    plt.savefig('D:/Files/Output/figures/5-损失函数可视化.png', dpi=200)


def main():
    visualize()
    visualize_3d()


if __name__ == '__main__':
    main()
