# encoding: utf-8
# author: Alan-learner
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i = j = 0
        n = len(start)
        while 1:
            while i <= n - 1 and start[i] == "X":
                i += 1
            while j <= n - 1 and end[j] == "X":
                j += 1
            if i >= n and j >= n:
                return True
            if i >= n or j >= n or start[i] != end[j]:
                # 判断L和R的相对顺序
                return False
            if start[i] == "L" and i < j:
                return False
            if start[i] == "R" and i > j:
                return False
            i += 1
            j += 1


def main():
    pass


if __name__ == '__main__':
    main()
