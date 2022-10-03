# encoding: utf-8
# author: Alan-learner
from bisect import bisect_left, bisect_right
from functools import reduce
from heapq import heappush, heappop
from sortedcontainers import SortedList

lowbit = lambda x: x & (-x)


# Binary Index Tree
class BIT:
    def __init__(self, n):
        self.tree = [0] * n

    def __len__(self):
        return len(self.tree)

    def add(self, i, val):
        while i < self.__len__():
            self.tree[i] += val
            i += lowbit(i)

    def query(self, i):
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
            i = bisect_right(nums, x + diff)
            ans += tree_array.query(i)
            tree_array.add(bisect_left(nums, x) + 1, 1)

        return ans


def main():
    s = Solution()
    res = s.numberOfPairs(nums1=[3, 2, 5], nums2=[2, 2, 1], diff=1)
    print(res)


if __name__ == '__main__':
    main()
