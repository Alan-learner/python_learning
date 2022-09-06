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

        for num in range(1 << len(mat[0])):
            if bin(num).count("1") != cols:
                continue
            cnt = 0
            for n in mask:
                if n & num == n:
                    cnt += 1
            ans = max(ans, cnt)
        return ans


def main():
    s = Solution()
    res = s.maximumRows([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], cols=2)
    print(res)


if __name__ == '__main__':
    main()
