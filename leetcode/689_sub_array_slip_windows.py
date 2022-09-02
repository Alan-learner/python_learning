# encoding: utf-8


class Solution:
    def maxSumOfThreeSubarrays(self, nums: list, k: int) -> list:
        length = len(nums)
        np = [0 for _ in range(length - k + 1)]
        np[0] = sum(nums[:k])
        for index in range(1, length - k + 1):
            np[index] = np[index - 1] - nums[index - 1] + nums[index + k - 1]
        res = [length] * 3
        s = 0
        # o(n**3)
        # for a in range(len(np)):
        #     s1 = np[a]
        #     for b in range(a + k, len(np)):
        #         s2 = s1 + np[b]
        #         for c in range(b + k, len(np)):
        #             s3 = s2 + np[c]
        #             if s3 > s:
        #                 s = s3
        #                 res = [a, b, c]
        # o(n**2)
        # for a in range(len(np) - k - 1, k - 1, -1):
        #     left = np[0]
        #     right = np[-1]
        #     s1 = np[a]
        #     s2 = s3 = 0
        #     for b in range(a - k, -1, -1):
        #         if np[b] >= left:
        #             left = np[b]     #计算左右最大点时候有重复计算
        #             s2 = np[b]
        #             res_b = b
        #     for c in range(len(np) - 1, a + k - 1, -1):
        #         if np[c] >= right:
        #             right = np[c]
        #             s3 = np[c]
        #             res_c = c
        #     if s2 and s3 and s1 + s2 + s3 >= s:
        #         s = s1 + s2 + s3
        #         res = [res_b, a, res_c]
        # o(n)
        lis_left = [0]
        for i in range(1, len(np)):
            if np[i - 1] > np[lis_left[-1]]:
                add = i - 1
            else:
                add = lis_left[-1]
            lis_left.append(add)
        lis_right = [len(np) - 1]
        for i in range(1, len(np)):
            if np[-i - 1] >= np[lis_right[0]]:
                add = len(np) - i - 1
            else:
                add = lis_right[0]
            lis_right.insert(0, add)

        for b in range(len(np) - k - 1, k - 1, -1):
            a = lis_left[b - k + 1]  # 找到左侧的间隔在k以外的最大下标
            c = lis_right[b + k]
            s_ = np[a] + np[b] + np[c]
            if s_ >= s:
                s = s_
                res = [a, b, c]
        return res


def main():
    s = Solution()
    res = s.maxSumOfThreeSubarrays(nums=[1, 2, 1, 2, 1, 2, 1, 2, 1], k=2)
    print(res)


if __name__ == '__main__':
    main()
