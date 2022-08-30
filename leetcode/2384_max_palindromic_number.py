# encoding: utf-8
import string
from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = Counter(num)  # python自带的计数工具
        if cnt["0"] == len(num):  # 特判
            return "0"
        res = ""
        dig = string.digits  # 自带的字符串数字集合,'0123456789'
        for c in dig[:0:-1]:
            res += c * (cnt[c] // 2)
        if res and cnt.get("0"):
            res += "0" * (cnt["0"] // 2)
        res2 = res[::-1]
        for c in dig[::-1]:
            if cnt[c] % 2 == 1:
                res += c
                break
        return res + res2


def main():
    s = Solution()
    s.largestPalindromic(num="444947137")


if __name__ == '__main__':
    main()
