# encoding: utf-8
from heapq import heappush, heappop
from sortedcontainers import SortedList


class Solution:
    def busiestServers(self, k: int, arrival: list, load: list) -> list:
        work = [0] * k  # 存放不同服务器处理服务的次数
        # idle = list(range(k))  # 小顶堆，用来存放空闲服务器的列表
        idle = SortedList(range(k))
        using = []  # [(end_time, serves_id)]小顶堆，用来根据剩余使用时间由小到大得存储使用中的服务器
        for i, (t, l) in enumerate(zip(arrival, load)):
            while using and t >= using[0][0]:  # O(k*log(k))
                # 先检查当前时间点所有可释放的服务器
                # heappush(idle, heappop(using)[1])
                idle.add(heappop(using)[1])
            if not idle:
                continue
            target_id = idle.bisect_left(i % k)  # O(log(k))
            if target_id == len(idle):
                target_id = 0
            end_time = t + l
            heappush(using, (end_time, idle[target_id]))  # O(log(k))
            work[idle[target_id]] += 1
            idle.pop(target_id)  # O(log(k))
        res = []
        max_work = max(work)
        for i, v in enumerate(work):  # O(k)
            if v == max_work:
                res.append(i)
        return res


def main():
    s = Solution()
    res = s.busiestServers(3,
                           [1, 2, 3, 4, 8, 9, 10],
                           [5, 2, 10, 3, 1, 2, 2])
    print(res)


if __name__ == '__main__':
    main()
