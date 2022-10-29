# encoding: utf-8
# author: Alan-learner
from typing import List

from executing import cache

MOD = 10 ** 9 + 7


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        @cache
        def move(x, y, s):
            # 从(n-1, m-1)到(0,0)的过程中，(x, y)状态所累加的s
            nonlocal ans
            if x < 0 or y < 0:
                return 0
            s = (s + grid[x][y]) % k
            if x == y == 0:
                # 到(0,0)时，如果累加s为1,则答案+1
                return s == 0
            return (move(x - 1, y, s) + move(x, y - 1, s)) % MOD

        ans = move(n - 1, m - 1, 0)
        move.cache_clear()
        return int(ans)


def main():
    s = Solution()
    res = s.numberOfPaths([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1)
    print(res)


if __name__ == '__main__':
    main()
