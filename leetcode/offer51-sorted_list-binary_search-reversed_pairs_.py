# encoding: utf-8
# author: Alan-learner
from bisect import bisect_left
from sortedcontainers import SortedList

lowbit = lambda x: x & (-x)



class Solution:
    def reversePairs(self, nums1: list) -> int:
        lst = SortedList()
        ans = 0
        for x in nums1:
            # 二分查找一下符合条件数字在有序数组中的位置
            i = bisect_left(lst, -x)
            # 查询当前遍历的数字所有符合条件的数的总数
            ans += i
            # 当前遍历的数字每出现一次，就对它的频率+1
            lst.add(-x)

        return ans


def main():
    s = Solution()
    res = s.reversePairs(nums1=[7, 5, 6, 4])
    print(res)


if __name__ == '__main__':
    main()
