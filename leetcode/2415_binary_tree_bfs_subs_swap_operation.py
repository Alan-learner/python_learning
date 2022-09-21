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
        q = [root]
        flag = 1
        # BFS根据遍历
        while q:
            tmp = []
            while q:
                nd = q.pop(0)
                if nd.left:
                    tmp.append(nd.left)
                if nd.right:
                    tmp.append(nd.right)
            if flag:
                for i in range(len(tmp)//2):
                    tmp[i].val,tmp[len(tmp)-i-1].val = tmp[len(tmp)-i-1].val, tmp[i].val
            q = tmp
            flag ^= 1
        return root


def main():
    s = Solution()
    res = s.reverseOddLevels(TreeNode())
    print(res)


if __name__ == '__main__':
    main()
