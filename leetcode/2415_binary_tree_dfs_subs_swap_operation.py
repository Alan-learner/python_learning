# encoding: utf-8

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(nd1, nd2, odd_flag):
            if nd1 is None:
                return
            if odd_flag:
                nd1.val, nd2.val = nd2.val, nd1.val
            dfs(nd1.left, nd2.right, not odd_flag)
            dfs(nd1.right, nd2.left, not odd_flag)

        dfs(root.left, root.right, True)
        return root


def main():
    s = Solution()
    res = s.reverseOddLevels(TreeNode())
    print(res)


if __name__ == '__main__':
    main()
