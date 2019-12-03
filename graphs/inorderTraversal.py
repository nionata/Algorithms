# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
    # Iterative
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        visited, stack, curr = [], [], root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            visited.append(curr.val)
            curr = curr.right

        return visited
