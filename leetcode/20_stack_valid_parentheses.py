# encoding: utf-8
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")",
               "{": "}",
               "[": "]"}
        stack = list()
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c != dic[top]:
                    return False
        if stack:
            return False
        return True


def main():
    pass


if __name__ == '__main__':
    main()
