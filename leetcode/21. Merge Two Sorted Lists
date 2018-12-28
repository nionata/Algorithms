class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = head = ListNode(0)
        while l1 or l2:
            val1 = l1.val if l1 else float('inf')
            val2 = l2.val if l2 else float('inf')
            if val1 <= val2:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        return head.next
