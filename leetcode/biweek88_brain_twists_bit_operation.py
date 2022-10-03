# encoding: utf-8
# author: Alan-learner
from functools import reduce
from heapq import heappush, heappop


class Solution:
    def xorAllNums(self, nums1: list, nums2: list) -> int:
        ans = 0
        f = lambda x, y: x ^ y
        if len(nums2) % 2:
            ans ^= reduce(f, nums1)

        if len(nums1) % 2:
            ans ^= reduce(f, nums2)
        return ans


def main():
    s = Solution()
    res = s.xorAllNums(nums1=[2, 1, 3], nums2=[10, 2, 5, 0])
    print(res)


if __name__ == '__main__':
    main()
