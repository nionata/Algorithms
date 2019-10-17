# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = cur = ListNode(0) 
        
        while l1 or l2:
            curVal = cur.val
            
            if l1:
                curVal += l1.val
                l1 = l1.next
            if l2:
                curVal += l2.val
                l2 = l2.next
                
            r = 0
            
            if curVal > 9: 
                r = 1
                curVal = curVal % 10
                
            cur.val = curVal
                
            if l1 or l2 or r != 0:
                cur.next = ListNode(r)
                cur = cur.next
        
        return h
