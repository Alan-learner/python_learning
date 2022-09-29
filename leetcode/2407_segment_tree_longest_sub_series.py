# encoding: utf-8

class Solution:
    def lengthOfLIS(self, nums: list, k: int) -> int:
        u = max(nums) + 1
        mx = [0] * u * 4

        def modify(o, l, r, i, val):
            if l == r:
                mx[o] = val
                return
            mid = (l + r) // 2
            if i <= mid:
                modify(o * 2, l, mid, i, val)
            else:
                modify(o * 2 + 1, mid + 1, r, i, val)
            mx[o] = max(mx[o * 2], mx[o * 2 + 1])

        def query(o, l, r, L, R):
            if L <= l and r <= R:
                return mx[o]
            mid = (l + r) // 2
            res = 0
            if mid >= L:
                res = query(o * 2, l, mid, L, R)
            if mid < R:
                res = max(res, query(o * 2 + 1, mid + 1, r, L, R))
            return res

        for x in nums:
            x += 1
            res = 1 + query(1, 1, u, max(x - k, 1), x - 1)
            modify(1, 1, u, x, res)
        return mx[1]


def main():
    s = Solution()
    res = s.lengthOfLIS(nums=[4, 2, 1, 4, 3, 4, 5, 8, 15], k=3)
    print(res)


if __name__ == '__main__':
    main()
