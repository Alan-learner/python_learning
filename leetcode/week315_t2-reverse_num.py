# encoding: utf-8
# author: Alan-learner

import math
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

lowbit = lambda x: x & -x
MOD = 10 ** 9 + 7


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        tmp = nums.copy()
        for n in nums:
            tmp.append(int(str(n)[::-1]))
        s = set(tmp)
        return len(s)


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
