# encoding: utf-8
# author: Alan-learner

import math
from collections import deque, defaultdict
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
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        dic = defaultdict(int)
        for a, b, c in zip(creators, ids, views):
            dic[a] += c
        lst = list(dic.items())
        lst.sort(key=lambda x: x[1])
        mx = lst[-1][1]
        s = set()
        for i, v in lst:
            if mx == v:
                s.add(i)
        d = {}
        for a, b, c in zip(creators, ids, views):
            if a in s:
                if d.get(a):
                    if c > d[a][1]:
                        d[a] = (b, c)
                    elif c == d[a][1] and b <= d[a][0]:
                        d[a] = (b, c)
                else:
                    d[a] = (b, c)
        ans = []
        for k, v in d.items():
            ans.append([k, v[0]])
        return ans


def main():
    s = Solution()
    res = s.mostPopularCreator(creators=["alice", "alice", "alice"], ids=["a", "b", "c"], views=[1, 2, 2])
    print(res)


if __name__ == '__main__':
    main()
