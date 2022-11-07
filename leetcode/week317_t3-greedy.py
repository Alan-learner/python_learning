# encoding: utf-8
# author: Alan-learner

import math
from collections import deque, defaultdict
from copy import copy
from math import inf
from typing import List
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
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        m = copy(n)

        def fuc(x):
            """

            :param x:
            :return: x各位数字之和
            """
            s = 0
            t = copy(x)
            while t != 0:
                s += t % 10
                t = t // 10
            return s

        tmp = 10
        while fuc(m) > target:
            # 贪心
            m += (tmp - m % tmp)
            tmp *= 10
        return m - n


def main():
    s = Solution()
    res = s.makeIntegerBeautiful(1,
                                 1)
    print(res)


if __name__ == '__main__':
    main()
