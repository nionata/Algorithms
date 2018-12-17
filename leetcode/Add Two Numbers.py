# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        currNode = head
        while l1 or l2:
            newVal =  currNode.val
            if l1: 
                newVal += l1.val
                l1 = l1.next
            if l2:
                newVal += l2.val
                l2 = l2.next
            remainder = 0
            if newVal >= 10:
                remainder = 1
                newVal = newVal - 10
            currNode.val = newVal
            currNode.next = None
            if l1 or l2 or remainder != 0:
                nextNode = ListNode(remainder)
                currNode.next = nextNode
                currNode = currNode.next
        return head
