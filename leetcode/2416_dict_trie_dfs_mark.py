# encoding: utf-8
from collections import defaultdict


class Trie:
    __slots__ = "son", "score", "ids"

    def __init__(self):
        self.son = defaultdict(Trie)
        self.score = 0
        self.ids = list()


class Solution:
    def sumPrefixScores(self, words: list) -> list:
        root = Trie()
        for idx, word in enumerate(words):
            cur = root
            for c in word:
                cur = cur.son[c]
                cur.score += 1
            cur.ids.append(idx)
        ans = [0] * len(words)

        def dfs(nd, sm):
            if nd is None: return
            sm += nd.score
            for i in nd.ids:
                ans[i] = sm
            for child in nd.son.values():
                dfs(child, sm)

        dfs(root, 0)
        return ans


def main():
    s = Solution()
    res = s.sumPrefixScores(words=["abc", "ab", "bc", "b"])
    print(res)


if __name__ == '__main__':
    main()
