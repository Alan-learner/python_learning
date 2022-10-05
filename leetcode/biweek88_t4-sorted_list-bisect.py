# encoding: utf-8
# author: Alan-learner
from bisect import bisect_left, bisect_right
from functools import reduce
from heapq import heappush, heappop
from sortedcontainers import SortedList



class Solution:
    def numberOfPairs(self, nums1: list, nums2: list, diff: int) -> int:
        # 原地存储两个数组之间的差值
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]
        nums = nums1.copy()
        nums.sort()
        lst = SortedList()
        ans = 0
        for x in nums1:
            # 二分查找一下符合条件数字在有序数组中的位置
            i = bisect_right(lst, x + diff)
            # 查询当前遍历的数字所有符合条件的数的个数
            ans += i
            # 当前遍历的数字每出现一次，就对它的频率+1
            lst.add(x)

        return ans


def main():
    s = Solution()
    res = s.numberOfPairs(nums1=[3, 2, 5], nums2=[2, 2, 1], diff=1)
    print(res)


if __name__ == '__main__':
    main()
