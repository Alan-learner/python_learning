# encoding: utf-8
# author: Alan-learner
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        right = [n] * n
        r_stk = []
        for i, v in enumerate(arr[::-1]):
            while r_stk and arr[r_stk[-1]] > v:
                r_stk.pop()
            if r_stk:
                right[n - i - 1] = r_stk[-1]
            r_stk.append(n - i - 1)
        l_stk = []
        ans = 0
        for i, v in enumerate(arr):
            while l_stk and arr[l_stk[-1]] >= v:
                l_stk.pop()
            if l_stk:
                l_idx = l_stk[-1]
            else:
                l_idx = -1
            r_idx = right[i]
            l_stk.append(i)
            ans += v * (i - l_idx) * (r_idx - i)
        return ans % (10 ** 9 + 7)


def main():
    s = Solution()
    res = s.sumSubarrayMins(arr=[11, 81, 94, 43, 3])
    print(res)


if __name__ == '__main__':
    main()
