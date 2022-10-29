# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，长度为 n 。 
# 
#  数组 nums1 和 nums2 的 差值平方和 定义为所有满足 0 <= i < n 的 (nums1[i] - nums2[i])² 之和。 
# 
#  同时给你两个正整数 k1 和 k2 。你可以将 nums1 中的任意元素 +1 或者 -1 至多 k1 次。类似的，你可以将 nums2 中的任意元素 +
# 1 或者 -1 至多 k2 次。 
# 
#  请你返回修改数组 nums1 至多 k1 次且修改数组 nums2 至多 k2 次后的最小 差值平方和 。 
# 
#  注意：你可以将数组中的元素变成 负 整数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
# 输出：579
# 解释：nums1 和 nums2 中的元素不能修改，因为 k1 = 0 和 k2 = 0 。
# 差值平方和为：(1 - 2)2 + (2 - 10)2 + (3 - 20)2 + (4 - 19)² = 579 。
#  
# 
#  示例 2： 
# 
#  输入：nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
# 输出：43
# 解释：一种得到最小差值平方和的方式为：
# - 将 nums1[0] 增加一次。
# - 将 nums2[2] 增加一次。
# 最小差值平方和为：
# (2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)² = 43 。
# 注意，也有其他方式可以得到最小差值平方和，但没有得到比 43 更小答案的方案。 
# 
#  
# 
#  提示： 
# 
#  
#  n == nums1.length == nums2.length 
#  1 <= n <= 10⁵ 
#  0 <= nums1[i], nums2[i] <= 10⁵ 
#  0 <= k1, k2 <= 10⁹ 
#  
#  Related Topics 数组 数学 排序 堆（优先队列） 👍 25 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        nums = []
        ans = 0
        for a, b in zip(nums1, nums2):
            num = abs(a - b)
            nums.append(num)
            ans += num * num
        if sum(nums) <= k:
            return 0
        nums.sort(reverse=True)
        nums.append(0)
        for i, v in enumerate(nums):
            ans -= v ** 2
            c = i + 1
            cnt = c * (v - nums[c])
            if cnt < k:
                k -= cnt
                continue
            v -= k // c
            ans += (k % c) * (v - 1) * (v - 1)
            ans += (c - k % c) * v * v
            return ans
# leetcode submit region end(Prohibit modification and deletion)
