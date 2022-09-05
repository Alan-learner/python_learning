# encoding: utf-8
class Solution:
    def longestNiceSubarray(self, nums: list) -> int:
        ans = 1  # 使用双指针，及时将不满足要求的元素剔除在指针范围之外
        left = or_ = 0  # or_存储左指针到右指针之间元素“|”或操作的值
        for right, x in enumerate(nums):
            while x & or_:  # 对于不满足要求的情况，用异或剔除该元素，并移动指针
                or_ ^= nums[left]
                left += 1
            or_ |= x
            ans = max(ans, right - left + 1)
        return ans


def main():
    s = Solution()
    res = s.longestNiceSubarray(nums=[1, 3, 8, 48, 10])
    print(res)


if __name__ == '__main__':
    main()
