# O(n) / O(1)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            first = curr.next
            sec = curr.next.next
            curr.next = sec
            first.next = sec.next
            sec.next = first
            curr = curr.next.next
        return dummy.next
