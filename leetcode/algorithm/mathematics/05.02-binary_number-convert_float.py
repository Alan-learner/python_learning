class Solution:
    def printBin(self, num: float) -> str:
        # 小数部分二进制转化
        cnt = 0
        remain = num
        res = "0."
        while remain > 0 and cnt <= 32:
            # 小数部分二进制转换，乘2取余数累加，直到整乘
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
        # 32 是精度范围
        if cnt <= 32:
            return res
        else:
            return "ERROR"


def main():
    s = Solution()
    res = s.printBin(num=0.625)
    print(res)


if __name__ == '__main__':
    main()
