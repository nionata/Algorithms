# O(nlogn) / O(n)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        for char, count in Counter(tasks).items():
            heappush(heap, -1*count)
        t = 0
        while len(heap):
            tasks = []
            for i in range(n+1):
                if len(heap):
                    t+=1
                    count = heappop(heap)
                    if count < -1:
                        tasks.append(count+1)
                else:
                    if len(tasks):
                        t+=n+1-i
                    break
            for count in tasks:
                heappush(heap, count)
        return t
