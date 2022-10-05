# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = l1
        pointer2 = l2
        str1 = str2 = ""
        # 正序从两个链表中读取数据
        while pointer1:
            str1 += str(pointer1.val)
            pointer1 = pointer1.next
        while pointer2:
            str2 += str(pointer2.val)
            pointer2 = pointer2.next
        # 逆序将读出来的数据转化成数字，并进行加法运算
        n1 = int(str1[::-1])
        n2 = int(str2[::-1])
        res_str = str(n1 + n2)
        # 指针指向字符串末尾，反向依次将答案组织成链表
        pointer = res = ListNode(val=int(res_str[-1]))
        for k in res_str[::-1]:
            num = int(k)
            pointer.next = ListNode(val=num)
            pointer = pointer.next
        return res.next
