# encoding: utf-8

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        while q:
            tmp = []
            tp = []
            for nd in q:
                if nd.left:
                    tp.append(nd.left.val)
                    tmp.append(nd.left)
                else:
                    tp.append("a")
                if nd.right:
                    tp.append(nd.right.val)
                    tmp.append(nd.right)
                else:
                    tp.append("a")
            # tp = [n.val for n in tmp]
            if tp != tp[::-1]:
                return False
            q = tmp
        return True


def main():
    s = Solution()
    res = s.isSymmetric(TreeNode())
    print(res)


if __name__ == '__main__':
    main()
