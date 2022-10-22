# encoding: utf-8
# author: Alan-learner


class Solution:
    def threeEqualParts(self, arr: list) -> list:
        # 由0和1组成的数组，找到两个分割点，将数组的值分为三份
        cnt1 = arr.count(1)
        if cnt1 == 0:
            # 全为0的情况，返回数组最短时的正确分法
            return [0, 2]
        if cnt1 % 3 != 0:
            # 三部分1的数目不相同时，则无解
            return [-1, -1]
        cnt0 = 0 # 从右往左第一个0的位置
        for k in arr[::-1]:
            if k == 0:
                cnt0 += 1
            else:
                break
        cnt_1 = 0 # 从左往右数1的数目
        n = len(arr)
        left = right = n - 1
        for i, k in enumerate(arr):
            if cnt_1 == 2 * cnt1 // 3:
                # 右分割点为2/3 倍1的数目的位置
                right = i
                break
            if k == 1:
                cnt_1 += 1
            if cnt_1 == cnt1 // 3:
                # 左分割点为1/3 倍1的数目的位置
                left = min(left, i)

        left += cnt0
        right += cnt0
        # 将结果组织为答案的形式
        lst = [str(k) for k in arr]
        s = "".join(lst)
        # 处理先导0
        a = s[:left + 1].lstrip("0")
        b = s[left + 1:right].lstrip("0")
        c = s[right:].lstrip("0")
        if a == b == c:
            # 验证这种方法的结果是否可行
            return [left, right]
        return [-1, -1]


def main():
    s = Solution()
    res = s.threeEqualParts(arr=[1, 0, 1, 0, 1])
    print(res)


if __name__ == '__main__':
    main()
