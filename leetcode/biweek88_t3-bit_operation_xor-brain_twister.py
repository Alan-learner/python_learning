# encoding: utf-8
# author: Alan-learner
from heapq import heappush, heappop


class Solution:
    def minGroups(self, intervals: list) -> int:
        h = list()  # 小顶堆，动态记录每个分组最大右下标
        intervals.sort()
        for left, right in intervals:
            if not h:
                heappush(h, right)
                continue
            if left > h[0]:  # 当前左下标跟所有组中最小右下标无重叠，则至少可以插入到一组，更新堆顶元素
                heappop(h)
                heappush(h, right)
            else:  # 有重叠，新增分组
                heappush(h, right)
        return len(h)


def main():
    s = Solution()
    res = s.minGroups(intervals=[[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]])
    print(res)


if __name__ == '__main__':
    main()
