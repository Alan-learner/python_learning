# encoding: utf-8
from bisect import bisect_right


class Solution:
    def answerQueries(self, nums: list, queries: list) -> list:
        nums.sort()
        for n in range(1, len(nums)):
            nums[n] += nums[n - 1]  # 原地求前缀和
        for i, v in enumerate(queries):
            queries[i] = bisect_right(nums, v)  # 调用自带库二分求第一个小于等于自身的数
        return queries


def main():
    pass


if __name__ == '__main__':
    main()
