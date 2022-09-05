# encoding: utf-8
from collections import deque
from copy import copy
from heapq import heappush, heappop


class Solution:
    def mostBooked(self, n: int, meetings: list) -> int:
        h = 0
        heap = list(range(n))  # 用堆来存储空闲的会议室列表
        dic = {}
        dic2 = {k: 0 for k in range(n)}
        end_mark = [False] * len(meetings)
        end_flag = len(meetings)
        while end_flag > 0:
            for i, v in enumerate(meetings):
                s = v[0]
                e = v[1]
                tmp_s = copy(s)
                tmp_e = copy(e)
                if end_mark[i]:
                    continue
                if not s <= h <= e:
                    continue
                else:
                    if dic.get(i) is not None:  # 判断是否在开会
                        if h == e:
                            room = dic.pop(i)
                            heappush(heap, room)  # 结束的话释放会议室
                            end_mark[i] = True  # 列表的会议标记为结束
                            end_flag -= 1
                    else:
                        if heap:
                            dic[i] = heappop(heap)
                            dic2[dic[i]] += 1  # i号会议室使用次数+1
                        else:
                            if h == s:  # 到点了却没开始，说明要延期
                                meetings[i][0] = h + 1
                                meetings[i][1] = h + 1 + tmp_e - tmp_s
            h += 1
        lis2 = list(dic2.items())
        lis2.sort(key=lambda x: (x[1]), reverse=True)
        res = lis2[0][0]
        return res


def main():
    s = Solution()
    res = s.mostBooked(n=2, meetings=[[0, 10], [1, 5], [2, 7], [3, 4]])
    print(res)


if __name__ == '__main__':
    main()
