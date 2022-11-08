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
    def totalCost(self, costs: List[int], t: int, kd: int) -> int:
        hp1 = [(costs[k], k) for k in range(kd)]
        heapify(hp1)
        n = len(costs)
        if 2 * kd < n:
            hp2 = [(costs[k], k) for k in range(n - kd, n)]
        else:
            hp2 = [(costs[k], k) for k in range(kd, n)]

        heapify(hp2)
        left = deque(costs[kd:n - kd])
        ans = 0
        idx1 = kd
        idx2 = n - kd - 1
        while (hp1 or hp2) and t > 0:
            t -= 1
            if hp1 and hp2:
                if hp1[0][0] <= hp2[0][0]:
                    ans += heappop(hp1)[0]
                    if left:
                        heappush(hp1, (left.popleft(), idx1))
                        idx1 += 1
                else:
                    ans += heappop(hp2)[0]
                    if left:
                        heappush(hp2, (left.pop(), idx2))
                        idx2 -= 1
            else:
                if hp1:
                    ans += heappop(hp1)[0]
                    if left:
                        heappush(hp1, (left.popleft(), idx1))
                        idx1 += 1
                if hp2:
                    ans += heappop(hp2)[0]
                    if left:
                        heappush(hp2, (left.pop(), idx2))
                        idx2 -= 1

        return ans


def main():
    s = Solution()
    res = s.totalCost(
        [18, 64, 12, 21, 21, 78, 36, 58, 88, 58, 99, 26, 92, 91, 53, 10, 24, 25, 20, 92, 73, 63, 51, 65, 87, 6, 17, 32,
         14, 42, 46, 65, 43, 9, 75]
        , 13,
        23)
    print(res)


if __name__ == '__main__':
    main()
