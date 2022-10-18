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
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # 有序数组O(n^2*logn)
        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     s = SortedList()
        #     for j in range(i, n):
        #         s.add(nums[j])
        #         if s[0] == minK and s[-1] == maxK:
        #             ans += 1
        # return ans

        ans = 0
        min_i = max_i = extra = -1
        for idx, val in enumerate(nums):
            if val == maxK: max_i = idx
            if val == minK: min_i = idx
            if val < minK or val > maxK: extra = idx
            ans += max(0, min(max_i, min_i) - extra)
        return ans


def main():
    s = Solution()
    res = s.countSubarrays(
        nums=[35054, 398719, 945315, 945315, 820417, 945315, 35054, 945315, 171832, 945315, 35054, 109750, 790964,
              441974, 552913], minK=35054, maxK=945315)
    print(res)


if __name__ == '__main__':
    main()
