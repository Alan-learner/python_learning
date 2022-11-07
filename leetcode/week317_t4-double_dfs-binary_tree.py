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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = defaultdict(int)

        def get_height(nd):
            if nd is None:
                return 0
            height[nd] = 1 + max(get_height(nd.left), get_height(nd.right))
            return height[nd]

        get_height(root)

        res = [0] * (len(height) + 1)

        def dfs(nd: Optional[TreeNode], depth, res_h):
            if nd is None:
                return
            res[nd.val] = res_h
            depth += 1
            dfs(nd.left, depth, max(res_h, depth + height[nd.right]))
            dfs(nd.right, depth, max(res_h, depth + height[nd.left]))

        dfs(root, -1, 0)
        for i, v in enumerate(queries):
            queries[i] = res[v]
        return queries


def main():
    s = Solution()
    res = s
    print(res)


if __name__ == '__main__':
    main()
