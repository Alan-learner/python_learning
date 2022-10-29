# encoding: utf-8
# author: Alan-learner
from typing import List


class Solution:
    def validSubarraySize(self, arr: List[int], threshold: int) -> int:
        n = len(arr)
        right = [n] * n
        r_stk = []
        # 单调栈求小于当前元素的右边界
        for i, v in enumerate(arr[::-1]):
            while r_stk and arr[r_stk[-1]] > v:
                r_stk.pop()
            if r_stk:
                right[n - i - 1] = r_stk[-1]
            r_stk.append(n - i - 1)
        l_stk = []
        # 单调栈求小于当前元素的左边界
        for i, v in enumerate(arr):
            while l_stk and arr[l_stk[-1]] >= v:
                l_stk.pop()
            if l_stk:
                l_idx = l_stk[-1]
            else:
                l_idx = -1
            r_idx = right[i]
            l_stk.append(i)
            # 判断左右边界是否符合题目的阈值要求
            if v > threshold / (r_idx - l_idx - 1):
                return r_idx - l_idx - 1
        return -1


def main():
    pass


if __name__ == '__main__':
    main()
