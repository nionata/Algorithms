# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        sol = []
        
        def helper(node, lvl = 0):
            if node:
                if len(sol) == lvl:
                    sol.append([node.val])
                else: 
                    sol[lvl].append(node.val)
                    
                helper(node.left, lvl + 1)
                helper(node.right, lvl + 1)
            
        helper(root)
        return sol
        
    # Iterative
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        sol, q = [], []
        
        if root: q.append((0, root))
        while q:
            curr = q.pop(0)
            lvl, node = curr[0], curr[1]

            if len(sol) == lvl:
                sol.append([node.val])
            else:
                sol[lvl].append(node.val)

            if node.left: q.append((lvl + 1, node.left))
            if node.right: q.append((lvl + 1, node.right))
            
        return sol
