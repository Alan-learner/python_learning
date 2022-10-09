# encoding: utf-8
# author: Alan-learner


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        tmp = 0
        for i, c in enumerate(s):
            if c == "(":
                stk.append(c)
            if c == ")" and stk and stk[-1] == "(":
                stk.pop()
                tmp += 2
        return len(s) - tmp


def main():
    pass


if __name__ == '__main__':
    main()
