# encoding: utf-8
# author: Alan-learner
from itertools import accumulate
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        scores = [1 if k > 8 else -1 for k in hours]
        ac = list(accumulate(scores, initial=0))
        stk = [0]
        ans = 0
        for i, c in enumerate(ac):
            if stk and ac[stk[-1]] > c:
                stk.append(i)
        for i, c in enumerate(ac[::-1]):
            while stk and c - ac[stk[-1]] > 0:
                idx = len(ac) - i - 1
                ans = max(ans, idx - stk.pop())
        return ans


def main():
    s = Solution()
    res = s.longestWPI(hours = [9,9,6,0,6,6,9])
    print(res)


if __name__ == '__main__':
    main()
