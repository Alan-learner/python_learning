# encoding: utf-8
# author: Alan-learner


class Solution:
    def scoreOfParentheses2(self, s: str) -> int:
        stk = [0]
        for c in s:
            if c == "(":
                stk.append(0)
            else:
                val = stk.pop()
                stk[-1] += max(val * 2, 1)
        return stk[-1]

    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        for c in s:
            if c == "(":
                stk.append("(")
            else:
                val = 0
                while stk and stk[-1] != "(":
                    val += stk.pop()
                stk[-1] = max(1, val * 2)
        return sum(stk)


def main():
    s = Solution()
    res = s.scoreOfParentheses("(()(()))")
    print(res)


if __name__ == '__main__':
    main()
