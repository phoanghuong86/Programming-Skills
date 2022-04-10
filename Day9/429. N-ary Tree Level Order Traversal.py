"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        def dfs(node: Node, level: int):
            if len(ans) <= level:
                ans.append([])
            ans[level].append(node.val)
            if node.children:
                level += 1
                for child in node.children:
                    dfs(child, level)
        if root:
            dfs(root, 0)
        return ans
