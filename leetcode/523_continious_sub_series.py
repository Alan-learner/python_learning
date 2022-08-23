class Solution:
    # 动态规划 + 滑窗法 计算所有余数
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        length = len(nums)
        for h in range(length - 1):
            s = nums[h]
            for j in range(h + 1, length):
                s += nums[j]
                if s % k == 0:
                    return True
        return False

    def checkSubarraySum2(self, nums: list, k: int) -> bool:
        remainder_set = set()
        presum = remainder = 0
        for num in nums:
            pre_remainder = remainder
            presum += num
            remainder = presum % k
            if remainder in remainder_set:
                return True
            # 间隔为2，使用延迟更新来实现
            remainder_set.add(pre_remainder)
        return False

    def checkSubarraySum3(self, nums: list, k: int) -> bool:
        modes = set()
        presum = 0
        for num in nums:
            last = presum
            # 当前前缀和
            presum += num
            presum %= k
            # 同余定理
            if presum in modes:
                return True
            # 上一个前缀和，下一个就可以用了（距离为2了）
            modes.add(last)
        return False

    """作者：himymBen
    链接：https: // leetcode.cn / problems / continuous - subarray - sum / solution / python - tong - yu - ding - li - yan - chi - tian - jia - t85um /
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""


def main():
    s = Solution()
    # s.checkSubarraySum3(nums=[0, 1, 0, 3, 0, 4, 0, 4, 0], k=5)
    s.checkSubarraySum2(nums=[0, 1, 0, 3, 0, 4, 0, 4, 0], k=5)


if __name__ == '__main__':
    main()
