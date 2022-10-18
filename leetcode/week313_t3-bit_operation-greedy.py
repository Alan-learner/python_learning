# encoding: utf-8
# author: Alan-learner
import math
from bisect import bisect, bisect_right, bisect_left
from collections import defaultdict
from functools import reduce
from heapq import heappush, heappop

from fontTools.misc.intTools import bit_count
from sortedcontainers import SortedList

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        f = lambda x: bin(x).count("1")
        f2 = lambda x: len(bin(x)) - 2 if x != 0 else 0
        l = f(num2)
        left = f2(num1)
        ans = 0
        while left and l:
            l -= 1
            tmp = 1 << (f2(num1) - 1)
            num1 -= tmp
            ans += tmp
            left = f2(num1)
        while l:
            l -= 1
            s = bin(ans)[2:]
            idx = s[::-1].find("0")
            if idx != -1:
                ad = 1 << idx
            else:
                ad = 1 << (f2(ans))
            ans += ad

        return ans


def main():
    s = Solution()
    res = s.minimizeXor(num1=346, num2=6654)
    print(res)


if __name__ == '__main__':
    main()
