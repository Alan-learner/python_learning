import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.replace(" ", "")
        if len(s) < 1:
            return 0
        flag = re.findall(r"\+", s[0])
        flag2 = re.findall(r"\-", s[0])
        flag3 = re.findall(r"\d", s[0])
        if flag:
            s = s[1:]
            sign = True
        elif flag2:
            s = s[1:]
            sign = False
        elif flag3:
            sign = True
        else:
            return 0
        flag4 = re.findall(r"\d", s[0])
        if not flag4:
            return 0
        res_str_list = re.findall(r"\d+", s)
        res_str = res_str_list[0]
        res = int(res_str)
        if sign:
            return res
        else:
            return -res

def main():
    s = Solution()
    res = s.myAtoi(s="42")
    print(res)
bin()

if __name__ == '__main__':
    main()
