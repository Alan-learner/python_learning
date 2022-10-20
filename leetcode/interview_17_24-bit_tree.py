# encoding: utf-8
# author: Alan-learner


class Solution:
    def getMaxMatrix(self, matrix: list) -> list:
        m = len(matrix)  # 行数目
        n = len(matrix[0])  # 列数目
        r_lst = list()  # 行前缀和列表
        c_lst = list()  # 列前缀和列表
        for row in matrix:
            tp = [0]
            s = 0
            for i, val in enumerate(row):
                s += val
                tp.append(s)
            r_lst.append(tp)
        for col in range(n):
            tp = [0]
            s = 0
            for row in range(m):
                s += matrix[row][col]
                tp.append(s)
            c_lst.append(tp)
        global sm
        sm = matrix[0][0]
        global ans
        ans = [0, 0, 0, 0]

        def query_sum(start, end):
            global sm
            global ans
            if start:
                for r in range(start, -1, -1):
                    tmp = c_lst[end][start + 1] - c_lst[end][r]  # 区间和
                    if tmp > sm:
                        sm = tmp
                        ans = [r, end, start, end]
                    for c in range(end - 1, -1, -1):
                        tmp += c_lst[c][start + 1] - c_lst[c][r]
                        if tmp > sm:
                            sm = tmp
                            ans = [r, c, start, end]
                return
            if end:
                for c in range(end, -1, -1):
                    tmp = r_lst[start][end + 1] - r_lst[start][c]
                    if tmp > sm:
                        sm = tmp
                        ans = [start, c, start, end]
                    for r in range(start - 1, -1, -1):
                        tmp += r_lst[r][end + 1] - r_lst[r][c]
                        if tmp > sm:
                            sm = tmp
                            ans = [r, c, start, end]

        for row in range(m):
            for col in range(n):
                query_sum(row, col)
        return ans


def main():
    s = Solution()
    res = s.getMaxMatrix([[-4, -5]])
    print(res)


if __name__ == '__main__':
    main()
