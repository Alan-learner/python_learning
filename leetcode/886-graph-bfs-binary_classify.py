# encoding: utf-8
# author: Alan-learner
from collections import defaultdict, deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for x, y in dislikes:
            x -= 1
            y -= 1
            graph[x].append(y)
            graph[y].append(x)
        color = [0] * n
        for idx, col in enumerate(color):
            if col == 0:
                color[idx] = 1
                q = deque([idx])
                while q:
                    x = q.popleft()
                    for y in graph[x]:
                        if color[x] == color[y]:
                            return False
                        if color[y] == 0:
                            color[y] = -color[x]
                            q.append(y)
        return True


def main():
    s = Solution()
    res = s.possibleBipartition(n=4, dislikes=[[1, 2], [1, 3], [2, 4]])
    print(res)


if __name__ == '__main__':
    main()
