# encoding: utf-8
class Solution:
    def checkDistances(self, s: str, distance: list) -> bool:
        dic = {}
        for i, v in enumerate(s):
            n = ord(v) - ord("a")
            if dic.get(n) is not None:
                dic[n] = i - dic[n] - 1
                if dic[n] != distance[n]:
                    return False
            else:
                dic[n] = i
        return True


def main():
    s = Solution()
    res = s.checkDistances(s="abaccb",
                           distance=[1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print(res)


if __name__ == '__main__':
    main()
