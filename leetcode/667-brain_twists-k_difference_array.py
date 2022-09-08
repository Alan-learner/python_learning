# encoding: utf-8
class Solution:
    def constructArray(self, n: int, k: int) -> list:
        tmp = list(range(1, n + 1))
        ans = []
        flag = 1
        for j in range(k):
            flag = j % 2
            if flag:
                num = tmp.pop(-1)
            else:
                num = tmp.pop(0)
            ans.append(num)
        if flag:
            ans += tmp[::-1]
        else:
            ans += tmp
        return ans


def main():
    pass


if __name__ == '__main__':
    main()
