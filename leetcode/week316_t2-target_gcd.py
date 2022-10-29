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
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            x = nums[i]
            if x == k:
                ans += 1
            for j in range(i + 1, n):
                x = math.gcd(x, nums[j])
                if x == k:
                    ans += 1
        return ans


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
