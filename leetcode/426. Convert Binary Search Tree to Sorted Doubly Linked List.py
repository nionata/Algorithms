"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    # Iterative
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: 
            return
        
        head, last, stack, visited = None, None, [], set()
        
        stack.append(root)
        while stack:
            if stack[-1].left and stack[-1].left not in visited:
                stack.append(stack[-1].left)
                continue
            else:
                curr = stack.pop()
                visited.add(curr)
                
                if last:
                    curr.left = last
                    last.right = curr
                else:
                    head = curr
                    
                last = curr
                
                if curr.right:
                    stack.append(curr.right)
            
        last.right = head
        head.left = last  
        return head
        
    # Recursive
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        head, last = None, None
        
        def dfs(node):
            nonlocal head, last
            
            if node:
                if node.left:
                    dfs(node.left)
                
                if last:
                    node.left = last
                    last.right = node
                else:
                    head = node
                
                last = node
                
                dfs(node.right)
        
        if root:
            dfs(root)
            last.right = head
            head.left = last
        
        return head
