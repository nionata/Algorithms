class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        list, heap = [], [(node.val, i) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        while heap:
            v, i = heapq.heappop(heap)
            list.append(v)
            lists[i] = lists[i].next if lists[i].next else None
            if lists[i]: heapq.heappush(heap, (lists[i].val, i))
        return list
