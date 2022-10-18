# encoding: utf-8
# author: Alan-learner
from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        dic = defaultdict(int)
        left = 0
        for right, val in enumerate(fruits):
            dic[val] += 1
            if len(dic) <= 2:
                ans = max(right - left + 1, ans)
            while len(dic) > 2:
                dic[fruits[left]] -= 1
                if dic[fruits[left]] == 0:
                    dic.pop(fruits[left])
                left += 1
        return ans


def main():
    s = Solution()
    res = s.totalFruit([0, 1, 2, 2])
    print(res)


if __name__ == '__main__':
    main()
