# encoding: utf-8
# author: Alan-learner
from collections import deque
from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = inf
        ac = list(accumulate(nums, initial=0))
        q = deque()
        for i, v in enumerate(ac):
            while q and v - ac[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            while q and v <= ac[q[-1]]:
                q.pop()
            q.append(i)
        if ans == inf:
            ans = -1
        return ans


def main():
    s = Solution()
    res = s.shortestSubarray(nums=[1, 2, 3, 4, 5], k=15)
    print(res)


if __name__ == '__main__':
    main()
