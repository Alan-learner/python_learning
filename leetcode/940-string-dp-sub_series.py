# encoding: utf-8
# author: Alan-learner
from collections import defaultdict


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dic = defaultdict(int)
        ans = pre = 1
        for c in s:
            ans = 2 * pre
            ans -= dic[c]
            dic[c] += ans - pre
            pre = ans

        return (ans - 1) % (10 ** 9 + 7)


def main():
    s = Solution()
    res = s.distinctSubseqII(s=
                             "zchmliaqdgvwncfatcfivphddpzjkgyygueikthqzyeeiebczqbqhdytkoawkehkbizdmcnilcjjlpoeoqqoqpswtqdpvszfaksn")
    print(res)


if __name__ == '__main__':
    main()
