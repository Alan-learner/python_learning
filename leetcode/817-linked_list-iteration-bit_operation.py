# encoding: utf-8
# author: Alan-learner
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        pointer = head
        ans = 0
        s = set(nums)
        pre = 0
        while pointer:
            if pointer.val in s:
                flag = 1
            else:
                flag = 0
            ans += flag ^ pre
            pre = flag
            pointer = pointer.next
        if ans % 2:
            ans += 1
        return ans // 2


def main():
    pass


if __name__ == '__main__':
    main()
