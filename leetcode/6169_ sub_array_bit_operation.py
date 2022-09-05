# encoding: utf-8
class Solution:
    def longestNiceSubarray(self, nums: list) -> int:
        ans = 1
        for i in range(len(nums) - 1):
            or_ = nums[i]
            for j in range(i + 1, len(nums)):
                and_ = nums[j] & or_
                or_ |= nums[j]
                if and_ == 0:
                    ans = max(j - i + 1, ans)
                else:
                    break
        return ans


def main():
    s = Solution()
    res = s.longestNiceSubarray(nums=[1, 3, 8, 48, 10])
    print(res)


if __name__ == '__main__':
    main()
