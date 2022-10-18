# encoding: utf-8
# author: Alan-learner
from bisect import bisect_left, bisect_right
from functools import reduce
from heapq import heappush, heappop
from sortedcontainers import SortedList

lowbit = lambda x: x & -x


# Binary Index Tree
class BIT:
    def __init__(self, n):
        self.tree = [0] * n

    def __len__(self):
        return len(self.tree)

    def add(self, i, val):
        # 单点对树状数组下标为i的元素修改（+val），并保持树状数组其他元素的有效性
        while i < self.__len__():
            self.tree[i] += val
            i += lowbit(i)

    def query(self, i):
        # 查询树状数组中,前i个数的和（前缀和）
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= lowbit(i)
        return res


class Solution:
    def numberOfPairs(self, nums1: list, nums2: list, diff: int) -> int:
        # 原地存储两个数组之间的差值
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]
        nums = nums1.copy()
        nums.sort()
        tree_array = BIT(len(nums1) + 1)
        ans = 0
        for x in nums1:
            # 二分查找一下符合条件数字在有序数组中的位置
            i = bisect_right(nums, x + diff)
            # 查询当前遍历的数字所有符合条件的数的频率之和（前缀和）
            ans += tree_array.query(i)
            # 当前遍历的数字每出现一次，就对它的频率+1
            tree_array.add(bisect_left(nums, x) + 1, 1)

        return ans


def main():
    s = Solution()
    res = s.numberOfPairs(nums1=[3, 2, 5], nums2=[2, 2, 1], diff=1)
    print(res)


if __name__ == '__main__':
    main()
