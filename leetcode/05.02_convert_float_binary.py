class Solution:
    def printBin(self, num: float) -> str:
        cnt = 0
        remain = num
        res = "0."
        while remain > 0 and cnt <= 32:
            mult = remain * 2
            if mult > 1:
                res += "1"
                remain = mult - 1
            elif mult == 1:
                res += "1"
                return res
            else:
                res += "0"
                remain = mult
            cnt += 1
        if cnt <= 32:
            return res
        else:
            return "ERROR"


def main():
    s = Solution()
    res = s.printBin(num=0.625)
    res = s.printBin()
    print(res)


if __name__ == '__main__':
    main()
