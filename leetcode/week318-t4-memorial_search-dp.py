# encoding: utf-8
# author: Alan-learner

import math
from collections import deque, defaultdict
from math import inf
from typing import List, Optional
from bisect import bisect_left, bisect_right
from functools import reduce
from heapq import heappush, heappop, heapreplace, heapify
from math import comb
from executing import cache
from yarl import cache_clear

from numpy import lcm

from sortedcontainers import SortedList
from itertools import permutations, combinations

lowbit = lambda x: x & -x
MOD = int(1e9 + 7)
INF = int(1e20)


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)
        # dp[i][j] 为前 i 个工厂修理前 j 个机器人,所需要的最小移动距离
        # 动态规划，状态压缩
        dp = [inf for _ in range(n + 1)]
        dp[0] = 0  # dp[i] 为修理前 i 个机器人所需要的最小移动距离
        for pos, limit in factory:
            for i in range(n, 0, -1):
                # 倒着枚举，压缩状态
                cost = 0
                for k in range(1, min(limit, i) + 1):
                    cost += abs(pos - robot[i - k])
                    dp[i] = min(dp[i], dp[i - k] + cost)
        return dp[-1]

        # 记忆化搜索
        # def f(i: int, j: int):
        #     """
        #
        #     :param i: 使用[i:]数量的工厂
        #     :param j: 修理[j:]数量的机器人
        #     :return: 返回最小移动的距离
        #     """
        #     if j == n:
        #         # 所有机器人被修理完，返回0移动距离
        #         return 0
        #     if i == m - 1:
        #         # 修理到最后一个机器人
        #         if n - j > factory[i][1]:
        #             return inf
        #         return sum(abs(x - factory[i][0]) for x in robot[j:])
        #     res = f(i + 1, j)  # 一个都不修的情况
        #     s, k = 0, 1
        #     while k <= factory[i][1] and j + k - 1 < n:
        #         # 比较记录对于i工厂修理0-c(最大容量)个机器人的最小移动距离
        #         s += abs(robot[j + k - 1] - factory[i][0])
        #         res = min(res, s + f(i + 1, j + k))
        #         k += 1
        #     return res
        #
        # return f(0, 0)




def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
