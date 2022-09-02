# encoding: utf-8
# 集合判断数据是否存在的性能远优于列表
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list) -> list:
        s = set(range(n))
        for start, end in edges:
            if end in s:
                s.remove(end)
        res = list(s)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
