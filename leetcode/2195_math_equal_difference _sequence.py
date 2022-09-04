# encoding: utf-8
class Solution:
    def minimalKSum(self, nums: list, k: int) -> int:
        x = max(nums)
        y = min(nums)
        length = len(nums)
        if k < y:
            ans = (1 + k) * k // 2
        elif k >= x:
            ans = (1 + k + length) * (k + length) // 2 - sum(nums)
        else:
            nums.sort()
            index = 0
            for i, v in enumerate(nums):
                if k < v and i < length - 1 and k + i + 1 < nums[i]:
                    index = i
                    break
                else:
                    index = length
            ans = (1 + k + len(nums[:index])) * (k + len(nums[:index])) // 2 - sum(nums[:index])
        return ans


def main():
    s = Solution()
    res = s.minimalKSum(
        [96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40,
         84], k=35)
    print(res)


if __name__ == '__main__':
    main()
