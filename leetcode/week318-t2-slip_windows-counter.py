# encoding: utf-8
# author: Alan-learner

import math
from collections import deque, defaultdict
from math import inf
from typing import List, Optional, Counter
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
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s = set(nums[:k])
        n = len(nums)
        tmp = sum(nums[:k])
        ans = tmp if len(s) == k else 0
        for i in range(k, n):
            tmp -= nums[i - k]
            tmp += nums[i]
            if nums[i - k] in s:
                s.remove(nums[i - k])
            s.add(nums[i])
            if len(s) == k:
                ans = max(ans, tmp)
        return ans


def main():
    s = Solution()
    res = s.maximumSubarraySum([1, 1, 1, 7, 8, 9], 3)
    print(res)


if __name__ == '__main__':
    main()
