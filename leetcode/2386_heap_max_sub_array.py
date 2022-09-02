# encoding: utf-8
from heapq import heappop, heappush


class Solution:
    def kSum(self, nums: list, k: int) -> int:
        tot = 0
        for i, v in enumerate(nums):
            if v >= 0:
                tot += v
            else:
                nums[i] = -v
        nums.sort()
        heap = [(0, 0)]
        while k > 1:
            k -= 1
            sub_sum, index = heappop(heap)  # 弹出堆顶元素
            if index < len(nums):
                new_sub_sum = sub_sum + nums[index]
                new_index = index + 1
                heappush(heap, (new_sub_sum, new_index))
                if index:
                    new_sub2_sum = sub_sum + nums[index] - nums[index - 1]  # 将元素插入堆
                    new_index2 = index + 1
                    heappush(heap, (new_sub2_sum, new_index2))  # 将元素插入堆
        return tot - heap[0][0]


def main():
    s = Solution()
    res = s.kSum(nums=[2, 4, -2, 7, 9, -3, -1], k=128)
    print(res)


if __name__ == '__main__':
    main()
