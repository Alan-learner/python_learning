# encoding: utf-8
# author: Alan-learner
from math import inf
from typing import List

from sortedcontainers import SortedList


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mx = -1
        mn = inf
        ans = 0
        j = 0
        for i, v in enumerate(arr):
            mx = max(mx, v)
            mn = min(mn, v)
            if j == mn and i == mx:
                ans += 1
                j = i + 1
                mx = -1
                mn = inf
        return ans



def main():
    s = SortedList()


if __name__ == '__main__':
    main()
