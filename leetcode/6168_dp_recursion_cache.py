# encoding: utf-8
from executing import cache


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def f(x, left):
            if abs(x - endPos) > left:
                return 0
            if left == 0:
                return 1
            return f(x - 1, left - 1) + f(x + 1, left - 1)

        return f(startPos, k) % MOD


def main():
    s = Solution()
    res = s.numberOfWays(startPos=260, endPos=270, k=48)
    print(res)


if __name__ == '__main__':
    main()
