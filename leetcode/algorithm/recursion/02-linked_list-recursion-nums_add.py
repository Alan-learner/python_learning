from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        s = l1.val + l2.val
        sub_sum = self.addTwoNumbers(l1.next, l2.next)
        if s > 9:
            # 进位的情况特判,要注意进位的传递
            s -= 10
            add = ListNode(val=1)
            sub_sum = self.addTwoNumbers(add, sub_sum)
        return ListNode(val=s, next=sub_sum)
