class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
        def removeDuplicateNodes(self, head: ListNode) -> ListNode:
            if not head:
                return head
            occurred = {head.val}
            pos = head
            # 枚举前驱节点
            while pos.next:
                # 当前待删除节点
                cur = pos.next
                if cur.val not in occurred:
                    occurred.add(cur.val)
                    pos = pos.next
                else:
                    # 链表删除节点的方式
                    pos.next = pos.next.next
            return head