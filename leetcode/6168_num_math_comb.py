# encoding: utf-8
from math import comb


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        dif = abs(endPos - startPos)
        if k < dif:
            return 0
        if k == dif:
            return 1
        f1 = dif % 2
        f2 = k % 2
        if f1 != f2:
            return 0
        MOD = 10**9 + 7
        res = comb(k, (dif+k)//2) % MOD
        return res


def main():
    s = Solution()
    res = s.numberOfWays(startPos=272, endPos=270, k=6)
    print(res)


if __name__ == '__main__':
    main()
