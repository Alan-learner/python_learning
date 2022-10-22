# encoding: utf-8
# author: Alan-learner
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        info = sorted(zip(endTime, startTime, profit))
        max_profit = []  # 定义处理到第i份工作的最大报酬
        for i, v in enumerate(info):
            end, start, money = v
            if not max_profit:
                max_profit.append(money)
                continue
            idx = bisect_right(info, (start, end, money))
            if idx:
                cur_profit = max_profit[idx - 1] + money
                cur_max_profit = max(max_profit[i - 1], cur_profit)
            else:
                cur_max_profit = max(max_profit[i - 1], money)
            max_profit.append(cur_max_profit)
        return max_profit[-1]


def main():
    s = Solution()
    res = s.jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4])
    print(res)


if __name__ == '__main__':
    main()
