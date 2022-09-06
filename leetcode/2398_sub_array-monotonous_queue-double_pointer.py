# encoding: utf-8
from collections import deque


class Solution:
    def maximumRobots(self, chargeTimes: list, runningCosts: list, budget: int) -> int:
        ans = left = s = 0
        # monotonous_queue = deque()  # 单调队列，用来递减得存储由大到小chargeTimes的下标
        monotonous_queue = []  # 单调队列，用来递减得存储由大到小chargeTimes的下标
        for right, (t, c) in enumerate(zip(chargeTimes, runningCosts)):
            # 处理右端点
            while monotonous_queue and t >= chargeTimes[monotonous_queue[-1]]:  # 判断插入前是否可以删除无用数据
                monotonous_queue.pop()
            monotonous_queue.append(right)
            s += c
            # 处理左端点
            while monotonous_queue and chargeTimes[monotonous_queue[0]] + (right - left + 1) * s > budget:
                if monotonous_queue[0] == left:
                    # monotonous_queue.popleft()
                    monotonous_queue.pop(0)
                s -= runningCosts[left]
                left += 1  # 超出总支出，弹出左端点
            ans = max(ans, right - left + 1)
        return ans


def main():
    s = Solution()
    res = s.maximumRobots(chargeTimes=[3, 6, 1, 3, 4], runningCosts=[2, 1, 3, 4, 5], budget=25)
    print(res)


if __name__ == '__main__':
    main()
