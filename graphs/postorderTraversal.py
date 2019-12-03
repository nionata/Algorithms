# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: 
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    
    # Iterative
    def postorderTraversal(self, root: TreeNode) -> List[int]:
    stack, visited = [], []

    if root: stack.append(root)
    while stack:
        curr = stack.pop()

        if not curr.right and not curr.left:
            visited.append(curr.val)
        else:
            l, r, curr.left, curr.right = curr.left, curr.right, None, None

            for node in [curr, r, l]: 
                if node: stack.append(node) 

    return visited
