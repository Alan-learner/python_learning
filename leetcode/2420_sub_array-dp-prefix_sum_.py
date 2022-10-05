# encoding: utf-8
# author: Alan-learner

class Solution:
    def goodIndices(self, nums: list, k: int) -> list:
        n = len(nums)
        dec = [1] * n
        for i in range(n - 2, k, -1):
            if nums[i] <= nums[i + 1]:
                dec[i] = dec[i + 1] + 1
        inc = [1] * n
        for i in range(1, n - k - 1):
            if nums[i] <= nums[i - 1]:
                inc[i] = inc[i - 1] + 1
        ans = []
        for i in range(k, n - k):
            if inc[i - 1] >= k and dec[i + 1] >= k:
                ans.append(i)
        return ans


def main():
    pass


if __name__ == '__main__':
    main()
