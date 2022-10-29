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
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums1 = []
        nums2 = []
        for n in target:
            if n % 2 == 0:
                nums2.append(n)
            else:
                nums1.append(n)
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        cost = 0
        n = len(nums)
        for num in nums:
            if num % 2 == 0:

                b = bisect_right(nums2, num)
                a = b - 1
                if a > n2 - 1:
                    a = n2 - 1
                if b > n2 - 1:
                    b = n2 - 1
                x = abs(nums2[a] - num)
                y = abs(nums2[b] - num)
                cost += min(x, y)
            else:

                b = bisect_right(nums1, num)
                a = b - 1
                if a > n1 - 1:
                    a = n1 - 1
                if b > n1 - 1:
                    b = n1 - 1
                x = abs(nums1[a] - num)
                y = abs(nums1[b] - num)
                cost += min(x, y)
        return cost // 4


def main():
    s = Solution()
    res = s.makeSimilar(nums=[1, 2, 5], target=[4, 1, 3])
    print(res)


if __name__ == '__main__':
    main()
