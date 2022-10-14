# encoding: utf-8
# author: Alan-learner
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        global ans
        ans = 0
        if root is None:
            return 0

        def dfs(nd, lst: list):
            tmp_lst = [nd.val]
            if nd.val == targetSum:
                global ans
                ans += 1
            for val in lst:
                new_v = val + nd.val
                if new_v == targetSum:
                    ans += 1
                tmp_lst.append(new_v)
            if nd.left is not None:
                dfs(nd.left, tmp_lst)
            if nd.right is not None:
                dfs(nd.right, tmp_lst)

        dfs(root, list())
        return ans


def main():
    pass


if __name__ == '__main__':
    main()
