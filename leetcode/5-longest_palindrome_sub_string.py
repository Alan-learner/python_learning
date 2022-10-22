# encoding: utf-8
# author: Alan-learner

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mx = 1
        ans = s[0]
        # 中心扩散找最长回文串数目
        for i in range(n - 1):
            len1 = 1
            len2 = 0
            for j in range(1, n):
                # 讨论长度为奇数的回文串
                if i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
                    len1 += 2
                    if len1 > mx:
                        mx = len1
                        ans = s[i - j:i + j + 1]
                    continue
                break
            for k in range(1, n):
                if i - k >= -1 and i + k < n and s[i + 1 - k] == s[i + k]:
                    len2 += 2
                    if len2 > mx:
                        mx = len2
                        ans = s[i - k + 1:i + k + 1]
                    continue
                break
        return ans


def main():
    s = Solution()
    res = s.longestPalindrome("xaabacxcabaaxcabaax")
    print(res)


if __name__ == '__main__':
    main()
