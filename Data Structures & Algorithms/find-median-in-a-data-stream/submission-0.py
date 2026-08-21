class MedianFinder:

    def __init__(self):
        # two heaps = large (min Heap), small (max Heap)
        # both heaps should be approximately equal in size

        self.small, self.large = [],[]

    def addNum(self, num: int) -> None:
        # by default add to maxheap
        # python does not have maxheap so multiple all numbers by -1
        heapq.heappush(self.small, -1 * num)
        # condition 1
        # make sure every num in smallHeap is <= every num in largeHeap
        # if small and large heaps are not null
        # getting largest value from small Heap by [0]
        # everytime we are adding the valu to heap we multiple by -1 so we are reversing it by multiplying by -1 again to get the true value
        if (self.small and self.large and
            (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
             # pop from small heap and put  into large heap
            heapq.heappush(self.large, val)

            
        # condition 2
        # if size of heaps difference are more than one
        if len(self.small)>len(self.large)+1:
            # find max of small heap and put in minheap
            val = -1* heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large)>len(self.small)+1:
            # find min of large heap and put in maxheap
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)


    def findMedian(self) -> float:

        # odd len
        if len(self.small)>len(self.large):
            return -1 * self.small[0]

        if len(self.large)>len(self.small):
            return self.large[0]

        # even len
        if len(self.small) == len(self.large):
            mid = (-1*self.small[0] + self.large[0]) 
            return mid/2