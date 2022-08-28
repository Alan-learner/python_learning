# encoding: utf-8
class Solution:
    def removeStars(self, s: str) -> str:
        ans = list()
        for c in s:
            if "*" == c:
                ans.pop()
            else:
                ans.append(c)
        res = "".join(ans)
        return res


def main():
    pass


if __name__ == '__main__':
    main()
