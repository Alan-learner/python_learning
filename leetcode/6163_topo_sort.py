# encoding: utf-8
from collections import deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: list, colConditions: list) -> list:
        def topo_sort(edges):  # 将行约束和列约束视为图中边的集合
            # 初始化图
            graph = [[] for _ in range(k)]
            left_list = [0] * k
            # 构建图
            for x, y in edges:
                x -= 1  # 下标转换为从0开始，便于后续编码
                y -= 1
                graph[x].append(y)
                left_list[y] += 1
            sorted_list = list()  # 存储拓扑排序后的结果
            q = deque(i for i, v in enumerate(left_list) if v == 0)  # 使用队列，对图进行广度优先遍历,先取出前置依赖为0的节点
            while q:
                val = q.popleft()  # 取出一个节点后，将该节点添加到拓扑排序列表
                sorted_list.append(val)
                for v in graph[val]:  # 更新取出的节点指向节点的left信息
                    left_list[v] -= 1
                    if not left_list[v]:  # 如果该节点的前置依赖被减为0，就说明可以取出来放到队列里了
                        q.append(v)
            # 如果广度遍历完所有节点后拓扑排序列表未充满，说明图中有环，无解
            return sorted_list if len(sorted_list) == k else None

        row = topo_sort(rowConditions)
        if not row:
            return []
        col = topo_sort(colConditions)
        if not col:
            return []
        ans = [[0] * k for _ in range(k)]  # 初始化答案矩阵
        pos = {v: y_index for y_index, v in enumerate(col)}  # 构建行顺与列序之间的哈希表对应关系
        for x_index, value in enumerate(row):
            y_index = pos[value]
            value += 1  # 下标转换回来
            ans[x_index][y_index] = value
        return ans


def main():
    s = Solution()
    s.buildMatrix(k=3, rowConditions=[[1, 2], [3, 2]], colConditions=[[2, 1], [3, 2]])


if __name__ == '__main__':
    main()
