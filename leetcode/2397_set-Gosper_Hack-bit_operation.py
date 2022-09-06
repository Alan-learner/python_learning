# encoding: utf-8
class Solution:
    def maximumRows(self, mat: list, cols: int) -> int:
        ans = 0
        mask = []
        for lis in mat:
            s = 0
            for i, v in enumerate(lis):
                s += v << i
            mask.append(s)
        st = (1 << cols) - 1  # 位运算优先级低于加减，要加括号
        while st <= 1 << len(mat[0]):
            cnt = 0
            for n in mask:
                if n & st == n:
                    cnt += 1
            ans = max(ans, cnt)
            lowbit = st & -st
            left = st + lowbit
            right = ((st ^ left) // lowbit) >> 2
            st = right | left
        return ans


def main():
    s = Solution()
    res = s.maximumRows([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], cols=2)
    print(res)


if __name__ == '__main__':
    main()
