# encoding: utf-8
# author: Alan-learner
class Solution:
    def validSubarraySize(self, nums: list, threshold: int) -> int:
        n = len(nums)
        fa = list(range(n + 1))
        sz = [1] * (n + 1)

        def find(x: int) -> int:  # 返回根节点
            if fa[x] != x:
                return find(fa[x])
            return fa[x]

        for v, i in sorted(zip(nums, range(n)), reverse=True):
            # merge(i,i+1)
            j = find(i + 1)
            fa[i] = j
            sz[j] += sz[i]
            arr_siez = sz[j] - 1
            if v > threshold // arr_siez:
                return arr_siez
            return -1


def main():
    pass


if __name__ == '__main__':
    main()
