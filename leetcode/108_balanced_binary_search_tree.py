# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list) -> Optional[TreeNode]:
        length = len(nums)
        if length == 0:
            res = TreeNode()
            return res
        elif length == 1:
            res = TreeNode(nums[0])
            return res
        elif length == 2:
            res = TreeNode(nums[1])
            res.left = TreeNode(nums[0])
        else:
            mean_index = length // 2
            res = TreeNode(nums[mean_index])
            res.left = self.sortedArrayToBST(nums[:mean_index])
            res.right = self.sortedArrayToBST(nums[mean_index + 1:])
        return res
