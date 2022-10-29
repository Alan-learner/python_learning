# encoding: utf-8
# author: Alan-learner

from typing import List
from itertools import permutations


def get_1024(nums: List[int], signs: List[str]):
    if len(nums) < 4 or len(signs) < 3:
        print("卡片不足")
        return
    nums.sort(key=lambda x: nums.count(x), reverse=True)
    signs.sort(key=lambda x: signs.count(x), reverse=True)
    cnt = 0
    for num in permutations(nums, 4):
        for sign in permutations(signs, 3):
            stk = []
            num_list = list(num)
            sign_list = list(sign)
            stk.append(num_list.pop())
            ans = 0
            while sign_list:
                a = str(stk.pop())
                b = str(num_list.pop())
                s = sign_list.pop()
                try:
                    ans = eval(a + s + b)
                except:
                    pass
                stk.append(ans)
            if ans == 1024:
                cnt += 1
                print(f"方案{cnt}:")
                print(num[::-1])
                print(sign[::-1])
    if cnt == 0:
        print("没有可行的方案")


def main():
    get_1024(nums=[28, 965, 1075, 2, 9, 2, 2, 16, 2, 2, 996, 21],
             signs=[])


if __name__ == '__main__':
    main()
