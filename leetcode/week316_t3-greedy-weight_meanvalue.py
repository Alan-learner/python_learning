# encoding: utf-8
# author: Alan-learner

import math
from collections import deque
from math import inf
from typing import List
from bisect import bisect_left, bisect_right
from functools import reduce
from heapq import heappush, heappop
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
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        info = sorted(zip(nums, cost))
        total = sum(cost)
        val = 0
        s = 0
        for a, b in info:
            s += b
            if s >= total // 2:
                val = a
                break
        ans = sum([abs(x - val) * y for x, y in info])
        return ans


def main():
    s = Solution()
    res = s.minCost(nums=[1, 3, 5, 2], cost=[2, 3, 1, 14])
    print(res)


if __name__ == '__main__':
    main()
