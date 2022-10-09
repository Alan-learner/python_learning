# encoding: utf-8
class Solution:
    def removeStars(self, s: str) -> str:
        ans = list()
        for c in s:
            if "*" == c:
                # *可以匹配任何字符，此时弹出栈顶元素与之匹配，共同删除
                ans.pop()
            else:
                ans.append(c)
        res = "".join(ans)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
