# encoding: utf-8
# author: Alan-learner

from functools import reduce
from heapq import heappush, heappop
from sortedcontainers import SortedList


class Solution:
    def numberOfPairs(self, nums1: list, nums2: list, diff: int) -> int:
        num = [x - y for x, y in zip(nums1, nums2)]

        def merge_sort(lst: list) -> int:
            length = len(lst)
            if length == 1:
                return 0
            mid = length // 2
            lst1 = lst[:mid]
            lst2 = lst[mid:]
            cnt = merge_sort(lst1) + merge_sort(lst2)
            # 此时lst1 和lst2已经排好序
            i = 0
            n = len(lst1)
            for val in lst2:
                while i < n and lst1[i] <= val + diff:
                    i += 1
                cnt += i
            cur = i = j = 0
            m = len(lst2)
            while True:
                if i == n:
                    lst[cur:] = lst2[j:]
                    break
                if j == m:
                    lst[cur:] = lst1[i:]
                    break
                if lst1[i] > lst2[j]:
                    lst[cur] = lst2[j]
                    j += 1
                else:
                    lst[cur] = lst1[i]
                    i += 1
                cur += 1
            return cnt

        return merge_sort(num)


def main():
    s = Solution()
    res = s.numberOfPairs(nums1=[3, 2, 5], nums2=[2, 2, 1], diff=1)
    print(res)


if __name__ == '__main__':
    main()
