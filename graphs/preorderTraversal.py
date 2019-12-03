# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    # Iterative
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        visited, stack = [], []
        
        if root: stack.append(root)
        while stack:
            curr = stack.pop()
            visited.append(curr.val)
            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)
        
        return visited
