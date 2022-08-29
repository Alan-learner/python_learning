# encoding: utf-8
from collections import defaultdict


class Solution:
    def garbageCollection(self, garbage: list, travel: list) -> int:
        cost = 0
        dic = defaultdict(int)
        for i, gra in enumerate(garbage):
            cost += len(gra)  # 作业消耗
            for g in gra:
                dic[g] = i  # 动态刷新最后一次出现的位置
        for v in dic.values():
            cost += sum(travel[:v])
        return cost


def main():
    pass


if __name__ == '__main__':
    main()
