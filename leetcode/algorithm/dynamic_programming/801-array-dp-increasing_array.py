# encoding: utf-8
# author: Alan-learner
from math import inf
from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[inf, inf] for _ in range(n)]
        dp[0] = [0,1]
        for i in range(1,n):
            if nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i]:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1] + 1
            if nums2[i - 1] < nums1[i] and nums1[i - 1] < nums2[i]:
                dp[i][0] = min(dp[i - 1][1],dp[i][0])
                dp[i][1] = min(dp[i - 1][0] + 1,dp[i][1])

        return min(dp[-1])


def main():
    pass


if __name__ == '__main__':
    main()
