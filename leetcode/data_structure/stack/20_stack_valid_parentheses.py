# encoding: utf-8
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")",
               "{": "}",
               "[": "]"}
        stack = list()
        for c in s:
            if c in dic:
                # 左括号放入栈中
                stack.append(c)
            else:
                if not stack:
                    # 出现右括号，但存储左括号的栈为空
                    return False
                top = stack.pop()
                if c != dic[top]:
                    # 右括号和栈顶的左括号不匹配
                    return False
        if stack:
            # 栈内左括号有剩余未匹配完
            return False
        return True


def main():
    pass


if __name__ == '__main__':
    main()
