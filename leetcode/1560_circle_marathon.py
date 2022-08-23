class Solution:
    def mostVisited(self, n: int, rounds: list) -> list:
        length = len(rounds)
        if length <= 1:
            return rounds
        lis = list(range(1, 1 + n))
        left = rounds[0]
        right = rounds[-1]
        if left <= right:
            res = lis[left - 1:right]
        else:
            res = lis[:right]
            res += lis[left - 1:]
        return res
