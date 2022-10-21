# encoding: utf-8
# author: Alan-learner


class StockSpanner2:

    def __init__(self):
        self.prices = []
        self.dp = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        if not self.dp:
            self.dp.append(1)
            return 1
        cnt = 1
        while cnt < len(self.prices) and self.prices[-1] >= self.prices[-cnt - 1]:
            cnt += self.dp[-cnt]
        self.dp.append(cnt)
        return self.dp[-1]


class StockSpanner:
    # 单调栈
    def __init__(self):
        self.stack = [(0, 0)]
        self.dp = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


def main():
    S = StockSpanner()
    S.next(100)
    S.next(80)
    S.next(60)
    S.next(70)
    S.next(60)
    S.next(75)
    S.next(85)


if __name__ == '__main__':
    main()
