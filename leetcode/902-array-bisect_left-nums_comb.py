# encoding: utf-8
# author: Alan-learner
from bisect import bisect, bisect_right, bisect_left
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        lst = list(map(int, digits))
        n_len = len(str(n))
        ans = 0
        while n_len > 1:
            n_len -= 1
            ans += len(digits) ** n_len
        for i, c in enumerate(str(n)):
            cnt = bisect_left(lst, int(c))
            ans += cnt * ((len(digits)) ** (len(str(n)) - i - 1))
            if c not in digits:
                break
            else:
                if i == len(str(n))-1:
                    ans += 1
        return ans


def main():
    s = Solution()
    res = s.atMostNGivenDigitSet(["1", "7"], 231)
    print(res)


if __name__ == '__main__':
    main()
