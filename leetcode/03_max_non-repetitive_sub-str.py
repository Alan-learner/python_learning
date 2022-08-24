class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 1:
            return 1
        elif length == 2:
            if s[0] != s[1]:
                return 2
            else:
                return 1
        else:
            mean_index = length // 2
            s1 = s[:mean_index]
            s2 = s[mean_index:]
            res1 = self.lengthOfLongestSubstring(s1)
            res2 = self.lengthOfLongestSubstring(s2)
            res3 = self.merge(s1, s2)
            res = max(res1, res2, res3)
            return res

    def merge(self, s1, s2):
        cur_len = 0
        value_set = set()
        for v1 in s1[::-1]:
            if v1 not in value_set:
                value_set.add(v1)
                cur_len += 1
            else:
                break
        for v2 in s2:
            if v2 not in value_set:
                value_set.add(v2)
                cur_len += 1
            else:
                break
        return cur_len


def main():
    s = Solution()
    res = s.lengthOfLongestSubstring(
        100 * "bcdefghiajkabcdefghiajkabcdefghiaj")
    print(res)


if __name__ == '__main__':
    main()
