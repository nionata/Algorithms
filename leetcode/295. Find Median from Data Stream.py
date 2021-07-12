class MedianFinder:

    # Space: O(n)
    def __init__(self):

        self.maxHeap = []    
        self.minHeap = []

    # Time: O(logn)
    def addNum(self, num: int) -> None:

        # Source max <- min
        if self.isEven():
            heappush(self.minHeap, num)

            new_min = heappop(self.minHeap)

            heappush(self.maxHeap, -new_min)
        
        # Source max -> min 
        else: 
            heappush(self.maxHeap, -num)

            new_max = heappop(self.maxHeap)

            heappush(self.minHeap, -new_max)        

    # Time: O(1)
    def findMedian(self) -> float:

        if self.isEven():
            curr_max = self.maxHeap[0]
            curr_min = self.minHeap[0]

            return (-curr_max+curr_min)/2
        else:
            return -self.maxHeap[0]

    def isEven(self) -> bool:

        return len(self.maxHeap) == len(self.minHeap)
        
        
class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # n-2, n-1, n
        self.minHeap = [] # n+1, n+2, n+3
        
    # O(log n)
    def addNum(self, num: int) -> None:
        if self.isEven():
            # Get a new min and push to max
            heappush(self.minHeap, num)
            newMin = heappop(self.minHeap)
            heappush(self.maxHeap, -newMin)
        else:
            # Get a new max and push to min
            heappush(self.maxHeap, -num)
            newMax = heappop(self.maxHeap)
            heappush(self.minHeap, -newMax)

    # O(1)
    def findMedian(self) -> float:
        if self.isEven():
            return (self.minHeap[0] + (self.maxHeap[0]*-1))/2
        else:
            return self.maxHeap[0]*-1
        
    # O(1)
    def isEven(self) -> bool:
        return len(self.maxHeap) == len(self.minHeap)
