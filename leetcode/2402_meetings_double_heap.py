# encoding: utf-8
from heapq import heappush, heappop


class Solution:
    def mostBooked(self, n: int, meetings: list) -> int:
        meetings.sort()  # 先来先到，默认先按一号元素（开始时间）排序，再根据二号元素（结束时间）排序
        idle = list(range(n))  # 用堆来存储空闲的会议室列表
        using = []  # [(end_time,room_index)] ,结束时间放第一位方便小顶堆排序
        cnt = [0] * n  # 存储各会议室使用次数
        for st, ed in meetings:
            while using and using[0][0] <= st:  # 处理已结束的会议室
                heappush(idle, heappop(using)[1])
            if not idle:  # 判断没有空余会议室的情况
                e, i = heappop(using)  # 从使用中的会议室堆中，弹出结束时间最小的会议室
                ed = e + ed - st  # 会议延期，等待直到有空余会议室释放
                heappush(idle, i)  # 将释放的会议室添加到空闲会议室列表
            room_id = heappop(idle)
            heappush(using, (ed, room_id))
            cnt[room_id] += 1
        res = ct = 0
        for room_id, room_cnt in enumerate(cnt):
            if room_cnt > ct:
                ct = room_cnt
                res = room_id
        return res


def main():
    s = Solution()
    res = s.mostBooked(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]])
    print(res)


if __name__ == '__main__':
    main()
