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
        if not (root.left or root.right):
            return True

        def dfs(nd1, nd2):
            if not (nd1 or nd2):
                return True
            try:
                cond = nd1.val == nd2.val
            except:
                cond = False
            if not cond:
                return False
            cond1 = dfs(nd1.left, nd2.right)
            cond2 = dfs(nd1.right, nd2.left)
            if not cond1:
                return False
            if not cond2:
                return False
            return True

        return dfs(root.left, root.right)


def main():
    s = Solution()
    res = s.isSymmetric(TreeNode())
    print(res)


if __name__ == '__main__':
    main()
