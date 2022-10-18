# encoding: utf-8
# author: Alan-learner
from heapq import heappush, heappop


class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.arr = []
        self.con = 0

    def upload(self, video: int) -> None:
        heappush(self.arr, video)
        while self.arr and self.arr[0] - self.con == 1:
            self.con = heappop(self.arr)

    def longest(self) -> int:
        return self.con


def main():
    pass


if __name__ == '__main__':
    main()
