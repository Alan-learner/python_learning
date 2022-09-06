# encoding: utf-8
from collections import deque
from heapq import heappush, heappop


class Solution:
    def maximumRobots(self, chargeTimes: list, runningCosts: list, budget: int) -> int:
        ans = s = 0
        h = []  # 初始化大顶堆，用来存储满足条件的子序列cost列表
        for t, c in sorted(zip(chargeTimes, runningCosts)):
            s += c
            heappush(h, -c)
            while h and t + len(h) * s > budget:
                s += heappop(h)  # 从贪心的角度，弹出最影响支出的元素（堆中最大的cost）
            ans = max(ans, len(h))
        return ans


def main():
    s = Solution()
    res = s.maximumRobots(chargeTimes=[3, 6, 1, 3, 4], runningCosts=[2, 1, 3, 4, 5], budget=25)
    print(res)


if __name__ == '__main__':
    main()
