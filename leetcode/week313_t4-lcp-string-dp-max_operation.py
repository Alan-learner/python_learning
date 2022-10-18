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
    def deleteString(self, s: str) -> int:
        n = len(s)
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        # lcp[i][j] 表示字符串s[i:] 与 s[j:] 之间最长公共子串的长度
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        dp = [0] * n
        # dp[i] 表示删除 s[i:] 所需要的最大操作次数
        for i in range(n - 1, -1, -1):
            # i + 2 * j <= n
            # j <= (n - i) // 2
            for j in range(1, (n - i) // 2 + 1):
                # 等价于判断s[i: i + j] == s[i + j:i + 2 * j]
                if lcp[i][i + j] >= j:
                    dp[i] = max(dp[i + j], dp[i])
            dp[i] += 1
        return dp[0]


def main():
    s = Solution()
    res = s.minimizeXor(num1=346, num2=6654)
    print(res)


if __name__ == '__main__':
    main()
