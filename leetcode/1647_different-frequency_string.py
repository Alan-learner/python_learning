class Solution:
    def minDeletions(self, s: str) -> int:
        res = 0
        if not s:
            return res
        dic = dict()
        for val in s:
            if dic.get(val):
                dic[val] += 1
            else:
                dic[val] = 1
        lis = list(dic.values())
        lis.sort()
        while lis:
            tag = val = lis.pop(-1)
            while val in lis:
                res += 1
                val -= 1
            if tag != val and val != 0:
                lis.insert(0, val)
        return res


def main():
    s = Solution()
    res = s.minDeletions(s="bbcebab")
    print(res)


if __name__ == '__main__':
    main()
