# 给你一个下标从 0 开始的非负整数数组 nums 。对于 nums 中每一个整数，你必须找到对应元素的 第二大 整数。 
# 
#  如果 nums[j] 满足以下条件，那么我们称它为 nums[i] 的 第二大 整数： 
# 
#  
#  j > i 
#  nums[j] > nums[i] 
#  恰好存在 一个 k 满足 i < k < j 且 nums[k] > nums[i] 。 
#  
# 
#  如果不存在 nums[j] ，那么第二大整数为 -1 。 
# 
#  
#  比方说，数组 [1, 2, 4, 3] 中，1 的第二大整数是 4 ，2 的第二大整数是 3 ，3 和 4 的第二大整数是 -1 。 
#  
# 
#  请你返回一个整数数组 answer ，其中 answer[i]是 nums[i] 的第二大整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,4,0,9,6]
# 输出：[9,6,6,-1,-1]
# 解释：
# 下标为 0 处：2 的右边，4 是大于 2 的第一个整数，9 是第二个大于 2 的整数。
# 下标为 1 处：4 的右边，9 是大于 4 的第一个整数，6 是第二个大于 4 的整数。
# 下标为 2 处：0 的右边，9 是大于 0 的第一个整数，6 是第二个大于 0 的整数。
# 下标为 3 处：右边不存在大于 9 的整数，所以第二大整数为 -1 。
# 下标为 4 处：右边不存在大于 6 的整数，所以第二大整数为 -1 。
# 所以我们返回 [9,6,6,-1,-1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,3]
# 输出：[-1,-1]
# 解释：
# 由于每个数右边都没有更大的数，所以我们返回 [-1,-1] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 10⁹ 
#  
#  Related Topics 栈 数组 二分查找 排序 单调栈 堆（优先队列） 👍 9 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from bisect import bisect_left
from collections import deque
from functools import reduce
from heapq import heappush, heappop
from typing import List

from sortedcontainers import SortedList

any
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        s = []
        t = []
        # heap O(n*log(n))
        # for i, v in enumerate(nums):
        #     while t and t[0][0] < v:
        #         val, idx = heappop(t)
        #         ans[idx] = v
        #     while s and s[-1][0] < v:
        #         heappush(t, s.pop())
        #     s.append((v, i))
        # return ans

        # 下标整体移动 O(n)
        # s = []
        # t = []
        # for i, v in enumerate(nums):
        #     while t and nums[t[-1]] < v:
        #         ans[t.pop()] = v
        #     j = len(s) - 1
        #     while j >= 0 and nums[s[j]] < v:
        #         j -= 1
        #     t += s[j+1:]
        #     del s[j+1:]
        #     s.append(i)
        # return ans

        # deque O(n)
        # s = []
        # t = deque()
        # for i, v in enumerate(nums):
        #     while t and nums[t[-1]] < v:
        #         ans[t.pop()] = v
        #     tmp = deque()
        #     while s and nums[s[-1]] < v:
        #         tmp.appendleft(s.pop())
        #     t += tmp
        #     s.append(i)
        # return ans

        # SortedList
        s = SortedList()
        ans = [-1] * len(nums)
        for v, i in sorted((-y, x) for x, y in enumerate(nums)):
            idx = s.bisect_left(i)
            if idx + 1 < len(s):
                ans[i] = nums[s[idx + 1]]
            s.add(i)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
reduce