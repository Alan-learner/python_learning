# encoding: utf-8
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.target_node = None
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = {}
        def dfs(node: TreeNode, parent):
            if not node:
                return
            parents[node] = parent
            if node.val == start:
                self.target_node = node
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)
        ans = -1
        virus = set()
        increase = [self.target_node]
        while increase:
            ans += 1
            tmp = increase  # 延迟更新
            increase = []
            for node in tmp:
                for spread_node in [node.left, node.right, parents[node]]:
                    if not spread_node:
                        continue
                    if spread_node not in virus:
                        virus.add(spread_node)
                        increase.append(spread_node)
        return ans


def main():
    s = Solution()
    res = s.amountOfTime()
    print(res)


if __name__ == '__main__':
    main()
